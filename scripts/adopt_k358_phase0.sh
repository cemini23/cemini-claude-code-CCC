#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K358 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-echopath-gui-replayable-memory-2609.16635.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/execution-level-replayable-gui-memory.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/execution-level-replayable-gui-memory.md"
check "policy K358" grep -q "K358" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K358" grep -q "K358" "${REPO_ROOT}/.cursor/rules/ccc-k358-k362-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/execution-level-replayable-gui-memory"
warn_note "K358 ADOPT pattern"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
