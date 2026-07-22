#!/usr/bin/env bash
# K204 Phase-0 — LangGraph pathways
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K204 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/langgraph-stateful-workflow-pathways.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-langgraph-stateful-business-workflows-2607.19297.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-22_k204-langgraph-stateful-pathways-prod.md"
warn_note "Full LangGraph clone ~511MB — NO-GO; use existing install if any"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
