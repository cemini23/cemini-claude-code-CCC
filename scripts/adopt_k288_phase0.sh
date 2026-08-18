#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K288 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-esti-state-semantic-injection-2608.16806.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/planner-state-semantic-integrity-attack-surface.md"
check "pattern esti" test -f "${REPO_ROOT}/wiki/entities/patterns/state-semantic-injection-esti.md"
check "policy K288" grep -q "K288" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K288 ESTI state-semantic injection — no public code; policy only. Cybersec-primary stub. Pairs K259 traceable scholarship, K274 CDH."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
