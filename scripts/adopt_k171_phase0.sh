#!/usr/bin/env bash
# K171 Phase-0 — agent optimizer compounding (2607.14004)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K171 Phase-0 (CCC) — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "NO-GO local paper-repo clone (license and/or no public code) — pattern ADOPT only"
check "agent-optimizer-compounding-and-regression-control.md" test -f "${REPO_ROOT}/wiki/concepts/agent-optimizer-compounding-and-regression-control.md"
check "arxiv-agent-optimizers-compound-continual-learning-2607.14004.md" test -f "${REPO_ROOT}/wiki/sources/arxiv-agent-optimizers-compound-continual-learning-2607.14004.md"
check "relai-continual-learning-terminal-bench.md" test -f "${REPO_ROOT}/wiki/entities/tools/relai-continual-learning-terminal-bench.md"
check "2026-07-16_k171-agent-optimizer-compounding-prod.md" test -f "${REPO_ROOT}/briefs/2026-07-16_k171-agent-optimizer-compounding-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
