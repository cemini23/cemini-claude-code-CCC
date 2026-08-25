#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K309 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-prime-agent-rlm-harness-2608.23552.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/rlm-continual-harness.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/prime-agent.md"
check "policy K309" grep -q "K309" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K309" grep -q "K309" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/prime-agent"
check "mit-license-on-disk" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/prime-agent/LICENSE"
warn_note "K309 Prime Agent MIT GO REFERENCE clone <500MB; runtime wont_wire — do NOT replace Cursor//route/claude-ds; HITL before any self-write (pairs K229/K292/K162)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
