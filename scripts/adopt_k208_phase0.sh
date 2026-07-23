#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K208 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Ethics paper — cybersec primary deepen; CCC oversight posture only"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/offensive-agent-ethics-oversight-posture.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-ethics-offensive-autonomous-agents-2607.20255.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-23_k208-offensive-agent-ethics-oversight-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
