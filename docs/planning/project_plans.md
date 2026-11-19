# Project plans

<!--
AGENT NOTES: This file holds all project context, background info, requirements, ideas and decisions.
Ongoing tasks live in TODO.md (same folder), not here. Read this file first for context.
When adding an entry to "Ideas", "Decisions" or "General notes", include the date.
-->

## Project context

- **Project:** 10699. AI analyzer for Holter ECG signals
- **Lab:** High-Speed Digital Systems Lab (HSDSL)
- **Type:** General
- **Contact (supervisor):** Boaz Mizrachi - boazm@ee.technion.ac.il
- **Summary:** For revolutionary research in Rambam hospital, we are developing an AI tool to analyze signals taken from a heart monitoring device, in order to identify early signs of heart disease.
- **Data source:** A Holter device attached to the patient over a 24H period. The system collects signals from 12 probes mounted on different areas of the body. (The project description in the source image was cut off after "...in the", so the rest is unknown.)

## Goals and requirements

- Boaz mainly wants a ready-made product with a GUI. We need to define (characterize) what it does.
- We can explore what to build on our own, together with the other students working on this.

## Facts and constraints

- There are 12 independent channels.

## Research topics

- Heart conditions: Long QT, Brugada. Possibly Yoav's lab pages.
- Signal processing for ECG.

## Ideas

<!-- Ideas for what to build or try. Add the date to each entry. -->

## Decisions

<!-- Decisions we've made and why. Add the date to each entry. -->

## General notes

<!-- Free-form comments, meeting summaries, links. Add the date to each entry. -->

### 2026-11-19 — Prior work and data context

- Noam is a former student who worked on this project. His project references and report are stored under `docs/refs/Noam_project/`.
- The report documents work on the public LUDB and ISP databases. These provide ECG-wave annotations for four segmentation classes: P-wave, QRS complex, T-wave, and background. The report describes Long QT analysis using these online datasets.
- The report separately documents a clinical Brugada dataset derived from ISHNE Holter recordings annotated by cardiologists at Rambam, with Brugada Type 1 windows extracted for classification. The report says this dataset contained 273 patient windows. Confirm that this is the same classified Brugada data currently available to us.
- The report documents an approximately **30 ms** systematic QT/QTc measurement offset during clinical validation, not a 20 µs classification error. Treat the remembered 20 µs figure as unconfirmed until the report or source code establishes it.
- Boaz said that classified Long QT data may not be available. The clinical priority is Brugada, while Long QT is considered the easier project. Confirm the Long QT data situation with the doctor before planning around it.
- Miri is the doctor and clinical specialist for the project. Prepare the questions in `docs/planning/questions.md` before meeting with her and record her answers in the planning documents.
- The current reported data count is 12 Long QT recordings versus 120 Brugada recordings. Confirm the counts, labels, and patient-level independence before choosing the primary task.
- The available Brugada recordings appear to be Type 1 only. This must be validated with Miri and against the actual annotations before defining the classification target.
- Further coordination is needed with Amit and with Inbar, a former student.
