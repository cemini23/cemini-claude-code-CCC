#!/usr/bin/env bash
# K122 Phase-0 — XCIENTIST research harness (claim drift, validation contracts).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k122-phase0-ccc}"
XC="${PHASE0}/Xcientist"

echo "K122 Phase-0 adoption checks (CCC)"
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

if [[ ! -d "${XC}/.git" ]]; then
  git clone --depth 1 https://github.com/OpenDFM/Xcientist.git "${XC}"
fi

check "Xcientist clone" test -d "${XC}/.git"

if command -v gh >/dev/null 2>&1; then
  xc_lic="$(gh api repos/OpenDFM/Xcientist --jq '.license.spdx_id' 2>/dev/null || echo "")"
  [[ "${xc_lic}" == "MIT" ]] && check "Xcientist MIT license" true || warn_note "Xcientist license: ${xc_lic:-none}"
fi

warn_note "Xcientist — REFERENCE only; steal claim-drift + validation-contract patterns for CCC harness"
warn_note "NO-GO prod install — ML research stack; wiki ingest pipeline is separate"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
