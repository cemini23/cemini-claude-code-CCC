---
title: MCP pre-trade diligence boundary — research not execution (K106)
type: concept
tags: [concept, mcp, policy, k106]
keywords: [pre-trade, diligence, dex, mcp-boundary, no-execution]
related:
  - entities/tools/dexscreener-mcp.md
  - sources/trading-posts-compilation-6-2026-06-08.md
  - concepts/mcp-server-catalog-curation.md
  - entities/mcp-servers/pmxt-mcp-pattern.md
  - concepts/skill-vetting.md
  - concepts/selective-experience-memory-harness.md
maturity: draft
created: 2026-06-09
updated: 2026-06-17
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-6-2026-06-08.md"
---

## Relations

- `@entities/tools/dexscreener-mcp.md` — exemplar laptop MCP (K106)
- `@concepts/mcp-server-catalog-curation.md` — catalog + tier gates
- `@entities/mcp-servers/pmxt-mcp-pattern.md` — execution MCP class (Tier-2 gated)

## Raw Concept

K106 @AlphaCartell DexScreener MCP post: operator docs must state **pre-trade diligence, not execution** — MCP for mental models and screening, not EMS order routing.

## Narrative

| Allowed | Blocked |
|---------|---------|
| Claude Desktop research session | Prod `prod-mcp` execution without EMS review |
| `claude_desktop_config.json` MCP block | Substituting for audited Cemini connectors |
| Explicit risk section in briefs | Wiring unverified community MCP into trading bots |

Pairs with `@concepts/mcp-server-catalog-curation.md` exploraX USB-C model — discovery MCPs stay laptop-tier until Phase-0.

## Snippets

> Pre-trade diligence, not execution — operator boundary from K106 DexScreener MCP brief.
