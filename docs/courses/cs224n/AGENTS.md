# AGENTS.md — CS224N: NLP with Deep Learning (Winter 2021)

> **Scope:** Stanford CS224N · Winter 2021 only
> **Package role:** shared learning source for humans and agents
> **Evidence boundary:** Stanford Online Winter 2021 recordings (archive_official) + web.stanford.edu/class/cs224n public materials
> **Important:** reading this package is not proof that a human or agent can build, train, or evaluate NLP systems.

## 1. Purpose
Turns the public Stanford CS224N Winter 2021 course into a shared human/agent learning package. Humans read the Chinese teaching projection; agents read canonical concept JSON and course IR. Source ≠ Knowledge, Knowledge ≠ Capability, Course completion ≠ Mastery.

## 2. Version Boundary
Locked to Winter 2021. Anchor: Stanford Online CS224N playlist plus the public course site. Do not silently merge newer offerings: pretrained-model ecosystems (BERT variants, LLM era) evolve quickly and newer material must be labelled separately.

## 3. Read Order
1. this file; 2. course_ir.json (9-week sequence, quizzes, agent contracts); 3. concepts.json (canonical records with typed relations); 4. the HTML as projection only; 5. package_manifest.json for integrity.

## 4. Evidence Semantics
Concept records use status TEACHING_RECONSTRUCTION: teaching text is synthesized from the confirmed Winter 2021 topic structure plus standard deep-learning NLP knowledge. It is not a verbatim transcript; lecture-topic labels derived from week themes are marked `official: false`.

## 5. Agent Use Contract
State knowledge_used (concept + week + status), assumptions (e.g. tokenization scheme, embedding dimension, attention variant), failure_conditions, verification (run a small forward pass or metric check), escalation when claims about modern LLM behaviour exceed this package.

## 6. Suitable Uses
Explaining vector representations, sequence architectures, attention, and pretraining; comparing model families; generating practice problems; grounding team vocabulary for NLP work.

## 7. Prohibited Uses
Do not quote reconstruction as Stanford lecture text; do not claim a model's current benchmark performance from this package; do not assert mastery from reading; do not treat Winter 2021 model comparisons as current state of the art.

## 8. Concept Usage Rules
Check definition, why, failure conditions, example, relations, week context before applying. Example: "Self Attention" is not interchangeable with "Attention" — self-attention computes intra-sequence alignment with the same sequence as query, key and value source.

## 9. Human vs Agent View
Same concept identity, different projections. Human view: intuition, examples, pitfalls in Chinese. Agent view: canonical JSON record. Never maintain two truths.

## 10. Capability Rule
Reading is not evidence of learning. Sequence: Knowledge → Practice → External Feedback → Assessment → Transfer → Capability. Package quizzes demonstrate local comprehension only.

## 11. Skill Formation
Concept clusters (Word Embedding + Word2Vec + Gradient Descent) may suggest candidate skills like "TrainAndDiagnoseEmbeddings", promoted only after transfer to a new corpus or task.

## 12. Escalation Principle
Escalate when the question concerns post-2021 architectures, when tokenization or evaluation assumptions are unverified, or when a claim would drive high-impact decisions. "I do not know" is acceptable.

## 13. Update Rule
Experience → Evidence → Candidate → Evaluation → Transfer → Validated Knowledge. Never silently rewrite stable course knowledge from a single experiment.

## 14. Maintenance Contract
concepts.json schema: id (concept name = key), type, status, definition, why, failure_conditions, example, relations[{relation, kind, target}], weeks, source_weeks. weeks reference w1..w9 and must match course_ir. relations targets must resolve. Regenerate manifest sha256 after every change.
