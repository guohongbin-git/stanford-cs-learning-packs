# CS224W Course Pack · Autumn 2021 · v0.1

Stanford CS224W (Machine Learning with Graphs, Autumn 2021, Jure Leskovec) human/agent co-learning package.

## Contents
- `CS224W_interactive_Autumn2021_v0.1.html` — self-contained interactive course (runtime-rendered from embedded JSON, zero external references)
- `course_ir.json` — 9-week structure (objectives, pitfalls, quizzes, agent contracts)
- `concepts.json` — 31 canonical concepts (name ids, typed relations, non-empty weeks)
- `AGENTS.md` — 14-section agent contract, version-locked to Autumn 2021
- `package_manifest.json` — bytes + sha256 per file

## How to use
Open the HTML. Weeks render from embedded data; click concept chips for the Human/Agent drawer; quizzes update progress in localStorage.

## How to extend
1. Add concepts to `concepts.json` (10 schema fields; id = concept name; weeks reference w1..w9).
2. Reference them from the matching `course_ir.json` week.
3. Re-embed both JSONs into the HTML `#cs224w-data` block and regenerate the manifest.

## Version boundary
Autumn 2021 (archive_official). The canonical video source is the Stanford Online CS224W Autumn 2021 playlist.

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.

## Repair log

### 2026-09-27 — Issue #17 (topprismdata Deep Research proposal): adopt 3 concepts validated against Fall 2026 official schedule
Adopted 3 new concepts mapped to official Fall 2026 lectures (status = TEACHING_RECONSTRUCTION; detailed mechanism from Deep Research report):
- `GIN (Graph Isomorphism Network)` → Lecture 6 "Theory of GNNs" (reading *How Powerful Are GNNs*).
- `Graphlets / GDV` → Lecture 7 "Designing Powerful Graph Encoders" (reading *Counting Graph Substructures with GNNs*).
- `Graph Transformer (Graphormer)` → Lecture 8 "Graph Transformers".

Enriched 8 existing concepts with mechanisms from official lectures: DeepWalk/Node2Vec (NetMF matrix-factorization theorem), GCN (ChebNet), KG Reasoning (TransE/TransR/RotatE), Graph Generation (GraphRNN/GCPN), Motif (graphlet/GDV), Scaling Up GNNs (LightGCN/NNCF), Link Prediction (KG + recommender). New relations point only to existing concepts (acyclic, 0 dangling). HTML `#cs224w-data` embed overwritten (all 31 concepts) and manifest regenerated. verify_course: PASS (6/6, 58 relations, 0 dangling).

Not adopted (not in Fall 2026 lecture schedule): Modularity/Louvain, Structural Roles (RolX), PPR/RWR, Oversquashing — folded into Community Detection / PageRank / Over-smoothing existing concepts.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
