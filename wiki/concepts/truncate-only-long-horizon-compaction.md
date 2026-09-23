---
title: "CliffCompaction: Cost-Efficient Compaction for Long-Horizon LLM Agents (CCC K383)"
type: concept
tags: [concept, k383]
keywords: [2609.26779, k383]
related:
  - sources/arxiv-cliffcompaction-long-horizon-compaction-2609.26779.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@sources/arxiv-cliffcompaction-long-horizon-compaction-2609.26779.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

K383: ADOPT pattern — arXiv 2609.26779.

## Narrative

**Truncate-only long-horizon compaction** — evict context by **drop/truncate** only; **never rephrase** or LLM-summarize retained history into synthetic prose (pairs K265 blast-radius eviction / K124 compaction ≠ memory owner). `nguyenvuthientrang/cliffcompaction` **MIT** — REFERENCE note in narrative only; no clone required at Phase-0. Runtime **`wont_wire`**.

## Snippets

> "See source page for arXiv 2609.26779 locators." [Source: CCC K383 synthesis]
