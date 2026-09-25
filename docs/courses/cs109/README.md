# CS109 Course Pack · Autumn 2022 · v0.1

Stanford CS109 (Probability for Computer Scientists, Autumn 2022) human/agent co-learning package.

## Contents
- `CS109_interactive_Autumn2022_v0.1.html` — self-contained interactive course (runtime-rendered from embedded JSON, no external references)
- `course_ir.json` — 9-week structure with objectives, pitfalls, quizzes, agent contracts
- `concepts.json` — 35 canonical concepts (name ids, typed relations, non-empty weeks)
- `AGENTS.md` — 14-section agent contract, version-locked to Autumn 2022
- `package_manifest.json` — sha256 for every file

## How to use
Open the HTML in a browser. Weeks render from the embedded data; click concept chips for the Human/Agent drawer; quizzes update progress in localStorage.

## How to extend
1. Add a concept to `concepts.json` (all 10 schema fields; id = concept name; weeks must reference w1..w9).
2. Reference it from the relevant `course_ir.json` week's `concepts` array.
3. Re-embed both JSONs into the HTML `#cs109-data` block and regenerate the manifest.

## Version boundary
Autumn 2022 (archive_official). Lecture-topic labels derived from week themes are marked `official: false`; the canonical video source is the Stanford Online CS109 Autumn 2022 playlist.

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
