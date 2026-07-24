#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K211 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Do not wire Euclid-MCP to LIVE without operator ticket"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/deterministic-mcp-symbolic-reasoning.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-euclid-mcp-prolog-reasoning-2607.21412.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/euclid-mcp.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-24_k211-euclid-mcp-symbolic-reasoning-prod.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/euclid-mcp/.git"
check "LICENSE" test -f "${REPO_ROOT}/.local/adopts/euclid-mcp/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
