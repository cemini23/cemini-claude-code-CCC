#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K242 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-agent-trajectory-sentinel-2608.02464.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/telemetry-deterministic-agent-failure-repair.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/agent-trajectory-sentinel.md"
check "clone" test -d "${REPO_ROOT}/.local/adopts/agent-trajectory-sentinel" || warn_note "clone dir missing — git clone pending"
check "prod" test -f "${REPO_ROOT}/briefs/2026-08-04_k242-agent-trajectory-sentinel-prod.md" || warn_note "prod brief pending — parent handoff"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
