#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K311 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-scout-hybrid-mcp-tool-discovery-2608.23992.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/hybrid-mcp-tool-discovery-lazy-catalog.md"
check "policy K311" grep -q "K311" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K311" grep -q "K311" "${REPO_ROOT}/.cursor/rules/ccc-k310-k314-phase1-wires.mdc"
warn_note "K311 SCOUT has NO public repo (PayPal internal) — policy_wired only: lazy tool_search+execute_tool pattern, never full-catalog injection."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
