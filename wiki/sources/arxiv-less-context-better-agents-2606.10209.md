---
title: Less Context, Better Agents — MCP tool-response context engineering (arXiv 2606.10209)
type: source
tags: [source, arxiv, context-engineering, mcp, enterprise, k115]
keywords: [2606.10209, context-pruning, summarization, d365, tool-responses]
related:
  - concepts/tool-response-context-pruning-summarization.md
  - concepts/context-engineering.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/subagent-orchestration.md
maturity: draft
read_status: read
created: 2026-06-15
updated: 2026-06-15
---

## Relations

- `@concepts/tool-response-context-pruning-summarization.md` — CCC synthesis
- `@concepts/context-engineering.md` — parent context discipline
- `@concepts/mcp-context-optimization.md` — MCP verbose-response stack
- `@concepts/token-economics-and-prompt-caching.md` — token cost scaling

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Less Context, Better Agents: Efficient Context Engineering for Long-Horizon Tool-Using LLM Agents |
| **Authors** | Lodha et al. (Microsoft) |
| **arXiv** | 2606.10209v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.10209-less-context-better-agents-efficient-context-eng.pdf` |
| **Retrieved** | 2026-06-15 |
| **Read status** | read (configs C1–C4, D365 F&O MCP benchmark) |

## Narrative

Microsoft study on **GPT-5** agents itemizing hotel expenses in **Dynamics 365 F&O via MCP**. Verbose ERP tool responses cause context overflow and cost; paper formalizes **semantic-level** context policy: prune whole tool call/response pairs by recency + summarize evicted pairs (Algorithm 1) — distinct from token-level compression and external memory stores.

50-task benchmark, 5 runs, user model held constant across C2–C4:

| Config | Complete itemization | Tokens | Runtime |
|--------|---------------------|--------|---------|
| C1 no user model | 8.0% | — | — |
| C2 full context | 71.0% | 1,480,996 | 14.56 h |
| C3 prune last **N=5** pairs | 79.0% | 535,274 (−63.9%) | 5.39 h |
| C4 prune + summarize **W=3** | **91.6%** | 553,374 | 5.79 h |

Also: 95% CIs, sensitivity over N/W, failure taxonomy, five expense types, **Claude Sonnet 4.5** generalization.

**CCC relevance:** steal **N=5 / W=3** recency+summary defaults for long MCP-heavy Claude Code sessions; positions against "keep full history" default. No public code repo — inference-time policy only.

## Snippets

> "Context engineering with summarization achieves the best balance of performance and efficiency … selective retention of recent tool interactions is more decision-relevant than full history."

> "C4 pruning+summarization: 91.6% complete itemization with 553,374 tokens versus 71.0% at 1,480,996 tokens for full context."
