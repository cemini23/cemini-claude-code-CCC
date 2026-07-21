---
title: Backbone-internal tool-output pruning (SWE-Pruner Pro pattern)
type: concept
tags: [concept, context-pruning, coding-agent, open-weight, k201]
keywords: [2607.18213, internal representations, length-aware embedding, keep-or-prune]
related:
  - sources/arxiv-swe-pruner-pro-internal-prune-2607.18213.md
  - concepts/tool-response-context-pruning-summarization.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/self-compacting-adaptive-context.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- `@sources/arxiv-swe-pruner-pro-internal-prune-2607.18213.md` — provenance
- `@concepts/tool-response-context-pruning-summarization.md` — K115 N/W policy peer
- `@concepts/mcp-context-optimization.md` — cost stack
- `@concepts/token-economics-and-prompt-caching.md` — tokens
- `@concepts/self-compacting-adaptive-context.md` — compaction peer

## Raw Concept

K201: the coder LLM's hidden states while reading tool output already encode line-level relevance. Read them out with a small head instead of a second classifier. Open-weight only; no LICENSE on public repo → **NO-GO** install.

## Narrative

### Steal

| Host | Action |
|------|--------|
| Open-weight local (Ollama / self-host) | **WATCH** when SPDX appears; pattern is strong |
| Claude Code / Cursor closed models | Keep **K115** N/W prune+summarize; cannot read internals |
| TipDrop / poker long tool dumps | Cap retained tool lines; prefer summarization over full `cat` dumps |

| Verdict | **ADOPT** "don't pay a second model to prune" principle; **NO-GO** swe-pruner-pro clone until SPDX |

## Snippets

> "Rather than building pruning around the agent, it suffices to read the signal the agent has already formed."
> — [Source: arxiv-2607.18213 Conclusion]
