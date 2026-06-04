---
title: MCP context optimization — the four-layer stack
type: concept
tags: [concept, mcp, context, optimization, lazy-loading, caching, claude-code, cost-discipline]
keywords: [mcp context optimization, four-layer stack, lazy-tool, claude-code-router, openrouter caching, context-budget audit, 46% reduction]
related:
  - entities/tools/claude-code.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code-router.md
  - entities/tools/ttok.md
  - concepts/three-cache-architecture.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/context-engineering.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/claude-mem.md
  - entities/tools/optillm.md
  - entities/tools/lap-platform.md
  - entities/tools/n8n-mcp.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/claude-code-large-codebase-workflow.md
  - concepts/maven-agentic-tool-calling-generalization.md
  - sources/arxiv-maven-agentic-tool-calling-2605.30738.md
  - concepts/slm-agent-orchestration-gateway.md
  - concepts/runtime-context-mcp-file-refs.md
  - concepts/agent-skills-progressive-disclosure.md
  - sources/arxiv-agent-skills-architecture-security-2602.12430.md
  - concepts/mcp-server-catalog-curation.md
maturity: validated
created: 2026-05-13
updated: 2026-06-04
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/tools/lazy-tool.md` — Layer 1
- `@entities/tools/claude-code-router.md` — Layer 2
- `@entities/tools/ttok.md` — measurement tool used at every layer
- `@concepts/three-cache-architecture.md` — Layer 3 detail
- `@concepts/token-economics-and-prompt-caching.md` — sibling cost-discipline page
- `@concepts/context-engineering.md` — context-side companion
- `@entities/tools/optillm.md` — OpenAI-API-compatible multi-provider LLM proxy + MCP client (a routing-layer option adjacent to Layer 2)
- `@entities/tools/lap-platform.md` — compiles API specs into agent-native MCP scaffolding; reduces hand-coded tool-definition surface

Cross-wiki: `@osint-wiki/concepts/mcp-context-optimization.md` is the original 4-layer methodology source (K34 ingest, OSINT side).

## Raw Concept

Question this page answers: **what are the layers Cemini stacks to keep multi-MCP Claude Code sessions affordable?**

## Narrative

A Cemini session with 5-10 MCP servers connected directly to the harness burns 30,000-75,000 tokens per turn on tool catalog overhead alone — before the user types anything. Per-session that's expensive; per-day across multi-day work it compounds. The four-layer optimization stack (originally synthesized by `@osint-wiki/concepts/mcp-context-optimization.md` from the K34 source-pair) is Cemini's response.

### Layer 1 — Lazy-loading proxy (lazy-tool)

`@entities/tools/lazy-tool.md`. Replaces the full MCP tool catalog with 5 meta-tools. The LLM searches for tools on demand instead of carrying the catalog in every prompt.

- **Saves**: ~46% input tokens, ~32% per-turn latency (per source measurements; treat as upper bound)
- **Cost**: one local daemon, one extra layer of indirection
- **Break-even**: ~5 MCP servers
- **Cemini posture**: CONDITIONAL-GO — the harness's built-in `ToolSearch` deferred-tool surface covers built-in tools; lazy-tool extends the trick to MCP

### Layer 2 — Routing proxy (claude-code-router or cc-switch)

`@entities/tools/claude-code-router.md`. Local proxy that:
- Routes cheap requests to small/cheap models (Haiku for grep summaries)
- Routes complex requests to capable models (Opus for synthesis)
- Adds OpenRouter caching headers
- Provides failover

- **Saves**: variable; depends on the cost-class distribution of the workload
- **Cost**: one more local daemon, multi-provider auth complexity
- **Break-even**: requires multi-provider workflows (OpenRouter + Anthropic, or multi-API)
- **Cemini posture**: documented, not adopted — direct-Anthropic for billing simplicity

### Layer 3 — Three-cache discipline

`@concepts/three-cache-architecture.md`. Anthropic KV cache (5-min TTL), OpenRouter Response Cache (full-prompt key), OpenRouter Edge Cache (latency).

- **Saves**: cached input tokens at ~10% of normal rate
- **Cost**: discipline (static-at-start, volatile-at-end; pace turns to TTL)
- **Break-even**: every session
- **Cemini posture**: CORE — followed in every session

### Layer 4 — Context-budget audit + ToolSearch deferred tools

The harness's `ToolSearch` keeps tool definitions out of the prompt until the LLM needs them. Cemini also uses:
- `Read` with `offset` + `limit` for slices of large files
- `Grep` + `Glob` over full-file reads
- Subagent dispatch for codebase exploration > 3 queries deep
- `ttok` to preview-count any blob before pasting

- **Saves**: variable — directly proportional to discipline
- **Cost**: behavioral
- **Break-even**: every session
- **Cemini posture**: CORE — see `@concepts/context-engineering.md`

### How the layers compose

Without the stack:
- 150 MCP tools × ~300 tokens each = 45,000 tokens/turn overhead
- Prompt cache busted on every tool connect/disconnect
- OpenRouter charges full price on every turn (if routing)

With the stack:
- 5 meta-tools in system prompt (deterministic, cacheable)
- ~900 input tokens/turn vs ~1,700 (46% reduction per Layer 1)
- Cache hits at ~10% cost on repeated prompt prefixes (Layer 3)
- **80-95% per-session cost reduction** for long-running sessions (per source claim; treat as upper bound)

### What the layers don't do

- **Don't compress conversation history** — that's `@entities/tools/claude-mem.md`'s job (passive observation memory) and the harness's auto-summarization
- **Don't free you from `/goal` discipline** — the goal-condition still has to be tight; cache savings on a wandering session still bill more than a focused session
- **Don't replace context-engineering judgment** — see `@concepts/context-engineering.md` for the parent discipline

## Dead Ends

- **Adopting all four layers on a 1-MCP setup** — premature optimization; the layers add moving parts that aren't paying for themselves yet.
- **Using lazy-tool but ignoring the static-at-start rule** — Layer 1 stops MCP-catalog churn but a fresh timestamp in the system prompt still busts the KV cache.
- **Trusting the upstream "46%" / "80-95%" numbers blindly** — those are source-claimed maxima. Measure your own workload.
