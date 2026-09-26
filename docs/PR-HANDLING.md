# PR / Issue Handling Plan

Autonomous handling policy for [`guohongbin-git/stanford-cs-learning-packs`](https://github.com/guohongbin-git/stanford-cs-learning-packs).

Maintained by `tools/pr_guard.sh`, run as an hourly [launchd](#cron-policy) job.

## 0. Quick state (last audit)

| Item | Status | Action |
|---|---|---|
| PR #7–#12 (relations DAG) | **CLOSED — superseded** | main (v2.4) already acyclic; PRs forked from pre-v2.4 main |
| PR #13 (program_ir evidence_status) | **CLOSED — superseded** | `program/program_ir.json` structurally identical to main (zero diff) |
| Issue #14 (cs336 Deep Research 建议书) | **RECORDED** | 8 new concepts — recorded for human/next-agent adoption (needs official-source validation) |

## 1. The three PR outcomes

`pr_guard.sh` classifies every open PR into exactly one outcome:

| Outcome | Condition | Action |
|---|---|---|
| **superseded** | PR content structurally identical to `main` (e.g. `program_ir.json` deep-equal, or course relations already acyclic in v2.4) | `gh pr close` with note "superseded by v2.4" |
| **clean** | PR changes apply to `main`, `verify_course.py` PASSES after manifest regen | commit + push + `gh pr close` with note "applied" |
| **flagged** | PR introduces relation cycles / dangling refs that `main` does not have | leave PR open; record in report for human review |

Decision rule: **apply only what `verify_course.py` accepts; never merge a cycle.**

### Why #7–#13 were superseded (v2.4 already won)

- PRs #7–#12 forked from **pre-v2.4 main** (`4c96cdd`). Their `course_ir.json` / relation structure is stale.
- main (v2.4) already produces an **acyclic** relations graph for every course — `verify_course.py` reports `ALL PASS`, no cycles.
- PR #13's `program_ir.json` is **byte-for-byte structurally identical** to main (168 courses, all `evidence_status` identical).
- Net: these PRs duplicate or conflict with v2.4 → close as superseded, do not merge (merging would revert v2.4 audit fixes).

## 2. `tools/pr_guard.sh`

Idempotent bash (3.2 compatible). On each run it:

1. Lists open PRs. For each (skipping already-processed ones recorded in `tools/state/pr_guard_state.json`):
   - Classify changed files (`concepts.json` / `*.html` / `program_ir.json`).
   - **superseded** check: deep-compare PR branch content vs `main`.
   - **clean** check: apply changed course files to `main`, `gen_manifest.py` + `verify_course.py`; if PASS → commit + push + close.
   - **flagged**: otherwise, leave open, record in report.
2. Lists open issues. For `topprismdata` content-suggestion issues (body contains 建议/新增/充实): **record** for adoption — `pr_guard` never fabricates concepts.
3. Writes a per-run report to `tools/reports/pr_guard_YYYY-MM-DD_HH.md`.
4. Records processed PR/issue numbers in `tools/state/pr_guard_state.json`.

Run manually: `bash tools/pr_guard.sh`.

## 3. Cron policy

Installed as an hourly [launchd](#cron-policy) job:

- **plist**: `~/Library/LaunchAgents/com.guohongbin.pr-guard.plist`
- **schedule**: `StartInterval` 3600s (hourly), anchored `00:00`.
- **script**: `tools/pr_guard.sh` (bash 3.2 compatible; no `mapfile`).
- **env**: `PATH` includes `~/.bun/bin`, `/opt/homebrew/bin`; `GH_TOKEN`/keyring auth honored; `GH_TERMINAL=launchd`.
- **logs**: `tools/reports/pr_guard_{stdout,stderr}.log`.

Load / reload / inspect:

```sh
launchctl load  -w ~/Library/LaunchAgents/com.guohongbin.pr-guard.plist
launchctl list  com.guohongbin.pr-guard
launchctl kickstart -k gui/$(id -u)/com.guohongbin.pr-guard   # force one run
```

Verified: `kickstart` runs the script; `tools/reports/pr_guard_stdout.log` echoes the run.

## 4. Content-suggestion issues (e.g. #14)

Issue #14 (cs336 Deep Research 建议书) proposes 8 new concepts + 6 enhancements. Handling:

- **Never fabricate concepts.** `pr_guard` records such issues as `recorded` — they require **official-source validation** before adoption.
- Adoption workflow (human / next agent, not `pr_guard`):
  1. Validate each suggested concept against **official cs336 materials** (cs336.stanford.edu, `stanford-cs336/lectures`, assignment repos). Search may be blocked from datacenter IP — retry or use a credentialed provider.
  2. Assign `status` per the [constitution](../AGENTS.md): `SOURCE_CONFIRMED` if verbatim official; otherwise `TEACHING_RECONSTRUCTION`.
  3. Add to `docs/courses/cs336/concepts.json` with acyclic relations + `weeks` linkage.
  4. `gen_manifest.py` + `verify_course.py` (must PASS, no cycle).
  5. Commit + push, then `gh pr close` (or close the issue) noting the change.

Current status: **#14 is recorded, not adopted** — web search is blocked and there is no local official lecture transcript to validate the 8 concepts against. Adopt once an official source is reachable.

## 5. Constitution alignment

- Concept `status` is tri-state: `SOURCE_CONFIRMED` / `TEACHING_RECONSTRUCTION` / `HYPOTHESIS`.
- After fixing a pack: append README Repair log + regenerate `package_manifest.json`.
- `verify_course.py` is the gate: no pack lands without passing (manifest bytes/sha256, self-contained HTML, embedded-JSON consistency, concept-field completeness, relations resolvable, **no cycles**).
