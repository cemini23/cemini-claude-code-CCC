#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K271 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-enterprise-mcp-auth-gateway-2608.10760.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/enterprise-mcp-auth-gateway.md"
check "policy K271" grep -q "K271" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K271 pattern/NO-GO — no required local adopt"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
