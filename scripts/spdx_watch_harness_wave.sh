#!/usr/bin/env bash
# SPDX watch — harness-wave leftovers. Report only; never clones.
#
# Two lookup paths, because `gh search repos` matches on name/description ONLY:
#   1. watch_slug  — exact `gh api repos/<owner>/<repo>`. Use when the paper names its repo.
#   2. watch_query — fuzzy search fallback for repos whose slug is still unknown.
#
# Do not feed a full arXiv title to watch_query: search will return [] or unrelated
# fuzzy matches, and the failure is silent.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "SPDX watch — harness wave leftovers ($(date -u +%Y-%m-%d))"

watch_slug() {
  local slug="$1" note="${2:-}"
  echo ""
  echo "==> $slug  ${note:+($note)}"
  local json
  if ! json="$(gh api "repos/${slug}" 2>&1)"; then
    echo "  WATCH — slug not reachable: $(printf '%s' "$json" | head -1)"
    return 0
  fi
  printf '%s' "$json" | python3 -c "
import json, sys
d = json.load(sys.stdin)
lic = (d.get('license') or {}).get('spdx_id') or 'NOASSERTION'
print(f\"  SPDX={lic}  stars={d.get('stargazers_count')}  pushed={(d.get('pushed_at') or '?')[:10]}  archived={d.get('archived')}\")
"
}

watch_query() {
  local label="$1" query="$2"
  echo ""
  echo "==> $label (query: $query)"
  local out
  if ! out="$(gh search repos "$query" --limit 3 --json fullName,license 2>&1)"; then
    echo "  WATCH — search failed: $(printf '%s' "$out" | head -1)"
    return 0
  fi
  printf '%s' "$out" | python3 -c "
import json, sys
rows = json.load(sys.stdin)
if not rows:
    print('  WATCH — no public GitHub repo found')
    raise SystemExit(0)
for x in rows:
    # gh search repos returns license.key; only gh api repos/... has license.spdx_id.
    lic = (x.get('license') or {}).get('key') or 'NOASSERTION'
    print(f\"  {x['fullName']}  SPDX={lic}\")
"
}

# -- Exact slugs (paper names the repo) ---------------------------------------
watch_slug "OmShiv/assay-research" "K406 Assay"
watch_slug "qiancheng-apodex/MetaSkill-AI4AI" "K409 meta-skills"
watch_slug "cjchanh/longmemeval-evidence" "K407 auditable LTM"

# -- Fuzzy fallback (repo slug still unknown) ---------------------------------
watch_query "CordisBench" "CordisBench"
watch_query "HarnessDev" "HarnessDev"
watch_query "InstructionArbitrationBench" "InstructionArbitrationBench"
watch_query "DelegationWithoutTrust" "delegation-without-trust"
watch_query "HarnessDesignCodingAgents" "harness-design-coding-agents"
watch_query "Agensh" "Agensh"
watch_query "RecreationWorld" "RecreationWorld"
watch_query "AgentApprovalLaundering" "agent-approval-laundering"
watch_query "AgentEditingWorldModel" "agent-editing-world-model"
watch_query "RecToolBench" "RecToolBench"
watch_query "TokenCast" "TokenCast"
watch_query "MotorMind" "MotorMind"

echo ""
echo "Done. No clones performed — report only."
