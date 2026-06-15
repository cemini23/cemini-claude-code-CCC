---
title: Tool-response context pruning and summarization — Less Context Better Agents
type: concept
tags: [concept, context-engineering, mcp, token-economics, k115]
keywords: [2606.10209, context-pruning, n5-w3, tool-call-pairs, context-rot]
related:
  - sources/arxiv-less-context-better-agents-2606.10209.md
  - concepts/context-engineering.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/subagent-orchestration.md
  - concepts/long-thread-context-decay.md
maturity: draft
created: 2026-06-15
updated: 2026-06-15
---

## Relations

- `@sources/arxiv-less-context-better-agents-2606.10209.md` — Microsoft D365 MCP study
- `@concepts/context-engineering.md` — parent discipline
- `@concepts/mcp-context-optimization.md` — four-layer MCP stack
- `@concepts/token-economics-and-prompt-caching.md` — linear cost in context length
- `@concepts/subagent-orchestration.md` — alternative: isolate verbose work in subagent
- `@concepts/long-thread-context-decay.md` — context rot before hard limit

## Raw Concept

When MCP/ERP tool responses bloat the window, should we keep full history or prune+summarize?

## Narrative

**Semantic context policy** [CONFIRMED on D365 hotel-expense MCP, 2606.10209]: retain last **N** whole tool call/response pairs; summarize evicted pairs into rolling summary window **W**. Inference-time only — no retraining.

| Parameter | Paper default | Effect |
|-----------|---------------|--------|
| N (recency pairs) | 5 | Drop older tool pairs entirely |
| W (summary window) | 3 | Compress evicted pairs into summary block |

**Results vs full history:** +20.6pp complete itemization (71→91.6%), −63% tokens, −60% wall time — **better accuracy and cheaper**.

**Steal-from for Cemini:**

1. Long conductor/MCP sessions: cap retained tool pairs; don't rely on compaction alone.
2. Pair with `@concepts/subagent-orchestration.md` when single-task tool volume exceeds N.
3. Document N/W in `/goal` envelopes for multi-step ERP-style workflows.

**Verdict:** **REFERENCE** — adopt policy in rules/briefs; no Microsoft code release.

## Snippets

> "Processing costs scale linearly with context length … context rot degrades effective recall before the hard limit."

> "Pruning last 5 pairs + summarization window 3: 91.6% vs 71.0% full context at 37% of tokens."
