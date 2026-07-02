#!/usr/bin/env bash
# K137 Phase-0 — AutoMem metamemory cognitive skill (2607.01224).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K137 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"

pass=0
fail=0
warn=0

check() {
  local label="$1"
  shift
  if "$@"; then
    echo "  PASS  ${label}"
    pass=$((pass + 1))
  else
    echo "  FAIL  ${label}"
    fail=$((fail + 1))
  fi
}

warn_note() {
  echo "  WARN  $1"
  warn=$((warn + 1))
}

if command -v gh >/dev/null 2>&1; then
  license="$(gh api repos/autoLearnMem/AutoMem --jq '.license.spdx_id // empty' 2>/dev/null || true)"
  if [[ -n "${license}" ]]; then
    check "autoLearnMem/AutoMem license (${license})" true
  else
    warn_note "autoLearnMem/AutoMem — no SPDX license (REFERENCE only, NO-GO install)"
  fi
  vgp_license="$(gh api repos/verygoodplugins/automem --jq '.license.spdx_id // empty' 2>/dev/null || true)"
  if [[ "${vgp_license}" == "MIT" ]]; then
    warn_note "verygoodplugins/automem is MIT — DIFFERENT product from Stanford 2607.01224; do not conflate"
  fi
else
  warn_note "gh unavailable — skip GitHub license checks"
fi

warn_note "2607.01224 — REFERENCE; steal scaffold/proficiency split + meta-LLM trajectory review"
warn_note "Distinct from 2606.04315 AutoMEM cross-scenario eval (K100)"
warn_note "Harness steals: hot.md/claude-mem schema iteration; search-before-write; no LoRA on laptop"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
