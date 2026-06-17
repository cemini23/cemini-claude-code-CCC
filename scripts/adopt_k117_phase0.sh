#!/usr/bin/env bash
# K117 Phase-0 — MemRefine, SEAGym, FinAcumen (2026-06-17 ingest).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K117 Phase-0 adoption checks (CCC)"
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

echo ""
echo "=== 2606.13177 MemRefine (KAIST) ==="
if command -v gh >/dev/null 2>&1; then
  lic="$(gh api repos/zz2cc/MemRefine --jq '.license.spdx_id' 2>/dev/null || echo "missing")"
  if [[ "${lic}" != "missing" && "${lic}" != "null" ]]; then
    warn_note "zz2cc/MemRefine exists but is different project (3DrawAgent CKE) — not paper 2606.13177"
  else
    warn_note "no verified MemRefine repo for 2606.13177 (REFERENCE)"
  fi
else
  warn_note "gh not available"
fi

echo ""
echo "=== 2606.17546 SEAGym (Tsinghua) ==="
warn_note "no public SEAGym repo — Harbor dependency (REFERENCE eval methodology)"

echo ""
echo "=== 2606.17642 FinAcumen (finance) ==="
if command -v gh >/dev/null 2>&1; then
  if gh api repos/CamelliaLilium/FinAcumen --jq '.name' >/dev/null 2>&1; then
    lic="$(gh api repos/CamelliaLilium/FinAcumen --jq '.license.spdx_id' 2>/dev/null || echo "")"
    stars="$(gh api repos/CamelliaLilium/FinAcumen --jq '.stargazers_count' 2>/dev/null || echo 0)"
    check "CamelliaLilium/FinAcumen exists" true
    echo "  INFO  license: ${lic:-none} stars: ${stars}"
    warn_note "unverified vs paper anonymous.4open.science link — osint cross-wiki only"
  else
    warn_note "FinAcumen GitHub not found — anonymous link only"
  fi
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
echo "Verdict: MemRefine/SEAGym REFERENCE; FinAcumen finance → osint-wiki"
exit 0
