---
title: Execution fidelity — irreversible agent invariants (K239)
type: concept
tags: [concept, safety, invariants, execution-fidelity, irreversible, k239]
keywords: [2608.00783, I1-I7, confirm gate, Datumpont, preview-before-write]
related:
  - sources/arxiv-safety-invariants-irreversible-transitions-2608.00783.md
  - entities/tools/datumpont-execution-fidelity.md
  - concepts/agent-completion-verification-gates.md
  - concepts/production-agent-deployment-checklist.md
  - concepts/mcp-app-hitl-approval-gap.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
  - concepts/edge-mcp-meta-action-executor-pattern.md
  - sources/arxiv-scale-cda-cooperative-driving-mcp-2608.04235.md
  - concepts/hardware-confined-agent-signing.md
  - entities/tools/hardware-keystore-mcp-signing.md
  - sources/arxiv-hardware-keystores-ai-agent-signing-2608.06130.md
  - concepts/persona-hat-claude-code-sdlc.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - sources/arxiv-agentrewind-recoverable-execution-2608.14380.md
maturity: draft
created: 2026-08-04
updated: 2026-08-17
---

## Relations

- `@sources/arxiv-safety-invariants-irreversible-transitions-2608.00783.md` — K239 provenance
- `@concepts/agent-completion-verification-gates.md` — completion proof at session end; fidelity at irreversible bind
- `@concepts/production-agent-deployment-checklist.md` — deployment checklist for LIVE/trading/writes
- `@concepts/mcp-app-hitl-approval-gap.md` — I1 confirm gate extends blocking-approval gap

## Raw Concept

How do we guarantee that an agent's realized irreversible effect matches what was previewed to the operator — exactly once — without claiming preview equals intent?

## Narrative

K239 Datumpont (arXiv **2608.00783**) defines **execution fidelity**: realized irreversible effect is either **nothing** or **exactly** the transition previewed to the user, **exactly once**. Explicitly does **not** claim preview matches true user intent.

### Seven invariants (ADOPT checklist)

| ID | Invariant | CCC steal |
|----|-----------|-----------|
| I1 | Confirm gate — preview before key derive | Pair `@concepts/mcp-app-hitl-approval-gap.md`; blocking gate before LIVE Discord / trading / durable writes |
| I2 | Pre-state sufficiency | Capture observable pre-state before irreversible bind |
| I3 | Post-state observability | Verify post-state matches preview |
| I4 | No phantom success | Tool success ≠ side effect committed |
| I5 | Scoped delegation | Subagent writes bounded by delegation scope |
| I6 | Plan-level retry safety | Verify-then-retry, not bare retry |
| I7 | Idempotent intent receiver | Receiver tolerates at-most-once delivery |

Applies to any irreversible external state — not only ledgers.

| Verdict | **ADOPT** invariant checklist. **NO-GO** Datumpont install (no public repo). Entity `wont_wire`. |

## Dead Ends

- **Treating preview as intent proof** — paper explicitly separates fidelity from intent alignment
- **Single-model safety eval as sufficient** — paper notes near-unfalsifiability without diverse write profiles
