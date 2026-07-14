#!/usr/bin/env bash
# K162 Phase-0 — RSI survey / verification hierarchy (2607.07663).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K162 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.07663 — REFERENCE survey (~1250 papers); no product install"
warn_note "Cited github.com/bamboodrift/recursive_self_improvement — 404 at Phase-0 (2026-07-14); no LICENSE / no clone"
warn_note "Steal: verification hierarchy (formal > execution > judges > intrinsic)"
warn_note "NO-GO: closed self-reward that rewrites its own pass criteria"
warn_note "No David adopt — TipDrop stays human-on-the-loop for signal quality"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/bounded-self-refinement-vs-rsi-taxonomy.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-recursive-self-improvement-survey-2607.07663.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-14_k162-rsi-verification-hierarchy-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
