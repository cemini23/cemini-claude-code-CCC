#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K386 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-regulated-insurers-multi-agent-solvency-2609.27636.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/regulated-enterprise-multi-agent-governance.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/regulated-enterprise-multi-agent-governance.md"
check "policy K386" grep -q "K386" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K386" grep -q "K386" "${REPO_ROOT}/.cursor/rules/ccc-k385-k389-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/regulated-enterprise-multi-agent-governance"
warn_note "K386 ADOPT policy awareness"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
