#!/usr/bin/env bash
# SPDX watch — harness-wave leftovers. Report only; never clones.
#
# Two lookup paths, because `gh search repos` matches on name/description ONLY:
#   1. watch_slug  — exact `gh api repos/<owner>/<repo>`. Use when the paper names its repo.
#   2. watch_query — fuzzy search fallback for repos whose slug is still unknown.
#
# Do not feed a full arXiv title to watch_query: search returns [] or unrelated fuzzy
# matches, and the failure is silent.
#
# Absence and failure are DIFFERENT results and must not be conflated:
#   - HTTP 404 on `gh api`  → the repo is absent. A real answer.
#   - any other error       → the lookup FAILED. Not an answer at all.
# The script exits 3 if any lookup failed, so automation cannot read a broken
# lookup as "no repo exists". Adopted from the Cybersecurity wiki's gh_lookup.sh
# after their 2026-09-30 review of this file.
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

LOOKUP_FAILED=0
MISSING=0

echo "SPDX watch — harness wave leftovers ($(date -u +%Y-%m-%d))"

# Prints repo JSON on stdout. Returns 0=ok, 2=absent (404), 3=lookup failure.
gh_api_slug() {
  local slug="$1" out rc
  out="$(gh api "repos/${slug}" 2>&1)" && { printf '%s' "$out"; return 0; }
  rc=$?
  if grep -q "HTTP 404" <<<"$out"; then return 2; fi
  printf '%s\n' "$out" >&2
  return 3
}

watch_slug() {
  local slug="$1" note="${2:-}"
  echo ""
  echo "==> $slug  ${note:+($note)}"
  local json rc
  json="$(gh_api_slug "$slug")" && rc=0 || rc=$?
  case "$rc" in
    0)
      printf '%s' "$json" | python3 -c "
import json, sys
d = json.load(sys.stdin)
lic = (d.get('license') or {}).get('spdx_id') or 'NOASSERTION'
print(f\"  SPDX={lic}  stars={d.get('stargazers_count')}  pushed={(d.get('pushed_at') or '?')[:10]}  archived={d.get('archived')}\")
" ;;
    2)
      MISSING=$((MISSING + 1))
      echo "  ABSENT — GitHub 404. The repo does not exist under this slug." ;;
    *)
      LOOKUP_FAILED=$((LOOKUP_FAILED + 1))
      echo "  ERROR — lookup failed (details on stderr). This is NOT an absence." ;;
  esac
}

watch_query() {
  local label="$1" query="$2"
  echo ""
  echo "==> $label (query: $query)"
  local out
  if ! out="$(gh search repos "$query" --limit 3 --json fullName,license 2>&1)"; then
    LOOKUP_FAILED=$((LOOKUP_FAILED + 1))
    printf '%s\n' "$out" >&2
    echo "  ERROR — search failed (details on stderr). This is NOT an absence."
    return 0
  fi
  printf '%s' "$out" | python3 -c "
import json, sys
rows = json.load(sys.stdin)
if not rows:
    print('  EMPTY — search returned no candidates (a true negative for this query)')
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
echo "Done. ${MISSING} absent, ${LOOKUP_FAILED} lookup failure(s). No clones performed — report only."
if [[ "$LOOKUP_FAILED" -gt 0 ]]; then
  echo "A lookup failed. Absence was NOT established for those entries." >&2
  exit 3
fi
