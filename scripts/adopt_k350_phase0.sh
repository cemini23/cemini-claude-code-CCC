#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K350 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-scanning-harness-supply-chain-defects-2609.07360.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/harness-supply-chain-defects.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/harness-supply-chain-defects.md"
check "policy K350" grep -q "K350" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K350" grep -q "K350" "${REPO_ROOT}/.cursor/rules/ccc-k346-k357-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/harness-supply-chain-defects"
check "no attack text" bash -c "! grep -rEi jailbreak|attack\\ prompt|exploit\\ template ${REPO_ROOT}/wiki/sources/arxiv-scanning-harness-supply-chain-defects-2609.07360.md ${REPO_ROOT}/wiki/concepts/harness-supply-chain-defects.md"
warn_note "K350 Cybersec-primary + ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
