#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K446 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-tofu-orchestrator-tool-trust-boundary-2610.13651.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/tool-metadata-as-security-contract.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/tool-metadata-as-security-contract.md"
check "policy K446" grep -q "K446" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K446" grep -q "K446" "${REPO_ROOT}/.cursor/rules/ccc-k445-k448-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/ToFu"
warn_note "K446 ADOPT pattern (MCP tool security)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
