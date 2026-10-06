---
title: "Understanding the Hierarchical Structure and Functional Landscape of the Model Context Protocol Ecosystem (CCC K426)"
type: source
tags: [source, arxiv, k426]
keywords: [2610.05319, k426]
related:
  - concepts/mcp-tool-taxonomy-navigation.md
  - briefs/2026-10-06_ccc-k426-k430-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@concepts/mcp-tool-taxonomy-navigation.md`
- `@briefs/2026-10-06_ccc-k426-k430-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Understanding the Hierarchical Structure and Functional Landscape of the Model Context Protocol Ecosystem |
| **arXiv** | 2610.05319 (2026-10) |
| **Retrieved** | 2026-10-06 |

## Narrative

**Verdict: ADOPT pattern (no repo).**

**MCPacific — the MCP ecosystem mapped by capability, not by marketplace.** The largest tool-level study of MCP: **368,754 listings from 17 marketplaces**, resolved to **124,267 unique servers**, from which **1,328,233 tool specifications** are statically extracted in seven languages and organised into a **hierarchical functional taxonomy of 58,915 capabilities** — 7.5× more tools than the largest prior collection. The gap it fills: marketplaces organise by coarse vendor categories (Communication, Productivity), never by **what a tool actually does**, so neither agents nor users can answer *which capabilities exist* or *what can substitute for what*. The taxonomy is built by an iterative LLM **design → test → refine** loop and mapped with calibrated embedding routing; evaluation: 90.19% of tools reach a leaf, 87.00% land correctly, 85.00% of same-leaf pairs are functionally comparable. **Four findings matter to CCC.** (1) **85% of tools serve domains beyond software development** — the ecosystem is not a dev-tooling backwater. (2) **Alternatives are widespread but uneven:** 98.5% of tools have ≥1 alternative and 74.1% have ≥20, yet **nearly a quarter of capabilities have exactly one tool** — the single points of failure. (3) **Comparable tools are not interchangeable:** security alerts concentrate in a subset of alternatives, cyclomatic complexity differs **>2.5× in 41% of pairs**, and in 60% of capabilities some alternatives are maintained while others are not. (4) **Presentation changes outcomes** — exposing candidates through the taxonomy rather than a flat list improves task completion on all four models tested, **up to +12 points Pass@0.75 as the candidate set crowds**. That last one is the CCC lesson: at scale, *how tools are organised in the context* is a capability lever, not a UI nicety. Pairs K311 lazy MCP catalog / `@concepts/mcp-tool-interface-granularity-eval.md` / K402 error surfaces / `@concepts/mcp-server-catalog-curation.md` / K427 privacy audit. **No repo surfaced.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "presenting candidate tools through the taxonomy rather than a flat list improves task completion rate across all four evaluated models, with gains of up to 12 percentage points in Pass@0.75 for crowded candidate sets." [Source: arXiv 2610.05319 (retrieved 2026-10-06)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.05319-understanding-the-hierarchical-structure-and-fun.pdf` |
