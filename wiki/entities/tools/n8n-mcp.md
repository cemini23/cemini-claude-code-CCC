---
title: n8n-mcp — n8n workflows exposed to Claude/Cursor via MCP (MIT)
type: entity
tags: [tool, mcp-server, workflow-automation, cross-wiki-route]
keywords: [n8n-mcp, czlonkowski, n8n, workflow, mcp, cursor, windsurf, claude]
related:
  - concepts/mcp-context-optimization.md
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - entities/tools/claude-code.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-05-22
updated: 2026-05-22
cross-wiki-source: "@osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md"
---

## Relations

- `@concepts/mcp-context-optimization.md` — workflow MCPs can explode tool-catalog size; lazy-tool candidate
- `@concepts/subagent-orchestration.md` — long workflows may be better as delegated subagent tasks than parent-session MCP spam
- `@entities/tools/conductor-mcp.md` — different primitive (read-only wiki fan-out vs n8n execution graphs)
- `@entities/tools/claude-code.md` — host harness

Cross-wiki: K55-2 ridark list #36; license **MIT CONFIRMED** 2026-05-22 (~21.2k★).

## Raw Concept

`czlonkowski/n8n-mcp` bridges **n8n automation graphs** to Claude Code / Cursor / Windsurf via MCP. CCC interest: **workflow-automation MCP server pattern** — compare tool surface area and auth model before adoption.

## Narrative

### Phase-0 questions (unanswered)

- Stdio vs HTTP transport; credential storage for n8n API
- How many tools exported per workflow (MCP catalog inflation)
- Blast radius if an LLM triggers production n8n flows

### Adoption posture

| Check | Status |
|-------|--------|
| License | MIT [CONFIRMED 2026-05-22] |
| Phase-0 | **Not run** |
| Verdict | **CONDITIONAL-GO** — pattern reference; adopt only if a concrete n8n graph is already in production |

## Dead Ends

- **Default MCP for all sessions** — catalog overhead violates `@concepts/mcp-context-optimization.md` without lazy-tool.
