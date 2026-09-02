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
  hit="$(gh search repos "$query" --limit 3 --json fullName,licenseInfo,updatedAt 2>/dev/null || echo '[]')"
  if [[ "$hit" == "[]" || -z "$hit" ]]; then
    echo "  WATCH — no public GitHub repo found"
    return 0
  fi
  echo "$hit" | python3 -c "
import json, sys
rows = json.load(sys.stdin)
for r in rows:
    lic = (r.get('licenseInfo') or {}).get('spdxId') or 'NOASSERTION'
    updated = (r.get('updatedAt') or '?')[:10]
    print(f\"  {r['fullName']}  SPDX={lic}  updated={updated}\")
"
}

watch_repo "CordisBench" "CordisBench arxiv 2609.01600"
watch_repo "HarnessDev" "HarnessDev self-developing-agents"
watch_repo "InstructionArbitrationBench" "InstructionArbitrationBench instruction arbitration"
watch_repo "DelegationWithoutTrust" "delegation without trust votal LLM Shield"

echo ""
echo "Done. No clones performed — report only."
