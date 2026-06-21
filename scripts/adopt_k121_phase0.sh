#!/usr/bin/env bash
# K121 Phase-0 — TokenPilot/LightMem2, SafeClawBench, gatekeeper eval papers.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k121-phase0-ccc}"
LM="${PHASE0}/LightMem2"

echo "K121 Phase-0 adoption checks (CCC)"
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

if [[ ! -d "${LM}/.git" ]]; then
  git clone --depth 1 https://github.com/zjunlp/LightMem2.git "${LM}"
fi

check "LightMem2 clone" test -d "${LM}/.git"

if command -v gh >/dev/null 2>&1; then
  lm_lic="$(gh api repos/zjunlp/LightMem2 --jq '.license.spdx_id' 2>/dev/null || echo "")"
  [[ "${lm_lic}" == "MIT" ]] && check "LightMem2 MIT license" true || warn_note "LightMem2 license: ${lm_lic:-none}"
fi

warn_note "SafeClawBench — HF dataset sairights/safeclawbench; route eval to cybersecurity-wiki"
warn_note "Gatekeepers paper — REFERENCE eval pattern only; no quantum stack install"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
