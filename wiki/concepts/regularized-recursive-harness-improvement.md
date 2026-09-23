---
title: "RRSI: Regularized Recursive Self-Improvement of Agent Harnesses (CCC K378)"
type: concept
tags: [concept, k378]
keywords: [2609.24972, k378]
related:
  - sources/arxiv-rrsi-regularized-recursive-self-improvement-2609.24972.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@sources/arxiv-rrsi-regularized-recursive-self-improvement-2609.24972.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

K378: ADOPT pattern — arXiv 2609.24972.

## Narrative

**Regularized recursive harness improvement**: proposer operates under a **budget**; **critic** scores candidate harness edits; **pruner** drops regressions before commit — RSI on harness artifacts without unbounded self-rewrite of pass criteria (pairs K281 AutoDesign / K313 StarHarness stratification / K292 continual harness learning). `google-research/rrsi` **Apache-2.0** → optional **GO REFERENCE** at Phase-0, not required for policy wire. Trainer runtime **`wont_wire`**. **Never auto-evolve** `.cursor/skills`.

## Snippets

> "See source page for arXiv 2609.24972 locators." [Source: CCC K378 synthesis]
