#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K257 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-av-aivat-anytime-valid-agent-eval-2608.06362.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/anytime-valid-agent-eval-stopping.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/av-aivat.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-07_k257-av-aivat-anytime-valid-eval-prod.md" || warn_note "prod brief pending"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
