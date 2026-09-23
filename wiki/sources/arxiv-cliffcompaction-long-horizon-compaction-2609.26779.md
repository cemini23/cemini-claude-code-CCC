---
title: "CliffCompaction: Cost-Efficient Compaction for Long-Horizon LLM Agents (CCC K383)"
type: source
tags: [source, arxiv, k383]
keywords: [2609.26779, k383]
related:
  - concepts/truncate-only-long-horizon-compaction.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@concepts/truncate-only-long-horizon-compaction.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CliffCompaction: Cost-Efficient Compaction for Long-Horizon LLM Agents |
| **arXiv** | 2609.26779 (2026-09) |
| **Retrieved** | 2026-09-23 |

## Narrative

**Verdict: ADOPT pattern.**

**Truncate-only long-horizon compaction** — evict context by **drop/truncate** only; **never rephrase** or LLM-summarize retained history into synthetic prose (pairs K265 blast-radius eviction / K124 compaction ≠ memory owner). `nguyenvuthientrang/cliffcompaction` **MIT** — REFERENCE note in narrative only; no clone required at Phase-0. Runtime **`wont_wire`**.

## Snippets

> "CliffCompaction: Cost-Efficient Compaction for Long-Horizon LLM Agents — CCC K383 synthesis." [Source: arXiv 2609.26779 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.26779-cliffcompaction-cost-efficient-compaction-for-lo.pdf` |
