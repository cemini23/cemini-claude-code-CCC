#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K240 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-mixed-complementarity-problems-jl-2608.00959.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/batched-open-mcp-solver-robotics.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/mixed-complementarity-problems-jl.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/MixedComplementarityProblems.jl" || warn_note "clone dir missing — git clone pending"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-04_k240-mixed-complementarity-jl-prod.md" || warn_note "prod brief pending — parent handoff"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
