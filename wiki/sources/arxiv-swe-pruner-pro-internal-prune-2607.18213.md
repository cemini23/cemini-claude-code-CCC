---
title: "SWE-Pruner Pro — prune tool outputs from the coder LLM's own reps"
type: source
tags: [source, arxiv, context-pruning, coding-agent, open-weight, k201]
keywords: [2607.18213, SWE-Pruner Pro, length-aware embedding, SJTU, Douyin]
related:
  - concepts/backbone-internal-tool-output-pruning.md
  - concepts/tool-response-context-pruning-summarization.md
  - concepts/mcp-context-optimization.md
  - concepts/token-economics-and-prompt-caching.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- `@concepts/backbone-internal-tool-output-pruning.md` — synthesized steal
- `@concepts/tool-response-context-pruning-summarization.md` — prior prune policy peer (K115)
- `@concepts/mcp-context-optimization.md` — MCP cost stack
- `@concepts/token-economics-and-prompt-caching.md` — token cost

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SWE-Pruner Pro: The Coder LLM Already Knows What to Prune |
| **Author** | Yuhang Wang, Yuling Shi, et al. (SJTU / Douyin) |
| **arXiv** | 2607.18213 |
| **Pages** | 28 |
| **Retrieved** | 2026-07-21 |
| **Code** | `github.com/Ayanami1314/swe-pruner-pro` — **no SPDX / no LICENSE file** → **NO-GO** install |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.18213-swe-pruner-pro-the-coder-llm-already-knows-what.pdf` |

## Narrative

Separate classifier (SWE-Pruner) unnecessary: agent hidden states while reading tool output already encode line-level keep/prune. Small head + length-aware embedding; shares backbone prefill. Up to **39%** prompt+completion token savings; MiMo-V2-Flash: **+3.8%** SWE-Bench Verified, **+2.2** Oolong [TENTATIVE]. Open-weight only (needs hidden states).

### CCC steal

Prefer pruning that reuses the agent's own pass over an extra model call. For Claude/Cursor closed models: keep K115 N/W policy; watch for vendor-exposed internal scores. No install without SPDX.

## Snippets

> "the agent itself encodes internal representations indicating the relevance of code context when reading tool output"
> — Abstract
