#!/usr/bin/env bash
# K123 Phase-0 — DIA (REFERENCE), dual-agent paper (REFERENCE), Agentverse (REFERENCE), AOHP clone.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k123-phase0-ccc}"
AOHP="${PHASE0}/aohp"

echo "K123 Phase-0 adoption checks (CCC)"
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

if [[ ! -d "${AOHP}/.git" ]]; then
  git clone --depth 1 https://github.com/aohp-os/aohp.git "${AOHP}"
fi

check "AOHP clone" test -d "${AOHP}/.git"

if command -v gh >/dev/null 2>&1; then
  lic="$(gh api repos/aohp-os/aohp --jq '.license.spdx_id' 2>/dev/null || echo "")"
  [[ "${lic}" == "Apache-2.0" ]] && check "AOHP Apache-2.0 license" true || warn_note "AOHP license: ${lic:-none}"
fi

warn_note "DIA (2606.19319) — C3 AI product paper; REFERENCE ACA pattern only"
warn_note "Dual-agent protocol (2606.20120) — REFERENCE cross-model verification"
warn_note "Agentverse gap paper (2606.20570) — REFERENCE taxonomy; CC-BY 4.0 paper"
warn_note "AOHP full AOSP build — NO-GO without dedicated Android build lab"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
