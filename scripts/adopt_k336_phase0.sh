#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K336 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-cordisbench-component-lifecycle-2609.01600.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/harness-component-lifecycle-reasoning.md"
check "policy K336" grep -q "K336" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K336" grep -q "K336" "${REPO_ROOT}/.cursor/rules/ccc-k333-k336-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/CordisBench"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/harness-component-lifecycle-reasoning.md"
warn_note "K336 ADOPT eval axis — teardown order matters; prefer execution/reference semantics at scale. GitHub+HF cited but no public SPDX at Phase-0 — WATCH, no clone."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
