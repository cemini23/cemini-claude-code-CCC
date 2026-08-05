#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K245 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-screenshots-or-tools-gui-mcp-2608.03327.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/hybrid-gui-mcp-tool-adoption-gap.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/hybrid-gui-mcp-osworld.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-05_k245-gui-mcp-tool-adoption-gap-prod.md" || warn_note "prod brief pending — parent handoff"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
