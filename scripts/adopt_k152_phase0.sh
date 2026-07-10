#!/usr/bin/env bash
# K152 Phase-0 — PolyWorkBench multilingual long-horizon eval (2607.06008).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K152 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"

pass=0
fail=0
warn=0

check() {
  local label="$1"; shift
  if "$@"; then echo "  PASS  ${label}"; pass=$((pass + 1)); else echo "  FAIL  ${label}"; fail=$((fail + 1)); fi
}
warn_note() { echo "  WARN  $1"; warn=$((warn + 1)); }

warn_note "2607.06008 — REFERENCE; benchmark paper (Tencent/BJTU)"
warn_note "No public GitHub repo located at Phase-0"
warn_note "Steal: hybrid eval (structural + executable + LLM semantic)"
warn_note "Steal: multilingual compounding degradation lens"
warn_note "Steal: client-first-order evidence (Claude Code, OpenClaw in eval)"
warn_note "No David adopt — English-primary TipDrop unless multilingual pipelines expand"

check "concept page exists" test -f "${REPO_ROOT}/wiki/concepts/multilingual-long-horizon-agent-eval.md"
check "source page exists" test -f "${REPO_ROOT}/wiki/sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
