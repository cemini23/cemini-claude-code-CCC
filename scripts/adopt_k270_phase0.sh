#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K270 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-llm-assisted-writing-biomedical-pmc-2608.10715.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/llm-assisted-writing-detection-hygiene.md"
check "policy K270" grep -q "K270" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K270 pattern/NO-GO — no required local adopt"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
