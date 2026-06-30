#!/usr/bin/env bash
# K135 Phase-0 — Clarus research collaboration infrastructure (2606.30246).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K135 Phase-0 adoption checks (CCC)"
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

if command -v curl >/dev/null 2>&1; then
  code="$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 https://clarus.holosai.io/ || echo 000)"
  if [[ "${code}" =~ ^(200|301|302|307|308)$ ]]; then
    check "clarus.holosai.io reachable (${code})" true
  else
    warn_note "clarus.holosai.io HTTP ${code} — verify manually"
  fi
else
  warn_note "curl unavailable — skip Clarus URL check"
fi

warn_note "Clarus (2606.30246) — REFERENCE SaaS; no public GitHub at Phase-0"
warn_note "ToS + attribution audit before any trial; NO-GO replace conductor/wiki ingest"
warn_note "Steal project-agent-resource model + auditable collaboration vs closed PaperClaw pipeline"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
