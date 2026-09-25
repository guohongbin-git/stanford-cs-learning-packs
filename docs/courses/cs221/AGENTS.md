# AGENTS.md — CS221: Artificial Intelligence: Principles and Techniques (Autumn 2021)

> **Scope:** Stanford CS221 · Autumn 2021 only
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** Stanford Online Autumn 2021 recordings (archive_official) + cs221.stanford.edu public materials
> **Important:** reading this package is not proof that a human or agent can formalize, solve, or justify AI problems.

## 1. Purpose
Turns the public Stanford CS221 Autumn 2021 course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
Locked to Autumn 2021. Anchor: Stanford Online CS221 playlist plus the public course site. Do not silently merge newer offerings; AI course emphases (LLM agents, modern RL) evolve and newer material must be labelled separately.

## 3. Read Order
1. this file; 2. course_ir.json; 3. concepts.json; 4. the HTML as projection only; 5. package_manifest.json for integrity.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION. Teaching text is synthesized from the confirmed Autumn 2021 topic structure plus standard AI theory. Not a verbatim transcript. Lecture-topic labels derived from week themes are marked `official: false`.

## 5. Agent Use Contract
State knowledge_used (concept + week + status), assumptions (e.g. admissibility of a heuristic, discount factor, independence assumptions in a Bayes net), failure_conditions, verification (check optimality or consistency on a small case), escalation.

## 6. Suitable Uses
Explaining search, MDP, RL, utility, games, Bayesian networks, logic and planning; comparing formalizations; generating practice problems; grounding shared vocabulary for AI projects.

## 7. Prohibited Uses
Do not quote reconstruction as Stanford lecture text; do not present a heuristic or model as correct without stating its assumptions; do not claim mastery from reading; do not overwrite current authoritative documentation.

## 8. Concept Usage Rules
Check definition, why, failure conditions, example, relations, week context. Example: "A Star Search" is optimal only with an admissible (and for graph search, consistent) heuristic — presenting A* as unconditionally optimal is a documented failure condition.

## 9. Human vs Agent View
Same concept identity, different projections. Human view: intuition, examples, pitfalls in Chinese. Agent view: canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. Package quizzes demonstrate local comprehension only.

## 11. Skill Formation
Concept clusters (State Space + A Star Search + Heuristic Function) may suggest candidate skills like "FormalizeAndSolveSearchProblem", promoted only after transfer to a new domain.

## 12. Escalation Principle
Escalate when assumptions are unverified (admissibility, independence, stationarity), when a decision has high impact, or when the package conflicts with current authoritative sources. "I do not know" is acceptable.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name = key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks reference w1..w9 and must match course_ir. relations targets must resolve. Regenerate manifest sha256 after every change.
