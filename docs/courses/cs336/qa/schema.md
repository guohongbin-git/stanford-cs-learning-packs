# CS336 Course Package Schema · Spring 2025 · v0.1

## Truth-source rule

The external `course_ir.json` and `concepts.json` are canonical package files. The HTML contains one exact semantic snapshot:

```html
<script type="application/json" id="cs336-data">{"course_ir": ..., "concepts": ...}</script>
```

The UI derives week rendering, quizzes and concept projections from that payload.

## course_ir.json

Top-level required fields:

- `course`
- `title`
- `term`
- `version`
- `evidence_status`
- `version_boundary`
- `public_materials`
- `weeks`
- `assignments`

Each week includes:

- `id`, `label`, `title`, `part`
- `lectures[]`
- `question`, `why`
- `objectives[]`
- `concepts[]`
- `model_title`, `model_nodes[]`
- `example`, `pitfalls[]`
- `quiz {q, choices, correct, explain}`
- `agent {goal, inputs, actions, evidence, risks}`
- `assignment_ties[]`
- `evidence_status`

## concepts.json

Each concept object includes:

- `id`: canonical English identity, equal to top-level key
- `type`: `Concept`
- `status`: `TEACHING_RECONSTRUCTION`
- `definition`
- `why`
- `failure_conditions`
- `example`
- `relations[]`: `{relation, kind, target}`
- `weeks[]`: explicit Human curriculum locations
- `source_weeks[]`: lecture/assignment evidence anchors

Supported relation kinds in v0.1:

- `prerequisite`
- `related_to`
- `opposes`
- `enables`

All relation targets must resolve to canonical ids.

## Quiz derivation

There is no independent quiz constant. JavaScript derives:

```js
const quizzes = Object.fromEntries(courseIR.weeks.map(w => [w.id, w.quiz]));
```

## Version boundary

All source claims in this package are bound to Spring 2025. Newer course material requires a new package/version.
