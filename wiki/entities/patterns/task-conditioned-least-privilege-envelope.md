---
title: Task-conditioned least-privilege envelope
type: entity
tags: [entity, pattern, least-privilege, security, k290]
keywords: [2608.18351, sufficient-authority envelope, excess-authority]
related:
  - concepts/task-conditioned-least-privilege-agent-learning.md
  - sources/arxiv-task-conditioned-least-privilege-learning-2608.18351.md
  - entities/patterns/signed-mandate-mcp-proxy.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- `@concepts/task-conditioned-least-privilege-agent-learning.md`
- `@sources/arxiv-task-conditioned-least-privilege-learning-2608.18351.md`

## Raw Concept

Pattern: per-task sufficient-authority envelope + trajectory excess-privilege scoring.

## Narrative

Define task-relative minimum authority; audit trajectories for actions beyond envelope. Complements signed mandates (K285) — learned restraint does not replace gates.
