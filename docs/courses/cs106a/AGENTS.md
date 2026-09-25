# AGENTS.md — CS106A: Programming Methodology (SEE Official, Java)

> **Scope:** Stanford CS106A · SEE official recording (Java edition, Mehran Sahami)
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** SEE.stanford.edu official CS106A course (Java) + web.stanford.edu class archive
> **Important:** reading this package is not proof that a human or agent can write, design, or debug programs.

## 1. Purpose
Turns the official SEE CS106A Java course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
Locked to the SEE (Java) edition. Current Stanford CS106A teaches Python with different assignments and libraries; do not mix Python-era material into this package. Newer offerings must be labelled separately if ever added.

## 3. Read Order
1. this file; 2. course_ir.json; 3. concepts.json; 4. the HTML as projection only; 5. package_manifest.json for integrity.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION: teaching text is synthesized from the confirmed SEE Java syllabus plus standard introductory-programming practice. Not a verbatim transcript.

## 5. Agent Use Contract
State knowledge_used (concept + week + status), assumptions (language edition, library version), failure_conditions, verification (simple runnable check or hand trace), escalation when the question targets modern Python-era CS106A or Java version specifics outside this package.

## 6. Suitable Uses
Explaining programming fundamentals, control flow, decomposition, data structures, OOP and debugging; generating practice exercises; grounding beginner-level instruction.

## 7. Prohibited Uses
Do not present reconstruction as lecture text; do not claim current CS106A syllabus coverage (it is now Python); do not assert mastery from reading; do not use as the sole reference for production Java design.

## 8. Concept Usage Rules
Check definition, why, failure conditions, example, relations, week context. Example: "Loop Invariant" must hold before and after every iteration, not merely at termination — confusing the two is a documented failure condition.

## 9. Human vs Agent View
Same concept identity, different projections. Human view: intuition, examples, pitfalls in Chinese. Agent view: canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. Package quizzes demonstrate local comprehension only.

## 11. Skill Formation
Concept clusters (Method Decomposition + Control Flow + Debugging) may suggest candidate skills like "DecomposeAndImplementSmallProgram", promoted only after transfer to a new problem.

## 12. Escalation Principle
Escalate when the task requires current-edition APIs, when a design decision has real maintenance cost, or when the package conflicts with the learner's actual course materials. "I do not know" is acceptable.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name = key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks reference w1..w9 and must match course_ir. relations targets must resolve. Regenerate manifest sha256 after every change.
