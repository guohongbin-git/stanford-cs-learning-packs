# CS107 Course Pack · SEE Official · v0.1

Stanford CS107 (Programming Paradigms, SEE official edition) human/agent co-learning package.

## Contents
- `CS107_interactive_SEE_v0.1.html` — self-contained interactive course (runtime-rendered from embedded JSON, zero external references)
- `course_ir.json` — 9-week structure (objectives, pitfalls, quizzes, agent contracts)
- `concepts.json` — 26 canonical concepts (name ids, typed relations, non-empty weeks)
- `AGENTS.md` — 14-section agent contract, version-locked to the SEE edition
- `package_manifest.json` — bytes + sha256 per file

## How to use
Open the HTML. Weeks render from embedded data; click concept chips for the Human/Agent drawer; quizzes update progress in localStorage.

## How to extend
1. Add concepts to `concepts.json` (10 schema fields; id = concept name; weeks reference w1..w9).
2. Reference them from the matching `course_ir.json` week.
3. Re-embed both JSONs into the HTML `#cs107-data` block and regenerate the manifest.

## Version boundary
SEE edition (archive_official). The current CS107 has updated toolchains and assignments; this package deliberately does not mix editions.

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.

## Repair log round 11 (2026-09-25)
- Added 4 SEE-core system concepts missing from the concept set (Void Pointer and Generic Functions, memcpy and memmove, Generic Linear Search, Activation Record Layout), each bound to its week and relation-linked; concept count 26 → 30.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
