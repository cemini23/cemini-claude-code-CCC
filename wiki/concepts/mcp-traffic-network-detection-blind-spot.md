---
title: "When Agents Look Like Beacons: NIDS Evasion by MCP Traffic (CCC K366)"
type: concept
tags: [concept, k366]
keywords: [2609.19091, k366]
related:
  - sources/arxiv-mcp-traffic-nids-beacon-evasion-2609.19091.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-17_ccc-k363-k367-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-17
updated: 2026-09-17
---

## Relations

- `@sources/arxiv-mcp-traffic-nids-beacon-evasion-2609.19091.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-17_ccc-k363-k367-sip-ready.md`

## Raw Concept

K366: Cybersec-primary + ADOPT policy — synthesized from arXiv 2609.19091.

## Narrative

MCP Streamable HTTP introduces authenticated, high-frequency JSON-RPC agent traffic into enterprise networks. Without explicit rules, this traffic can resemble **beacon-like cadence** — breaking historical NIDS IoC assumptions. CCC steal: treat MCP/agent egress as first-class observability surface (pairs K353 registry / K367 remote MCP observability). **No PoCs / no evasion recipes.** `policy_wired`.

## Snippets

> "See source page for arXiv 2609.19091 locators." [Source: CCC K366 synthesis]
