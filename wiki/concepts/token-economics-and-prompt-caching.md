---
title: Token economics + prompt caching
type: concept
tags: [concept, tokens, cost, prompt-caching, cache-ttl, claude-code]
keywords: [prompt caching, cache TTL, 5 minute cache, ScheduleWakeup, cache amortization, token economics, cost discipline]
related:
  - entities/tools/claude-code.md
  - entities/patterns/ralph-loop.md
  - concepts/context-engineering.md
  - concepts/subagent-orchestration.md
  - concepts/three-cache-architecture.md
  - concepts/mcp-context-optimization.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code-router.md
  - entities/tools/ttok.md
  - entities/tools/everos.md
  - entities/openusage.md
  - entities/tools/ai-token-monitor.md
  - entities/tools/codexbar.md
  - entities/patterns/cpr-context-compression.md
  - entities/tools/repomix.md
  - concepts/local-llm-mechanics-primer.md
  - concepts/tools-we-dont-use.md
  - entities/tools/openevolve.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/karpathy-token-efficiency-patterns.md
maturity: validated
created: 2026-05-13
updated: 2026-05-27
---

## Relations

- `@entities/tools/claude-code.md` — the harness whose pricing this concept reasons about
- `@entities/patterns/ralph-loop.md` — Ralph's many-fresh-contexts profile interacts with cache TTL
- `@concepts/context-engineering.md` — context-engineering decisions are funded out of the same budget
- `@concepts/subagent-orchestration.md` — subagent dispatch trades parent-context tokens for subagent setup tokens
- `@concepts/three-cache-architecture.md` — the three independent caches that this discipline pages reasons about (mechanism)
- `@concepts/mcp-context-optimization.md` — the four-layer optimization stack
- `@entities/tools/lazy-tool.md` — Layer 1 of the optimization stack (46% input-token reduction per source claim)
- `@entities/tools/claude-code-router.md` — Layer 2 (cost-class routing + cache headers)
- `@entities/tools/ttok.md` — preview-counting before paste
- `@entities/openusage.md` — background telemetry daemon tracking API token consumption + spend across local dev environments
- `@entities/tools/ai-token-monitor.md` — cross-platform Tauri desktop app monitoring Claude Code + Codex token usage (offline-first)
- `@entities/tools/codexbar.md` — macOS menu-bar app with daily/weekly limit tracking + overrun notifications

## Raw Concept

Question this page answers: **what does a Claude Code session cost, and how do you minimize it without sacrificing quality?**

## Narrative

Claude Code's per-session cost is dominated by three lines:

1. **Input tokens** — everything in the model's context window each turn: the prompt envelope, conversation history, tool-call results, file contents the model `Read`. Larger windows = more per-turn input tokens.
2. **Cached input tokens** — same as input, but at a steep discount (typically ~10% of regular input cost) when served from the prompt cache.
3. **Output tokens** — the model's reply. Usually small compared to input.

The prompt cache makes the difference between an affordable session and a runaway. Two facts govern Cemini's pacing:

### Fact 1 — the cache TTL is 5 minutes

The Anthropic prompt cache has a 5-minute (~300 s) TTL. Any subsequent turn within 5 minutes of the previous turn reads most of the prior context from cache at the discount rate. **Crossing the 5-minute boundary means a cache miss** — the full context gets re-billed as fresh input.

### Fact 2 — `ScheduleWakeup` and `/loop` delays should respect the TTL

When the harness offers `ScheduleWakeup` for /loop dynamic mode or `delaySeconds` for polling, the right delay is **never 300 seconds**:

- **Under 270s** → cache stays warm. Use this when actively polling an external job (CI run, deploy, remote queue).
- **300s** → worst-of-both. Pay the cache miss without amortizing it. Never pick this.
- **1200s-1800s+** → commit to the cache miss; one miss buys a much longer wait. Use this for idle ticks or when the watched state changes slowly.

The CCC ScheduleWakeup tool docs encode this rule. The OSINT CLAUDE.md "External research — Exa MCP" section carries a parallel cost-discipline write-up for the Exa API; the principles compose.

