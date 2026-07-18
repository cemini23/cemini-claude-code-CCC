#!/usr/bin/env bash
# K189 Phase-0 — FlowGuard MCP signals vs evidence (2607.14754)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K189 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.14754 — no public FlowGuard artifact; NO-GO install"
warn_note "Do not adopt name-collision mcp-flowguard repos without SPDX + identity match"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mcp-security-signals-vs-runtime-evidence.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-18_k189-flowguard-mcp-evidence-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
