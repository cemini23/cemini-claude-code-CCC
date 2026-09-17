---
title: "Measuring Implicit Trust in LLM Tool-Calling Pipelines (CCC K368)"
type: source
tags: [source, arxiv, k368, cybersec, mcp]
keywords: [2609.18217, implicit trust, mcp, tool-calling, k368]
related:
  - concepts/implicit-trust-mcp-input-channels.md
  - briefs/2026-09-17_ccc-k368-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-17
updated: 2026-09-17
---

## Relations

- `@concepts/implicit-trust-mcp-input-channels.md`
- `@briefs/2026-09-17_ccc-k368-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Measuring Implicit Trust in LLM Tool-Calling Pipelines |
| **arXiv** | 2609.18217 (2026-09) |
| **Retrieved** | 2026-09-17 |

## Narrative

**Verdict: Cybersec-primary + ADOPT policy.**

MCP tool interactions expose models to attacker-controlled text via **multiple input channels** (tool descriptions, tool results, sampling messages) in one **shared context window without privilege separation**. Framework measures per-model **trust profiles** across channel/payload framings; cross-channel fragmentation can reassemble harmful intent from benign-looking pieces. CCC steal: **channel-aware trust measurement** + external enforcement — not model self-arbitration (pairs K310 pre-auth intent / K326 recognition≠enforcement / K365 session privacy / K274 CDH). **No PoCs, no attack templates, no fragmentation recipes anywhere.** Runtime **`wont_wire`**.

## Snippets

> "Shared MCP context lacks privilege separation across tool description, result, and sampling channels." [Source: arXiv 2609.18217 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.18217-measuring-exploiting-implicit-trust-tool-calling.pdf` |
