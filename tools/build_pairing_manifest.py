import csv
import argparse
import re
import unicodedata
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
META = ROOT / "data" / "metadata"
OUT = META / "pairing_manifest.csv"

parser = argparse.ArgumentParser(description="Build a local ECG/XML pairing manifest.")
parser.add_argument("--output", type=Path, default=OUT)
parser.add_argument("--alias", action="append", default=[], metavar="OLD=NEW",
                    help="Local patient ID correction. Repeat for additional aliases.")
args = parser.parse_args()

aliases = {}
for alias in args.alias:
    old, separator, new = alias.strip().upper().partition("=")
    if not separator or not old or not new or "=" in new:
        parser.error("--alias requires OLD=NEW")
    aliases[old] = new

def canonical_id(value: str) -> str:
    value = "".join(c for c in value.upper() if not unicodedata.combining(c))
    return aliases.get(value, value)

def ecg_info(path):
    dates = set()
    for token in re.findall(r"(?<!\d)(?:\d{4}-\d{2}-\d{2}|\d{1,2}\.\d{1,2}\.(?:\d{4}|\d{2}))(?!\d)", path.stem):
        fmt = "%Y-%m-%d" if "-" in token else (
            "%d.%m.%Y" if len(token.split(".")[-1]) == 4 else "%d.%m.%y"
        )
        try:
            dates.add(datetime.strptime(token, fmt).date().isoformat())
        except ValueError:
            continue
    return path.stem.split("_")[0].upper(), next(iter(dates)) if len(dates) == 1 else None

def xml_info(path):
    name_id, date = ecg_info(path)
    valid = True
    try:
        ET.parse(path)
    except ET.ParseError:
        valid = False
    return name_id, date, valid

def rel(path):
    return path.relative_to(ROOT).as_posix()

rows = []
for dataset in ("Brugada_N_HL", "BS_HL"):
    base = RAW / dataset
    ecgs = sorted(base.rglob("*.ecg"))
    xmls = sorted(base.rglob("*.xml"))
    if not ecgs or not xmls:
        raise SystemExit(f"Missing dataset files under {base}")
    ecg_keys = defaultdict(list)
    for ecg in ecgs:
        pid, date = ecg_info(ecg)
        if date:
            ecg_keys[(canonical_id(pid), date)].append(ecg)
    xml_by_key = defaultdict(list)
    xml_meta = {}
    for path in xmls:
        pid, date, valid = xml_info(path)
        meta = (pid, date, valid)
        xml_meta[path] = meta
        if date:
            xml_by_key[(canonical_id(pid), date)].append(path)
    used = set()
    for ecg in ecgs:
        raw_pid, date = ecg_info(ecg)
        pid = canonical_id(raw_pid)
        candidates = xml_by_key.get((pid, date), []) if date else []
        valid_candidates = [path for path in candidates if xml_meta[path][2]]
        if len(valid_candidates) == 1 and len(ecg_keys[(pid, date)]) == 1:
            xml = valid_candidates[0]
            used.add(xml)
            _, _, valid = xml_meta[xml]
            status = "PROBABLE" if raw_pid in aliases or xml_meta[xml][0] in aliases else "PAIRED"
            confidence = "HIGH" if status == "PAIRED" and valid and xml.stat().st_size else "MEDIUM"
            reason = "unique patient/date match"
            if status == "PROBABLE":
                reason = "unique date match using a configured patient ID alias"
            if not valid or xml.stat().st_size == 0:
                status, confidence, reason = "CORRUPTED_XML", "NONE", "XML is empty or invalid"
            xml_path = rel(xml)
            xml_pid, xml_date, _ = xml_meta[xml]
        elif valid_candidates:
            status, confidence, reason = "AMBIGUOUS", "LOW", "multiple ECG or XML records share patient/date"
            xml_path, xml_pid, xml_date = "", "", date or ""
        else:
            status, confidence, reason = "MISSING_XML", "NONE", "no valid XML with matching canonical patient/date"
            if candidates:
                status, reason = "CORRUPTED_XML", "all same-key XML candidates failed parsing"
            elif not date:
                status, reason = "UNRESOLVED", "filename has no unique valid recording date"
            xml_path, xml_pid, xml_date = "", "", ""
        rows.append({"pair_id": f"{dataset}_{len(rows)+1:06d}", "dataset": dataset,
                     "ecg_path": rel(ecg), "xml_path": xml_path,
                     "canonical_patient_id": pid, "ecg_patient_id": raw_pid,
                     "xml_patient_id": xml_pid, "ecg_date": date or "",
                     "xml_date": xml_date, "status": status,
                     "confidence": confidence, "reason": reason,
                     "ecg_bytes": ecg.stat().st_size,
                     "xml_bytes": str(xml.stat().st_size) if xml_path else "",
                     "candidate_paths": " | ".join(rel(path) for path in candidates if not xml_path)})
    for xml in xmls:
        if xml in used:
            continue
        pid, date, valid = xml_meta[xml]
        status = "CORRUPTED_XML" if (not valid or xml.stat().st_size == 0) else "MISSING_ECG"
        reason = "XML is empty or invalid" if status == "CORRUPTED_XML" else "no ECG with matching canonical patient/date"
        candidates = ecg_keys.get((canonical_id(pid), date), [])
        if valid and candidates:
            status, reason = "AMBIGUOUS", "same-key ECG exists but assignment was not unique"
        elif valid and not date:
            status, reason = "UNRESOLVED", "filename has no unique valid recording date"
        rows.append({"pair_id": f"{dataset}_{len(rows)+1:06d}", "dataset": dataset,
                     "ecg_path": "", "xml_path": rel(xml),
                     "canonical_patient_id": canonical_id(pid), "ecg_patient_id": "",
                     "xml_patient_id": pid, "ecg_date": "", "xml_date": date or "",
                     "status": status, "confidence": "NONE", "reason": reason,
                     "ecg_bytes": "", "xml_bytes": xml.stat().st_size,
                     "candidate_paths": " | ".join(rel(path) for path in candidates)})

META.mkdir(parents=True, exist_ok=True)
fields = ["pair_id", "dataset", "ecg_path", "xml_path", "canonical_patient_id",
          "ecg_patient_id", "xml_patient_id", "ecg_date", "xml_date", "status",
          "confidence", "reason", "ecg_bytes", "xml_bytes", "candidate_paths"]
output = args.output
with output.open("w", newline="", encoding="utf-8") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)
print(f"Wrote {len(rows)} manifest rows to {output}")
