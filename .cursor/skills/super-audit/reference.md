# Super audit — reference

## Default 5-auditor roster

| Slot | Channel | Model slug | Provider | Env / key |
|------|---------|------------|----------|-----------|
| 1 | Cursor Task | `claude-opus-4-8-thinking-high` | Anthropic | (Cursor subscription) |
| 2 | Cursor Task | `gpt-5.3-codex` | OpenAI | (Cursor subscription) |
| 3 | Cursor Task | `gemini-3.1-pro` | Google | (Cursor subscription) |
| 4 | HTTP API | `x-ai/grok-4.3` | OpenRouter | `OPENROUTER_API_KEY` |
| 5 | HTTP API | `deepseek-reasoner` | DeepSeek | `DEEPSEEK_API_KEY` |

Substitute unavailable Cursor slugs per [cursor-audit reference](../cursor-audit/reference.md) (Anthropic fallback: opus → sonnet). Never duplicate provider family in slots 1–3.

### Quick mode (4 auditors)

Slots 1–3 unchanged; slot 5 only for API (`deepseek-reasoner`). Skip slot 4.

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
| `OPENROUTER_API_KEY` | Grok, Claude-via-OR, Gemini-via-OR, Kimi |
| `OPENROUTER_BASE_URL` | Default `https://openrouter.ai/api/v1` |
| `DEEPSEEK_API_KEY` | `deepseek-reasoner`, `deepseek-v4-flash` |
| `DEEPSEEK_BASE_URL` | Default `https://api.deepseek.com/v1` |
| `DEEPSEEK_MODEL` | Default model when slot says `deepseek-v4-flash` |
| `ADVISOR_API_KEY` | WC bot / custom advisor (often = OpenRouter) |
| `ADVISOR_BASE_URL` | Advisor OpenAI-compatible endpoint |
| `ADVISOR_MODEL` | e.g. `google/gemini-2.5-flash` |
| `ANTHROPIC_API_KEY` | Rare direct API (prefer OpenRouter for slot 4) |
| `OPENAI_API_KEY` | Direct OpenAI (usually not needed — Cursor covers) |

**Session bootstrap:**

```bash
source scripts/source_llm_routing_env.sh   # OSINT workspace
```

**Discovery script:**

```bash
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py --json
```

Output: which keys are present (masked), suggested API slots. Parent tells user what's missing before running API leg.

## auditors.json (override API slots)

Place beside pack or pass `--auditors`. Example:

```json
{
  "slots": [
    {
      "label": "grok-4.3-openrouter",
      "base_url_env": "OPENROUTER_BASE_URL",
      "api_key_env": "OPENROUTER_API_KEY",
      "model": "x-ai/grok-4.3",
      "extra": { "reasoning": { "effort": "high" } },
      "system": "Super audit — adversarial readonly reviewer."
    },
    {
      "label": "deepseek-reasoner",
      "base_url_env": "DEEPSEEK_BASE_URL",
      "api_key_env": "DEEPSEEK_API_KEY",
      "model": "deepseek-reasoner",
      "system": "Super audit — quant/strategy readonly reviewer."
    }
  ]
}
```

### Tailoring examples for API slots

| Domain | Slot 4 | Slot 5 |
|--------|--------|--------|
| Poker bot | `x-ai/grok-4.3` @ OR | `deepseek-reasoner` |
| WC bot / conviction | `google/gemini-2.5-flash` via `ADVISOR_*` | `deepseek-v4-flash` |
| Adoption brief | `anthropic/claude-opus-4.6` @ OR | `deepseek-reasoner` |
| Security | `x-ai/grok-4.3` @ OR | `moonshotai/kimi-k2.5` @ OR |

Use OpenRouter model IDs as listed on [openrouter.ai/models](https://openrouter.ai/models).

## Mode → Cursor triple

Same defaults as cursor-audit for slots 1–3:

| Mode | Model 1 | Model 2 | Model 3 |
|------|---------|---------|---------|
| **code-debug** | `gpt-5.3-codex` | `claude-opus-4-8-thinking-high` | `gemini-3.1-pro` |
| **security** | `claude-opus-4-8-thinking-high` | `gpt-5.3-codex` | `grok-4.3` |
| **config-infra** | `gemini-3.1-pro` | `gpt-5.5-medium` | `claude-4.6-sonnet-medium-thinking` |
| **brief-plan** | `claude-opus-4-8-thinking-high` | `gpt-5.3-codex` | `kimi-k2.5` |
| **architecture** | `claude-opus-4-8-thinking-high` | `gemini-3.1-pro` | `gpt-5.5-medium` |
| **prod-ship** | `claude-opus-4-8-thinking-high` | `gpt-5.3-codex` | `gemini-3.1-pro` |

**prod-ship** — default for bot/config deploy audits (poker S1, WC bot).

## Audit pack checklist

- [ ] Tailored prompt with `{{MODEL_SLOT}}` and `{pack_index}` placeholder
- [ ] `PACK_INDEX.md` lists every artifact with absolute paths
- [ ] Mission is one sharp question
- [ ] Regime boundaries explicit (no cross-pool claims)
- [ ] Required output format block in prompt
- [ ] Ruled-out hypotheses section
- [ ] `meta.json` records build timestamp

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
