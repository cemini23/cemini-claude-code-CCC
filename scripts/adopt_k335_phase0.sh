#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K335 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-harness-of-harness-multiday-swe-2609.01481.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/meta-harness-continual-improvement.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/harness-of-harness.md"
check "policy K335" grep -q "K335" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K335" grep -q "K335" "${REPO_ROOT}/.cursor/rules/ccc-k333-k336-phase1-wires.mdc"
check "clone dir" test -d "${REPO_ROOT}/.local/adopts/HarnessOfHarness"
check "clone LICENSE" test -f "${REPO_ROOT}/.local/adopts/HarnessOfHarness/LICENSE"
check "clone MIT" grep -qi "MIT" "${REPO_ROOT}/.local/adopts/HarnessOfHarness/LICENSE"
check "clone size" bash -c '[[ $(du -sm "'"${REPO_ROOT}"'/.local/adopts/HarnessOfHarness" | cut -f1) -lt 500 ]]'
check "entity wont_wire" grep -q "wire_status: wont_wire" "${REPO_ROOT}/wiki/entities/tools/harness-of-harness.md"
warn_note "K335 ADOPT meta-harness pattern — wrap existing harnesses; plan-code-test loops; versioned history. Flesymeb/HarnessOfHarness MIT REFERENCE. Runtime wont_wire."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
