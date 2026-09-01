#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K328 Phase-0 — ${REPO_ROOT}"
pass=0; fail=0; warn=0
check(){ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }
warn_note(){ echo "  WARN  $1"; warn=$((warn+1)); }
check "source" test -f "${REPO_ROOT}/wiki/sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md"
check "concept" test -f "${REPO_ROOT}/wiki/concepts/output-attestation-and-delegation-ancestry.md"
check "policy K328" grep -q "K328" "${REPO_ROOT}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K328" grep -q "K328" "${REPO_ROOT}/.cursor/rules/ccc-k328-k332-phase1-wires.mdc"
check "no clone" test ! -d "${REPO_ROOT}/.local/adopts/AttestingOutputs"
check "concept wired" grep -q "wire_status: policy_wired" "${REPO_ROOT}/wiki/concepts/output-attestation-and-delegation-ancestry.md"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|poc' '${REPO_ROOT}/wiki/sources/arxiv-attesting-outputs-delegation-ancestry-2608.30387.md' '${REPO_ROOT}/wiki/concepts/output-attestation-and-delegation-ancestry.md'"
warn_note "K328 ADOPT policy — credentials ≠ later output bytes; two layers = deployer-runtime output-hash signature + edge-authorization ancestry; after child-key compromise only a co-signed DAG rejects unauthorized parent binding (signed list / Merkle-chain do not). Signatures do not stop prompt injection. Pairs K278/K285/K310. No public SPDX → policy only, no clone. Cybersec steal."
echo "Summary: ${pass} pass, ${fail} fail, ${warn} warn"
[[ "${fail}" -eq 0 ]]
