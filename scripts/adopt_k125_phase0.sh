#!/usr/bin/env bash
# K125 Phase-0 — memory/orchestration cluster (4 arXiv papers).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K125 Phase-0 adoption checks (CCC)"
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

# ArgusFleet — paper cites public repo; verify availability
if command -v gh >/dev/null 2>&1; then
  argus_status="$(gh api "repos/caura-ai/argusfleet" --jq '.full_name' 2>/dev/null || true)"
  if [[ -n "${argus_status}" && "${argus_status}" != *"Not Found"* && "${argus_status}" != *"message"* ]]; then
    lic="$(gh api "repos/caura-ai/argusfleet" --jq '.license.spdx_id' 2>/dev/null || echo "")"
    check "ArgusFleet repo exists" true
    warn_note "ArgusFleet license: ${lic:-none} — verify before GO"
  else
    warn_note "ArgusFleet (caura-ai/argusfleet) — 404; REFERENCE until repo ships"
  fi
else
  warn_note "gh not available — skip ArgusFleet API check"
fi

warn_note "TaaS (2604.07065) — REFERENCE MCP trust vocabulary; IoT/6G domain NO-GO prod"
warn_note "VADAOrchestra (2606.22485) — REFERENCE on CCC; finance BPM → @osint-wiki"
warn_note "ESAA-Conversational (2606.23752) — CONDITIONAL-GO Windows/PowerShell laptop only; no public GitHub"
warn_note "MemClaw (2606.24535) — REFERENCE SaaS; ToS + scope audit before any trial"
warn_note "MemClaw URL: https://memclaw.net — SaaS Phase-0 = pricing/ToS skim only"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
