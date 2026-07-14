#!/usr/bin/env bash
# K164 Phase-0 — hierarchical skill stack + lazy discovery (2607.11138).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K164 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.11138 — REFERENCE architecture (UPI Help context); no public product repo"
warn_note "Steal: capability tree + LIFO stack + lazy manifests + capability fencing"
warn_note "Require mutually exclusive top-level domains or hierarchy underperforms flat"
warn_note "David adopt: TipDrop multi-vendor / Discord bot skill tree"
warn_note "Poker steal: exclusive domains for tools/memory/opponent — not flat dump"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/hierarchical-skill-stack-lazy-orchestration.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-14_k164-hierarchical-skill-stack-lazy-orchestration-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
