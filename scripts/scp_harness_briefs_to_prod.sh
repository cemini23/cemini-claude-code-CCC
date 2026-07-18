#!/usr/bin/env bash
# SCP CCC harness adoption briefs to cemini-prod:/opt/cemini/briefs/
# Skips files already present with same size (re-scp with FORCE=1 to overwrite).
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
BRIEFS_DIR="${REPO_ROOT}/briefs"
REMOTE="cemini-prod:/opt/cemini/briefs"
FORCE="${FORCE:-0}"

BRIEFS=(
  "2026-06-10_k109-bayesian-agent-harness-cluster-prod.md"
  "2026-06-15_k115-context-memory-recursion-prod.md"
  "2026-06-16_k116-orchrm-harnessx-llm-as-code-prod.md"
  "2026-06-17_k117-memory-seagym-finacumen-prod.md"
  "2026-06-18_k118-spec-driven-pegasus-workflow-prod.md"
  "2026-06-19_k119-agent-first-web-eda-handoff-prod.md"
  "2026-06-20_k120-user-as-code-dynamo-prod.md"
  "2026-06-21_k121-tokenpilot-safeclaw-gatekeepers-prod.md"
  "2026-06-22_k122-xcientist-claim-drift-prod.md"
  "2026-06-22_k126-nvidia-mattpocock-skills-adopt.md"
  "2026-06-23_k123-dia-agentic-web-aohp-prod.md"
  "2026-06-23_k127-aohp-secure-agent-interfaces-reference.md"
  "2026-06-24_k124-harness-memory-research-cluster-prod.md"
  "2026-06-24_k124-harness-policy-hands-on.md"
  "2026-06-25_k125-memory-orchestration-cluster-prod.md"
  "2026-06-25_k122-k126-federation-cursor-harness-adoptions-cemini-prod.md"
  "2026-06-26_k128-memprobe-memory-recovery-prod.md"
  "2026-06-27_k129-tool-reliability-orchestration-prod.md"
  "2026-06-27_k132-local-adoptions-cursor-federation-prod.md"
  "2026-06-29_k134-codebase-memory-cursor-federation-prod.md"
  "2026-06-30_k135-clarus-research-collaboration-prod.md"
  "2026-07-01_k136-agentic-orchestration-options-abpm-prod.md"
  "2026-07-02_k137-automem-metamemory-cognitive-skill-prod.md"
  "2026-07-07_k138-substrate-constraints-agent-oversight-prod.md"
  "2026-07-07_k139-agentic-online-rl-self-evolving-prod.md"
  "2026-07-09_k150-algorithmic-impermeability-orchestration-prod.md"
  "2026-07-10_k151-cage-1-prebind-assurance-prod.md"
  "2026-07-10_k152-polyworkbench-multilingual-eval-prod.md"
  "2026-07-13_k153-miles-modular-instruction-memory-prod.md"
  "2026-07-13_k154-hierarchical-bounded-agent-memory-prod.md"
  "2026-07-13_k156-deepsearch-world-verifiable-search-prod.md"
  "2026-07-13_k157-trustx-agent-risk-classification-prod.md"
  "2026-07-14_k155-ideagene-lineage-eval-prod.md"
  "2026-07-15_k156-llm-risk-behaviour-audit-prod.md"
  "2026-07-17_k158-play-adequacy-world-model-eval-prod.md"
  "2026-07-14_k162-rsi-verification-hierarchy-prod.md"
  "2026-07-14_k164-hierarchical-skill-stack-lazy-orchestration-prod.md"
  "2026-07-14_k162-k164-k155-harness-policy-hands-on.md"
  "2026-07-14_stash-mcp-redeploy-prod.md"
  "2026-07-15_k168-slm-harness-adaptation-prod.md"
  "2026-07-15_k169-harness-evolution-eval-discipline-prod.md"
  "2026-07-15_k168-k169-harness-policy-hands-on.md"
  "2026-07-15_k169-harness-adaptation-evaluation-rigor-prod.md"
  "2026-07-16_k175-amt-x-checklist-gated-asr-prod.md"
  "2026-07-16_k176-aha-vcg-production-agent-red-team-prod.md"
  "2026-07-16_k177-skillsec-lifecycle-skill-security-prod.md"
  "2026-07-16_k178-gflowrl-attacker-rl-reference-prod.md"
  "2026-07-16_k171-agent-optimizer-compounding-prod.md"
  "2026-07-16_k172-mcp-contract-validation-gate-prod.md"
  "2026-07-16_k173-mcp-graceful-degradation-prod.md"
  "2026-07-16_k171-k173-harness-policy-hands-on.md"
  "2026-07-17_k184-datashield-risky-finetune-prod.md"
  "2026-07-17_k185-prism-physical-vs-content-danger-prod.md"
  "2026-07-17_k186-agentic-hard-example-synthesis-prod.md"
  "2026-07-17_k187-statistical-self-consistency-prod.md"
  "2026-07-17_k179-coding-agent-preinstall-gate-prod.md"
  "2026-07-17_k180-searchos-socm-prod.md"
  "2026-07-17_k181-policy-as-code-guardrails-prod.md"
  "2026-07-17_k182-acp-mcp-three-layer-prod.md"
  "2026-07-17_k179-k182-harness-policy-hands-on.md"
  "2026-07-18_k159-aleena-lifecycle-alignment-prod.md"
  "2026-07-18_k159-memory-scarcity-open-inference-prod.md"
  "2026-07-18_k188-armor-plusplus-deepfake-prod.md"
  "2026-07-18_k189-flowguard-mcp-evidence-prod.md"
  "2026-07-18_k189-harness-policy-hands-on.md"
)

echo "SCP harness briefs → ${REMOTE}"
ssh cemini-prod 'mkdir -p /opt/cemini/briefs'

sent=0
skipped=0
missing=0

for name in "${BRIEFS[@]}"; do
  local_path="${BRIEFS_DIR}/${name}"
  if [[ ! -f "${local_path}" ]]; then
    echo "  MISSING local ${name}"
    missing=$((missing + 1))
    continue
  fi
  local_size="$(wc -c < "${local_path}" | tr -d ' ')"
  remote_size="$(ssh cemini-prod "test -f /opt/cemini/briefs/${name} && wc -c < /opt/cemini/briefs/${name} || echo 0" 2>/dev/null | tr -d ' ')"
  if [[ "${FORCE}" != "1" && "${remote_size}" == "${local_size}" && "${remote_size}" != "0" ]]; then
    echo "  SKIP ${name} (same size on prod)"
    skipped=$((skipped + 1))
    continue
  fi
  scp -q "${local_path}" "${REMOTE}/${name}"
  echo "  OK   ${name} (${local_size} bytes)"
  sent=$((sent + 1))
done

echo ""
echo "Summary: ${sent} sent, ${skipped} skipped, ${missing} missing local"
