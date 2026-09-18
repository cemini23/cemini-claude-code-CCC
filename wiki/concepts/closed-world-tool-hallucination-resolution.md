---
title: "Closed-World Resolution Against Tool Hallucination in LLM Agents (CCC K369)"
type: concept
tags: [concept, k369]
keywords: [2609.19425, k369]
related:
  - sources/arxiv-closed-world-resolution-tool-hallucination-2609.19425.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-18_ccc-k369-k372-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-18
updated: 2026-09-18
---

## Relations

- `@sources/arxiv-closed-world-resolution-tool-hallucination-2609.19425.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-18_ccc-k369-k372-sip-ready.md`

## Raw Concept

K369: ADOPT policy — arXiv 2609.19425.

## Narrative

Tool-selection and tool-gating presuppose the emitted call refers to a **real tool** — **hallucinated tools/arguments** bypass both (not a gate decision at all). Closed-world resolution validates calls against an explicit tool registry/schema before execution. Pairs K259 tool affordances / K368 implicit trust / K274 CDH. Runtime **`wont_wire`** — schema validation belongs in broker/harness.

## Snippets

> "See source page for arXiv 2609.19425 locators." [Source: CCC K369 synthesis]
