---
title: "LLM Agents Can Easily Tamper With Their Own Traces (CCC K394)"
type: concept
tags: [concept, k394]
keywords: [2609.30266, k394]
related:
  - sources/arxiv-agent-trace-tampering-2609.30266.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-25_ccc-k390-k394-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-25
updated: 2026-09-25
---

## Relations

- `@sources/arxiv-agent-trace-tampering-2609.30266.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-25_ccc-k390-k394-sip-ready.md`

## Raw Concept

K394: Cybersec + ADOPT policy — arXiv 2609.30266.

## Narrative

**Cybersec-primary + ADOPT policy:** agent-writable traces break audit — require **external append-only / tamper-evident logging** (pairs K277/K239/K327 Logos transcript). **No PoCs / no tamper recipes.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.30266 locators." [Source: CCC K394 synthesis]
