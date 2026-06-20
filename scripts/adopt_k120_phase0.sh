#!/usr/bin/env bash
# K120 Phase-0 — user-as-code + DynAMO (2606.16707, 2606.19382 ingest).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k120-phase0-ccc}"
UAC="${PHASE0}/user-as-code"
DYNAMO="${PHASE0}/DynAMO"

echo "K120 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"
echo "  phase0 dir: ${PHASE0}"

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

if [[ ! -d "${UAC}/.git" ]]; then
  git clone --depth 1 https://github.com/19PINE-AI/user-as-code.git "${UAC}"
fi
if [[ ! -d "${DYNAMO}/.git" ]]; then
  git clone --depth 1 https://github.com/kushwaha001/DynAMO.git "${DYNAMO}"
fi

check "user-as-code clone" test -d "${UAC}/.git"
check "DynAMO clone" test -d "${DYNAMO}/.git"

if command -v gh >/dev/null 2>&1; then
  uac_lic="$(gh api repos/19PINE-AI/user-as-code --jq '.license.spdx_id' 2>/dev/null || echo "")"
  dyn_lic="$(gh api repos/kushwaha001/DynAMO --jq '.license.spdx_id' 2>/dev/null || echo "")"
  [[ "${uac_lic}" == "Apache-2.0" ]] && check "user-as-code Apache-2.0" true || warn_note "user-as-code license: ${uac_lic:-none}"
  [[ "${dyn_lic}" == "Apache-2.0" ]] && check "DynAMO Apache-2.0" true || warn_note "DynAMO license: ${dyn_lic:-none}"
fi

warn_note "user-as-code — CONDITIONAL-GO laptop personal-agent experiments; NO-GO replace claude-mem"
warn_note "DynAMO — REFERENCE orchestration pattern; NO-GO Cemini prod (Industry 4.0)"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
