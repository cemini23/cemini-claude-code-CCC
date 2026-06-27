#!/usr/bin/env bash
# K129 Phase-0 — tool reliability + confidence orchestration cluster (2 arXiv papers).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k129-phase0-ccc}"
TOOLBENCH="${PHASE0}/ToolBench-X"

echo "K129 Phase-0 adoption checks (CCC)"
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

clone_if_missing "https://github.com/Foreverskyou/ToolBench-X.git" "${TOOLBENCH}"
check "ToolBench-X clone" test -d "${TOOLBENCH}/.git"

if command -v gh >/dev/null 2>&1; then
  lic="$(gh api "repos/Foreverskyou/ToolBench-X" --jq '.license.spdx_id' 2>/dev/null || echo "")"
  if [[ -n "${lic}" && "${lic}" != "null" ]]; then
    check "ToolBench-X license ${lic}" true
  else
    warn_note "ToolBench-X — no SPDX license on GitHub; verify LICENSE file before GO"
  fi
fi

warn_note "ToolBench-X (2606.25819) — REFERENCE benchmark; CONDITIONAL-GO laptop eval after license verify"
warn_note "Robust-TO (2606.26904) — REFERENCE orchestration pattern; video-primary → @image-gen-wiki"
warn_note "Five hazard types: Spec Drift, Invocation Error, Execution Failure, Output Drift, Cross-source Conflict"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
