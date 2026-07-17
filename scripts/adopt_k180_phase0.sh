#!/usr/bin/env bash
# K180 Phase-0 — SearchOS SOCM (2607.15257)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K180 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "SearchOS SOCM (2607.15257)"
check "$(basename wiki/concepts/searchos-socm-explicit-search-state.md)" test -e "${REPO_ROOT}/wiki/concepts/searchos-socm-explicit-search-state.md"
check "$(basename wiki/entities/tools/searchos.md)" test -e "${REPO_ROOT}/wiki/entities/tools/searchos.md"
check "$(basename briefs/2026-07-17_k180-searchos-socm-prod.md)" test -e "${REPO_ROOT}/briefs/2026-07-17_k180-searchos-socm-prod.md"
check "$(basename .local/adopts/SearchOS/LICENSE)" test -e "${REPO_ROOT}/.local/adopts/SearchOS/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
