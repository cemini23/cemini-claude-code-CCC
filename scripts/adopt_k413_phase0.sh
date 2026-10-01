#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K413 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-dynaharness-execution-contract-attribution-2609.40306.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/execution-contract-failure-attribution.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/execution-contract-failure-attribution.md"
check "policy K413" grep -q "K413" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K413" grep -q "K413" "${REPO_ROOT}/.cursor/rules/ccc-k411-k415-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/dynaharness"
warn_note "K413 REFERENCE (cross-domain; 3 primitives transfer)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
