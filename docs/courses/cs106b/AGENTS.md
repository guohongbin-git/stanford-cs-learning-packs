# AGENTS.md — CS106B: Programming Abstractions (SEE Official, C++)

> **Scope:** Stanford CS106B · SEE official recording (C++ edition, Julie Zelenski)
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** SEE.stanford.edu official CS106B course (C++, Julie Zelenski) + web.stanford.edu class archive
> **Important:** reading this package is not proof that a human or agent can write, design, or debug programs.

## 1. Purpose
Turns the official SEE CS106B (C++) course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
Locked to the SEE (C++) edition. Current Stanford CS106B uses updated libraries (e.g. Stanford C++ library) and different assignments; do not mix newer material into this package.

## 3. Read Order
1. this file; 2. course_ir.json; 3. concepts.json; 4. the HTML as projection only; 5. package_manifest.json for integrity.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION: teaching text is synthesized from the confirmed SEE C++ syllabus plus standard introductory-programming practice. Not a verbatim transcript.

## 5. Agent Use Contract
State knowledge_used (concept + week + status), assumptions (language edition, library version), failure_conditions, verification (simple runnable check or hand trace), escalation when the question targets modern Python-era CS106B or C++/library version specifics outside this package.

## 6. Suitable Uses
Explaining recursion, backtracking, algorithm analysis, ADTs, graph algorithms and memory concepts; generating practice exercises; grounding intermediate programming instruction.

## 7. Prohibited Uses
Do not present reconstruction as lecture text; do not claim current CS106B syllabus/library coverage; do not assert mastery from reading; do not use as the sole reference for production C++ design.

## 8. Concept Usage Rules
Check definition, why, failure conditions, example, relations, week context. Example: "Recursion" requires a reachable base case; and "Memoization" only helps when subproblems actually repeat — both are documented failure conditions.

## 9. Human vs Agent View
Same concept identity, different projections. Human view: intuition, examples, pitfalls in Chinese. Agent view: canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. Package quizzes demonstrate local comprehension only.

## 11. Skill Formation
Concept clusters (Recursion + Memoization + Algorithm Analysis) may suggest candidate skills like "DesignAndAnalyzeRecursiveSolution", promoted only after transfer to a new problem.

## 12. Escalation Principle
Escalate when the task requires current-edition APIs, when a design decision has real maintenance cost, or when the package conflicts with the learner's actual course materials. "I do not know" is acceptable.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name = key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks reference w1..w9 and must match course_ir. relations targets must resolve. Regenerate manifest sha256 after every change.
