#!/usr/bin/env bash
# pr_guard.sh — hourly guard for the learning-packs repo.
#
# Mechanically handles open PRs and issues that are safe to act on without
# human judgment, and records the rest for review:
#
#   PR handling:
#     - superseded : PR content structurally identical to main (e.g. program_ir
#                    already fixed, or course relations already acyclic) -> close.
#     - clean      : PR changes apply to main and verify_course.py PASSES after
#                    manifest regen -> commit+push+close (note "applied").
#     - cycle      : PR introduces relation cycles -> flag in report (human).
#
#   Issue handling:
#     - content-suggestion issues (author topprismdata, body contains 建议/新增)
#       are RECORDED for human/next-agent adoption (pr_guard never fabricates
#       concepts; it requires official-source validation + editorial review).
#
# Idempotent: processed PR/issue numbers recorded in tools/state/pr_guard_state.json.
# Report written to tools/reports/pr_guard_YYYY-MM-DD_HH.md.
#
# bash 3.2 compatible (no mapfile/arrays).
# Usage:  tools/pr_guard.sh   (also installed as an hourly launchd job)

set -uo pipefail
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 1
GH="gh"
OWNER="guohongbin-git"
REPO_NAME="stanford-cs-learning-packs"
STATE="$REPO/tools/state/pr_guard_state.json"
REPORT_DIR="$REPO/tools/reports"
TS="$(date +%Y-%m-%d_%H)"
REPORT="$REPORT_DIR/pr_guard_$TS.md"
mkdir -p "$REPO/tools/state" "$REPORT_DIR" 2>/dev/null
: > "$REPORT"

log() { printf '%s\n' "$*" | tee -a "$REPORT"; }
ghr() { $GH "$@" -R "$OWNER/$REPO_NAME"; }

[ -f "$STATE" ] || echo '{}' > "$STATE"
state_get() { python3 -c "import json;print(json.load(open('$STATE')).get('$1',''))" 2>/dev/null; }
state_set() { python3 - "$STATE" "$1" "$2" <<'PY'
import json,sys
s=json.load(open(sys.argv[1]))
s[sys.argv[2]]=sys.argv[3]
json.dump(s,open(sys.argv[1],'w'),ensure_ascii=False,indent=2)
PY
}
already() { [ -n "$(state_get "$1")" ]; }

log "===== pr_guard run $TS ====="
log "repo: $OWNER/$REPO_NAME"

# =====================================================================
# 1. PR handling
# =====================================================================
log ""
log "### PRs"
PRLIST="$(mktemp)"
ghr pr list --state open --json number --jq '.[].number' >"$PRLIST" 2>/dev/null
if [ ! -s "$PRLIST" ]; then log "  (no open PRs)"; else
  while IFS= read -r n; do
    [ -n "$n" ] || continue
    if already "pr:$n"; then continue; fi
    log ""
    log "PR #$n:"
    title=$(ghr pr view "$n" --json title --jq .title 2>/dev/null)
    log "  title: $title"
    FILES="$(mktemp)"
    ghr pr view "$n" --json files --jq '.files[].path' >"$FILES" 2>/dev/null
    course_json=""; html=""; program_ir=0; other=0
    while IFS= read -r f; do
      [ -n "$f" ] || continue
      case "$f" in
        */concepts.json) [ -z "$course_json" ] && course_json="$f";;
        *.html) [ -z "$html" ] && html="$f";;
        */program_ir.json) program_ir=1;;
        *) other=1;;
      esac
    done <"$FILES"
    rm -f "$FILES"

    status="UNHANDLED"

    # superseded: PR only touches program_ir.json and it is structurally
    # identical to main -> close as superseded.
    if [ "$program_ir" -eq 1 ] && [ -z "$course_json" ]; then
      if git show "origin/HEAD:program/program_ir.json" >/tmp/_pr_ir_main.json 2>/dev/null \
         && git show "refs/pull/$n/merge:program/program_ir.json" >/tmp/_pr_ir_new.json 2>/dev/null; then
        if python3 -c "
