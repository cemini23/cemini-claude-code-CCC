#!/usr/bin/env bash
# K124 Phase-0 — harness/memory research cluster (7 arXiv papers).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PHASE0="${PHASE0:-/tmp/k124-phase0-ccc}"
PAPERCLAW="${PHASE0}/paperclaw"
FARA="${PHASE0}/fara"
AWESOME="${PHASE0}/awesome-agent-engineering"

echo "K124 Phase-0 adoption checks (CCC)"
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

clone_if_missing "https://github.com/SequenxAI/PaperClaw.git" "${PAPERCLAW}"
clone_if_missing "https://github.com/microsoft/fara.git" "${FARA}"
clone_if_missing "https://github.com/ggjy/Awesome-Agent-Engineering.git" "${AWESOME}"

check "PaperClaw clone" test -d "${PAPERCLAW}/.git"
check "Fara clone" test -d "${FARA}/.git"
check "Awesome-Agent-Engineering clone" test -d "${AWESOME}/.git"

if command -v gh >/dev/null 2>&1; then
  for spec in "SequenxAI/PaperClaw:MIT" "microsoft/fara:MIT" "ggjy/Awesome-Agent-Engineering:MIT"; do
    repo="${spec%%:*}"
    want="${spec##*:}"
    lic="$(gh api "repos/${repo}" --jq '.license.spdx_id' 2>/dev/null || echo "")"
    if [[ "${lic}" == "${want}" ]]; then
      check "${repo} ${want}" true
    else
      warn_note "${repo} license: ${lic:-none} (expected ${want})"
    fi
  done
fi

warn_note "Harness survey (2606.20683) — REFERENCE taxonomy; Awesome list ingest pointer only"
warn_note "BioInsight (2606.20997) — REFERENCE evidence-layer pattern; biomedical domain NO-GO prod"
warn_note "Procedural memory AFTER (2606.23127) — REFERENCE skill-transfer eval; benchmark artifact TBD"
warn_note "SelfCompact (2606.23525) — REFERENCE rubric-gated compaction; no public repo"
warn_note "Metis (2606.24151) — REFERENCE dual memory; work-in-progress, no repo"
warn_note "PaperClaw — CONDITIONAL-GO laptop eval; overlaps XCIENTIST research harness niche"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
