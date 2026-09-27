CS229 archive_official Spring 2022

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.
## Repair log (2026-09-27)
Adopted **issue #15** (cs229 Deep Research 建议书): 9 new concepts validated against the **official cs229 schedule (Spring 2026)** — the course description explicitly lists "non-parametric learning / clustering / dimensionality reduction / learning theory / reinforcement learning and adaptive control", covering all 9:
- Locally Weighted Regression → non-parametric learning (W01)
- Newton Method (IRLS) → optimisation (W01)
- SMO (Sequential Minimal Optimization) → SVM dual (W01)
- Laplace Smoothing → smoothing (W04)
- Factor Analysis → dimensionality reduction (W04)
- k-means → clustering (W04)
- VC Dimension → learning theory (W08)
- Ensemble Learning → learning theory (W08)
- LQR → reinforcement learning / adaptive control (W09)

Concept count **61→70**; all `status = TEACHING_RECONSTRUCTION` (topic official, mechanism from Deep Research). Relations 142 edges, 0 self/dangling; `verify_course.py` PASS.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
