# AGENTS.md — CS107: Programming Paradigms (SEE Official)

> **Scope:** Stanford CS107 · SEE official recording (C / systems layer)
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** SEE.stanford.edu + web.stanford.edu class archive for CS107
> **Important:** reading this package is not proof that a human or agent can reason about machine-level behaviour or write safe systems code.

## 1. Purpose
Turns the official SEE CS107 course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
Locked to the SEE edition (C / systems layer). Current CS107 uses updated toolchains and assignments; do not mix newer material into this package.

## 3. Read Order
1. this file; 2. course_ir.json; 3. concepts.json; 4. the HTML as projection only; 5. package_manifest.json for integrity.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION: teaching text is synthesized from the confirmed SEE syllabus plus standard systems-programming knowledge. Not a verbatim transcript.

## 5. Agent Use Contract
State knowledge_used (concept + week + status), assumptions (architecture, word size, compiler flags), failure_conditions, verification (hand trace, disassembly or sanitizer reasoning), escalation when behaviour depends on unspecified/undefined semantics or on a specific toolchain.

## 6. Suitable Uses
Explaining bit-level representation, assembly correspondence, stack/heap behaviour, memory safety, caching and virtual memory; generating systems exercises; grounding low-level debugging discussions.

## 7. Prohibited Uses
Do not present reconstruction as lecture text; do not claim behaviour that C leaves undefined as guaranteed; do not assert mastery from reading; do not use as sole reference for production systems programming.

## 8. Concept Usage Rules
Check definition, why, failure conditions, example, relations, week context. Example: signed integer overflow is undefined behaviour — optimisation may legally delete checks that rely on it, which is a documented failure condition, not a curiosity.

## 9. Human vs Agent View
Same concept identity, different projections. Human view: intuition, examples, pitfalls in Chinese. Agent view: canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. Package quizzes demonstrate local comprehension only.

## 11. Skill Formation
Concept clusters (Pointer Arithmetic + Heap Allocation + Undefined Behavior) may suggest candidate skills like "DiagnoseMemoryDefect", promoted only after transfer to a new codebase.

## 12. Escalation Principle
Escalate when the question depends on undefined behaviour, on a specific compiler/architecture, or when a memory-safety claim would drive high-impact decisions. "I do not know" is acceptable.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name = key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks reference w1..w9 and must match course_ir. relations targets must resolve. Regenerate manifest sha256 after every change.
