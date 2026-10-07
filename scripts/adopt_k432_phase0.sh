#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K432 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-four-quadrant-rag-eval-2610.07937.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/two-level-retrieval-generation-eval.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/two-level-retrieval-generation-eval.md"
check "policy K432" grep -q "K432" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K432" grep -q "K432" "${REPO_ROOT}/.cursor/rules/ccc-k431-k435-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/redpine-benchmarks"
warn_note "K432 ADOPT eval-methodology (vendor report)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
