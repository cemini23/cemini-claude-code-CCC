# Super audit — examples

## Example 1 — Poker Tournament S1 (reference run)

**User:**

> super audit before Tournament S1 — should we ship current decide commit?

**Parent:**

1. **Tailor** — `agents/devfun-poker-arena/prompts/tournament_s1_super_audit.md` (S1 win table, S2 struggle, env toggles, VPIP band)
2. **Pack** — `build_tournament_super_audit_pack.py` (domain-specific) or generic `build_audit_pack.py` with HL artifacts
3. **Cursor** — fable + codex + gemini, `prod-ship` mode (`opus` if user overrides Anthropic leg)
4. **API** — `run_tournament_super_audit_api.py` or generic `run_api_auditors.py` (Grok + DeepSeek)
5. **Synthesize** — `briefs/2026-06-09_tournament-s1-super-audit-synthesis.md`

**Outcome:** 4/5 recommended `70f2527` revert; operator shipped lane-gate hybrid `4a6df45` after conflict resolution.

---

## Example 2 — WC bot prod posture

**User:**

> super audit on world cup conviction config before match day

**Parent:**

1. **Tailor** prompt with 43-team matrix, `conviction.yaml` excerpts, LP safety cadence, inflow posture
2. **Artifacts** — `gemini-wc-conviction-config-audit` snippets, prod pull briefs, `wiki/meta/wc-lp-safety-cadence.md`
3. **Mode** — `brief-plan` + `prod-ship`
4. **API override** (`auditors.json`):

```json
{
  "slots": [
    {
      "label": "advisor-gemini",
      "base_url_env": "ADVISOR_BASE_URL",
      "api_key_env": "ADVISOR_API_KEY",
      "model": "google/gemini-2.5-flash"
    },
    {
      "label": "deepseek-v4",
      "base_url_env": "DEEPSEEK_BASE_URL",
      "api_key_env": "DEEPSEEK_API_KEY",
      "model": "deepseek-v4-flash"
    }
  ]
}
```

5. **Synthesize** — team downgrade list, cancel-window risk, SHIP-WITH-FIXES on stale `fade_watch` rows

**Keys:** `source scripts/source_llm_routing_env.sh` wires `ADVISOR_*` from OpenRouter when set.

---

## Example 3 — Quick super audit

**User:**

> quick super audit on scripts/sync_wiki_to_librarian.sh

**Parent:**

1. Mode `quick-triage` — cursor: composer + gpt-5.5-medium + sonnet
2. API: DeepSeek only (skip Grok)
3. Minimal pack — script source + recent log excerpt
4. Top-3 issues synthesis only

---

## Example 4 — Missing API keys

**Discovery output:**

```
OPENROUTER_API_KEY: present (sk-or-…xxxx)
DEEPSEEK_API_KEY: missing
```

**Parent:**

> API leg: DeepSeek slot skipped. Proceed with 4 auditors (3 Cursor + Grok)? Or add `DEEPSEEK_API_KEY` to `~/.cemini/llm-routing.env` and retry.

Never ask user to paste keys in chat.

---

## Example 5 — Re-audit after deploy

**User:**

> we shipped 4a6df45 but VPIP still low — super audit again

**Parent:**

1. Copy prior synthesis into **Already ruled out** / prior consensus section
2. Refresh pack with new `deploys.jsonl` + playground status
3. Swap one Cursor model for fresh eyes (e.g. kimi for gemini)
4. Compare deploy commit recommendations vs previous rollup
