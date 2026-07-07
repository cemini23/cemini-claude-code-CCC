#!/usr/bin/env bash
# K138 Phase-0 — Steerability via constraints (2607.02389).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

echo "K138 Phase-0 adoption checks (CCC)"
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

if command -v gh >/dev/null 2>&1; then
  license="$(gh api repos/NVIDIA/OpenShell --jq '.license.spdx_id // empty' 2>/dev/null || true)"
  if [[ "${license}" == "Apache-2.0" ]]; then
    check "NVIDIA/OpenShell license (${license})" true
  else
    warn_note "NVIDIA/OpenShell — license not Apache-2.0 at check time (${license:-unknown})"
  fi
else
  warn_note "gh unavailable — skip GitHub license checks"
fi

warn_note "2607.02389 — REFERENCE; no canonical public repo at Phase-0 (BACKDOORS.md promised)"
warn_note "Steal: substrate stack (ruff/pyrefly/beartype/pydantic), module Invariants docstrings, ~200 LoC docs CLI"
warn_note "Steal: multi-pass per-function review for ≤8B reviewer subagents"
warn_note "OpenShell — REFERENCE machine-layer peer; CUA remains laptop default"
warn_note "David checklist: @cybersecurity-wiki/briefs/2026-07-07_harness-substrate-constraints-checklist.md"

echo ""
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
