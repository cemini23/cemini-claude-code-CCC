---
title: Deterministic MCP symbolic reasoning — Euclid-IR / Prolog pattern
type: concept
tags: [concept, mcp, neuro-symbolic, prolog, compliance, k211]
keywords: [2607.21412, Euclid-MCP, rule enforcement, not semantic RAG]
related:
  - sources/arxiv-euclid-mcp-prolog-reasoning-2607.21412.md
  - entities/tools/euclid-mcp.md
  - concepts/solver-grounded-agent-numerics.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k210-k214-traceable-euclid-acm-openforge-2026-07-24.md
maturity: draft
created: 2026-07-24
updated: 2026-07-24
---

## Relations

- `@sources/arxiv-euclid-mcp-prolog-reasoning-2607.21412.md`
- `@entities/tools/euclid-mcp.md`
- `@concepts/solver-grounded-agent-numerics.md`

## Raw Concept

K211: for rule/compliance/RBAC-style questions, don't use semantic RAG — translate to IR, run deterministic engine, inspect/repair.

## Narrative

### Steal (ADOPT)

1. TipDrop/prod policy questions: LLM describes facts; solver/engine decides.
2. Prefer translate-run-inspect-repair MCP loop over "ask the model to reason about rules."
3. Euclid-MCP Apache clone REFERENCE (~1.2MB).

| Verdict | **ADOPT** symbolic-MCP checklist; **GO** Euclid-MCP REFERENCE |
