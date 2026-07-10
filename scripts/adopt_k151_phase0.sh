#!/usr/bin/env bash
# K151 Phase-0 — CAGE-1 enterprise agent governance (2607.03510).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K151 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"

pass=0
fail=0
warn=0

check() {
  local label="$1"; shift
  if "$@"; then echo "  PASS  ${label}"; fail=$((fail + 0)); pass=$((pass + 1)); else echo "  FAIL  ${label}"; fail=$((fail + 1)); fi
}
warn_note() { echo "  WARN  $1"; warn=$((warn + 1)); }

warn_note "2607.03510 — REFERENCE; independent technical report (Roopam W. Sure)"
warn_note "No installable product repo at Phase-0"
warn_note "NOT lahlfors/cybernetic-governance-engine (different CAGE acronym)"
warn_note "Steal: Prebind Assurance — prove control before action binds"
warn_note "Steal: 12-dimension enterprise eval checklist"
warn_note "Steal: Standing (time-specific authority) vocabulary"
warn_note "David adopt: Prebind checklist for prod-touching TipDrop bots"

check "concept page exists" test -f "${REPO_ROOT}/wiki/concepts/cage-1-enterprise-agent-governance-eval.md"
check "source page exists" test -f "${REPO_ROOT}/wiki/sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md"
check "prod brief exists" test -f "${REPO_ROOT}/briefs/2026-07-10_k151-cage-1-prebind-assurance-prod.md"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
