#!/usr/bin/env bash
# K156 Phase-0 — DeepSearch-World verifiable search env (2607.07820).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K156 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.07820 — WATCH; env+420K+code promised, not public at Phase-0"
warn_note "Steal: deterministic verifiable search environment for eval"
warn_note "Steal: self-distillation loop (generate/filter/mix/finetune)"
warn_note "No David adopt unless TipDrop adds deep-research search agents"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/verifiable-search-agent-environment.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-deepsearch-world-self-distillation-2607.07820.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-13_k156-deepsearch-world-verifiable-search-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
