#!/usr/bin/env bash
# Phase-0 laptop trial for TimeClaw (arXiv 2606.05404) — NOT 2605.10038 homonym.
# Clone + venv import smoke only; benchmarks need OPENAI_API_KEY in .env.
set -euo pipefail

PHASE0="${PHASE0:-/tmp/timeclaw-phase0-ccc}"
REPO_DIR="${PHASE0}/TimeClaw"
VENV="${PHASE0}/venv"
REPO_URL="https://github.com/iDEA-iSAIL-Lab-UIUC/TimeClaw.git"

echo "TimeClaw Phase-0 (2606.05404)"
echo "  dir: ${PHASE0}"

pass=0
fail=0
warn=0

if [[ ! -d "${REPO_DIR}/.git" ]]; then
  git clone --depth 1 "${REPO_URL}" "${REPO_DIR}"
fi

if [[ -f "${REPO_DIR}/LICENSE" ]] && grep -q "Apache License" "${REPO_DIR}/LICENSE"; then
  echo "  PASS  Apache-2.0 LICENSE present"
  pass=$((pass + 1))
else
  echo "  FAIL  LICENSE missing or unexpected"
  fail=$((fail + 1))
fi

if [[ ! -d "${VENV}" ]]; then
  python3 -m venv "${VENV}"
  "${VENV}/bin/pip" install -q -r "${REPO_DIR}/requirements.txt"
fi

if cd "${REPO_DIR}" && "${VENV}/bin/python" -c "from timeclaw.agents import TimeClaw" 2>/dev/null; then
  echo "  PASS  timeclaw.agents.TimeClaw import"
  pass=$((pass + 1))
else
  echo "  FAIL  import timeclaw.agents"
  fail=$((fail + 1))
fi

if [[ -z "${OPENAI_API_KEY:-}" ]] && [[ ! -f "${REPO_DIR}/.env" ]]; then
  echo "  WARN  no OPENAI_API_KEY — copy .env.example before running main.py benchmarks"
  warn=$((warn + 1))
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
echo "Clone: ${REPO_DIR}"
echo "NO-GO: do not install into ~/.claude/ or prod paths"
if [[ "${fail}" -gt 0 ]]; then
  exit 1
fi
