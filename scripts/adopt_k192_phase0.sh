#!/usr/bin/env bash
# K192 Phase-0 — TARS ToM personalization (2607.15948)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K192 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "TARS is VS Code — do not treat VSIX as Cursor drop-in"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/theory-of-mind-personalized-agent-explanations.md"
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-tars-theory-of-mind-ide-2607.15948.md"
check "entity" test -f "${REPO_ROOT}/wiki/entities/tools/tars-vscode.md"
check "prod brief" test -f "${REPO_ROOT}/briefs/2026-07-20_k192-tars-tom-personalization-prod.md"
check "local tars clone" test -d "${REPO_ROOT}/.local/adopts/tars/.git"
check "tars MIT LICENSE" test -f "${REPO_ROOT}/.local/adopts/tars/LICENSE"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
