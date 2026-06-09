#!/usr/bin/env bash
# K108 Phase-0 — omnifs laptop eval (Apache-2.0). THE HIVE /ship are pattern-only.
set -euo pipefail

PHASE0="${PHASE0:-/tmp/k108-phase0-ccc}"
REPO="${PHASE0}/omnifs"
REPO_URL="https://github.com/0xff-ai/omnifs.git"

echo "K108 Phase-0 checks"
echo "  dir: ${PHASE0}"

pass=0
fail=0
warn=0

if command -v gh >/dev/null 2>&1; then
  lic="$(gh api repos/0xff-ai/omnifs --jq '.license.spdx_id' 2>/dev/null || echo null)"
  if [[ "${lic}" == "Apache-2.0" ]]; then
    echo "  PASS  omnifs license Apache-2.0"
    pass=$((pass + 1))
  else
    echo "  FAIL  omnifs license: ${lic}"
    fail=$((fail + 1))
  fi
else
  echo "  WARN  gh not on PATH — skip license api"
  warn=$((warn + 1))
fi

if [[ ! -d "${REPO}/.git" ]]; then
  git clone --depth 1 "${REPO_URL}" "${REPO}"
fi
if [[ -f "${REPO}/LICENSE-APACHE" || -f "${REPO}/LICENSE" ]]; then
  echo "  PASS  omnifs clone"
  pass=$((pass + 1))
else
  echo "  FAIL  omnifs clone incomplete"
  fail=$((fail + 1))
fi

if command -v docker >/dev/null 2>&1; then
  echo "  INFO  docker present — optional: npm install -g @0xff-ai/omnifs && omnifs setup"
else
  echo "  WARN  docker not on PATH — omnifs FUSE path needs Docker today"
  warn=$((warn + 1))
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn/info"
echo "Patterns only (no install): THE HIVE loops, /ship subagents — see wiki K108 ingest"
echo "NO-GO: prod/librarian/conductor until design brief"
if [[ "${fail}" -gt 0 ]]; then
  exit 1
fi
