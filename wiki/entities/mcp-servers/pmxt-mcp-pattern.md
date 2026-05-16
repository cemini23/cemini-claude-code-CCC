---
title: "pmxt — MCP-exposes-trading-execution pattern (@pmxt/mcp)"
type: entity
tags: [entity, mcp-server, pattern, trading-execution-mcp, prediction-markets, cross-wiki-stub, cross-wiki-route-2026-05-16]
keywords: [pmxt, pmxt-mcp, ccxt-for-prediction-markets, create-order, fetch-balance, polymarket-kalshi-limitless, mcp-trading-execution, mit-license]
related:
  - entities/mcp-servers/exa.md
  - concepts/subagent-orchestration.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/entities/tools/pmxt.md"
---

## Relations

- @entities/mcp-servers/exa.md — sibling MCP-server page; pmxt is a contrasting MCP class (execution-side, not research-side)
- @concepts/subagent-orchestration.md — an execution-capable MCP server is exactly the kind of high-blast-radius tool a Tier-2 subagent gates access to
- @osint-wiki/entities/tools/pmxt.md — cross-wiki primary page (full tool write-up + audit lives in OSINT)

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16. pmxt is "CCXT for prediction markets" (MIT, https://github.com/pmxt-dev/pmxt). The CCC-relevant slice is the MCP package it ships, `@pmxt/mcp`. Primary page: `@osint-wiki/entities/tools/pmxt.md` — the prediction-market and financial detail belongs in OSINT; this stub documents only the Claude-Code-side pattern.

## Narrative

**Pattern: MCP server exposes trading execution directly to Claude Code agents.**

`@pmxt/mcp` exposes native prediction-market *execution* APIs — `create_order`, `fetch_balance`, and the rest of a CCXT-style unified surface — across Polymarket, Kalshi, and Limitless, callable directly from a Claude Code agent. Most MCP servers Cemini uses are *research-side* (Exa, Brave, librarian-kb-server): read-only, low blast radius. pmxt is the opposite class — an MCP server that can move money.

The CCC takeaway is the blast-radius distinction. An execution-capable MCP server is the highest-consequence tool class Cemini can wire into a session. It belongs behind the Tier-2 gate of `@concepts/subagent-orchestration.md`: never callable from an unscoped Tier-1 agent, always requiring explicit operator confirmation per call. The pattern is worth cataloguing as a *reference class* — when CCC documents MCP-server adoption, "does this server have write/execution side effects?" is a Phase-0 audit question that pmxt makes concrete.

Full financial context, the CCXT-unification rationale, and the Phase-0 verdict are in the OSINT primary page.

## Snippets

> pmxt ships `@pmxt/mcp`, exposing native prediction-market execution APIs (`create_order`, `fetch_balance`) across Polymarket / Kalshi / Limitless directly to Claude Code agents.
[Source: @osint-wiki/entities/tools/pmxt.md]
