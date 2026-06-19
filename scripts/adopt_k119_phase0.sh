#!/usr/bin/env bash
# K119 Phase-0 — Agent-first web (2606.19116) + EDA handoff survey (2606.19795).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K119 Phase-0 adoption checks (CCC)"
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

warn_note "2606.19116 — vision/framework paper; no CCC prod install (ATML/agents.txt REFERENCE)"
warn_note "2606.19795 — EACP is research agenda; steal handoff vocabulary only"

if command -v gh >/dev/null 2>&1; then
  mcp_lic="$(gh api repos/modelcontextprotocol/specification --jq '.license.spdx_id' 2>/dev/null || echo "")"
  if [[ -n "${mcp_lic}" ]]; then
    echo "  INFO  MCP specification repo license: ${mcp_lic}"
    if [[ "${mcp_lic}" == "MIT" ]] || [[ "${mcp_lic}" == "Apache-2.0" ]]; then
      check "MCP spec repo license OK" true
    fi
  else
    warn_note "could not verify MCP specification repo license via gh"
  fi
fi

warn_note "Agent-first web publisher work → seo-wiki GEO/AEO track"
warn_note "EDA handoff → CCC harness only; NO-GO hardware EDA agent install"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
