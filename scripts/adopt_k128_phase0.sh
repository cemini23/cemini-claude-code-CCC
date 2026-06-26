#!/usr/bin/env bash
# K128 Phase-0 — MemProbe memory recovery benchmark (2606.24595).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k128-phase0-ccc}"
MEMPROBE="${PHASE0}/MemProbe"

echo "K128 Phase-0 adoption checks (CCC)"
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

clone_if_missing() {
  local url="$1"
  local dest="$2"
  if [[ ! -d "${dest}/.git" ]]; then
    git clone --depth 1 "${url}" "${dest}"
  fi
}

clone_if_missing "https://github.com/sora1998/MemProbe.git" "${MEMPROBE}"
check "MemProbe clone" test -d "${MEMPROBE}/.git"

if command -v gh >/dev/null 2>&1; then
  lic="$(gh api "repos/sora1998/MemProbe" --jq '.license.spdx_id' 2>/dev/null || echo "")"
  if [[ "${lic}" == "CC-BY-4.0" ]]; then
    check "MemProbe CC-BY-4.0" true
  else
    warn_note "MemProbe license: ${lic:-none} (expected CC-BY-4.0)"
  fi
fi

warn_note "MemProbe — REFERENCE eval benchmark; CC-BY-4.0 attribution on any derived rubrics"
warn_note "CONDITIONAL-GO laptop — run recovery audit on claude-mem/hot.md methodology only; no prod mount"
warn_note "Task-success benchmarks (LongMemEval etc.) insufficient — steal recovery axis for memory audits"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
