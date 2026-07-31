#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K232 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/passive-awareness-async-multi-agent-coordination.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agentradio-passive-awareness-multi-agent-2607.28430.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/agentradio.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-31_k232-agentradio-passive-awareness-prod.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/AgentRadio/.git"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
