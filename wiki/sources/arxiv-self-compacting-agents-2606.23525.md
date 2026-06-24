---
title: Self-Compacting Language Model Agents (arXiv 2606.23525)
type: source
tags: [source, arxiv, context-compaction, selfcompact, k124]
keywords: [2606.23525, context-rot, rubric-gated-compaction]
related:
  - concepts/self-compacting-adaptive-context.md
  - entities/patterns/cpr-context-compression.md
  - concepts/long-thread-context-decay.md
  - concepts/tool-response-context-pruning-summarization.md
  - entities/tools/claude-code.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@concepts/self-compacting-adaptive-context.md` — SELFCOMPACT scaffold synthesis
- `@entities/patterns/cpr-context-compression.md` — CCC compress leg analogue

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Self-Compacting Language Model Agents |
| **Authors** | Li et al. (JHU, Apple) |
| **arXiv** | 2606.23525v1 [cs.CL] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.23525-2606-23525v1-self-compacting-language-model-agen.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (SELFCOMPACT design + benchmark gains) |

## Narrative

**SELFCOMPACT** — model-invoked compaction tool + **lightweight rubric** specifying when to compress (sub-task resolved, trajectory converging) vs suppress (mid-derivation, stuck loops). Contrasts with fixed token-threshold compaction (Cursor) and user-triggered `/compact` (Anthropic).

**Results [TENTATIVE]:** matches/exceeds fixed-interval summarization at 30–70% lower token cost; up to +18.1 math / +5–9 agentic search vs no-summarization baseline.

**CCC relevance:** informs when to rewrite `hot.md`, when to spawn fresh Task subagent vs compact parent thread. **REFERENCE** — Claude Code `/compact` and native compaction are fixed-interval-ish; rubric-gated pattern is steal-from for custom Stop/UserPromptSubmit hooks.

## Snippets

> "We propose SELFCOMPACT, a scaffold that allows the model itself to decide when and how to compact."
> — [Source: arxiv-2606.23525-2606-23525v1-self-compacting-language-model-agen.pdf abstract, retrieved 2026-06-24]

> "Existing systems try to manage it with rigid rules: compacting the trajectory when a token threshold is met, or delegating the burden of identifying context rot to the user via /compact."
> — [Source: arxiv-2606.23525-2606-23525v1-self-compacting-language-model-agen.pdf, retrieved 2026-06-24]
