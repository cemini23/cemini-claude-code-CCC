#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K295 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-delegating-or-doing-hybrid-human-agent-interfaces-2608.19551.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/hybrid-human-agent-delegation-effort-vs-duration.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/delegating-or-doing-hybrid-hai.md"
check "policy K295" grep -q "K295" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K295 delegAgents no public repo -> policy_wired only (pairs K245/K247)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
