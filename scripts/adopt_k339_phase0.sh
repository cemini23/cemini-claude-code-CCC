#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K339 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-bilevel-coordinated-reflection-2609.02750.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/bilevel-coordinated-reflection.md"
check "policy K339" grep -q "K339" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K339" grep -q "K339" "${REPO_ROOT}/.cursor/rules/ccc-k337-k341-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/BilevelCoordinatedReflection"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/bilevel-coordinated-reflection.md"
warn_note "K339 ADOPT pattern — bilevel orchestrator–worker game; external verification in reflection loop. No public repo → policy only."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
