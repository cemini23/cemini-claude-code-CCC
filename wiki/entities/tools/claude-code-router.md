---
title: claude-code-router — local LLM proxy for routing + caching
type: entity
tags: [tool, proxy, routing, caching, openrouter, claude-code, model-switching]
keywords: [claude-code-router, musistudio, openrouter, model routing, caching headers, X-OpenRouter-Cache, failover, cc-switch]
related:
  - entities/tools/claude-code.md
  - entities/tools/lazy-tool.md
  - concepts/three-cache-architecture.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/local-llm-mechanics-primer.md
  - concepts/deepseek-coding-cost-routing.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
maturity: draft
created: 2026-05-13
updated: 2026-06-05
---

## Relations

- `@entities/tools/claude-code.md` — host harness
- `@entities/tools/lazy-tool.md` — MCP-level cousin (lazy-tool reduces tool catalog; claude-code-router routes the traffic)
- `@concepts/three-cache-architecture.md` — Layer 2 of the optimization stack (OpenRouter Response Cache + Edge Cache)
- `@concepts/mcp-context-optimization.md` — Layer 2 of the four-layer optimization stack
- `@concepts/token-economics-and-prompt-caching.md` — sibling cost-discipline page

Cross-wiki: `@seo-wiki/entities/tools/claude-code-tool-stack.md` (Tool 2 of the SEO-side stack reference).

## Raw Concept

`github.com/musistudio/claude-code-router` — MIT, Node.js. A local proxy daemon that sits between Claude Code and the LLM provider. Three jobs:

1. **Model routing** — direct cheap requests (file reads, grep summaries) to small/cheap models, complex requests (code generation, architecture) to capable models.
2. **Failover** — if a provider rate-limits, route to a backup.
3. **Cache header injection** — adds `X-OpenRouter-Cache: true` for OpenRouter-side response caching.

Cemini has not adopted claude-code-router operationally yet — Cemini runs Claude Code directly against Anthropic's API, not through OpenRouter. The page is documented because it's the canonical example of the **proxy-as-cost-control** pattern and because it pairs with `@entities/tools/lazy-tool.md` in the SEO-wiki canonical tool stack.

## Narrative

Claude Code talks to one LLM endpoint. Per-session that's fine; for sustained multi-day work the lack of routing has two costs:

- **All-traffic-to-frontier** — using Opus 4.7 for tasks Sonnet 4.6 (or Haiku 4.5) would have nailed cheaper.
- **No failover** — when Anthropic returns 529 (overloaded), the session has no fallback path.

claude-code-router solves both by being an HTTP/JSON proxy with rules that map request shape → upstream provider. Rules are written in JSON and live in `~/.config/claude-code-router/config.json`.

### Install

```bash
npm install -g @musistudio/claude-code-router
claude-code-router --port 3456 &
# point Claude Code's settings at the proxy
```

### What's in scope for adoption

- **Multi-provider workflows** — if Cemini ever runs Claude Code through OpenRouter (instead of native Anthropic), the router's caching headers cut cost.
- **Failover** — when sessions matter (e.g., live presentation, demo recording) and a single provider's reliability matters less than uptime.
- **Cost-class routing** — when a session is doing both heavy reads (cheap) and creative synthesis (expensive), routing via shape saves money.

### Cemini-specific notes

Cemini's current posture (2026-05-13) is direct-Anthropic: no proxy. The reasons:
- One vendor for billing simplicity.
- Anthropic's prompt-cache discipline (5-min TTL) is well-understood; introducing OpenRouter's separate caching adds a layer to reason about.
- Failover is not a load-bearing requirement for solo-dev cadence.

If those constraints change (team adoption, demo-stability requirements, OpenRouter cost advantage on a model class), revisit. The page exists so the option is documented.

### Companion: cc-switch

`github.com/synthesia-ai/cc-switch` (Rust binary, no deps) covers a narrower subset — SSE streaming repair through OpenRouter — when the full router is overkill. Mentioned for completeness; same Cemini posture (not adopted).

## Dead Ends

- **Routing through claude-code-router when running native Anthropic** — adds latency for no gain. The router earns its slot when ≥2 providers are in play.
- **Treating OpenRouter caching as a substitute for Anthropic prompt caching** — they're orthogonal layers (see `@concepts/three-cache-architecture.md`).
