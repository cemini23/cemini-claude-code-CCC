#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K284 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-differential-fault-injection-llm-modernization-2608.14527.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/differential-fault-injection-llm-modernization.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/patterns/differential-fault-injection-validation.md"
check "policy K284" grep -q "K284" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K284 differential fault injection — no public ftinj SPDX clone; policy only, no GAMESS runtime on CCC laptop. Cybersec brief stub."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
