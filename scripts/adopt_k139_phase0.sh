#!/usr/bin/env bash
# K139 Phase-0 — AReaL / next-gen agentic online-RL (2607.01120).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K139 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"

pass=0
fail=0
warn=0

check() {
  local label="$1"; shift
  if "$@"; then echo "  PASS  ${label}"; pass=$((pass + 1)); else echo "  FAIL  ${label}"; fail=$((fail + 1)); fi
}
warn_note() { echo "  WARN  $1"; warn=$((warn + 1)); }

if command -v gh >/dev/null 2>&1; then
  license="$(gh api repos/areal-project/AReaL --jq '.license.spdx_id // empty' 2>/dev/null || true)"
  if [[ "${license}" == "Apache-2.0" ]]; then
    check "areal-project/AReaL license (${license})" true
  else
    warn_note "areal-project/AReaL — license not Apache-2.0 at check time (${license:-unknown})"
  fi
else
  warn_note "gh unavailable — skip GitHub license checks"
fi

warn_note "2607.01120 — REFERENCE/WATCH; enterprise online-RL infra, NO-GO laptop dependency"
warn_note "Steal: ATDP step-granular trajectory logging (learnable, not just observable)"
warn_note "Steal: statistics-triggered harness edits (pairs with HarnessFix)"
warn_note "Steal: egress-fi archive as governed data-proxy substrate"
warn_note "No local LoRA/RL — harness axis only on Cemini prod"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
