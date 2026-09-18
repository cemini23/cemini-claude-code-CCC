---
title: "An Empirical Study of Harness Design for Coding Agents (CCC K370)"
type: source
tags: [source, arxiv, k370]
keywords: [2609.20804, k370]
related:
  - concepts/coding-agent-harness-component-design.md
  - briefs/2026-09-18_ccc-k369-k372-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-18
updated: 2026-09-18
---

## Relations

- `@concepts/coding-agent-harness-component-design.md`
- `@briefs/2026-09-18_ccc-k369-k372-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | An Empirical Study of Harness Design for Coding Agents |
| **arXiv** | 2609.20804 (2026-09) |
| **Retrieved** | 2026-09-18 |

## Narrative

**Verdict: ADOPT eval-first.**

Coding harnesses are usually evaluated **monolithically** — component contributions unclear. Lightweight fixed execution loop with **three varied components**: planning, action space, context management. Four models × component ablations → component-level harness design evidence. CCC steal: decompose harness eval (pairs K334 harness-as-eval-artifact / K281 five-component audit / K350 supply-chain). No public SPDX at Phase-0 → no clone. Runtime **`wont_wire`**.

## Snippets

> "An Empirical Study of Harness Design for Coding Agents — CCC K370 synthesis." [Source: arXiv 2609.20804 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.20804-an-empirical-study-of-harness-design-for-coding.pdf` |
