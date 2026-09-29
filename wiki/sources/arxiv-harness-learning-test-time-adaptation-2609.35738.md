---
title: "Harness Learning Enables Generalizable Test-Time Adaptation (CCC K404)"
type: source
tags: [source, arxiv, k404]
keywords: [2609.35738, k404]
related:
  - concepts/harness-learning-test-time-adaptation.md
  - briefs/2026-09-29_ccc-k401-k405-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-29
updated: 2026-09-29
---

## Relations

- `@concepts/harness-learning-test-time-adaptation.md`
- `@briefs/2026-09-29_ccc-k401-k405-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Harness Learning Enables Generalizable Test-Time Adaptation |
| **arXiv** | 2609.35738 (2026-09) |
| **Retrieved** | 2026-09-29 |

## Narrative

**Verdict: ADOPT eval-first.**

**Harness learning** — proposer revises solver **executable harness** from execution feedback; meta-learning over programs with harness edits as weight updates (pairs K292 harness CL / K281 meta-harness / K162 external eval — **never rewrite pass criteria**). Trainer runtime **`wont_wire`**. Concept **`policy_wired`** eval-first.

## Snippets

> "A language-model agent is jointly defined by its model and its harness, the executable program that organizes model calls, tool use, and information flow." [Source: arXiv 2609.35738 abstract (retrieved 2026-09-29)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.35738-harness-learning-enables-generalizable-test-time.pdf` |
