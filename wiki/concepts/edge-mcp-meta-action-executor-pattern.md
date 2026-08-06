---
title: Edge MCP meta-action executor pattern (K249)
type: concept
tags: [concept, mcp, edge, meta-action, safety-boundary, k249]
keywords: [2608.04235, Scale-CDA, MCP-bridge, JSON-advisory, verified-executor, safety-core]
related:
  - sources/arxiv-scale-cda-cooperative-driving-mcp-2608.04235.md
  - entities/tools/scale-cda.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
maturity: draft
created: 2026-08-06
updated: 2026-08-06
---

## Relations

- `@sources/arxiv-scale-cda-cooperative-driving-mcp-2608.04235.md` — K249 provenance
- `@concepts/execution-fidelity-irreversible-agent-invariants.md` — safety-core boundary peer (K239)
- `@concepts/schema-bound-mcp-tool-surface.md` — typed executor surface peer

## Raw Concept

How should GenAI advisory layers connect to safety-critical actuators without mutating certified control cores?

## Narrative

K249 Scale-CDA (arXiv **2608.04235**): edge MLLM connects via **MCP bridge** → JSON advisories + **meta-action executors** into Openpilot planner hooks. Safety-certified core unchanged. End-to-end &lt;60ms; on-board privacy. Automotive domain is OOD.

### Pattern (ADOPT)

| Layer | Role |
|-------|------|
| GenAI / MLLM | Propose structured advisories (JSON) |
| MCP bridge | Typed tool surface between model and actuators |
| Meta-action executors | Verified enactment into planner hooks |
| Safety core | Immutable — no direct model mutation |

GenAI **proposes**; verified executors **enact**; do not mutate safety-certified core.

### Cemini mapping

- Pair with `@concepts/execution-fidelity-irreversible-agent-invariants.md` (K239) for irreversible binds
- Schema-bound MCP args before side effects (`@concepts/schema-bound-mcp-tool-surface.md`)
- No Scale-CDA / Openpilot install

| Verdict | **ADOPT** pattern. **NO-GO** automotive stack. Entity `wont_wire`. |
