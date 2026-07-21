#!/usr/bin/env bash
# K200 Phase-0 — FlashRT measurement-gated harness (2607.18171)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K200 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Infini-AI-Lab/FlashRT 404 at Phase-0 — NO-GO install"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/measurement-gated-agent-harness-optimization.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-flashrt-agent-harness-realtime-2607.18171.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-21_k200-flashrt-measurement-gated-harness-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
