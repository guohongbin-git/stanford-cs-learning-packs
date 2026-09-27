# CS224N Course Pack · Winter 2021 · v0.1

Stanford CS224N (NLP with Deep Learning, Winter 2021) human/agent co-learning package.

## Contents
- `CS224N_interactive_Winter2021_v0.1.html` — self-contained interactive course (runtime-rendered from embedded JSON, zero external references)
- `course_ir.json` — 9-week structure (objectives, pitfalls, quizzes, agent contracts)
- `concepts.json` — 44 canonical concepts (name ids, typed relations, non-empty weeks)
- `AGENTS.md` — 14-section agent contract, version-locked to Winter 2021
- `package_manifest.json` — bytes + sha256 per file

## How to use
Open the HTML. Weeks render from embedded data; click concept chips for the Human/Agent drawer; quizzes update progress in localStorage.

## How to extend
1. Add concepts to `concepts.json` (10 schema fields; id = concept name; weeks reference w1..w9).
2. Reference them from the matching `course_ir.json` week.
3. Re-embed both JSONs into the HTML `#cs224n-data` block and regenerate the manifest.

## Version boundary
Winter 2021 (archive_official). Lecture-topic labels derived from week themes are `official: false`; the canonical video source is the Stanford Online CS224N Winter 2021 playlist.

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.
## Repair log (2026-09-27)
Adopted **issue #16** (cs224n Deep Research 建议书): 10 new concepts validated against the **official cs224n schedule (Winter 2026)** — Word Vectors (GloVe), Assignment 1 (word vectors), RNNs (vanishing gradient), Pretraining (ELMo), Default Final Project (GPT-2), Week 5 (Prompting + PEFT) cover all 10:
- GloVe + Distributional Hypothesis (Co-occurrence SVD) → Word Vectors (w1)
- BPTT (Backpropagation Through Time) → RNNs (w3)
- Gradient Clipping (梯度裁剪) → RNNs (w3)
- Cross-Attention (交叉注意力) → Seq2Seq / Encoder-Decoder (w4)
- ELMo → Pretraining reading (w5)
- GPT (autoregressive pretrained) → Default Final Project (GPT-2)
- T5 (Text-to-Text Span-Denoising) → Transformer (w4)
- Prompting + In-Context Learning → Week 5 (PEFT)
- Extractive QA + Anaphora Resolution → BERT (w4)

Concept count **34→44**; all `status = TEACHING_RECONSTRUCTION`. Relations 93 edges, 0 self/dangling; `verify_course.py` PASS.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
