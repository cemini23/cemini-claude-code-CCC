#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K372 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-obstacle-aware-harness-robot-manipulation-2609.20822.md"
check "no concept" test ! -f "${REPO_ROOT}/wiki/concepts/obstacle-aware-harness-robot-manipulation.md"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/obstacle"
warn_note "K372 OOD stub"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