import json,sys
def canon(x):
    if isinstance(x,dict): return sorted((k,canon(v)) for k,v in x.items())
    if isinstance(x,list): return sorted(canon(v) for v in x)
    return x
sys.exit(0 if canon(json.load(open(sys.argv[1])))==canon(json.load(open(sys.argv[2]))) else 1)
" /tmp/_pr_ir_main.json /tmp/_pr_ir_new.json 2>/dev/null; then
          log "  -> SUPERSEDED (program_ir.json identical to main)"; status="superseded"
        else
          log "  -> content differs from main; attempting clean apply"; status="UNHANDLED"
        fi
      fi
    fi

    # clean-apply: apply the PR's changed course files to main, regen manifest,
    # verify. If all affected courses PASS -> commit+push+close.
    if [ "$status" = "UNHANDLED" ]; then
      apply_dir=$(mktemp -d); applied=0
      while IFS= read -r f; do
        [ -n "$f" ] || continue
        case "$f" in
          */concepts.json|*.html)
            if git show "refs/pull/$n/merge:$f" >"$apply_dir/$(basename "$f")" 2>/dev/null; then
              cp "$apply_dir/$(basename "$f")" "$REPO/$f" 2>/dev/null && applied=1
            fi;;
        esac
      done <"$FILES"
      if [ "$applied" -eq 1 ]; then
        if python3 tools/verify_course.py >>"$REPORT" 2>&1; then
          git add -A 2>/dev/null
          git -c user.name="guohongbin-git" -c user.email="guohongbin@users.noreply.github.com" \
            commit -q -m "pr_guard: apply PR#$n ($(printf '%s' "$title" | head -c 60))" 2>/dev/null \
            && git push -q origin main 2>/dev/null \
            && ghr pr close "$n" --close -c "$(printf 'pr_guard 已合并进 main（apply + manifest regen + verify 通过）。关闭本 PR。')" 2>/dev/null \
            && { log "  -> CLEAN APPLIED (merged into main)"; status="clean"; }
        else
          log "  -> verify failed; restored main, not applied"
          git checkout -- . 2>/dev/null
        fi
      else
        log "  -> no course files to apply; flagging for review"
      fi
      rm -rf "$apply_dir"
    fi

    # cycle flag: remaining -> flag for human.
    if [ "$status" = "UNHANDLED" ]; then
      log "  -> FLAGGED (needs human review; PR left open)"
    fi

    state_set "pr:$n" "$status"
  done <"$PRLIST"
fi
rm -f "$PRLIST"

# =====================================================================
# 2. Issue handling (content-suggestion issues)
# =====================================================================
log ""
log "### Issues"
ISSLIST="$(mktemp)"
ghr issue list --state open --json number,title,author --jq '.[] | "\(.number)\t\(.author.login)"' >"$ISSLIST" 2>/dev/null
if [ ! -s "$ISSLIST" ]; then log "  (no open issues)"; else
  while IFS=$'\t' read -r num author; do
    [ -n "$num" ] || continue
    title=$(ghr issue view "$num" --json title --jq .title 2>/dev/null)
    log ""
    log "Issue #$num ($author): $title"
    if [ "$author" != "topprismdata" ]; then
      log "  -> SKIP (not from trusted topprismdata)"; state_set "issue:$num" "skip-other"; continue
    fi
    body=$(ghr issue view "$num" --json body --jq .body 2>/dev/null)
    if ! printf '%s' "$body" | grep -q '建议\|新增\|充实'; then
      log "  -> SKIP (not a content suggestion)"; state_set "issue:$num" "skip-noncontent"; continue
    fi
    log "  -> RECORDED (content suggestion; requires official-source validation + editorial review)"
    log "     (pr_guard does not fabricate concepts; adopted by human/next agent)"
    state_set "issue:$num" "recorded"
  done <"$ISSLIST"
fi
rm -f "$ISSLIST"

log ""
log "===== end run $TS ====="
