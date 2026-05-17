---
title: "polymarket-mcp-server (caiovicentino) — 45-tool autonomous-trading MCP (MIT, Wave 5B Adopt)"
type: entity
tags: [mcp-server, polymarket, prediction-markets, autonomous-trading, claude-code, python, mit-license, execution-mcp, cross-wiki-stub]
keywords: [polymarket-mcp-server, caiovicentino, 45-tools, autonomous-trading, market-discovery, position-management, websocket, polygon-blockchain, fastmcp, fork-and-maintain]
related:
  - entities/mcp-servers/pmxt-mcp-pattern.md
  - concepts/subagent-orchestration.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/agent-vm-sandboxing.md
maturity: draft
created: 2026-05-17
updated: 2026-05-17
cross-wiki-source: "@osint-wiki/sources/caiovicentino-polymarket-mcp-server.md"
---

## Relations

- @entities/mcp-servers/pmxt-mcp-pattern.md — adjacent execution-MCP class (`@pmxt/mcp`); pmxt is the multi-exchange CCXT-style wrapper, this is the Polymarket-specific 45-tool surface. Same blast-radius class.
- @concepts/subagent-orchestration.md — execution-capable MCP servers belong behind the Tier-2 gate; this is the canonical example
- @entities/patterns/tier1-tier2-agent-model.md — explicit operator confirmation per call is the Tier-2 requirement for write/execution MCP surfaces
- @concepts/agent-vm-sandboxing.md — first-run isolation surface for any execution MCP server before trust is established
- @osint-wiki/sources/caiovicentino-polymarket-mcp-server.md — cross-wiki primary; full Phase-0 audit, 45-tool inventory, Polymarket deployment detail, and trading-strategy integration live there

## Raw Concept

CCC-side stub for the polymarket-mcp-server. `github.com/caiovicentino/polymarket-mcp-server` (MIT) — Python MCP server exposing 45 tools for autonomous Polymarket trading: market discovery, market analysis, position management, real-time WebSocket monitoring. OSINT verdict: Wave 5B Adopt-but-fork-and-pin (1 contributor). This stub records the Claude-Code-side relevance — specifically the "execution-capable MCP server" class and its Tier-2 implications.

## Narrative

### The class, not the tool

CCC catalogues this MCP server for the same reason as @entities/mcp-servers/pmxt-mcp-pattern.md — it's a concrete example of the **execution-MCP class**, the highest-blast-radius MCP server category Cemini can wire into a session.

The Polymarket trading detail belongs in OSINT (it's a financial-research wiki concern). The Claude-Code-side concern is: how does a session safely call a tool that can move real money?

### Three operational rules for execution MCPs (extracted from this case)

1. **Never callable from an unscoped Tier-1 agent.** The execution tool surface must be wired only into a Tier-2 subagent with a narrow, audited prompt (see @entities/patterns/tier1-tier2-agent-model.md).
2. **Explicit operator confirmation per call.** No "yes to all" mode. Every `create_order` / `close_position` / `withdraw` invocation requires a human confirmation in the session.
3. **First-run inside agent-VM.** A first invocation runs inside an isolated VM with action tracing on (see @concepts/agent-vm-sandboxing.md). Only after a trusted-run interval does the tool move to the host.

### Phase-0 highlights (from OSINT)

- **License**: MIT — verified.
- **Maturity**: 395★, 1 contributor, single maintainer. **Fork-and-pin** is mandatory for execution MCPs at this bus-factor.
- **45-tool surface area**: large. Each tool requires a separate audit; OSINT's primary documents the per-tool inventory.
- **Polygon-blockchain dependency**: requires a wallet passphrase. Credential hygiene is part of the audit; see @CLAUDE.md § Related — environment + secrets.
- **Dual-MCP pattern for Polymarket**: kukapay's read-only odds MCP + this one's execution MCP. OSINT operates both; CCC catalogues only the execution-class member because that's the unusual one from a Claude-Code-safety perspective.

### Why catalogued in CCC despite being an OSINT tool

The CCC concern is the **harness configuration that gates this MCP server**, not the tool itself. Three derivatives:

- `~/.claude/settings.json` patterns for gating execution MCPs (still draft; @briefs/ candidate).
- The Tier-1 / Tier-2 boundary policy this MCP exemplifies.
- The agent-VM first-run discipline.

The Polymarket detail (markets to trade, strategies to run, risk-management) lives entirely in OSINT.

## Snippets

> Enable Claude to trade prediction markets with 45 tools, real-time monitoring, and enterprise-grade safety features.
[Source: @osint-wiki/sources/caiovicentino-polymarket-mcp-server.md]
