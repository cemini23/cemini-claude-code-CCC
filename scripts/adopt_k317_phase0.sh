#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K317 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-tau-agent-traffic-rag-2608.25935.md"
check "policy K317" grep -q "K317" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K317" grep -q "K317" "${REPO_ROOT}/.cursor/rules/ccc-k315-k324-phase1-wires.mdc"
check "no TAU clone" test ! -d "${REPO_ROOT}/.local/adopts/TAU-Agent"
warn_note "K317 OOD video/traffic — short stub; wont_wire. siri-rouser/TAU-Agent MIT but skip clone (OOD; Image-gen skip). Steal: retrieval agent picks evidence then VLM."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
