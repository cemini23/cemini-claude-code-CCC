#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K374 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-industrial-test-failure-rca-llm-agents-2609.21843.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/industrial-test-failure-rca-agents.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/industrial-test-failure-rca-agents.md"
check "policy K374" grep -q "K374" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K374" grep -q "K374" "${REPO_ROOT}/.cursor/rules/ccc-k373-k375-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/industrial-test-failure-rca-agents"
warn_note "K374 ADOPT pattern"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
