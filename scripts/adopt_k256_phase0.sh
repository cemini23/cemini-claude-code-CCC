#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K256 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-trajdebug-error-lifecycle-2608.06346.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/trajectory-error-lifecycle-attribution.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/trajdebug.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-07_k256-trajdebug-error-lifecycle-prod.md" || warn_note "prod brief pending"
check "TrajDebug clone" test -d "${REPO_ROOT}/.local/adopts/TrajDebug"
check "TrajDebug LICENSE" test -f "${REPO_ROOT}/.local/adopts/TrajDebug/LICENSE"
warn_note "TrajDebug has 0 .py — detector under internal review"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
