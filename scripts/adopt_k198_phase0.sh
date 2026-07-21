#!/usr/bin/env bash
# K198 Phase-0 — schema-bound MCP skills (2607.17012)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K198 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "nuance-mcp is REFERENCE — do not wire to LIVE TipDrop without ticket"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/schema-bound-mcp-tool-surface.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-schema-bound-mcp-instrument-skills-2607.17012.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/nuance-mcp.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-21_k198-schema-bound-mcp-skills-prod.md"
check "local nuance-mcp" test -d "${REPO_ROOT}/.local/adopts/nuance-mcp/.git"
check "nuance MIT LICENSE" test -f "${REPO_ROOT}/.local/adopts/nuance-mcp/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
