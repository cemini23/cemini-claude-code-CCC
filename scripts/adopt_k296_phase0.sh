#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K296 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/terminal-state-eval-discovery-reliability-gap.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/thinkingbox.md"
check "policy K296" grep -q "K296" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/thinkingbox"
check "mit-license" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/thinkingbox/LICENSE.txt"
warn_note "K296 Thinkingbox MIT GO REFERENCE; benchmark runtime wont_wire (pairs K239/K275/K277)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
