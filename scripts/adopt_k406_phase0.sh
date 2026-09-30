#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K406 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-assay-content-addressed-evidence-graphs-2609.36170.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/assay-content-addressed-evidence-graphs.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/assay-content-addressed-evidence-graphs.md"
check "policy K406" grep -q "K406" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K406" grep -q "K406" "${REPO_ROOT}/.cursor/rules/ccc-k406-k410-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/assay-research"
warn_note "K406 CONDITIONAL-GO (Apache-2.0)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
