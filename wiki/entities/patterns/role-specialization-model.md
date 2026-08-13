---
title: "Role Specialization Model (RSM) — multi-tool coordination framework"
type: entity
tags: [entity, pattern, agentic-se, role-coordination, k276]
keywords: [k276, RSM, role-specialization, multi-tool, HITL, prompt-hardening]
related:
  - sources/arxiv-role-specialization-model-rsm-2608.12311.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - concepts/code-as-agent-harness.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- `@sources/arxiv-role-specialization-model-rsm-2608.12311.md`
- `@concepts/role-specialization-model-multi-tool-coordination.md`

## Raw Concept

Phase-0 entity for CCC k276 — RSM coordination framework.

## Narrative

Framework from an exploratory case study — **no product, `wont_wire`** at the runtime level. Wires as a **policy pattern**: explicit role distribution across tools, HITL verification of agent outputs, prompt-hardening via explicit negative constraints, failure-backed instructions. Applicable to Cemini's multi-tool orchestration (claude-ds worker, /route skill, subagents).

**Phase-0:** `scripts/adopt_k276_phase0.sh`
