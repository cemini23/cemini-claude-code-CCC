---
title: "A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem (CCC K382)"
type: concept
tags: [concept, k382]
keywords: [2609.26761, k382]
related:
  - sources/arxiv-a2m-mcp-metadata-hijacking-2609.26761.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-23_ccc-k376-k384-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-23
updated: 2026-09-23
---

## Relations

- `@sources/arxiv-a2m-mcp-metadata-hijacking-2609.26761.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-23_ccc-k376-k384-sip-ready.md`

## Raw Concept

K382: Cybersec-primary ADOPT policy — arXiv 2609.26761.

## Narrative

**Semantic MCP hijacking** via **tool metadata + trajectory traces** — descriptions and prior tool results shape selection without touching server binaries. **Cybersec-primary** supply-chain surface for MCP catalogs (pairs K274 CDH / K368 implicit trust / K350 harness supply-chain scan). Operator helper: `scripts/mcp_metadata_precheck.py` + federation skill `mcp-metadata-precheck` (heuristic review only; pair `cursor-security-preflight`). `Lilaizhen/A2M` **null license** → **NO clone**. **No PoCs / no attack templates anywhere.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2609.26761 locators." [Source: CCC K382 synthesis]
