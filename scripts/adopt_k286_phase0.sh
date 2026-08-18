#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K286 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-vibeworlding-3d-open-worlds-2608.15265.md"
check "primary" test -f "${REPO_ROOT}/wiki/concepts/vibeworlding-multimodal-3d-world-agents.md"
check "entity vibeworlding-gym" test -f "${REPO_ROOT}/wiki/entities/tools/vibeworlding-gym.md"
check "policy K286" grep -q "K286" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "no-clone" bash -c '! test -d "${REPO_ROOT}/.local/adopts/VibeWorlding-Gym"'
warn_note "K286 VibeWorlding-Gym — null SPDX (no LICENSE) NO-GO clone; WATCH pattern only; wont_wire CCC/Image-gen/3D. Game-dev stub."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
