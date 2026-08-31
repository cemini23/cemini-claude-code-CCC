---
title: "LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment (CCC K325)"
type: source
tags: [source, arxiv, survey, security, agents, bounded-authority, auditability, k325]
keywords: [2608.28490, systematic literature review, SLR, security agents, bounded authority, auditable trajectories, evidence-centered, risk-aware autonomy]
related:
  - concepts/bounded-authority-auditable-trajectories.md
  - concepts/execution-fidelity-irreversible-agent-invariants.md
  - concepts/agentified-eval-evidence-tree-harness.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - briefs/2026-08-31_ccc-k325-k327-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-31
updated: 2026-08-31
---

## Relations

- `@concepts/bounded-authority-auditable-trajectories.md`
- `@concepts/execution-fidelity-irreversible-agent-invariants.md`
- `@concepts/agentified-eval-evidence-tree-harness.md`
- `@concepts/measurement-integrity-mcp-security-eval.md`
- `@briefs/2026-08-31_ccc-k325-k327-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LLM-Based Agents for Software and Systems Security: Approaches, Applications, and Assessment |
| **arXiv** | 2608.28490 (cs.CR, 2026-08-28) |
| **Authors** | Jingjing Nie, Jiawei Guo, Krishna Meda, Haipeng Cai (University at Buffalo, SUNY) |
| **Venue** | ACM manuscript (submitted), 72 pages |
| **Code** | None (survey) — Phase-0 SPDX hunt: no repo |
| **Retrieved** | 2026-08-31 |

## Narrative

**Verdict: Cybersec-primary — CCC steal is the bounded-authority / auditable-trajectories gap.** This is a short CCC page, not a 72-page survey dump. The paper is a systematic literature review of 100 peer-reviewed papers (Jan 2023 – Mar 2026) on LLM-based agents for software and systems security, organized along three axes: **Approach** (architecture, perception, memory, reasoning/planning, action space, orchestration, self-improvement), **Application** (security tasks served), and **Assessment** (datasets, outcome + trajectory metrics, safety measures, baselines).

Central synthesis — the field has built agents that **act** but not yet agents whose **authority is bounded** or whose **behavior is auditable**:

- **Built to act:** 91% adopt a modular pipeline; 88% place the backbone LLM in a planner-and-actor role; 95% support fully autonomous operation.
- **Rarely bounded or inspected:** explicit critic/verifier roles in 15%; guardrail layers in 13%; any human review point in 13%.
- **Outcome measures routine, process measures not:** success/completion in 51%; precision/recall/F1 in 34% — vs hallucination rate 11%, scope containment 5%, tool-call accuracy 1% (despite nearly every surveyed system being tool-using).
- Applications concentrate on the vulnerability lifecycle and offensive assessment; post-access phases, low-level artifact analysis, and governance tasks (access-control review, supply-chain security) are underdeveloped.

Future directions named by the survey: **evidence-centered architecture** (explicit evidence graphs/ledgers recording source, time, producing tool/model, confidence, validation status, downstream uses), **risk-aware autonomy levels** (low/medium/high-risk tasks with HITL for exploit execution, production remediation, disclosure, active response), and **realistic + reproducible + safe benchmark ecosystems** (executable instrumented environments, not static datasets).

CCC adoption: keep HITL on irreversible tools (pairs K239); evaluate with evidence trees, not scalars (pairs K289); treat bounded authority + auditable trajectories as the design gap for any security agent (pairs K277 measurement integrity). Runtime `wont_wire` — this is a survey, nothing to wire. **No exploit/PoC content in this page.**

| Confidence | `[CONFIRMED]` — survey synthesis over 100 papers; quoted statistics read from the PDF |
|------------|------------|

## Snippets

> "The field has built agents able to act but not yet agents whose authority is bounded or whose behavior is auditable." [Source: arXiv 2608.28490 abstract]

> "Agents are built to act: 91% adopt a modular pipeline, 88% place the backbone LLM in a planner-and-actor role, and 95% support fully autonomous operation. They are far less often built to be bounded or inspected: explicit critic or verifier roles appear in 15% of systems, guardrail layers in 13%, and any human review point in 13%." [Source: arXiv 2608.28490 §9 Conclusion]

> "Outcome measures are routine — success or completion in 51% of papers, precision/recall/F1 in 34% — while the measures that would expose *how* an outcome was reached are not: hallucination rate appears in 11%, scope containment in 5%, and tool-call accuracy in 1%." [Source: arXiv 2608.28490 §9 Conclusion]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.28490-llm-based-agents-for-software-and-systems-securi.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
