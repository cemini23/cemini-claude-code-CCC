---
title: "Bounded authority + auditable trajectories — the missing axis for security agents (CCC K325)"
type: concept
tags: [concept, security, agents, bounded-authority, auditability, hitl, evidence-tree, k325]
keywords: [bounded authority, auditable trajectories, security agents, evidence ledger, risk-aware autonomy, HITL, K325, 2608.28490]
related:
  - sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/agentified-eval-evidence-tree-harness.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/recognition-vs-enforcement-instruction-arbitration.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
maturity: draft
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- `@sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@concepts/agentified-eval-evidence-tree-harness.md`
- `@concepts/measurement-integrity-mcp-security-eval.md`
- `@concepts/recognition-vs-enforcement-instruction-arbitration.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

The question: 100 peer-reviewed papers (2023–2026) build LLM agents for software and systems security — but along which axis are they all weak? Answer from the K325 SLR [Source: wiki/sources/arxiv-llm-agents-software-systems-security-slr-2608.28490.md]: agents are built to **act**, not to be **bounded** or **audited**. 91% modular, 88% planner-and-actor, 95% fully autonomous — vs 15% critic/verifier roles, 13% guardrail layers, 13% human review points.

## Narrative

The survey's asymmetry is the design lesson:

| Built to act | Rarely bounded / inspected |
|--------------|----------------------------|
| 91% modular pipeline | 15% explicit critic/verifier role |
| 88% backbone LLM planner-and-actor | 13% guardrail layer |
| 95% fully autonomous | 13% any human review point |
| 51% report success/completion | 11% report hallucination rate |
| 34% report P/R/F1 | 5% report scope containment |
| — | 1% report tool-call accuracy |

**CCC policy — bounded authority:**

1. **Keep HITL on irreversible tools.** Exploit execution, production remediation, disclosure decisions, and active response are high-risk; they need explicit human approval or policy-verified execution, not model self-arbitration (pairs `@concepts/execution-fidelity-irreversible-agent-invariants.md`, K239). Low-risk tasks (offline summarization, documentation retrieval) may run autonomous.
2. **Expose control points for authorization, rollback, and policy enforcement** in the architecture — not as prompts, as layers (pairs `@concepts/recognition-vs-enforcement-instruction-arbitration.md`, K326).

**CCC policy — auditable trajectories:**

1. **Evaluate with evidence trees, not scalars.** Final-answer correctness is insufficient unless the supporting chain of evidence is inspectable (pairs `@concepts/agentified-eval-evidence-tree-harness.md`, K289).
2. **Maintain an evidence ledger** per claim: source, time, producing tool/model, confidence, validation status, downstream uses (pairs `@concepts/measurement-integrity-mcp-security-eval.md`, K277).
3. **Report process metrics alongside outcomes** — hallucination rate, scope containment, tool-call accuracy — not only success rate.

The K325 survey is Cybersec-primary; CCC holds the short source page + this concept. Runtime `wont_wire` — a survey wires nothing.

| Confidence | `[CONFIRMED]` — statistics read from the PDF (2026-08-31); policy is CCC synthesis |
|------------|------------|
