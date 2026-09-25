# AGENTS.md — CS336: Language Modeling from Scratch (Spring 2025)

> **Scope:** Stanford CS336 · Spring 2025 only  
> **Package role:** Shared Learning Source Package for humans and agents  
> **Evidence boundary:** 17 Stanford Online core recordings + archived Spring 2025 course site/coursework.  
> **Important:** Reading this package is not proof that a human or agent can build, train, optimize, evaluate, or align a language model.

## 1. Purpose

This repository turns the public **Stanford CS336 Spring 2025** course into a shared human/agent learning package. It exists to preserve a single semantic identity for concepts while supporting two projections:

- humans: Chinese teaching view, examples, failure modes, quizzes;
- agents: canonical concept JSON, course IR, evidence anchors, workflow contracts.

Keep these separations strict:

1. **Source ≠ Knowledge**
2. **Knowledge ≠ Capability**
3. **Course completion ≠ Mastery**

## 2. Version Boundary

This package is locked to **Spring 2025**.

Canonical version anchors:

- Archived course site: https://cs336.stanford.edu/spring2025/
- Stanford Online playlist (17 core lectures): https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_
- Spring 2025 lecture materials: https://github.com/stanford-cs336/spring2025-lectures

Do not silently merge Spring 2026 material. The official assignment repositories are live and may now default to newer offerings; use the archived Spring 2025 course page to bind assignment scope to this package version.

The Spring 2025 schedule contains 19 class meetings. This package models the 17 recorded core lectures as 9 teaching weeks. The May 29 (Junyang Lin) and June 3 (Mike Lewis) guest lectures are retained as supplemental schedule events, not invented as members of the 17-video core playlist.

## 3. Agent Read Order

1. Read `AGENTS.md`.
2. Read `course_ir.json` for the 9-week teaching sequence, lecture anchors, coursework, quizzes, and week-level agent contracts.
3. Read `concepts.json` for canonical concept records and typed relations.
4. Use `CS336_interactive_Spring2025_v0.1.html` as a projection of the same JSON, not as an independent truth source.
5. Consult `qa/schema.md` before changing schema or writing parsers.

## 4. Evidence Semantics

Concept records use:

`status: TEACHING_RECONSTRUCTION`

This means the teaching explanation is synthesized from the confirmed Spring 2025 topic/coursework structure and general technical knowledge. It is **not** a verbatim Stanford transcript or faculty quotation.

Use these statuses consistently:

- `SOURCE_CONFIRMED`: directly verified in an identified public source.
- `TEACHING_RECONSTRUCTION`: pedagogical synthesis grounded in the verified course structure.
- `DERIVED`: inference from course knowledge.
- `HYPOTHESIS`: plausible but unvalidated.
- `VALIDATED`: passed an explicit external evaluation.

Never silently promote one status to another.

## 5. Agent Use Contract

When this package materially informs work, the agent should be able to expose internally:

```yaml
knowledge_used:
  - concept: Scaling Law
    source_weeks: ["Lecture 9", "Lecture 11", "Assignment 3"]
    status: TEACHING_RECONSTRUCTION
assumptions:
  - "Pilot runs are representative enough for the proposed extrapolation."
failure_conditions:
  - "Architecture or data distribution changes outside the fitted regime."
verification:
  - "Check residuals and validate against held-out scale points."
escalation:
  - "Do not commit a large compute budget when the extrapolation is weak or contradictory."
```

## 6. Safe Uses

Use the package to:

- explain how language models are built end-to-end;
- reason about tokenizer/model/training/system/data/alignment tradeoffs;
- create candidate implementation or evaluation plans;
- generate training exercises and transfer tests;
- identify likely bottlenecks and failure modes;
- share a common vocabulary between humans and agents.

## 7. Prohibited Overclaims

Do not use the package alone to:

- claim a production LM implementation is correct;
- claim GPU/distributed code is numerically correct or performant without measurement;
- claim a scaling-law extrapolation is valid outside its measured regime;
- claim a benchmark proves general intelligence or safety;
- claim an alignment method is safe because training reward increased;
- claim Stanford faculty stated a `TEACHING_RECONSTRUCTION` explanation verbatim;
- claim an agent has mastered CS336 after ingesting the package.

## 8. Canonical Concept Contract

`concepts.json` is canonical. Every record must include:

```yaml
id: <canonical English concept identity; equals object key>
type: Concept
status: TEACHING_RECONSTRUCTION
definition: <teaching definition>
why: <why it matters>
failure_conditions: <misuse / failure modes>
example: <concrete example>
relations:
  - relation: <label>
    kind: prerequisite | related_to | opposes | enables
    target: <canonical concept id>
weeks:
  - Week N
source_weeks:
  - Lecture N | Assignment N
```

Rules:

- `weeks` and `source_weeks` must be non-empty.
- `relations[].target` must resolve to another concept key.
- A cross-week concept is one canonical concept with all actual weeks enumerated.
- Do not create week-specific duplicates of the same concept.

## 9. Human View vs Agent View

Human and Agent views share the same concept identity.

Human view emphasizes:

- intuition;
- Chinese explanation;
- examples;
- failure modes;
- transfer questions.

Agent view renders the canonical JSON record directly.

The HTML must not manufacture a second agent-only schema.

## 10. HTML Synchronization Contract

The HTML contains one self-contained data block:

```html
<script type="application/json" id="cs336-data">{"course_ir": ..., "concepts": ...}</script>
```

The UI renders weeks, concept drawer, agent view, and quizzes from that payload. There are no independent hard-coded `conceptData`, `courseIR`, or `quizzes` truth blocks.

When `course_ir.json` or `concepts.json` changes, re-embed the payload and rerun QA before release.

## 11. Capability Rule

Reading is not learning evidence.

Required promotion path:

`Knowledge → Practice → External Feedback → Assessment → Transfer Test → Capability`

A quiz in this package measures local comprehension only.

For example, access to `FlashAttention` knowledge does not prove the agent can implement a correct Triton kernel; access to `GRPO` knowledge does not prove it can run stable RL training.

## 12. Course-Specific Mental Model

```text
Raw Data
  ↓
Tokenizer
  ↓
Transformer + Optimizer
  ↓
GPU Kernels + Distributed Training
  ↓
Scaling Decisions
  ↓
Inference + Evaluation
  ↓
Data Curation
  ↓
SFT / RLHF / Reasoning RL
  ↓
Measured Model Behavior
```

The course is deliberately end-to-end. A decision in one layer can move cost, risk, or failure into another.

## 13. Escalation Principle

Escalate when:

- numerical equivalence is not verified;
- profiler evidence contradicts the proposed bottleneck;
- scaling extrapolation is outside observed support;
- benchmark contamination is plausible;
- dataset provenance is missing;
- RL reward and independent evaluation diverge;
- compute/security/production risk exceeds authority.

“I do not know” is an acceptable state.

## 14. Update Rule

New experiments do not silently rewrite canonical knowledge.

Use:

`Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge / Skill`

Spring 2026 content must enter a separate package/version before any cross-version synthesis.

## 15. Output Discipline

When using this package to support work, expose:

- task framing;
- relevant canonical concepts;
- assumptions;
- measured/available evidence;
- failure modes;
- verification plan;
- escalation boundary.

Do not merely repeat CS336 terminology.
