---
title: "LifePlanner — geo-spatial + social MCP benchmark (CCC K316, OOD stub)"
type: source
tags: [source, arxiv, benchmark, geospatial, mcp, ood, k316]
keywords: [2608.25039, LifePlanner, geo-spatial planning, social media, MCP toolset, pass rate, trip planning]
related:
  - concepts/structured-state-semantic-actions.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/structured-state-semantic-actions.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LifePlanner: Evaluating LLM Agents for Geo-spatial Planning with Social Media Data |
| **arXiv** | 2608.25039 (2026-08-25) |
| **Authors** | Zhen Dong, Yuning Peng, Yutao Shi, Lei Zhong, Yongsen Mao, Yuan Liu, Haiping Wang (Wuhan University + HKUST) |
| **Code** | None (OOD — no clone) |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: OOD** — trip-planning benchmark, **short stub**. `wont_wire`. No clone.

Geo-spatial planning benchmark that enriches map data with large-scale local social media posts, exposed through an **MCP toolset** — four task categories, three difficulty levels. Frontier LLMs do well on simple retrieval but degrade sharply on complex planning: **Pass Rate drops to 40.2%**.

Failure analysis is the steal: failures stem from **incomplete evidence acquisition** from the large multimodal database, **imprecise tool use**, and **weak constraint integration** — not model size or reasoning length. Progress needs grounded planning, not scaling. Pairs K244/K246 (evidence acquisition + tool precision beats model size).

| Confidence | `[TENTATIVE]` — benchmark results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "Frontier LLMs perform well on simple retrieval but degrade sharply on complex planning, with the Pass Rate dropping to 40.2%." [Source: arXiv 2608.25039 abstract]

> "Failures mainly stem from incomplete evidence acquisition … imprecise tool use, and weak constraint integration rather than model size or reasoning length." [Source: arXiv 2608.25039 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.25039-lifeplanner-evaluating-llm-agents-for-geo-spatia.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
