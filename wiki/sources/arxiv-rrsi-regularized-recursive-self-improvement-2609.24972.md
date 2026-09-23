---
title: "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses (CCC K378)"
type: source
tags: [source, arxiv, k378]
keywords: [2609.24972, k378]
related:
  - concepts/regularized-recursive-harness-improvement.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@concepts/regularized-recursive-harness-improvement.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | RRSI: Regularized Recursive Self-Improvement of Agent Harnesses |
| **arXiv** | 2609.24972 (2026-09) |
| **Retrieved** | 2026-09-23 |

## Narrative

**Verdict: ADOPT pattern.**

**Regularized recursive harness improvement**: proposer operates under a **budget**; **critic** scores candidate harness edits; **pruner** drops regressions before commit — RSI on harness artifacts without unbounded self-rewrite of pass criteria (pairs K281 AutoDesign / K313 StarHarness stratification / K292 continual harness learning). `google-research/rrsi` **Apache-2.0** → optional **GO REFERENCE** at Phase-0, not required for policy wire. Trainer runtime **`wont_wire`**. **Never auto-evolve** `.cursor/skills`.

## Snippets

> "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses — CCC K378 synthesis." [Source: arXiv 2609.24972 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.24972-rrsi-regularized-recursive-self-improvement-of-a.pdf` |
