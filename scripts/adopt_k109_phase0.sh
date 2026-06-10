#!/usr/bin/env bash
# K109 Phase-0 — Bayesian-Agent (MIT) laptop trial from arXiv 2606.08348 ingest.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k109-phase0-ccc}"
REPO_URL="https://github.com/DataArcTech/Bayesian-Agent.git"
CLONE_DIR="${PHASE0}/Bayesian-Agent"

mkdir -p "${PHASE0}"

echo "K109 Phase-0 adoption checks (CCC)"
echo "  repo: ${REPO_ROOT}"
echo "  phase0 dir: ${PHASE0}"

pass=0
fail=0

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

if [[ ! -d "${CLONE_DIR}/.git" ]]; then
  echo "  INFO  cloning Bayesian-Agent..."
  git clone --depth 1 "${REPO_URL}" "${CLONE_DIR}"
fi

check "clone present" test -d "${CLONE_DIR}/.git"

if command -v gh >/dev/null 2>&1; then
  lic="$(gh api repos/DataArcTech/Bayesian-Agent --jq '.license.spdx_id' 2>/dev/null || echo "")"
  if [[ "${lic}" == "MIT" ]]; then
    check "license MIT (API)" true
  else
    echo "  WARN  license API returned: ${lic:-empty}"
    fail=$((fail + 1))
  fi
fi

if [[ -f "${CLONE_DIR}/README.md" ]]; then
  check "README.md" true
else
  check "README.md" false
fi

if [[ -f "${CLONE_DIR}/requirements.txt" ]] || [[ -f "${CLONE_DIR}/pyproject.toml" ]]; then
  check "python deps file" true
else
  echo "  WARN  no requirements.txt or pyproject.toml"
fi

DATA_ROOT="${PHASE0}/GA-Technical-Report/datasets"
if [[ ! -d "${DATA_ROOT}/sop_bench" ]]; then
  echo "  INFO  cloning GA-Technical-Report datasets..."
  git clone --depth 1 https://github.com/JinyiHan99/GA-Technical-Report.git "${PHASE0}/GA-Technical-Report" 2>/dev/null || true
fi
if [[ -f "${DATA_ROOT}/sop_bench/test_set_with_outputs.csv" ]]; then
  check "GA-Technical-Report datasets" true
else
  echo "  WARN  datasets missing — clone JinyiHan99/GA-Technical-Report beside Bayesian-Agent parent"
fi

if [[ -n "${DEEPSEEK_API_KEY:-}" && -f "${DATA_ROOT}/sop_bench/test_set_with_outputs.csv" ]]; then
  echo "  INFO  optional SOP smoke: DEEPSEEK_API_KEY set — run manually:"
  echo "    python experiments/run_benchmarks.py --bench sop --mode baseline --limit 1 --data-root ${DATA_ROOT}"
else
  echo "  INFO  SOP bench smoke skipped (set DEEPSEEK_API_KEY + datasets for live run)"
fi

echo ""
echo "Summary: ${pass} pass, ${fail} fail"
exit 0
