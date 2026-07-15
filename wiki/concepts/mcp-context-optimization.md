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
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
  - concepts/time-series-native-agent-harness.md
  - sources/arxiv-timeclaw-contextualized-time-series-2606.05404.md
  - entities/tools/omnifs.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/mcp-adaptive-systems-context-survey.md
  - sources/arxiv-mcp-externalizing-context-survey-2508.19239.md
  - concepts/openagenet-trusted-agent-discovery.md
  - concepts/queen-bee-beespec-enterprise-orchestration.md
  - concepts/enterprise-mcp-adoption-practice.md
  - sources/arxiv-enterprise-mcp-adoption-2606.09182.md
  - concepts/tool-response-context-pruning-summarization.md
  - sources/arxiv-less-context-better-agents-2606.10209.md
  - concepts/specification-driven-scientific-workflow-management.md
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
  - concepts/agent-first-web-framework.md
  - sources/arxiv-agent-first-web-redesign-2606.19116.md
  - concepts/prompt-cache-aligned-context-management.md
  - sources/arxiv-tokenpilot-cache-efficient-context-2606.17016.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - sources/arxiv-shopx-intent-to-item-fulfillment-2606.31693.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - sources/arxiv-hierarchical-skill-stack-lazy-orchestration-2607.11138.md
  - concepts/failure-mode-harness-adaptation-mapping.md
maturity: validated
created: 2026-05-13
updated: 2026-07-14
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
- `@entities/tools/omnifs.md` — projected filesystem for APIs; shell `cat`/`grep` ergonomics vs MCP catalog (K108)

Cross-wiki: `@osint-wiki/concepts/mcp-context-optimization.md` is the original 4-layer methodology source (K34 ingest, OSINT side).
- `@concepts/failure-mode-harness-adaptation-mapping.md` — K168 tool-filter / progressive-reveal adaptations

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

### Reliability complement (2606.05339)

Cost optimization does not prevent **runtime coordination faults**. `@concepts/mcp-server-runtime-fault-taxonomy.md` (837 GitHub threads, 11 categories) is the reliability layer beneath this page — e.g. Tool Result propagation faults look like "MCP worked" while burning tokens on retry loops. Phase-0 MCP GO should pass taxonomy checks before counting servers toward the lazy-tool break-even threshold.

### What the layers don't do

- **Don't compress conversation history** — that's `@entities/tools/claude-mem.md`'s job (passive observation memory) and the harness's auto-summarization
- **Don't free you from `/goal` discipline** — the goal-condition still has to be tight; cache savings on a wandering session still bill more than a focused session
- **Don't replace context-engineering judgment** — see `@concepts/context-engineering.md` for the parent discipline

### K138 — local code review vs MCP dumps [REFERENCE]

arXiv **2607.02389** argues MCP-mediated retrieval can **saturate reviewer context** with raw payloads when auditing **developer-owned local repos**. Complement lazy-tool cost discipline with **projection CLI** (`docs module` / `docs symbol`) for review subagents — see `@concepts/substrate-constraints-coding-agent-oversight.md`. Lazy-tool remains correct for **untrusted remote MCP** discovery; projection CLI is for **in-repo** audit bundles.

## Dead Ends

- **Adopting all four layers on a 1-MCP setup** — premature optimization; the layers add moving parts that aren't paying for themselves yet.
- **Using lazy-tool but ignoring the static-at-start rule** — Layer 1 stops MCP-catalog churn but a fresh timestamp in the system prompt still busts the KV cache.
- **Trusting the upstream "46%" / "80-95%" numbers blindly** — those are source-claimed maxima. Measure your own workload.
