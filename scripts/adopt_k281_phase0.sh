#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K281 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-autodesign-meta-harness-2608.13560.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/meta-harness-optimization-hitl-eval-contract.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/autodesign.md"
check "policy K281" grep -q "K281" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/AutoDesign"
check "mit-license" grep -qi "MIT License" "${REPO_ROOT}/.local/adopts/AutoDesign/LICENSE"
warn_note "K281 AutoDesign MIT GO REFERENCE (clone present; gh API NOASSERTION but LICENSE file is MIT); poster/image-gen wont_wire; pairs K162 HITL eval contract."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
