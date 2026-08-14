#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K277 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/measurement-integrity-mcp-security-eval.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/patterns/treatment-blind-endpoint-integrity.md"
check "policy K277" grep -q "K277" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
warn_note "K277 labels ≠ endpoints — no public product/SPDX; policy_wired, runtime wont_wire. Cybersec brief (treatment leakage)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
