#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K392 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-low-cost-cross-vendor-behavior-assays-2609.30012.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/low-cost-cross-vendor-behavior-assays.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/low-cost-cross-vendor-behavior-assays.md"
check "policy K392" grep -q "K392" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K392" grep -q "K392" "${REPO_ROOT}/.cursor/rules/ccc-k390-k394-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/low-cost-cross-vendor-behavior-assays"
warn_note "K392 ADOPT eval-first"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
