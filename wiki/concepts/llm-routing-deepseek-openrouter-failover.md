---
title: LLM routing — DeepSeek primary, OpenRouter failover
type: concept
tags: [concept, llm, deepseek, openrouter, routing, failover, cemini, cross-project]
keywords: [llm-routing, deepseek, openrouter, failover, DEEPSEEK_API_KEY, OPENROUTER_API_KEY, llm_analyst, brain]
related:
  - concepts/deepseek-coding-cost-routing.md
  - concepts/mcp-context-optimization.md
  - concepts/three-cache-architecture.md
  - entities/tools/claude-code-router.md
  - entities/tools/ai-token-monitor.md
  - entities/tools/agent-toolkit.md
  - entities/skills/route.md
  - entities/tools/opencode.md
  - entities/tools/reasonix.md
  - entities/tools/deepseek-harness.md
  - "@osint-wiki/concepts/api-credential-registry.md"
  - "@osint-wiki/entities/infrastructure/deepseek-api.md"
  - "@gambling-wiki/concepts/poker-hl-analyst-loop.md"
  - "@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md"
maturity: draft
created: 2026-06-04
updated: 2026-08-14
---

## Relations

- @concepts/deepseek-coding-cost-routing.md — cheap-model discipline; this page is **automatic failover** when DeepSeek quota hits
- @entities/tools/claude-code-router.md — prod proxy layer; complementary to app-level `llm_routing.py`
- @entities/tools/agent-toolkit.md — private `/route` script host (`ROUTE_KIT`)
- @entities/skills/route.md — federation `/route` skill v2.3
- @entities/tools/opencode.md — Phase-0; NO-GO mid swap (not `@osint-wiki/entities/tools/opencodex.md`)
- @entities/tools/reasonix.md — Phase-0; NO-GO mid swap
- @entities/tools/deepseek-harness.md — official `dsh` `/route` worker behind `claude-ds` (v2.3.2)
- @osint-wiki/concepts/api-credential-registry.md — key names only (`DEEPSEEK_*`, `OPENROUTER_*`)
- @osint-wiki/entities/infrastructure/deepseek-api.md — Cemini brain entity
- @gambling-wiki/concepts/poker-hl-analyst-loop.md — `cemini_hl_loop.sh` sources routing env at start
- @osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md — canonical implementation paths

## Raw Concept

Operator asked for OpenRouter as a **backup when DeepSeek tokens run out**, across poker HL, world-cup-bot advisor, CeminiSuite `llm_analyst` brain, and OSINT scripts (`_llm_retry` / `skill_audit --llm-mode`). Implemented 2026-06-04 in OSINT WORKSPACE as shared env + Python router.

## Narrative

### One-time install

```bash
cd ~/Desktop/OSINT\ WORKSPACE
bash scripts/install_llm_routing_env.sh
# Edit ~/.cemini/llm-routing.env — DEEPSEEK_API_KEY + OPENROUTER_API_KEY
```

Install copies `config/llm-routing.env.example` → `~/.cemini/llm-routing.env` (never overwrites an existing file).

### Per session (any project)

```bash
source ~/Desktop/OSINT\ WORKSPACE/scripts/source_llm_routing_env.sh
```

Search order: `CEMINI_LLM_ROUTING_ENV` → `~/.cemini/llm-routing.env` → OSINT `.env` → `config/llm-routing.env`.

Also sets `ADVISOR_*` for world-cup-bot when unset (OpenRouter preferred if `OPENROUTER_API_KEY` is set).

### Failover rules

| Trigger | Action |
|---------|--------|
| HTTP 402 / 429 from DeepSeek | Retry same request on OpenRouter |
| Body mentions `quota`, `balance`, `billing`, `insufficient` | Same |
| `DEEPSEEK_API_KEY` unset, `OPENROUTER_API_KEY` set | OpenRouter-only |
| `LLM_FALLBACK_ENABLED=false` | No failover |

Default model map: `deepseek-v4-flash` → `deepseek/deepseek-chat` on OpenRouter. Override: `LLM_FALLBACK_MODEL`.

### Code consumers

| Consumer | Module |
|----------|--------|
| OSINT `skill_audit --llm-mode` | `scripts/_llm_retry.py` → `scripts/llm_routing.py` |
| CeminiSuite brain | `services/llm_analyst/deepseek_client.py` |
| Poker HL loop | `examples/cemini_hl_loop.sh` sources env before analyze |
| WC advisor | `ADVISOR_*` via `source_llm_routing_env.sh` |

**Prod:** add `OPENROUTER_*` to `/opt/cemini/.env` and redeploy `llm_analyst` container (`docker/compose.intelligence.yml` already passes vars).

### Cursor / Claude Code

Routing is **env-driven**, not a Cursor setting. Open a terminal, `source` the script, then run scripts or point OpenAI-compat tools at the same env. For HL patches, use OpenRouter in chat after sourcing (no runtime LLM in `cemini_decide.py`).

**`/route` claude-ds (2026-08-14 v2.3.2):** official DeepSeek Harness `dsh` behind PATH name `claude-ds`. Flash = easy/mid execute; Pro = Grok CLI usage-out stand-in (`-Model` → per-job `--patch`). Always-approve = `DSH_PERMISSION_MODE=danger-full-access`. Isolated Claude Code at `~/.deepseek-claude` is fallback only (`@entities/tools/deepseek-harness.md`).

## Snippets

> `Neither DEEPSEEK_API_KEY nor OPENROUTER_API_KEY is configured` — `scripts/llm_routing.py` when both keys missing.
