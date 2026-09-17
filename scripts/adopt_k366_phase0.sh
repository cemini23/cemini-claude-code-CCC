#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K366 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mcp-traffic-nids-beacon-evasion-2609.19091.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-traffic-network-detection-blind-spot.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/mcp-traffic-network-detection-blind-spot.md"
check "policy K366" grep -q "K366" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K366" grep -q "K366" "${REPO_ROOT}/.cursor/rules/ccc-k363-k367-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/mcp-traffic-network-detection-blind-spot"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template' '${REPO_ROOT}/wiki/sources/arxiv-mcp-traffic-nids-beacon-evasion-2609.19091.md' '${REPO_ROOT}/wiki/concepts/mcp-traffic-network-detection-blind-spot.md'"
warn_note "K366 Cybersec-primary + ADOPT policy"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
