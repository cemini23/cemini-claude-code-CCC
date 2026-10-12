#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K448 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-x-agentred-cross-service-red-teaming-2610.13886.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/cross-service-compositional-harm-graph.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/cross-service-compositional-harm-graph.md"
check "policy K448" grep -q "K448" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K448" grep -q "K448" "${REPO_ROOT}/.cursor/rules/ccc-k445-k448-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/X-AgentRed"
warn_note "K448 ADOPT pattern (cross-service composition risk)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
