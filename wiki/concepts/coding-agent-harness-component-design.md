---
title: "An Empirical Study of Harness Design for Coding Agents (CCC K370)"
type: concept
tags: [concept, k370]
keywords: [2609.20804, k370]
related:
  - sources/arxiv-harness-design-coding-agents-empirical-2609.20804.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-18_ccc-k369-k372-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-18
updated: 2026-09-18
---

## Relations

- `@sources/arxiv-harness-design-coding-agents-empirical-2609.20804.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-18_ccc-k369-k372-sip-ready.md`

## Raw Concept

K370: ADOPT eval-first — arXiv 2609.20804.

## Narrative

Coding harnesses are usually evaluated **monolithically** — component contributions unclear. Lightweight fixed execution loop with **three varied components**: planning, action space, context management. Four models × component ablations → component-level harness design evidence. CCC steal: decompose harness eval (pairs K334 harness-as-eval-artifact / K281 five-component audit / K350 supply-chain). No public SPDX at Phase-0 → no clone. Runtime **`wont_wire`**.

## Snippets

> "See source page for arXiv 2609.20804 locators." [Source: CCC K370 synthesis]
