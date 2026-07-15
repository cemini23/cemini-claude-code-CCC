#!/usr/bin/env bash
# K168 Phase-0 — SLM harness adaptation / failure-mode map (2607.08938).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K168 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.08938 — ADOPT failure→adaptation taxonomy; REFERENCE optimizer; NO-GO clone (no LICENSE)"
warn_note "Magnitude claims need K169 matched-budget / held-out gate"
warn_note "github.com/malusamayo/migration-analysis — replication package only (~43MB shallow); figshare artifacts separate"
warn_note "David: TipDrop repetitive parse/classify/post paths; Poker: per-hand decide harness"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/failure-mode-harness-adaptation-mapping.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-better-harnesses-smaller-models-2607.08938.md"
check "entity page" test -f "${REPO_ROOT}/wiki/entities/tools/migration-analysis-replication-package.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-15_k168-slm-harness-adaptation-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
