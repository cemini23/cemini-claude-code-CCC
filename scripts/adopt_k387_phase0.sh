#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K387 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-kv-cache-working-set-capacity-2609.27746.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/kv-cache-working-set-serving.md"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/kv-cache-working-set-serving.md"
check "policy K387" grep -q "K387" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K387" grep -q "K387" "${REPO_ROOT}/.cursor/rules/ccc-k385-k389-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/kv-cache-working-set-serving"
warn_note "K387 ADOPT awareness"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
