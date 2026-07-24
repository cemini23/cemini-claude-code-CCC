#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K210 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "Prefer AIH-Infra MIT root over Open WebUI forks with unclear SPDX"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/traceable-scholarship-citation-first-generation.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-traceable-scholarship-aih-infra-2607.20916.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/aih-infra.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-24_k210-traceable-scholarship-citation-first-prod.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/AIH-Infra/.git"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
