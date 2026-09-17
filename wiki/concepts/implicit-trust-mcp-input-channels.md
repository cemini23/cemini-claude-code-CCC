---
title: "Measuring Implicit Trust in LLM Tool-Calling Pipelines (CCC K368)"
type: concept
tags: [concept, k368, cybersec, mcp, implicit-trust]
keywords: [2609.18217, implicit trust, mcp channels, k368]
related:
  - sources/arxiv-implicit-trust-mcp-tool-calling-2609.18217.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-17_ccc-k368-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-17
updated: 2026-09-17
---

## Relations

- `@sources/arxiv-implicit-trust-mcp-tool-calling-2609.18217.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-17_ccc-k368-sip-ready.md`

## Raw Concept

K368: MCP tool-calling **implicit trust** across undifferentiated input channels.

## Narrative

MCP tool interactions expose models to attacker-controlled text via **multiple input channels** (tool descriptions, tool results, sampling messages) in one **shared context window without privilege separation**. Framework measures per-model **trust profiles** across channel/payload framings; cross-channel fragmentation can reassemble harmful intent from benign-looking pieces. CCC steal: **channel-aware trust measurement** + external enforcement — not model self-arbitration (pairs K310 pre-auth intent / K326 recognition≠enforcement / K365 session privacy / K274 CDH). **No PoCs, no attack templates, no fragmentation recipes anywhere.** Runtime **`wont_wire`**.

## Snippets

> "Measure trust per channel; enforce externally — do not rely on model refusal alone." [Source: CCC K368 synthesis]
