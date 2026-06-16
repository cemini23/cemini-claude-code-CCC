# Super audit — reference

Extends [cursor-audit model delegation](../cursor-audit/reference.md). Same **premium tier** and **role-based** picks for Cursor slots 1–3; API slots 4–5 use **API roles** below.

## 5-auditor layout

| Slot | Channel | Delegation |
|------|---------|------------|
| 1–3 | Cursor Task | Mode → role matrix (cursor-audit reference) |
| 4–5 | HTTP API | Mode → API role matrix (this file) |

**Quick mode:** slots 1–3 (premium Cursor roles) + slot 5 API only (skip slot 4 adversarial).

## Selection procedure (parent — Step 2)

1. Classify **mode** (add **`prod-ship`** for bot/config deploy GO/NO-GO).
2. Resolve **Cursor roles** for slots 1–3 per cursor-audit reference.
3. Resolve **API roles** for slots 4–5 per mode → API role matrix.
4. Run `discover_api_keys.py` — map available keys to API role candidates.
5. Build or select `auditors.json` from role picks (see templates below).
6. Announce:

   > Super audit — mode: `prod-ship` · Cursor roles: agentic-reasoning/codex/third-lens · API roles: adversarial/deep-reasoning · pack: `{path}`

Never paste API keys into chat.

## Mode → Cursor roles (slots 1–3)

Same as cursor-audit, plus:

| Mode | Slot 1 | Slot 2 | Slot 3 | Use when |
|------|--------|--------|--------|----------|
| **prod-ship** | agentic-reasoning | code-implementation | third-lens | Bot deploy, conviction.yaml, tournament lane (**super-audit default**) |

