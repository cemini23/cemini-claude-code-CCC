---
title: agents4geos — BSD-3 MCP skills harness for GEOS (REFERENCE)
type: entity
tags: [tool, mcp, skills, bsd, k202]
keywords: [adricortes/agents4geos, GEOS, MCP, TotalEnergies]
related:
  - sources/arxiv-agents4geos-mcp-multiphyics-2607.18557.md
  - concepts/domain-mcp-skills-fresh-subagent-orchestration.md
  - concepts/solver-grounded-agent-numerics.md
maturity: draft
created: 2026-07-22
updated: 2026-07-31
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-ccc-harness.mdc"
---

## Relations

- `@sources/arxiv-agents4geos-mcp-multiphyics-2607.18557.md` — paper
- `@concepts/domain-mcp-skills-fresh-subagent-orchestration.md` — pattern
- `@concepts/solver-grounded-agent-numerics.md` — solver-grounded peer

## Raw Concept

`github.com/adricortes/agents4geos` — BSD-3-Clause. Local `.local/adopts/agents4geos` (~2.3MB). Skills under `skills/geos:*.md`; MCP tools for schema/mesh/fluids/run/validate.

## Narrative

### Phase-0

| Check | Result |
|-------|--------|
| License | **BSD-3-Clause** [CONFIRMED] |
| Size | ~2.3MB — OK |
| GEOS dependency | LGPL; ~586MB — **NO-GO** under 500MB budget |
| Failure mode | Domain-specific; do not wire to TipDrop LIVE |

### Verdict

**GO** REFERENCE clone for skills+MCP packaging. **NO-GO** GEOS full stack. Not a default prod MCP.
