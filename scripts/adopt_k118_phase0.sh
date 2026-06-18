#!/usr/bin/env bash
# K118 Phase-0 — Pegasus AI plugin marketplace (2606.18425 ingest).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k118-phase0-ccc}"
MARKETPLACE="${PHASE0}/claude-plugin-marketplace"

echo "K118 Phase-0 adoption checks (CCC)"
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

if [[ ! -d "${MARKETPLACE}/.git" ]]; then
  git clone --depth 1 https://github.com/pegasus-isi/claude-plugin-marketplace.git "${MARKETPLACE}"
fi

check "claude-plugin-marketplace clone" test -d "${MARKETPLACE}/.git"

if command -v gh >/dev/null 2>&1; then
  mp_lic="$(gh api repos/pegasus-isi/claude-plugin-marketplace --jq '.license.spdx_id' 2>/dev/null || echo "")"
  pg_lic="$(gh api repos/pegasus-isi/pegasus --jq '.license.spdx_id' 2>/dev/null || echo "")"
  if [[ "${mp_lic}" == "Apache-2.0" ]]; then
    check "marketplace license Apache-2.0" true
  else
    warn_note "marketplace license: ${mp_lic:-none}"
  fi
  echo "  INFO  pegasus core license: ${pg_lic:-unknown}"
fi

if [[ -d "${MARKETPLACE}/plugins/pegasus-ai" ]] || find "${MARKETPLACE}" -maxdepth 3 -iname '*pegasus*' | head -1 | grep -q .; then
  check "pegasus-ai plugin path present" true
else
  warn_note "pegasus-ai plugin path not found at expected layout — inspect clone"
fi

warn_note "HPC/Pegasus stack — NO-GO for Cemini prod; REFERENCE for spec-driven workflow pattern"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