All other modes: see [cursor-audit reference](../cursor-audit/reference.md#mode--role-matrix).

## Mode → API roles (slots 4–5)

| Mode | Slot 4 role | Slot 5 role |
|------|-------------|-------------|
| **prod-ship** | api-adversarial | api-deep-reasoning |
| **code-debug** | api-adversarial | api-deep-reasoning |
| **security** | api-adversarial | api-deep-reasoning |
| **config-infra** | api-deep-reasoning | api-adversarial |
| **brief-plan** | api-strategic | api-deep-reasoning |
| **architecture** | api-adversarial | api-deep-reasoning |
| **quick** | *(skip)* | api-deep-reasoning |

## API premium catalog

Premium API models only — no flash/lite defaults unless env explicitly configures a pro-tier advisor.

| API role | Purpose | Provider / key | Premium candidates (best first) |
|----------|---------|----------------|----------------------------------|
| **api-adversarial** | Red-team, exploit paths, contrarian deploy takes | `OPENROUTER_API_KEY` | `x-ai/grok-4.3`, `moonshotai/kimi-k2.5` |
| **api-deep-reasoning** | Quant/strategy depth, numeric claims, patch ranking | `DEEPSEEK_API_KEY` | `deepseek-reasoner` |
| **api-strategic** | Brief displacement, narrative holes, GO/NO-GO | `OPENROUTER_API_KEY` or `ADVISOR_*` | `anthropic/claude-opus-4.6`, `ADVISOR_MODEL` if pro-tier |
| **api-advisor** | Domain-tuned leg when `ADVISOR_*` set | `ADVISOR_API_KEY` | `ADVISOR_MODEL` — **upgrade** flash/lite IDs to pro equivalent when tailoring |

**Excluded from default API legs:** `deepseek-v4-flash`, `google/gemini-*-flash` (unless user confirms advisor-only env and no pro key).

### Tailoring API roles by domain

| Domain | Slot 4 | Slot 5 |
|--------|--------|--------|
| Poker / trading bot | api-adversarial (Grok @ OR) | api-deep-reasoning |
| WC bot / conviction | api-advisor (pro `ADVISOR_MODEL`) | api-deep-reasoning |
| Adoption brief | api-strategic (Opus @ OR) | api-deep-reasoning |
| Security | api-adversarial (Grok or Kimi @ OR) | api-deep-reasoning |

Use OpenRouter model IDs from [openrouter.ai/models](https://openrouter.ai/models).

## API key discovery (run before Step 4b)

Search order (first file wins for each variable; script does not overwrite existing env):

| Priority | Path |
|----------|------|
| 1 | `$CEMINI_LLM_ROUTING_ENV` |
| 2 | `~/.cemini/llm-routing.env` |
| 3 | `{workspace}/.env` |
| 4 | `{workspace}/config/llm-routing.env` |
| 5 | `{project}/.env` (when auditing a subproject) |

**Variables to probe:**

| Variable | Used for |
|----------|----------|
| `OPENROUTER_API_KEY` | api-adversarial, api-strategic |
| `OPENROUTER_BASE_URL` | Default `https://openrouter.ai/api/v1` |
| `DEEPSEEK_API_KEY` | api-deep-reasoning |
| `DEEPSEEK_BASE_URL` | Default `https://api.deepseek.com/v1` |
| `ADVISOR_API_KEY` | api-advisor / api-strategic |
| `ADVISOR_BASE_URL` | Advisor OpenAI-compatible endpoint |
| `ADVISOR_MODEL` | Must be pro-tier for premium audit |
| `ANTHROPIC_API_KEY` | Rare direct API (prefer OpenRouter) |
| `OPENAI_API_KEY` | Direct OpenAI (Cursor leg usually sufficient) |

**Session bootstrap:**

```bash
source scripts/source_llm_routing_env.sh   # OSINT workspace
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py --json
```

Discovery output lists **role → model** suggestions; parent picks two roles per mode matrix.

## auditors.json (build from roles)

Pass `--auditors path/to/auditors.json` to `run_api_auditors.py`. Labels should reflect **role**, not vendor lock-in.

**Default fallback** (`auditors.default.json`) — prod-ship generic: api-adversarial + api-deep-reasoning.

```json
{
  "slots": [
    {
      "label": "api-adversarial",
      "role": "api-adversarial",
      "base_url_env": "OPENROUTER_BASE_URL",
      "api_key_env": "OPENROUTER_API_KEY",
      "model": "x-ai/grok-4.3",
      "extra": { "reasoning": { "effort": "high" } },
      "system": "Super audit — adversarial readonly reviewer. Follow required output format exactly."
    },
    {
      "label": "api-deep-reasoning",
      "role": "api-deep-reasoning",
      "base_url_env": "DEEPSEEK_BASE_URL",
      "api_key_env": "DEEPSEEK_API_KEY",
      "model": "deepseek-reasoner",
      "system": "Super audit — deep reasoning readonly reviewer. Follow required output format exactly."
    }
  ]
}
```

**Brief-plan example** — swap slot 4 to api-strategic:

```json
{
  "label": "api-strategic",
  "role": "api-strategic",
  "base_url_env": "OPENROUTER_BASE_URL",
  "api_key_env": "OPENROUTER_API_KEY",
  "model": "anthropic/claude-opus-4.6",
  "system": "Super audit — strategic readonly reviewer. Follow required output format exactly."
}
```

Parent **rewrites `model`** fields when discovery or tailoring picks a different premium candidate for the role.

## Audit pack checklist

- [ ] Tailored prompt with `{{MODEL_SLOT}}` and `{pack_index}` placeholder
- [ ] `PACK_INDEX.md` lists every artifact with absolute paths
- [ ] Mission is one sharp question
- [ ] Regime boundaries explicit (no cross-pool claims)
- [ ] Required output format block in prompt
- [ ] Ruled-out hypotheses section
- [ ] `meta.json` records build timestamp
- [ ] Synthesis header lists roles + resolved slugs for all 5 slots

## Synthesis thresholds (5 auditors)

| Pattern | Verdict |
|---------|---------|
| ≥4 agree on critical issue | FAIL → REJECT or REWORK |
| ≥3 agree on critical | FAIL |
| Critical from 1–2 only | WARN → investigate |
| ≥4 PASS | SHIP (note unique warns) |
| Split on deploy commit / root cause | REWORK until conflict resolved |

## HTTP requirements

API script needs `httpx` (`uv pip install httpx` or project venv). Timeout 600s per call. Temperature 0.2.

## Integration with static brief audit

For `briefs/` handoffs:

1. Super audit synthesis (qualitative, 5-model)
2. `python3 scripts/skill_audit.py briefs/<file>.md`

Static REJECT overrides multi-model SHIP.
