#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K306 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-argus-mcp-k8s-rca-2608.23084.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/diagnostic-prescriptive-asymmetry-mcp-rca.md"
check "policy K306" grep -q "K306" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K306" grep -q "K306" "${REPO_ROOT}/.cursor/rules/ccc-k300-k309-phase1-wires.mdc"
warn_note "K306 ARGUS MCP K8s RCA diagnostic/prescriptive asymmetry; no public repo; runtime wont_wire; dual-ID vs CCC K253 Argus persist/pivot (different product)."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
