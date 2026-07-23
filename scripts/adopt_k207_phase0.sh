#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K207 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Adelsamir01/slms_mal 404 — NO-GO; pattern only"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/hybrid-slm-ensemble-orchestration.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-slm-ensemble-malware-orchestration-2607.20216.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-23_k207-hybrid-slm-ensemble-orchestration-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
