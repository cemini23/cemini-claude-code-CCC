#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K443 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-code-only-as-policy-embodied-turing-2610.12369.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/code-only-policy-shared-library.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/code-only-policy-shared-library.md"
check "policy K443" grep -q "K443" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K443" grep -q "K443" "${REPO_ROOT}/.cursor/rules/ccc-k441-k444-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/COAP"
warn_note "K443 REFERENCE (cross-domain; pattern transfers)"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
