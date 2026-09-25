# AGENTS.md — CS224W: Machine Learning with Graphs (Autumn 2021)

> **Scope:** Stanford CS224W · Autumn 2021 only
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** Stanford Online Autumn 2021 recordings (archive_official) + cs224w.stanford.edu public materials
> **Important:** reading this package is not proof that a human or agent can model, train, or evaluate graph learning systems.

## 1. Purpose
Turns the public Stanford CS224W Autumn 2021 course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
Locked to Autumn 2021. Anchor: Stanford Online CS224W playlist plus the public course site. Do not silently merge newer offerings; the GNN ecosystem (graph transformers, temporal and heterogeneous stacks) evolves quickly.

## 3. Read Order
1. this file; 2. course_ir.json; 3. concepts.json; 4. the HTML as projection only; 5. package_manifest.json for integrity.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION: teaching text is synthesized from the confirmed Autumn 2021 topic structure plus standard graph-learning knowledge. Not a verbatim transcript.

## 5. Agent Use Contract
State knowledge_used (concept + week + status), assumptions (graph type, homophily, layer count, aggregation), failure_conditions, verification (check on a small graph or compare with a known baseline), escalation when claims exceed what a message-passing GNN of bounded depth can express.

## 6. Suitable Uses
Explaining node embeddings, message passing, GNN architectures, expressive-power limits, knowledge graphs and graph generation; generating practice problems; grounding team vocabulary for relational ML.

## 7. Prohibited Uses
Do not present reconstruction as lecture text; do not claim a GNN separates structures beyond its Weisfeiler-Lehman bound; do not assert mastery from reading; do not treat Autumn 2021 model comparisons as current state of the art.

## 8. Concept Usage Rules
Check definition, why, failure conditions, example, relations, week context. Example: "Over-smoothing" means deep message passing makes node representations converge — adding layers is not automatically more expressive, which is a documented failure condition.

## 9. Human vs Agent View
Same concept identity, different projections. Human view: intuition, examples, pitfalls in Chinese. Agent view: canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. Package quizzes demonstrate local comprehension only.

## 11. Skill Formation
Concept clusters (Message Passing + Graph Pooling + Expressiveness) may suggest candidate skills like "DesignAndBoundGNN", promoted only after transfer to a new graph domain.

## 12. Escalation Principle
Escalate when the task depends on graphs beyond the WL bound, on temporal or heterogeneous specifics not covered, or when a modelling choice has high impact. "I do not know" is acceptable.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name = key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks reference w1..w9 and must match course_ir. relations targets must resolve. Regenerate manifest sha256 after every change.
