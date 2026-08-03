#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K235 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mcp-tester-mutation-consistency-transpilers-2607.29247.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/mutation-consistency-metamorphic-transpiler-testing.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/mcp-tester-transpiler.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/mcp-tester-transpiler" || warn_note "clone dir missing — Zenodo download pending"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-03_k235-mcp-tester-mutation-consistency-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
