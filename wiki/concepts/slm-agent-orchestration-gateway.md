---
title: SLM agent orchestration gateway pattern
type: concept
tags: [concept, agent-orchestration, slm, routing, k95]
keywords: [2606.03557, intent-routing, service-registry, thin-router-fat-backend]
related:
  - sources/arxiv-slm-orchestration-gateway-2606.03557.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - concepts/mcp-context-optimization.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@sources/arxiv-slm-orchestration-gateway-2606.03557.md` — primary paper
- `@entities/tools/lazy-tool.md` — deferred MCP surface
- `@entities/tools/conductor-mcp.md` — cross-wiki backend fan-out

## Raw Concept

K95 arXiv **2606.03557** — edge **intent router** (compact SLM) + **service registry** + transparent backend invocation. Client unchanged when new AI services added.

## Narrative

### Cemini mapping [TENTATIVE]

| Gateway component | CCC stack |
|-------------------|-----------|
| Intent classifier | User prompt + `@path` routing rules |
| Service registry | lazy-tool catalog + MCP server list |
| Backend invocation | `invoke_proxy_tool`, conductor_query, direct MCP |
| Client stability | Cursor rules + CLAUDE.md schema without per-tool client edits |

| Verdict | **STEAL-FROM** — validates lazy-tool + conductor as orchestration-gateway pattern; sub-billion SLM routers not deployed locally |

## Snippets

> "Decouples a virtual world client from heterogeneous AI backends through intent-driven service routing."
> — [Source: arxiv-2606.03557-from-prompt-to-service-an-slm-based-agent-orches.pdf p.1]
