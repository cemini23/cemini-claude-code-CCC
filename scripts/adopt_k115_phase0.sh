#!/usr/bin/env bash
# K115 Phase-0 — context/memory/recursion cluster from arXiv ingest 2026-06-15.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k115-phase0-ccc}"

echo "K115 Phase-0 adoption checks (CCC)"
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

echo ""
echo "=== 2606.10209 Less Context Better Agents (Microsoft) ==="
warn_note "no public code — inference-time N=5/W=3 policy only (REFERENCE)"

echo ""
echo "=== 2606.11869 Agents All the Way Down ==="
warn_note "methodology paper only — no framework repo (REFERENCE)"

echo ""
echo "=== 2606.12945 Multi-factor memory / BorgeAgent ==="
if command -v gh >/dev/null 2>&1; then
  if gh api repos/zhibao-dev/BorgeAgent --jq '.name' >/dev/null 2>&1; then
    lic="$(gh api repos/zhibao-dev/BorgeAgent --jq '.license.spdx_id' 2>/dev/null || echo "")"
    check "BorgeAgent repo exists" true
    echo "  INFO  license: ${lic:-none}"
  else
    warn_note "BorgeAgent github.com/zhibao-dev/BorgeAgent — 404 (paper cites 2026; repo missing)"
  fi
else
  warn_note "gh not available — skip BorgeAgent API check"
fi

echo ""
echo "=== 2606.13643 Recursive Agent Harnesses (PwC) ==="
RAH_DIR="${PHASE0}/recursive-agent-harness"
if [[ ! -d "${RAH_DIR}/.git" ]]; then
  git clone --depth 1 https://github.com/darkness22s/recursive-agent-harness.git "${RAH_DIR}" 2>/dev/null || true
fi
if [[ -d "${RAH_DIR}/.git" ]]; then
  check "darkness22s/recursive-agent-harness clone" true
  if command -v gh >/dev/null 2>&1; then
    lic="$(gh api repos/darkness22s/recursive-agent-harness --jq '.license.spdx_id' 2>/dev/null || echo "null")"
    if [[ "${lic}" == "null" || -z "${lic}" ]]; then
      warn_note "recursive-agent-harness license null — NO-GO install; unrelated to PwC paper eval"
    else
      echo "  INFO  license: ${lic}"
    fi
  fi
  if command -v npm >/dev/null 2>&1; then
    if (cd "${RAH_DIR}" && npm install --silent && npm test --silent); then
      check "npm test (unverified third-party package)" true
    else
      warn_note "npm test failed — do not adopt"
    fi
  else
    warn_note "npm not on PATH — skip test"
  fi
else
  warn_note "could not clone darkness22s/recursive-agent-harness"
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
echo "Verdict: all four papers REFERENCE/pattern-only — no prod install from this cluster"
exit 0
