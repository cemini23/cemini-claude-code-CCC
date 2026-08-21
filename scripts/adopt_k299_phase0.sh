#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K299 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-midtool-mid-training-data-synthesis-2608.20314.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mid-training-tool-use-affordance-grounding.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/midtool.md"
check "policy K299" grep -q "K299" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-hf-download" test ! -d "${REPO_ROOT}/.local/adopts/midtool"
warn_note "K299 MidTool WATCH wont_wire runtime; no HF MidTool/midtool-release download (pairs K259)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
