# CS106A Course Pack · SEE Official (Java) · v0.1

Stanford CS106A (Programming Methodology, SEE official Java edition) human/agent co-learning package.

## Contents
- `CS106A_interactive_SEE_v0.1.html` — self-contained interactive course (runtime-rendered from embedded JSON, zero external references)
- `course_ir.json` — 9-week structure (objectives, pitfalls, quizzes, agent contracts)
- `concepts.json` — 43 canonical concepts (name ids, typed relations, non-empty weeks)
- `AGENTS.md` — 14-section agent contract, version-locked to the SEE Java edition
- `package_manifest.json` — bytes + sha256 per file

## How to use
Open the HTML. Weeks render from embedded data; click concept chips for the Human/Agent drawer; quizzes update progress in localStorage.

## How to extend
1. Add concepts to `concepts.json` (10 schema fields; id = concept name; weeks reference w1..w9).
2. Reference them from the matching `course_ir.json` week.
3. Re-embed both JSONs into the HTML `#cs106a-data` block and regenerate the manifest.

## Version boundary
SEE Java edition (archive_official). The current CS106A teaches Python; this package deliberately does not mix editions.

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
