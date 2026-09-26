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

## 3b. Concept status 三态语义

概念 `status` 枚举为三态，按证据强度使用，不要一律填同一值：

- `SOURCE_CONFIRMED` — 定义逐字/直接取自绑定官方课程的讲义/笔记/课表，可逐条溯源。仅当确有官方原文支撑时使用（如 CS336 的逐字课表投影）。
- `TEACHING_RECONSTRUCTION` — 由公开课程主题 + 标准领域知识综合而成的教学重构（本仓库绝大多数概念的正确状态）。
- `HYPOTHESIS` — 未经官方来源核实、仅为合理推测的概念或关系，必须显式标注，不得当作已确认知识。

当前 11 包概念均为 `TEACHING_RECONSTRUCTION`（诚实默认）。若后续为某概念补上逐字官方依据，应升级为 `SOURCE_CONFIRMED`；无法核实的推测应降为 `HYPOTHESIS`。

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