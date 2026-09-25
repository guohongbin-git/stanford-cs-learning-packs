# AGENTS.md — CS109: Probability for Computer Scientists (Autumn 2022)

> **Scope:** Stanford CS109 · Autumn 2022 only
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** Stanford Online Autumn 2022 recordings (archive_official) + cs109.stanford.edu public materials
> **Important:** reading this package is not proof that a human or agent can model, derive, or reason under uncertainty.

## 1. Purpose
This repository turns the public Stanford CS109 Autumn 2022 course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
This package is locked to Autumn 2022 (Chris Piech). Canonical anchors: Stanford Online CS109 playlist; cs109.stanford.edu public schedule and notes. Do not silently merge newer offerings: CS109 assignments and probability applications evolve.

## 3. Read Order
1. this file; 2. course_ir.json (9-week sequence, quizzes, agent contracts); 3. concepts.json (canonical records, typed relations); 4. the HTML as a projection only; 5. qa output for validation evidence.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION: teaching text is synthesized from the confirmed Autumn 2022 topic structure plus standard probability theory. It is not a verbatim transcript, and lecture-topic labels derived from week themes are marked `official: false`.

## 5. Agent Use Contract
When this package materially informs an answer, state: knowledge_used (concept + source week + status), assumptions (e.g. independence or identical-distribution assumptions), failure_conditions, verification (check the formula against a small case), escalation.

## 6. Suitable Uses
Explaining probability concepts; building intuition for distributions, expectation, limiting theorems; generating practice problems; grounding shared team vocabulary for ML/data work.

## 7. Prohibited Uses
Do not present reconstruction as Stanford lecture text; do not use the package alone to certify safety-critical statistical decisions; do not claim mastery from reading; do not overwrite current authoritative documentation.

## 8. Concept Usage Rules
Before applying a concept, check definition, why, failure conditions, example, relations, and week context. Example: "Independence" is not "uncorrelated" — it requires P(A∩B)=P(A)P(B), and mistaking the two is a documented failure condition.

## 9. Human vs Agent View
Same concept identity, different projections. Human view emphasizes intuition, concrete examples and pitfalls; agent view emits the canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Sequence: Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. A quiz in this package demonstrates local comprehension only.

## 11. Skill Formation
Concepts (Conditional Probability + Bayes Rule + Estimator) may suggest candidate skills such as "UpdateBeliefFromEvidence", promoted only after transfer to a new dataset or problem domain.

## 12. Escalation Principle
Escalate when assumptions are unverified (independence, identical distribution), when a statistical claim would drive high-impact decisions, or when the package conflicts with current authoritative sources. "I do not know" is an acceptable state.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable course knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name, must equal key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks must be non-empty w1..w9 keys matching course_ir. relations targets must resolve within the concept set. Manifest sha256 must be regenerated on every change.
