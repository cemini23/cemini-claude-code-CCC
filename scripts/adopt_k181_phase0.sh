#!/usr/bin/env bash
# K181 Phase-0 — policy-as-code (2607.14798)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K181 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "policy-as-code (2607.14798)"
check "$(basename wiki/concepts/policy-as-code-layered-validation-for-agent-artifacts.md)" test -e "${REPO_ROOT}/wiki/concepts/policy-as-code-layered-validation-for-agent-artifacts.md"
check "$(basename wiki/entities/tools/satellite-mission-compiler.md)" test -e "${REPO_ROOT}/wiki/entities/tools/satellite-mission-compiler.md"
check "$(basename briefs/2026-07-17_k181-policy-as-code-guardrails-prod.md)" test -e "${REPO_ROOT}/briefs/2026-07-17_k181-policy-as-code-guardrails-prod.md"
check "$(basename .local/adopts/satellite-mission-compiler/LICENSE)" test -e "${REPO_ROOT}/.local/adopts/satellite-mission-compiler/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
