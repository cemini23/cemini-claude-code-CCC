#!/usr/bin/env bash
# K179 Phase-0 — preinstall gate (2607.15143)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K179 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
warn_note "preinstall gate (2607.15143)"
check "$(basename wiki/concepts/coding-agent-install-gap-and-preinstall-gate.md)" test -e "${REPO_ROOT}/wiki/concepts/coding-agent-install-gap-and-preinstall-gate.md"
check "$(basename wiki/sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md)" test -e "${REPO_ROOT}/wiki/sources/arxiv-weaponizing-setup-instructions-coding-agents-2607.15143.md"
check "$(basename briefs/2026-07-17_k179-coding-agent-preinstall-gate-prod.md)" test -e "${REPO_ROOT}/briefs/2026-07-17_k179-coding-agent-preinstall-gate-prod.md"
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
exit 0
