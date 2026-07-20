#!/usr/bin/env bash
# K191 Phase-0 — ToolVerse turn-aware RL (2607.15660)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K191 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "No official ToolVerse artifact — NO-GO install; reject name collisions"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/toolverse-gust-turn-aware-agentic-rl.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-toolverse-long-horizon-mcp-rl-2607.15660.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-20_k191-toolverse-turn-aware-rl-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
