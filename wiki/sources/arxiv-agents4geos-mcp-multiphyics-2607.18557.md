---
title: "Agents4GEOS — MCP agent platform for open-source multi-physics sim"
type: source
tags: [source, arxiv, mcp, skills, subagents, solver-grounded, geoscience, k202]
keywords: [2607.18557, Agents4GEOS, GEOS, MCP tools, fresh-context subagents]
related:
  - concepts/domain-mcp-skills-fresh-subagent-orchestration.md
  - entities/tools/agents4geos.md
  - concepts/solver-grounded-agent-numerics.md
  - concepts/nl2pipeline-platform-grounded-mutations.md
  - sources/brief-k202-k205-agents-langgraph-biosec-2026-07-22.md
maturity: draft
created: 2026-07-22
updated: 2026-07-22
---

## Relations

- `@concepts/domain-mcp-skills-fresh-subagent-orchestration.md` — synthesized steal
- `@entities/tools/agents4geos.md` — BSD-3 REFERENCE clone
- `@concepts/solver-grounded-agent-numerics.md` — ground quantities in computation (K199)
- `@concepts/nl2pipeline-platform-grounded-mutations.md` — platform-grounded peer (K197)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | AGENTS4GEOS: agentic platform for open-source multi-physics simulation |
| **Author** | Adriano M. A. Côrtes et al. (UFRJ / TotalEnergies) |
| **arXiv** | 2607.18557 |
| **Pages** | 14 |
| **Retrieved** | 2026-07-22 |
| **Code** | `adricortes/agents4geos` — **BSD-3-Clause**; GEOS simulator LGPL-2.1 (~586MB) — **NO-GO** clone (over 500MB) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.18557-agents4geos-agentic-platform-for-open-source-mul.pdf` |

## Narrative

MCP layer with **52 domain-aware tools** for GEOS (input files, mesh, fluids, post-process). Human-curated skills + fresh-context subagents under an orchestrator; every quantity grounded in actual computation (not LLM arithmetic). Geoscience body OOD — steal harness shape.

## Snippets

> "Through human-curated skills and fresh-context subagents coordinated by an orchestrator, the system executes complex workflows … grounding every quantity in actual computation."
> — Abstract
