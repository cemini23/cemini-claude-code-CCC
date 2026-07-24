---
title: "Euclid-MCP — deterministic Prolog reasoning via MCP"
type: source
tags: [source, arxiv, mcp, neuro-symbolic, prolog, k211]
keywords: [2607.21412, Euclid-MCP, Euclid-IR, SWI-Prolog, meob]
related:
  - concepts/deterministic-mcp-symbolic-reasoning.md
  - entities/tools/euclid-mcp.md
  - concepts/solver-grounded-agent-numerics.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k210-k214-traceable-euclid-acm-openforge-2026-07-24.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- `@concepts/deterministic-mcp-symbolic-reasoning.md`
- `@entities/tools/euclid-mcp.md`
- `@concepts/solver-grounded-agent-numerics.md` — tool-as-truth peer (K199)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Euclid-MCP: A Model Context Protocol Server for Deterministic Logical Reasoning via Prolog |
| **Author** | Bartolomeo Bogliolo |
| **arXiv** | 2607.21412 |
| **Pages** | 30 |
| **Retrieved** | 2026-07-24 |
| **Code** | `meob/Euclid-MCP` — **Apache-2.0** [CONFIRMED LICENSE] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.21412-euclid-mcp-a-model-context-protocol-server-for-d.pdf` |

## Narrative

LLM describes facts in Euclid-IR; Prolog does deduction. Translate-run-inspect-repair loop. At 1k+ RBAC facts LLMs hallucinate; Euclid-MCP exact + faster. Thesis: semantic RAG unfit for rule enforcement.
