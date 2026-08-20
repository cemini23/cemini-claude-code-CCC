#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K294 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-spade-self-play-synthetic-environments-2608.19197.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/self-play-adaptive-synthetic-executable-environments.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/spade-rl.md"
check "policy K294" grep -q "K294" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/spade"
check "mit-license" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/spade/LICENSE"
warn_note "K294 SPADE MIT GO REFERENCE; trainer runtime wont_wire (pairs K162)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
