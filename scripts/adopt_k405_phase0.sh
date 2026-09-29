#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K405 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-tokencast-agent-token-forecast-2609.35760.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/tokencast-agent-token-consumption-forecast.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/tokencast-agent-token-consumption-forecast.md"
check "policy K405" grep -q "K405" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K405" grep -q "K405" "${REPO_ROOT}/.cursor/rules/ccc-k401-k405-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/tokencast"
warn_note "K405 ADOPT awareness"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
