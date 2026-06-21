---
title: lazy-tool — MCP discovery proxy for prompt-cache friendliness
type: entity
tags: [tool, mcp, proxy, lazy-loading, token-optimization, prompt-cache, claude-code]
keywords: [lazy-tool, MCP proxy, lazy tool discovery, token reduction, prompt cache, sqlite tool index, search_tools, invoke_proxy_tool, rpgeeganage]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/exa.md
  - concepts/three-cache-architecture.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/context-engineering.md
  - entities/tools/claude-code-router.md
  - concepts/code-as-agent-harness.md
  - concepts/cursor-ide-workspace.md
  - concepts/deep-research-evaluation-prompt.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - entities/tools/ai-engineering-roadmap.md
  - concepts/claude-code-large-codebase-workflow.md
  - concepts/codex-side-fork-workflow.md
  - entities/tools/skillnet.md
  - concepts/slm-agent-orchestration-gateway.md
  - sources/arxiv-slm-orchestration-gateway-2606.03557.md
  - concepts/harness-layer-competition-cursor-claude-perplexity.md
  - concepts/maven-agentic-tool-calling-generalization.md
  - sources/arxiv-maven-agentic-tool-calling-2605.30738.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - sources/arxiv-failed-trajectory-harness-repair-2606.06324-2026-06-05.md
  - entities/tools/tool-forge.md
  - concepts/runtime-context-mcp-file-refs.md
  - concepts/mcp-server-catalog-curation.md
  - concepts/seclaw-agent-security-evaluation.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
  - concepts/cross-wiki-tool-adoption-routing.md
  - entities/tools/omnifs.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - concepts/prompt-cache-aligned-context-management.md
maturity: validated
created: 2026-05-13
updated: 2026-06-21
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/mcp-servers/exa.md` — typical "real" MCP server that hides behind the proxy
- `@concepts/three-cache-architecture.md` — lazy-tool is what makes Anthropic KV-cache hits actually happen
- `@concepts/mcp-context-optimization.md` — Layer 1 of the four-layer optimization stack
- `@concepts/token-economics-and-prompt-caching.md` — the cost model lazy-tool moves
- `@concepts/context-engineering.md` — same trick as the harness's built-in `ToolSearch` deferred-tool surface
- `@concepts/code-as-agent-harness.md` — deferred MCP tool surface in harness mechanisms layer
- `@concepts/skillrae-retrieval-augmented-execution.md` — compiles skill context after tool/skill selection (complementary layer)
- `@concepts/codex-side-fork-workflow.md` — Codex as parallel OpenAI harness in same federation
- `@entities/tools/omnifs.md` — path-namespace API projection; partial overlap on fetch ergonomics (K108)

Cross-wiki: `@osint-wiki/concepts/mcp-context-optimization.md` carries the K34 4-layer methodology source. `@seo-wiki/entities/tools/claude-code-tool-stack.md` is the SEO-side adoption brief.

## Raw Concept

`github.com/rpgeeganage/lazy-tool` — MIT. The single highest-ROI tool for any Claude Code user with ≥3 MCP servers wired up. Distilled across multiple sibling-wiki ingests (OSINT K34 mcp-context-optimization, SEO claude-code-tool-stack 2026-05-10) — same numbers reported across both: **46% input-token reduction, 32% per-turn latency reduction.**

## Narrative

Every MCP server connected to Claude Code injects its full tool catalog into every turn — `name + description + JSON schema` for every tool. With 5-10 servers (Exa, Brave, Playwright, claude-mem, stash, finance-*, conductor, …), that's 30,000-75,000 tokens burned **before the user types a single character**. At Anthropic input pricing this adds up; worse, every tool connect/disconnect busts the prompt cache so subsequent turns re-pay full price too.

**lazy-tool** sits in between the harness and the real MCP servers. It reads `claude_desktop_config.json` (or `.mcp.json`), builds a local SQLite index of every tool, and exposes only **5 meta-tools** to the LLM:

1. `search_tools` — natural-language search across the catalog
2. `inspect_capability` — fetch a single tool's full schema on demand
3. `invoke_proxy_tool` — execute a discovered tool with given args
4. `get_proxy_prompt` — fetch a server-provided prompt template
5. `read_proxy_resource` — fetch a server-provided resource

The LLM searches for tools when it needs them instead of carrying the full catalog in every prompt envelope. Same outcome as Claude Code's built-in `ToolSearch` deferred-tool pattern, but applied to the entire MCP surface.

### Setup

```bash
curl -sSfL https://raw.githubusercontent.com/rpgeeganage/lazy-tool/main/install.sh | sh
lazy-tool reindex
lazy-tool serve --transport http --addr :8080
# point Claude Code's .mcp.json at http://localhost:8080/mcp
```

### Why the cache cooperates

Static, deterministic system prompt = cache-friendly prompt prefix. With every MCP server connected directly, the prefix changes whenever a server reconnects, a tool gets added, or a description gets edited — every drift busts the Anthropic KV cache. With lazy-tool, the system-prompt portion is a fixed 5-tool block; the cache stays warm across turns and across long sessions.

This is the load-bearing reason CCC's `@concepts/token-economics-and-prompt-caching.md` recommends lazy-tool as the first install for any Cemini-style multi-MCP setup.

### Cemini's adoption posture (2026-05-13)

CONDITIONAL-GO: Cemini already runs the harness's `ToolSearch` deferred-tool pattern, which solves the same problem at the harness level for built-in tools. lazy-tool extends the trick to MCP. Worth running when MCP-server count exceeds 5; not worth the added moving part for fewer.

## Snippets

> "Without it, every tool connect/disconnect busts the cache and you pay full price on every turn."
> [Source: @seo-wiki claude-code-tool-stack.md, 2026-05-10]

## Dead Ends

- **Running lazy-tool with 1-2 MCP servers** — not worth the added local daemon. The break-even is ~5 MCP servers.
- **Trusting the 46% / 32% numbers blindly** — those are the rpgeeganage README claims, not Cemini-measured. Treat as upper bound; measure your own workload.
