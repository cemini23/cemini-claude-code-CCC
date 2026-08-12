---
title: Domain solvers as agent-callable MCP + Skills (K272)
type: concept
tags: [concept, mcp, skills, packaging, k272]
keywords: [2608.10866, agent4binary, Skill, MCP-tools]
related:
  - sources/arxiv-agent-callable-spectroscopic-binary-2608.10866.md
  - entities/tools/agent4binary.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/skill-vetting.md
  - sources/brief-k270-k273-mcp-acm-wave-2026-08-12.md
  - briefs/2026-08-12_ccc-handoff-k270-k273-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-12
updated: 2026-08-12
---

## Relations

- `@sources/arxiv-agent-callable-spectroscopic-binary-2608.10866.md`
- `@entities/tools/agent4binary.md`
- `@concepts/schema-bound-mcp-tool-surface.md`

## Raw Concept

How should scientific/domain solvers be exposed to coding agents?

## Narrative

K272 packages a domain detector as **MCP tool servers + Skill**. Pattern: keep the solver authoritative; wrap with typed tools + SKILL.md; do not ask the LLM to reimplement the science.

### Steal (ADOPT)

1. Prefer MCP+Skill wrappers around verified solvers for domain quantities (pairs solver-grounded numerics).
2. Skill packaging must pass Phase-0 / skill-vetting before enable.
3. Astronomy runtime **wont_wire**; REFERENCE clone OK.

| Verdict | **ADOPT** packaging pattern. |
