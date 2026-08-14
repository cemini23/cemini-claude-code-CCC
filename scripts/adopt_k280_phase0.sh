#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K280 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-vero-repo-verified-code-proof-2608.13522.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/repo-level-verified-code-proof-eval.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/vero.md"
check "policy K280" grep -q "K280" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "clone" test -d "${REPO_ROOT}/.local/adopts/vero"
check "apache-license" grep -qi "Apache License" "${REPO_ROOT}/.local/adopts/vero/LICENSE"
warn_note "K280 Vero Apache-2.0 GO REFERENCE (clone present); runtime wont_wire (Lean bench)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
