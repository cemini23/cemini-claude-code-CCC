---
title: Domain MCP skills + fresh-context subagent orchestration
type: concept
tags: [concept, mcp, skills, subagents, solver-grounded, k202]
keywords: [2607.18557, Agents4GEOS, curated skills, fresh-context subagents]
related:
  - sources/arxiv-agents4geos-mcp-multiphyics-2607.18557.md
  - entities/tools/agents4geos.md
  - concepts/solver-grounded-agent-numerics.md
  - concepts/subagent-orchestration.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/nl2pipeline-platform-grounded-mutations.md
  - sources/brief-k202-k205-agents-langgraph-biosec-2026-07-22.md
  - concepts/multi-stage-rag-architect-reviewer-triad.md
  - sources/arxiv-iterasim-rag-multistage-2607.20346.md
maturity: draft
created: 2026-07-22
updated: 2026-07-23
---

## Relations

- `@sources/arxiv-agents4geos-mcp-multiphyics-2607.18557.md` — provenance
- `@entities/tools/agents4geos.md` — BSD-3 clone
- `@concepts/solver-grounded-agent-numerics.md` — compute, don't invent
- `@concepts/subagent-orchestration.md` — fresh-context peer
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — skill routing peer

## Raw Concept

K202 Agents4GEOS pattern: large domain MCP tool surface + **human-curated skills** + **fresh-context subagents** under an orchestrator; quantities from tools only.

## Narrative

### Steal (ADOPT)

1. Domain bots (TipDrop scanner, poker tools): expose typed MCP tools; wrap procedures as curated skills — not one mega-prompt.
2. Spawn **fresh-context** subagents for heavy steps; orchestrator keeps the plan.
3. Never let the LLM invent physical/financial quantities — call tools (pairs with K199).
4. GEOS binary/sim stack: **NO-GO** clone (>500MB). agents4geos harness: **GO** REFERENCE (~2.3MB).

| Verdict | **ADOPT** skills+fresh-subagent checklist; **GO** agents4geos clone; **NO-GO** GEOS |
