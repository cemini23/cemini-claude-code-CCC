---
title: "When Agents Look Like Beacons: NIDS Evasion by MCP Traffic (CCC K366)"
type: source
tags: [source, arxiv, k366]
keywords: [2609.19091, k366]
related:
  - concepts/mcp-traffic-network-detection-blind-spot.md
  - briefs/2026-09-17_ccc-k363-k367-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-17
updated: 2026-09-17
---

## Relations

- `@concepts/mcp-traffic-network-detection-blind-spot.md`
- `@briefs/2026-09-17_ccc-k363-k367-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | When Agents Look Like Beacons: NIDS Evasion by MCP Traffic |
| **arXiv** | 2609.19091 (2026-09) |
| **Retrieved** | 2026-09-17 |

## Narrative

**Verdict: Cybersec-primary + ADOPT policy.**

MCP Streamable HTTP introduces authenticated, high-frequency JSON-RPC agent traffic into enterprise networks. Without explicit rules, this traffic can resemble **beacon-like cadence** — breaking historical NIDS IoC assumptions. CCC steal: treat MCP/agent egress as first-class observability surface (pairs K353 registry / K367 remote MCP observability). **No PoCs / no evasion recipes.** `policy_wired`.

## Snippets

> "When Agents Look Like Beacons: NIDS Evasion by MCP Traffic — CCC K366 synthesis." [Source: arXiv 2609.19091 — paraphrase]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.19091-when-agents-look-like-beacons-nids-evasion-by-mo.pdf` |
