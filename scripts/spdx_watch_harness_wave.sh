#!/usr/bin/env bash
# SPDX watch — CordisBench, HarnessDev, InstructionArbitrationBench (CCC leftovers)
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "SPDX watch — harness wave leftovers ($(date -u +%Y-%m-%d))"

watch_repo() {
  local slug="$1"
  local query="$2"
  echo ""
  echo "==> $slug (query: $query)"
  local hit
  hit="$(gh search repos "$query" --limit 3 --json fullName,license,updatedAt 2>/dev/null || echo '[]')"
  if [[ "$hit" == "[]" || -z "$hit" ]]; then
    echo "  WATCH — no public GitHub repo found"
    return 0
  fi
  echo "$hit" | python3 -c "
import json, sys
rows = json.load(sys.stdin)
for r in rows:
    lic = (r.get('license') or {}).get('spdxId') or 'NOASSERTION'
    updated = (r.get('updatedAt') or '?')[:10]
    print(f\"  {r['fullName']}  SPDX={lic}  updated={updated}\")
"
}

watch_repo "CordisBench" "CordisBench arxiv 2609.01600"
watch_repo "HarnessDev" "HarnessDev self-developing-agents"
watch_repo "InstructionArbitrationBench" "InstructionArbitrationBench instruction arbitration"
watch_repo "DelegationWithoutTrust" "delegation without trust votal LLM Shield"
watch_repo "HarnessDesignCodingAgents" "empirical study harness design coding agents arxiv 2609.20804"
watch_repo "Agensh" "Agensh scaling organizational intelligence microsoft arxiv 2609.26781"
watch_repo "RecreationWorld" "RecreationWorld hybrid computer-use agents arxiv 2609.22000"

watch_repo "AgentApprovalLaundering" "Agent Approval Laundering arxiv 2609.28586"
watch_repo "AgentEditingWorldModel" "Agent-Editing World Model arxiv 2609.28416"
watch_repo "RecToolBench" "RecToolBench recommendation tool orchestration arxiv 2609.30717"

echo ""
watch_repo "Assay" "assay claims that decay with the code arxiv 2609.36170"
watch_repo "MetaSkill-AI4AI" "learning meta-skills agent harness design arxiv 2609.38143"
watch_repo "MotorMind" "motormind vision language robot manipulation arxiv 2609.38078"
watch_repo "AuditableLTM" "auditable long-term memory deterministic retrieval chain arxiv 2609.38021"
watch_repo "TokenCast" "TokenCast agent token forecast arxiv 2609.35760"
echo "Done. No clones performed — report only."
