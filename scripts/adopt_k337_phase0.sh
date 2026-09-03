#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K337 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-acle-mcp-attested-capability-leases-2609.02690.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/attested-capability-leases-execution-time-trust.md"
check "policy K337" grep -q "K337" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K337" grep -q "K337" "${REPO_ROOT}/.cursor/rules/ccc-k337-k341-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/ACLE-MCP"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/attested-capability-leases-execution-time-trust.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-acle-mcp-attested-capability-leases-2609.02690.md' '${REPO_ROOT}/wiki/concepts/attested-capability-leases-execution-time-trust.md'"
warn_note "K337 Cybersec-primary + CCC policy — post-authorization execution trust gap; capability lease + Execution Gate. No public SPDX → policy only, no clone. No PoCs."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
