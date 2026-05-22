---
title: Local LLM mechanics primer — token loop, KV cache, prefill/decode
type: concept
tags: [concept, local-llm, inference, kv-cache, cross-wiki-route]
keywords: [local-llm, kv-cache, prefill, decode, quantization, chat-templates, rag, inference-engines, token-loop]
related:
  - concepts/token-economics-and-prompt-caching.md
  - concepts/three-cache-architecture.md
  - concepts/context-engineering.md
  - entities/tools/claude-code-router.md
  - entities/tools/thuki.md
  - entities/mcp-servers/stash.md
  - entities/tools/anything-llm.md
  - entities/tools/claude-code.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
cross-wiki-source: "@osint-wiki/sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md"
---

## Relations

- `@concepts/token-economics-and-prompt-caching.md` — API-side cache economics; this page is the local-inference analogue
- `@concepts/three-cache-architecture.md` — Anthropic KV cache vs on-device KV cache (different layers, same vocabulary)
- `@concepts/context-engineering.md` — window budgeting applies equally to local and API models
- `@entities/tools/claude-code-router.md` — optional local-model routing via OpenRouter/LiteLLM paths
- `@entities/tools/thuki.md` — macOS Ollama overlay example (not Claude Code integration)
- `@entities/mcp-servers/stash.md` — supports OpenRouter/Ollama backends per entity page

Cross-wiki: Post 1 of `@osint-wiki/sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md` (@TheAhmadOsman, May 2026).

## Raw Concept

Routed from `briefs/2026-05-22_k57-local-llm-and-agent-infra-from-osint.md`. Question: **what should a Claude Code operator understand about local inference mechanics when evaluating Ollama/BYOK tools — without duplicating a full hardware course?**

## Narrative

Cemini's daily driver remains **Anthropic API + Claude Code**; local inference is secondary (Ollama appears in stash/lazy-tool/thuki references, not as the primary coding model). This stub captures the primer topics from the Ahmad Osman "LLMs 101 (2026 Edition)" post so CCC sessions can reason about token math when a tool claims "60–90% savings" or "runs locally."

### Core mechanics (expand on deep-read)

| Topic | One-line CCC relevance |
|-------|------------------------|
| Token loop / Transformer attention | Explains why repo-packing (`@entities/tools/repomix.md`) and MCP catalog overhead hurt equally on local models |
| KV-cache memory | Same "reuse prefix" intuition as Anthropic prompt caching — different implementation |
| Prefill vs decode | Prefill is parallel (batch-friendly); decode is serial — latency-sensitive agent turns are decode-heavy |
| Quantization | VRAM tradeoff; matters for on-prem fine-tuning candidates (e.g. unsloth in K55-2 list) |
| Chat templates | Model-specific formatting — skill/prompt portability breaks if templates mismatch |
| RAG | Tutorial steal-from: `@pguso/rag-from-scratch` (MIT) — patterns for kb-server docs, not a deploy |
| Serving engines | Hardware trilogy (VRAM, bandwidth, engines) linked from source post — defer to deep-read |

### Explicit non-actions

- No switch to local-first Claude Code workflow from this post alone.
- Do not treat creator "save thousands" lists (`@concepts/tools-we-dont-use.md`) as vetted local-inference advice.

## Snippets

> Long-form local-LLM primer: token loop, Transformer/attention, KV-cache memory math, prefill vs decode, quantization, chat templates, RAG, serving engines.
> — [Source: @osint-wiki/sources/trading-posts-llm-gustafsson-retail-weather-copy-2026-05-22.md Post 1]
