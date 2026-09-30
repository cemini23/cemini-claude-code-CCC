---
title: DexScreener MCP — Claude Desktop DEX research bridge
type: entity
tags: [tool, mcp, dex, reference, k106]
keywords: [dexscreener, claude-desktop, pre-trade-diligence, defi-research]
related:
  - sources/trading-posts-compilation-6-2026-06-08.md
  - concepts/mcp-pre-trade-diligence-boundary.md
  - concepts/mcp-server-catalog-curation.md
  - entities/tools/claude-code.md
  - "@osint-wiki/entities/tools/dexscreener-mcp.md"
maturity: draft
created: 2026-06-09
updated: 2026-06-09
phase_0_verdict: "REFERENCE 2026-06-09 — laptop Claude Desktop only; MCP repo license unverified"
---

## Relations

- `@sources/trading-posts-compilation-6-2026-06-08.md` — K106 Post 5 (@AlphaCartell)
- `@concepts/mcp-pre-trade-diligence-boundary.md` — pre-trade vs execution boundary
- `@concepts/mcp-server-catalog-curation.md` — MCP catalog discipline
- `@osint-wiki/entities/tools/dexscreener-mcp.md` — canonical narrative

## Raw Concept

Community MCP server exposing DexScreener free REST API to Claude Desktop — live DEX prices, liquidity, pairs, trending tokens (60+ chains). K106 documents `claude_desktop_config.json` block pattern (~15–30 min, Node 18+, no API key).

Distinct from K78 **Hermes + x402** forensics bundle (paid Nansen/Tokenomist legs).

## Narrative

**Verdict:** **REFERENCE** — laptop crypto diligence sessions only. Prod EMS uses audited Cemini connectors; **NO-GO** prod execution wiring without Phase-0 + security review.

**Risks (per source):** illiquid pairs, honeypots, AI hallucination on thin data.

**License:** the original source never named a specific repo. **Search 2026-09-30 surfaced two candidates, neither confirmed as the one referenced:** `vibeforge1111/dexscreener-cli-mcp-tool` (no license file) and `openSVM/dexscreener-mcp-server` (**Unlicense** — public domain). [CONFIRMED via GitHub API 2026-09-30] **No install** until the intended repo is identified. A third-party MCP server for a crypto data API is a credential-and-funds blast radius; the Unlicense gives no warranty.

## Snippets

> "Claude cannot directly query APIs. But MCP gives it a structured way to request external data through predefined tools." [Source: Posts.docx K106, @AlphaCartell Post 5]
