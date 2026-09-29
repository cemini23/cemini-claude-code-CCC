---
title: "HTN Planning as a Coordination Layer for Multi-Server MCP Tool Orchestration (CCC K401)"
type: concept
tags: [concept, k401]
keywords: [2609.33731, k401]
related:
  - sources/arxiv-htn-planning-mcp-multi-server-coordination-2609.33731.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-29_ccc-k401-k405-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-29
updated: 2026-09-29
---

## Relations

- `@sources/arxiv-htn-planning-mcp-multi-server-coordination-2609.33731.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-29_ccc-k401-k405-sip-ready.md`

## Raw Concept

K401: ADOPT pattern — arXiv 2609.33731.

## Narrative

**HTN planning as MCP coordination layer** — cross-server plans compiled once, executed deterministically via middleware and `${context.X}` binding; avoids LLM-host one-round-trip-per-tool orchestration (pairs K329 domain orchestration / K318 step routing / K311 lazy MCP). **Apache-2.0** artifact `PCfVW/hplan26-artifact` — REFERENCE optional HITL; runtime **`wont_wire`**. Concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.33731 locators." [Source: CCC K401 synthesis]
