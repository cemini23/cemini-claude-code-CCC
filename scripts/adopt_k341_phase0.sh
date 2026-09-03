#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K341 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-llms-telecom-rca-structured-reasoning-2609.02805.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/evidence-grounded-structured-rca.md"
check "policy K341" grep -q "K341" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K341" grep -q "K341" "${REPO_ROOT}/.cursor/rules/ccc-k337-k341-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/TelecomRCA"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/evidence-grounded-structured-rca.md"
warn_note "K341 ADOPT policy — evidence-grounded RCA; human-gated remediation (pairs K306 ARGUS). No public repo → policy only."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
