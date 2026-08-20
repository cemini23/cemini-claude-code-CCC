#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K291 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-enterprise-multi-agent-analytics-2608.18740.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/enterprise-conversational-multi-agent-analytics.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/enterprise-analytics-multi-agent-platform.md"
check "policy K291" grep -q "K291" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" bash -c '! test -d "${REPO_ROOT}/.local/adopts/enterprise-analytics"'
warn_note "K291 enterprise BI CrewAI — WATCH only; wont_wire CCC runtime (OOD)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
