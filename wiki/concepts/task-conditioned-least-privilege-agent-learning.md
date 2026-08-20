---
title: Task-conditioned least-privilege agent learning
type: concept
tags: [concept, least-privilege, mcp, security, k290]
keywords: [2608.18351, excess-authority, sufficient-authority envelope, brokered audit]
related:
  - sources/arxiv-task-conditioned-least-privilege-learning-2608.18351.md
  - entities/patterns/task-conditioned-least-privilege-envelope.md
  - concepts/signed-mandate-mcp-protocol-enforcement.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - sources/brief-k290-k294-harness-wave-2026-08-20.md
  - briefs/2026-08-20_ccc-handoff-k290-k294-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-20
updated: 2026-08-20
---

## Relations

- `@sources/arxiv-task-conditioned-least-privilege-learning-2608.18351.md`
- `@entities/patterns/task-conditioned-least-privilege-envelope.md`

## Raw Concept

Can post-training teach tool agents task-relative least privilege as a complement to permission gates?

## Narrative

**Task-relative excess authority:** actions beyond the sufficient minimum for the requested task — even when the final answer is correct. **Sufficient-authority envelopes** per task define what capability is necessary; penalize only excess beyond the envelope.

**Brokered terminal/MCP environment:** unseen broker parses each action, scores six-dimensional risk deterministically, records effects. Post-training (Dr. GRPO) optimizes safe success while reducing excess-authority events.

**Cemini steal:** Layer learned restraint **on top of** Mandato-style signed mandates and sandbox gates — never replace them (pairs K285, K239). Use deterministic trajectory auditors for excess-privilege metrics in harness eval packs.

| Verdict | **ADOPT** policy pattern. No public code → **policy_wired** only. |
