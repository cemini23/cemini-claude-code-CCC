#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K273 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentic-configuration-management-acm-2608.11166.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/agentic-configuration-management-acm.md"
check "policy K273" grep -q "K273" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K273 pattern/NO-GO — no required local adopt"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