### Fact 3 — subagents pay startup but save parent context

Each `Agent` (subagent) invocation pays its own setup tokens (~1-3K depending on subagent type and tool surface). In return, only the subagent's *reply* lands in the parent context — typically <1K. **Net win** when the subagent would have ingested >10K of raw read content otherwise. **Net loss** for trivial lookups where direct `Read`/`Grep` is fewer tokens.

### Fact 4 — Ralph's loops are an N×(setup+small-work) profile

Ralph's fresh-context-per-iteration trade is: N small contexts vs 1 large context. Each Ralph iteration pays its own startup tokens (no cache reuse across loops because the context is wiped). The trade is worth it when context degradation in the long single window would cost more than the setup tokens for N short windows.

### Cemini's cost rules of thumb

- **Default delay for idle ticks**: 1200-1800s. Don't burn cache 12×/hour for nothing.
- **Default delay for active polling**: 60-270s. Stay in the cache window.
- **Default for subagent dispatch**: when the alternative is >10K of raw reads, dispatch; otherwise direct.
- **Default for Exa `numResults`**: 3-5. Higher rarely improves signal-to-noise; see `@entities/mcp-servers/exa.md`.
- **Default for `deep_researcher_*`**: only when ≥3 distinct sources required.

### Fast mode (Opus 4.7)

`/fast` toggles fast-mode on Opus 4.7 — same model, faster output, no quality downgrade. Cost profile is comparable; the win is wall-clock time, not tokens. Cemini uses `/fast` for interactive sessions where the model needs to feel responsive, slower mode for autonomous loops where output speed doesn't matter.

### MCP overhead — the silent budget killer

Every MCP server connected to the harness injects its full tool catalog into every prompt envelope: `name + description + JSON schema` per tool. The numbers (per `@osint-wiki/concepts/mcp-context-optimization.md` and `@seo-wiki/entities/tools/claude-code-tool-stack.md`):

- 5-10 MCP servers × ~300 tokens per tool × 30-50 tools = **30,000-75,000 tokens per turn before the user types**
- Every tool connect/disconnect mutates the prefix → **busts the KV cache** → next turn re-bills full price
- Compounds across multi-turn sessions

Mitigation:

1. **`@entities/tools/lazy-tool.md`** — replaces the catalog with 5 meta-tools. Source claim: 46% input-token reduction, 32% latency reduction. Break-even at ~5 MCP servers.
2. **Static-at-start, volatile-at-end** — keep system prompt + tool definitions at the start, let stack traces / file content / user prompts pile up at the end. Anthropic KV cache stays warm.
3. **`cache_control: ephemeral` markers** — for direct API users; the harness applies these automatically.

### Three caches — quick reference (full detail in `@concepts/three-cache-architecture.md`)

| Cache | Saves | TTL / scope |
|-------|-------|-------------|
| Anthropic KV (load-bearing) | Cached input at ~10% of normal rate | 5-min TTL; busts on any prefix change |
| OpenRouter Response | 100% (zero-cost hit) | Per-prompt key; busts on any byte change |
| OpenRouter Edge | Latency only | Provider-stickiness |

### Cost asymmetry that justifies cache discipline

A typical Cemini session (~60K tokens carried forward turn-to-turn):
- Cold: 60K × $3/MTok input ≈ $0.18/turn
- Cached: 60K × $0.30/MTok cached-input ≈ $0.018/turn
- **10× difference** — pace turns to keep the cache warm and the same session costs an order of magnitude less.

## Dead Ends

- **Sleeping 5 minutes (300s)** — worst case. Either ≤270s or ≥1200s.
- **Subagent dispatch for trivial lookups** — pays setup, saves nothing. Direct `Read`/`Grep` is fewer tokens.
- **Manual cache management** — there isn't any. The harness manages it; pace your turns to stay within or commit beyond the TTL.
- **Loading the full MCP tool surface up front** — burns 30-75K tokens/turn. Use `ToolSearch` deferred-tools (built-in) or `@entities/tools/lazy-tool.md` (for MCP).
- **Putting a fresh timestamp anywhere in the system prompt** — busts the KV cache for every turn forever.
