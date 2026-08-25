#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K304 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agent-memory-poisoning-utility-2608.21230.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/memory-poisoning-content-screening-bound.md"
check "policy K304" grep -q "K304" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K304" grep -q "K304" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
warn_note "K304 memory poisoning ADOPT bounded occupancy + write-path grounding; content screening boundary; NO poison PoCs in wiki."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
