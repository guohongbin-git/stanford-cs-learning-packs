# AGENTS.md — Global Learning Constitution

> Scope: every course pack under `docs/courses/` in this repository.
> A course pack may add its own `AGENTS.md` with course-specific rules; that file refines this one and never contradicts it.

## 1. Purpose

This repository holds **shared learning source packs** built from public Stanford course material. Each pack supports two projections of one knowledge base:

- human projection — an interactive HTML teaching view;
- agent projection — canonical `course_ir.json` and `concepts.json`.

Keep these separations strict:

1. **Source ≠ Knowledge** — the public course (videos, pages) is a source; the pack is a reconstruction.
2. **Knowledge ≠ Capability** — holding a concept record is not evidence of being able to do the work.
3. **Course completion ≠ Mastery** — reading or passing a pack quiz proves local comprehension only.

## 2. Read order for agents

1. this file;
2. the pack's own `AGENTS.md` (version boundary and course-specific rules);
3. `course_ir.json` (weekly structure, objectives, failure modes, quizzes, agent contracts, lecture/talk evidence);
4. `concepts.json` (canonical concept records and typed relations);
5. the interactive HTML **only as a projection** — never treat its wording as a stronger source than the JSON;
6. `package_manifest.json` to verify file integrity.

## 3. Evidence semantics

- `status: TEACHING_RECONSTRUCTION` — teaching text synthesised from the confirmed public course structure plus standard domain knowledge. Never quote it as a Stanford lecture transcript.
- Lecture / talk entries: `official: true` means the title is taken verbatim from the bound official page; `official: false` means it is a derived topic label. Do not upgrade a derived label to a verbatim claim.
- Material binding: `active_recent` (public recordings from the last three academic years) or `archive_official` (the best public version of that course). Never mix a newer offering's material into a pack without relabelling it.

When answering with this material, state:

```yaml
knowledge_used: [{concept, source_week, status}]
assumptions: [...]
failure_conditions: [...]
verification: [...]
escalation: [...]
```

## 4. Concept usage rules

Before applying a concept, read its `definition`, `why`, `failure_conditions`, `example`, `relations` and `weeks`. A concept is a decision aid, not a label: if the failure conditions hold, do not apply it.

## 5. Capability rule

Knowledge → Practice → External Feedback → Assessment → Transfer Test → Capability. A pack quiz is an assessment artifact, not a transfer test. Do not claim mastery from ingestion.

## 6. Cross-pack rules

- Concept ids are canonical English identity keys; the same id in two packs refers to the same idea. Divergent definitions are a defect — report them rather than picking one silently.
- Week/theme membership must stay bidirectionally consistent between `concepts.json` and `course_ir.json`.
- Relation targets must resolve inside the same pack.
- When a pack is repaired, append to its `README.md` Repair log and regenerate `package_manifest.json`. Never rewrite stable knowledge silently.

## 7. Escalation

Escalate when: evidence is missing or contradictory; the task is high-impact and not safely reversible; required authority is absent; the pack's claims conflict with current authoritative documentation. "I do not know" is an acceptable state.