#!/usr/bin/env bash
# K202 Phase-0 — Agents4GEOS domain MCP
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K202 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/domain-mcp-skills-fresh-subagent-orchestration.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agents4geos-mcp-multiphyics-2607.18557.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-22_k202-agents4geos-domain-mcp-skills-prod.md"
check "local agents4geos" test -d "${REPO_ROOT}/.local/adopts/agents4geos/.git"
warn_note "GEOS ~586MB — NO-GO under 500MB budget"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
