#!/usr/bin/env bash
# K194 Phase-0 — 5G/6G agentic survey (2607.16066) REFERENCE only
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K194 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Telecom survey — CCC keeps source stub only; no product adopt"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentic-ai-5g6g-survey-2607.16066.md"
check "hands-on policy" test -f "${REPO_ROOT}/briefs/2026-07-20_k190-k194-harness-policy-hands-on.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
