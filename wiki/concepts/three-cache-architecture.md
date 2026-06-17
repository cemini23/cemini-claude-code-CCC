---
title: The three caches — OpenRouter Response, OpenRouter Edge, Anthropic KV
type: concept
tags: [concept, cache, prompt-cache, openrouter, anthropic, kv-cache, claude-code, cost-discipline]
keywords: [openrouter response cache, openrouter edge cache, anthropic kv cache, cache_control, ephemeral, static prompt prefix, cache invalidation]
related:
  - entities/tools/claude-code.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code-router.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/mcp-context-optimization.md
  - concepts/context-engineering.md
  - concepts/html-as-claude-code-output-format.md
  - concepts/local-llm-mechanics-primer.md
  - entities/tools/repomix.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - entities/tools/claude-subconscious.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - sources/arxiv-multi-factor-agentic-memory-2606.12945.md
  - concepts/storage-budgeted-agent-memory-compression.md
maturity: validated
created: 2026-05-13
updated: 2026-06-17
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/tools/lazy-tool.md` — keeps the static prefix actually static so KV cache stays warm
- `@entities/tools/claude-code-router.md` — injects OpenRouter cache headers when routing through it
- `@concepts/token-economics-and-prompt-caching.md` — cost-side write-up; this page covers the mechanism
- `@concepts/mcp-context-optimization.md` — how the three caches map to the four optimization layers
- `@concepts/context-engineering.md` — same toolkit from a different angle (what stays in context vs. what gets cached)

Cross-wiki: `@seo-wiki/entities/tools/claude-code-tool-stack.md` § "Key concept: the three caches" carries the original numbered list.

## Raw Concept

Question this page answers: **what's actually being cached when an LLM session is "cheap," and what invalidates each cache layer?**

## Narrative

Going from "AI is expensive" to "AI is nearly free" hinges on understanding three independent caches. Each has a different scope, different invalidation rule, and different cost-saving multiplier.

### Cache 1 — OpenRouter Response Cache

- **Scope**: full-prompt → full-response key.
- **Saves**: 100% (zero-cost hit). The provider returns a stored response without re-billing tokens.
- **Invalidation**: any byte change in the prompt — even a trailing space — busts the cache.
- **Where active**: only when routing via OpenRouter (e.g., through `@entities/tools/claude-code-router.md`) AND the response is still within the cache TTL. Not active when calling Anthropic directly.
- **Use case**: deterministic queries you re-run (regression checks, lookup-style prompts).

### Cache 2 — OpenRouter Edge Cache

- **Scope**: provider-routing decisions (which upstream provider served which prompt-class).
- **Saves**: latency, not tokens. Routing requests stick to a sticky upstream so subsequent prompts reuse the warm connection / model instance.
- **Invalidation**: provider rotation, upstream rate-limit, prompt-class change.
- **Where active**: when running through OpenRouter with provider-stickiness enabled.
- **Use case**: long sessions where consecutive prompts hit the same upstream.

### Cache 3 — Anthropic KV Cache (the load-bearing one)

- **Scope**: token-level prefix cache. Anthropic stores the model's KV state for the **prompt prefix** so subsequent turns reading the same prefix don't re-process those tokens.
- **Saves**: cached input tokens billed at ~10% of normal input rate.
- **TTL**: 5 minutes (~300 s). Crossing the boundary means a cache miss — full input cost.
- **Invalidation**: any change to the prefix. Inserting a token in the middle invalidates everything after.
- **Where active**: every Anthropic API call (and therefore every Claude Code session). This is the cache that matters most for Cemini.
- **Use case**: any session lasting >1 turn. Pace turns to stay under 270s for active work; commit to ≥1200s when idling. **Never sleep 300s** — see `@concepts/token-economics-and-prompt-caching.md`.

### The static-content-at-start rule

To maximize KV-cache hit rate, **keep static content (system instructions, tool definitions, large reference docs) at the START of the prompt; volatile content (stack traces, terminal output, recent file edits) at the END.**

- The prefix that doesn't change between turns gets cached.
- Anything after the first changing byte is fresh-billed.
- Putting a stack trace before the system prompt invalidates the entire system-prompt cache for that turn — wasteful.

This is why `@entities/tools/lazy-tool.md` matters: it freezes the system-prompt's MCP-tool block to a static 5-tool catalog. Without lazy-tool, every MCP server connect/disconnect mutates the system prompt and busts the cache.

### `cache_control: ephemeral` markers

Anthropic's API exposes `cache_control: { type: "ephemeral" }` markers on prompt blocks. Marked blocks are explicitly cache candidates. The Claude Code harness applies these automatically to its system prompt and large file reads. If you're calling the API directly (e.g., from `@osint-wiki/entities/tools/claude-mem.md` or the `claude-api` skill), set the marker explicitly on stable prompt sections.

### Cemini's cache discipline rules

1. Static at start, volatile at end — always.
2. Use `lazy-tool` if MCP-server count ≥ 5.
3. Active-poll delays: 60-270s (stay in window).
4. Idle delays: 1200-1800s (commit to one cache miss for a long wait).
5. **Never 300s** — worst-of-both.
6. Subagent dispatch is its own context; the parent's cache survives the subagent's work.

### What gets cached in a typical Cemini session

| Block | Cache behavior |
|-------|----------------|
| Harness instructions | KV-cached, stable across turns |
| Tool definitions (with lazy-tool) | KV-cached, stable across turns |
| Tool definitions (without lazy-tool) | Cache-busted on every connect/disconnect |
| Skill markdown (loaded via SessionStart hook) | KV-cached if loaded once at session start |
| File reads (via `Read` tool) | KV-cached during the 5-min window |
| Conversation history | KV-cached up to the most recent volatile insertion |
| User prompt | Volatile by definition (always re-billed) |

## Dead Ends

- **Treating OpenRouter caching as a substitute for Anthropic KV caching** — they're orthogonal. Native Anthropic = no OpenRouter cache; routing via OpenRouter = both, if configured.
- **Putting a fresh timestamp in the system prompt** — busts the prefix cache for every turn forever. Don't do it.
- **Trying to "cache" subagent results in the parent session** — subagents return a single message; that message becomes part of the parent's prompt and may or may not get re-cached on subsequent turns. Treat subagent dispatch as a one-shot context save, not a multi-turn cache strategy.
