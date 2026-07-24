#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K214 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "No official OpenForgeRL SPDX artifact; slime not cloned this batch"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/harness-native-agent-rl-training.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-openforgerl-harness-native-training-2607.21557.md"
check "prod" test -f "${REPO_ROOT}/briefs/2026-07-24_k214-harness-native-rl-training-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"; exit 0
