# CS336 Course Pack · Spring 2025 · v0.1

A shared human/agent learning package for **Stanford CS336: Language Modeling from Scratch — Spring 2025**.

This is the first replication trial of the CS146S v0.3.1 course-package pipeline on a second Stanford course.

## Version boundary

This package is explicitly locked to **Spring 2025**.

Confirmed public anchors:

- Archived course page / schedule: https://cs336.stanford.edu/spring2025/
- Stanford Online 17-lecture playlist: https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_
- Spring 2025 lecture materials: https://github.com/stanford-cs336/spring2025-lectures
- Public coursework: five assignments linked from the archived Spring 2025 site

The archived course page describes CS336 as an implementation-heavy 5-unit course that walks through the full LM development process, and lists the 17 core lecture topics from tokenization through alignment/RL. It also lists two later guest lectures; those are retained as supplemental schedule events rather than folded into the 17-video core sequence.

## Package contents

```text
CS336_course_pack_Spring2025_v0.1/
├── CS336_interactive_Spring2025_v0.1.html
├── course_ir.json
├── concepts.json
├── AGENTS.md
├── README.md
├── package_manifest.json
└── qa/
    ├── render_report.json
    ├── schema.md
    ├── contact_sheet.jpg
    └── screenshots/
        ├── 01_overview.png
        ├── 02_method.png
        ├── 03_knowledge-map.png
        ├── 04_w1.png
        └── ... 13_synthesis.png
```

## File roles

### `CS336_interactive_Spring2025_v0.1.html`

Single-file, self-contained interactive course. No external CDN is required. It includes:

- Chinese Human View;
- Agent View;
- clickable canonical concepts;
- local learning state;
- interactive weekly quizzes;
- a shared knowledge map;
- an embedded `<script type="application/json" id="cs336-data">` payload.

The week pages and quizzes are rendered from the embedded `course_ir`; concept views are rendered from the embedded `concepts` records.

### `course_ir.json`

The teaching sequence, grouped into 9 weeks from the actual Spring 2025 schedule:

1. L1–2 — tokenization, PyTorch, resource accounting
2. L3–4 — architecture, hyperparameters, MoE
3. L5–6 — GPUs, kernels, Triton
4. L7–8 — parallelism / distributed training
5. L9–10 — scaling laws and inference
6. L11–12 — scaling laws and evaluation
7. L13–14 — data
8. L15–16 — alignment: SFT/RLHF and RL
9. L17 — alignment/RL; end-to-end synthesis

Each week contains the required five teaching/agent blocks:

- `objectives`
- `concepts`
- `example`
- `pitfalls`
- `quiz`
- `agent` (goal / inputs / actions / evidence / risks)

### `concepts.json`

Canonical course concepts. Schema:

```json
{
  "Concept Name": {
    "id": "Concept Name",
    "type": "Concept",
    "status": "TEACHING_RECONSTRUCTION",
    "definition": "...",
    "why": "...",
    "failure_conditions": "...",
    "example": "...",
    "relations": [
      {"relation":"prerequisite","kind":"prerequisite","target":"Other Concept"}
    ],
    "weeks": ["Week 1"],
    "source_weeks": ["Lecture 1", "Assignment 1"]
  }
}
```

Concept IDs and schema keys are English. Human teaching explanations are Chinese. Agent View renders the same canonical JSON record directly.

### `AGENTS.md`

Defines:

- Spring 2025 version boundary;
- evidence semantics;
- Agent read order;
- canonical concept contract;
- capability and escalation rules;
- HTML/IR synchronization contract.

### `qa/`

Contains machine/browser QA evidence. `render_report.json` records:

- JSON schema checks;
- embedded JSON equality checks;
- concept relation integrity;
- browser rendering/overflow checks;
- Human/Agent toggle test;
- concept drawer test;
- quiz/progress-state test.

## Evidence discipline

The course schedule, assignment names/scopes, Spring 2025 term, and public source URLs are `SOURCE_CONFIRMED` inputs.

Concept explanations use `TEACHING_RECONSTRUCTION`. They are designed to teach the verified topics but are not Stanford quotations or transcripts.

The official assignment repositories are live repositories and can change after 2025. This package therefore uses the archived Spring 2025 course site as the version-binding source for assignment semantics.

## How to extend a concept

1. Edit `concepts.json`.
2. Preserve the canonical id/key equality.
3. Keep `weeks` and `source_weeks` non-empty.
4. Ensure every `relations[].target` exists.
5. Rebuild the HTML embedded `cs336-data` payload from the external JSON files.
6. Rerun QA and update `package_manifest.json` hashes.

Do not hand-edit an independent concept schema inside JavaScript.

## How to edit a week

1. Edit the week record in `course_ir.json`.
2. Update affected concept `weeks` / `source_weeks` mappings.
3. Rebuild the single embedded `cs336-data` JSON payload.
4. Open the HTML and verify both Human and Agent views.
5. Run render QA before release.

Because the HTML renders week content from the embedded IR, there is no second handwritten week truth source.

## How to test

Release validation must check:

1. `course_ir.json` parses.
2. `concepts.json` parses.
3. Embedded `cs336-data.course_ir` is semantically equal to external `course_ir.json`.
4. Embedded `cs336-data.concepts` is semantically equal to external `concepts.json`.
5. Every week concept resolves in `concepts.json`.
6. Every relation target resolves.
7. All concepts have non-empty `weeks` and `source_weeks`.
8. Browser renders the 13 release sections at 1600×900 without horizontal overflow; all 13 release sections are retained as screenshots for visual review.
9. Human → Agent mode switching works.
10. Opening a canonical concept renders Chinese Human View and canonical JSON Agent View.
11. A quiz answer updates the week state and progress bar.

The generated results are recorded in `qa/render_report.json`.

## Assignments

The Spring 2025 archived page lists five public coursework blocks:

- Assignment 1: Basics — tokenizer, model architecture, optimizer, minimal LM training
- Assignment 2: Systems — profiling, Triton/FlashAttention2, distributed memory-efficient training
- Assignment 3: Scaling — component understanding and empirical scaling-law fitting
- Assignment 4: Data — Common Crawl processing, filtering, deduplication
- Assignment 5: Alignment and Reasoning RL — SFT and RL for reasoning; optional safety alignment

## Release principle

This package is a **Learning Source Package**, not an authoritative LM engineering standard and not a capability certificate.

## Relations note (2026-09-25)
Some `relations` entries were derived from week co-membership during repair (the concept was previously unlinked). They express teaching co-occurrence (`related_to`), not typed conceptual semantics; authored edges are unchanged. A semantic relation-typing pass (prerequisite / enables / opposes) remains optional future work.

> **QA assets in this repo**: interactive screenshots / fullpage render are not committed (repository size). The complete QA bundle (13 screenshots, contact sheet, full-page render) ships with the Release zip. This directory's `package_manifest.json` describes exactly the files present here.
