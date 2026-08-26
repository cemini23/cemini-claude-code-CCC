#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K310 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-ap2-beyond-the-mandate-2608.23858.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mandate-signature-vs-preauth-intent.md"
check "policy K310" grep -q "K310" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K310" grep -q "K310" "${REPO_ROOT}/.cursor/rules/ccc-k310-k314-phase1-wires.mdc"
check "no AP2 clone" test ! -d "${REPO_ROOT}/.local/adopts/ap2"
warn_note "K310 ADOPT policy only — signed mandate != user intent when pre-auth context manipulated. No paper testbed/scanner clone; NO PoC or exploit text in wiki/briefs."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
