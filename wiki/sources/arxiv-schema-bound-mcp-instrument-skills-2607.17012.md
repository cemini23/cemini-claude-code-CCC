---
title: "Schema-bound LLM control of instruments via MCP skills"
type: source
tags: [source, arxiv, mcp, schema, skills, instrumentation, k198]
keywords: [2607.17012, nuance-mcp, schema-bound, live-job, NUANCE, Northwestern]
related:
  - concepts/schema-bound-mcp-tool-surface.md
  - entities/tools/nuance-mcp.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/coding-agent-install-gap-and-preinstall-gate.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- `@concepts/schema-bound-mcp-tool-surface.md` — synthesized steal
- `@entities/tools/nuance-mcp.md` — MIT reference implementation
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — validate-before-bind peer
- `@concepts/coding-agent-install-gap-and-preinstall-gate.md` — local/offline agent posture peer

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Schema-Bound LLM Control of Scientific Instrumentation through Model Context Protocol Skills |
| **Author** | Roberto dos Reis, Vinayak P. Dravid (Northwestern / NUANCE) |
| **arXiv** | 2607.17012 |
| **Pages** | 28 |
| **Retrieved** | 2026-07-21 |
| **Code** | `github.com/NUANCE-IT/nuance-mcp` — **MIT** [CONFIRMED] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.17012-schema-bound-llm-control-of-scientific-instrumen.pdf` |

## Narrative

### Method (four parts)

1. **Schema-bound tool surface** — validate every request against physical bounds before vendor dispatch
2. **Host-process adapter** — vendor-neutral ABC; language-side vs instrument-side split
3. **Live-processing job lifecycle** — long-running analyses as first-class typed tools
4. **Skill via MCP prompts** — parameterized tool sequences as reusable protocols

Reference: 30 typed tools, 5 live-job types, 6 skills; software-only simulator validation (120 HW-independent tests pass; 12–15/15 local-LLM integration).

### CCC steal

Any MCP that can emit unsafe args (shell, trading, TipDrop LIVE): **schema-bound bounds before dispatch**. Skills as MCP-prompt compositions of typed tools — not free-form chains.

## Snippets

> "a schema-bound tool surface validates every request against physical bounds before any vendor call is dispatched"
> — Abstract

> "The MIT-licensed source, simulator, and test suite are available at https://github.com/NUANCE-IT/nuance-mcp"
> — Conclusion
