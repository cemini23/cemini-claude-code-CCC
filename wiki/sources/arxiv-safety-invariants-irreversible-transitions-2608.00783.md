---
title: "Safety Invariants for Irreversible Agent Transitions — execution fidelity"
type: source
tags: [source, arxiv, safety, invariants, execution-fidelity, k239]
keywords: [2608.00783, Datumpont, Zhaoming Yin, irreversible transitions, confirm gate]
related:
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - entities/tools/datumpont-execution-fidelity.md
  - concepts/agent-completion-verification-gates.md
  - concepts/production-agent-deployment-checklist.md
  - concepts/mcp-app-hitl-approval-gap.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@entities/tools/datumpont-execution-fidelity.md`
- `@concepts/agent-completion-verification-gates.md`
- `@concepts/production-agent-deployment-checklist.md`
- `@concepts/mcp-app-hitl-approval-gap.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Safety Invariants for Irreversible Agent Transitions |
| **Author** | Zhaoming Yin (Datumpont AI) |
| **arXiv** | 2608.00783 |
| **Pages** | 29 |
| **Site** | datumpont.ai (live) |
| **Code/Availability** | No public repo found |
| **Retrieved** | 2026-08-04 |

## Narrative

Defines **execution fidelity**: the realized irreversible effect is either nothing or exactly the transition previewed to the user, exactly once. Does **not** claim the preview matches true user intent.

Seven invariants:

| ID | Invariant |
|----|-----------|
| I1 | Confirm gate — preview before key derive |
| I2 | Pre-state sufficiency |
| I3 | Post-state observability |
| I4 | No phantom success |
| I5 | Scoped delegation |
| I6 | Plan-level retry safety — verify-then-retry, not bare retry |
| I7 | Idempotent intent receiver |

Empirical: ~+74pp vs naive-ReAct on write-aggressive models, ~+3pp on write-cautious. Single-model safety evals nearly unfalsifiable. Production evidence: 108 prod writes / 8 chains.

Applies beyond ledgers to any irreversible external state (LIVE Discord, trading, durable writes).

| Verdict | **ADOPT** invariant checklist for consequential writes. **NO-GO** install (no public code). Entity `wont_wire`. |
