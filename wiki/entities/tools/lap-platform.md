---
title: "LAP (Lean API Platform) — agent-native API compiler [CCC stub]"
type: entity
category: tool
tags: [entity, tool, api-compilation, mcp-server-generation, openapi, graphql, k44, steal-from-doc-level-pending-phase-0]
keywords: [lap-platform, openapi-3-x, graphql-sdl, asyncapi, agent-native-format, langchain, apache-2-license]
related:
  - concepts/mcp-context-optimization.md
maturity: steal-from-doc-level-pending-phase-0
created: 2026-05-14
updated: 2026-05-15
cross-wiki-source: "@osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md"
---

## Relations

- @concepts/mcp-context-optimization.md — compiling API specs into agent-native MCP scaffolding cuts hand-coded tool-definition surface
- @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md — K44 source (doc-level verdict)
- @osint-wiki/entities/tools/lap-platform.md — OSINT-side cross-route page (kb-server REST→MCP compilation use case)

## Raw Concept

A Python+TypeScript framework that compiles API specs (OpenAPI 3.x, GraphQL, AsyncAPI) into agent-native formats optimized for Claude Code and Codex. **Apache-2.0, 241 stars, v0.7.0 (last commit 2026-03-26)**. K44 verdict: **Steal-from**. Primary fit: CCC. Cross-route: OSINT (kb-server REST→MCP).

## Narrative

The CCC-relevant pattern: programmatic generation of MCP server scaffolding from existing API specifications. If the compilation logic works, **any service with a published OpenAPI spec becomes a candidate MCP target without hand-coding tool definitions**.

**Phase-0 gates**:
- G1: Star + maturity verification (`gh api repos/Lap-Platform/LAP`)
- G2: License (Apache-2.0 confirmed)
- G3: Run compiler on a known OpenAPI spec (e.g., Cemini's kb-server) — verify output is a working MCP server
- G4: TypeScript SDK overhead on large GraphQL SDL (K44 NEEDS VERIFICATION)

## Snippets

> "LAP specializes in compiling disparate API specifications—including OpenAPI 3.x, GraphQL, and AsyncAPI—into standardized, agent-native formats optimized for Claude Code and Codex."
[Source: @osint-wiki/sources/eval-tool-evaluation-cemini-multi-wiki-v3-2026-05-14.md ¶49]
