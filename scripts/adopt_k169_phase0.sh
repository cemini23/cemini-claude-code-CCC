#!/usr/bin/env bash
# K169 Phase-0 — harness evolution vs test-time scaling eval (2607.12227).
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K169 Phase-0 (CCC) — repo: ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "2607.12227 — ADOPT five-row eval checklist; NO-GO clone (no LICENSE file; pyproject MIT text-only)"
warn_note "github.com/rethinking-harness-evolution/code — ~2.4MB; needs Claude/GPT/E2B/Serper"
warn_note "Caveat prior HarnessX/RHO/SEAGym/K164 magnitude claims"
check "concept page" test -f "${REPO_ROOT}/wiki/concepts/harness-evolution-vs-test-time-scaling-baseline.md"
check "source page" test -f "${REPO_ROOT}/wiki/sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md"
check "entity page" test -f "${REPO_ROOT}/wiki/entities/tools/rethinking-harness-evolution-eval-harness.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-15_k169-harness-evolution-eval-discipline-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
