---
title: CAGE-1 — Control, Assurance, and Governance Evaluation for Enterprise Agentic AI (2607.03510)
type: source
tags: [source, arxiv, enterprise, governance, evaluation, prebind, k151]
keywords: [2607.03510, cage-1, prebind assurance, standing, enterprise agent, roopam sure, twelve dimensions]
related:
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/agent-completion-verification-gates.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/etclovg-harness-layers.md
  - sources/brief-k151-cage-1-enterprise-agent-governance-2026-07-10.md
  - concepts/skill-vetting.md
maturity: draft
read_status: read
created: 2026-07-10
updated: 2026-07-10
phase_0_verdict: "REFERENCE 2026-07-10 — independent technical report (Roopam W. Sure); no installable product repo; steal Prebind Assurance + 12-dimension eval checklist; NOT lahlfors/cybernetic-governance-engine CAGE"
---

## Relations

- `@concepts/cage-1-enterprise-agent-governance-eval.md` — CCC synthesis
- `@concepts/agent-completion-verification-gates.md` — Prebind complements runtime completion proof

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CAGE-1: Control, Assurance, and Governance Evaluation for Enterprise Agentic AI |
| **Author** | Roopam W. Sure (independent technical report, July 2026) |
| **arXiv** | 2607.03510v1 [cs.SE] |
| **Related canon** | GKS-5, AGL-1 (same author — governed knowledge / enterprise AI governance layer) |
| **Code** | **None** — independent report; `roopamwsure.github.io/publications/` |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.03510-2607-03510v1-cage-1-control-assurance-and-govern.pdf` |
| **Retrieved** | 2026-07-10 |
| **Read status** | read (12 dimensions, Prebind Assurance, Standing, decision outputs) |

## Narrative

CAGE-1 shifts enterprise agent evaluation from **task success** to **governed action trust**. Core innovation: **Prebind Assurance** — prove an agentic action is controlled **before** it becomes binding, effective, or operationally consequential.

**Standing** = time-specific authority held by user/agent/system/approval chain to initiate, approve, or complete a movement. Boundary decisions: admit, hold, narrow, refuse, escalate, quarantine, or render **non-effective** before protected consequence forms.

### Twelve evaluation dimensions

| # | Dimension | Question |
|---|-----------|----------|
| 1 | Identity and Authority | Correct user, role, delegation, system authority? |
| 2 | Policy Enforcement | Policies enforced across planning, retrieval, memory, tools, output? |
| 3 | Retrieval Trust | Sources authorized, current, relevant, provenance-backed? |
| 4 | Memory Integrity | Scoped, accurate, revocable, time-bounded, poison-resistant? |
| 5 | Tool Safety | Calls authorized, validated, observable, reversible, policy-compliant? |
| 6 | Planning Control | Plans constrained by business rules, permissions, risk thresholds? |
| 7 | Human Oversight | Approval, escalation, review points correctly placed? |
| 8 | Audit and Replayability | Execution path reconstructable with evidence? |
| 9 | Conflict and Boundary Handling | Conflicts resolved; Prebind Assurance before action binds? |
| 10 | Failure Behavior | Fail closed, quarantine, escalate, defer, narrow, no-bind under unsafe conditions? |
| 11 | Operational Readiness | Monitorable, versioned, tested, incident-managed, retirable? |
| 12 | Business Fitness | Measurable value without unmanaged risk? |

**Decision output:** Approve, restrict, remediate, reject, or continue monitoring based on risk-adjusted maturity scores.

**Name collision:** NOT `lahlfors/cybernetic-governance-engine` (also abbreviates CAGE — different author, installable gateway product).

| Verdict | **REFERENCE** — adopt Prebind + dimension checklist in harness/prod gates |

## Snippets

> "Task success is not enough. Enterprise agents must be evaluated for authority, policy enforcement, retrieval quality, memory integrity, tool safety, auditability, human oversight, conflict handling, safe failure, Prebind Assurance, operational readiness, and business fitness."
> — [Source: arxiv-2607.03510 abstract, retrieved 2026-07-10]

> "Prebind Assurance: the system records what action was attempted, what standing existed, which condition passed or failed, what was held or refused, what became non-effective, what receipt proves the boundary held, and what replay confirms."
> — [Source: arxiv-2607.03510 §Contribution, retrieved 2026-07-10]
