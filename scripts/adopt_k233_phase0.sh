#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K233 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "concept" test -f "${REPO_ROOT}/wiki/concepts/claim-centered-retrieval-with-provenance.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-askchem-claim-centered-literature-2607.28618.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/askchem.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-31_k233-askchem-claim-centered-prod.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/askchem/.git"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
