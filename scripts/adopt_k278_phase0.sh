#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K278 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/intersage-trust-native-ioa-protocol.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/intersage.md"
check "policy K278" grep -q "K278" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" test ! -d "${REPO_ROOT}/.local/adopts/intersage"
warn_note "K278 InterSAGE — no public SPDX clone; policy_wired. Atto-priority (AIC identity / capability-bound discovery / audit trails)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
