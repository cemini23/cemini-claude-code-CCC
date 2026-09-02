#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K333 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-delegation-without-trust-2609.00267.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/untrusted-model-delegation-governance.md"
check "policy K333" grep -q "K333" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K333" grep -q "K333" "${REPO_ROOT}/.cursor/rules/ccc-k333-k336-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/DelegationWithoutTrust"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/untrusted-model-delegation-governance.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|forged token dump|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-delegation-without-trust-2609.00267.md' '${REPO_ROOT}/wiki/concepts/untrusted-model-delegation-governance.md'"
check "precheck helper" python3 "${REPO_ROOT}/scripts/delegation_broker_precheck.py" selftest
warn_note "K333 Cybersec-primary + CCC policy — untrusted-model property; external authorization broker; four delegation threats. VotalAI production reference — no public SPDX → policy only, no clone. No PoCs."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
