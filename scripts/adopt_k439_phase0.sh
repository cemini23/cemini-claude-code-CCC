#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K439 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-locaa-lossy-compression-tuning-2610.10487.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/compression-in-the-loop-tuning.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/compression-in-the-loop-tuning.md"
check "policy K439" grep -q "K439" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K439" grep -q "K439" "${REPO_ROOT}/.cursor/rules/ccc-k436-k440-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/pocket-agent"
warn_note "K439 ADOPT pattern (MIT framework)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
