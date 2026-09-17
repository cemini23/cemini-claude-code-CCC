---
title: "Ask the Tool, Don't Guess: Tool Calls Hold Their Progress (CCC K364)"
type: concept
tags: [concept, k364]
keywords: [2609.18849, k364]
related:
  - sources/arxiv-ask-the-tool-serving-progress-2609.18849.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-17_ccc-k363-k367-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-17
updated: 2026-09-17
---

## Relations

- `@sources/arxiv-ask-the-tool-serving-progress-2609.18849.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-17_ccc-k363-k367-sip-ready.md`

## Raw Concept

K364: ADOPT policy — synthesized from arXiv 2609.18849.

## Narrative

Agentic requests spend wall-clock time in tools while KV cache holds GPU memory. Serving systems evict/retain cache by **pre-call duration guesses** (name, history, declared duration) — but no pre-call estimate can know true tool duration or rank tools reliably. **Serving should read progress from the tool call itself**, not guess. Pairs K320 usage vs context / token economics / K327 resume boundaries. Awareness only; runtime **`wont_wire`**.

## Snippets

> "See source page for arXiv 2609.18849 locators." [Source: CCC K364 synthesis]
