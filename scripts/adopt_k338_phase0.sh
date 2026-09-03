#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K338 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-buildocc-llm-occupant-agent-building-energy-2609.02729.md"
check "no concept" test ! -f "${REPO_ROOT}/wiki/concepts/buildocc-occupant-agent.md"
check "no entity" test ! -f "${REPO_ROOT}/wiki/entities/tools/buildocc.md"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/BuildOcc"
warn_note "K338 OOD building energy — source stub only; wont_wire; no harness wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
