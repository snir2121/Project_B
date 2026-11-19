# General Project Information

## Project context

- **Project:** 10699 — AI analyzer for Holter ECG signals
- **Institution:** Technion — Israel Institute of Technology
- **Laboratory:** High-Speed Digital Systems Laboratory (HSDSL)
- **Project type:** General
- **Supervisor:** Boaz Mizrachi — boazm@ee.technion.ac.il
- **Summary:** The project develops an AI tool for analyzing signals collected from a heart-monitoring device, with the goal of identifying early signs of heart disease and supporting revolutionary research at Rambam Hospital.
- **Data source:** A Holter device worn by a patient for approximately 24 hours. The system collects signals from 12 probes attached to different areas of the body. The source project description was cut off after “...in the”, so the remaining text is unknown.

## Project-specific context for agents

- **Mony:** Laboratory administrator.
- **Boaz Mizrachi:** Project instructor/mentor and a friend of the doctor; supervisor contact is listed above.
- **The doctor:** A heart-disease specialist at Rambam Hospital. The project supports her work by helping classify heart diseases; it is not a substitute for clinical diagnosis.
- Noam is a former student who worked on this project. His report and reference materials are in `docs/refs/Noam_project/`.
- Noam used the public LUDB and ISP ECG databases for annotated wave-segmentation work. Their four target classes are P-wave, QRS complex, T-wave, and background. His report also describes a separate clinically annotated Brugada dataset from ISHNE/Rambam recordings.
- The report confirms an approximately 30 ms QT/QTc measurement offset during clinical validation. Do not repeat the remembered 20 µs figure as fact without verifying it.
- Boaz indicated that classified Long QT data may not exist. Confirm this with the doctor before assuming it is available. Brugada is currently the more important clinical priority, although Long QT may be technically easier.

## Intended system

The project will develop a heart-disease classifier to help a cardiac specialist assess whether a patient may be predisposed to a specific heart disease. The system is intended to support clinical specialists; it is not a replacement for medical diagnosis.

## Repository organization

- `docs/lab_docs/`: Administrative documents from the Technion laboratory, including rules, assignments, submission requirements, and dates. Some dates may refer to 2025 and may not apply to the current academic year.
- `docs/refs/`: Documentation, papers, and work from other projects that may serve as references.
- `docs/presentations_and_reports/`: Presentations and reports prepared for submission during the course.
- `docs/research/`: Research notes, literature reviews, experiments, and other research documents for this project.
- `docs/planning/`: Plans, milestones, task tracking, and project-management documents.
- `organizations/`: Information about relevant organizations and institutions, such as the Technion, HSDSL, and Rambam Hospital.
- `skills/`: Project-specific instructions and skills for coding agents. Add each reusable agent skill as a separate Markdown file.
- `data/`: Dataset-related files. Keep raw and processed data separated; do not commit private patient data or other sensitive clinical information.
- `src/`: Source code.
- `models/`: Model definitions, checkpoints, and model-related documentation.
- `tests/`: Automated tests and validation code.

## Collaborators and Git workflow

- **Snir:** `snir2121`
- **Yoav:** `yoavGT`

Snir and Yoav work independently from separate computers using Git and the shared GitHub repository. Before starting work, run `git pull`. After making a coherent change, run `git add`, `git commit`, and `git push`. Use descriptive commit messages and pull again before pushing if the remote has changed. Do not commit credentials, private patient data, or unverified medical claims.
