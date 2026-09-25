#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K394 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agent-trace-tampering-2609.30266.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/agent-trace-tampering-audit-gap.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/agent-trace-tampering-audit-gap.md"
check "policy K394" grep -q "K394" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K394" grep -q "K394" "${REPO_ROOT}/.cursor/rules/ccc-k390-k394-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/agent-trace-tampering"
warn_note "K394 Cybersec + ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
