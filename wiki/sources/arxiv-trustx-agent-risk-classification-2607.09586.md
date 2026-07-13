---
title: TrustX ARC — Agent Risk Classification Framework (2607.09586)
type: source
tags: [source, arxiv, governance, risk, classification, k157]
keywords: [2607.09586, trustx, arc, agent risk classification, twelve dimensions, gpa, iat, coding assistant]
related:
  - concepts/trustx-agent-risk-classification.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - entities/patterns/tier1-tier2-agent-model.md
  - sources/brief-k157-trustx-agent-risk-classification-2026-07-13.md
  - concepts/skill-vetting.md
maturity: draft
read_status: read
created: 2026-07-13
updated: 2026-07-13
phase_0_verdict: "REFERENCE 2026-07-13 — Responsible AI Institute framework paper; interactive tool at responsible.ai; no installable repo; adopt risk-tier rubric + coding-assistant extension"
---

## Relations

- `@concepts/trustx-agent-risk-classification.md` — CCC synthesis
- `@concepts/cage-1-enterprise-agent-governance-eval.md` — complementary (CAGE-1 Prebind vs ARC tiering)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems |
| **Author** | Hannah Liu — Responsible AI Institute |
| **arXiv** | 2607.09586 (Jul 2026) |
| **Tool** | Interactive framework at [responsible.ai/trustx](https://www.responsible.ai/trustx/) — not open-source repo |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.09586-trustx-agent-risk-classification-framework-arc-r.pdf` |
| **Retrieved** | 2026-07-13 |

## Narrative

ARC classifies **internally created** agentic AI into governance tiers using:

- **12-dimension risk scoring rubric** (critical-dimension approach — high risks not averaged away)
- **GPA + IAT** agent model (Goal/Perception/Action + Iteration/Adaptation/Termination)
- **5-level autonomy** framework (Bommarito, Feng)
- **3-tier output:** Low / Medium / High + mapped controls
- **7 agent types** (autonomous, coding assistant, deep research, …)
- **Coding Assistant extension** — Claude Code-class nuance

Aligns with NIST AI RMF, ISO 42001, EU AI Act references in paper.

| Verdict | **REFERENCE** — adopt tiering checklist; pair with K151 Prebind for prod-touching agents |

## Snippets

> "Twelve-dimension risk scoring rubric … combined with GPA + IAT classification model … three-tier governance output with mapped control recommendations."
> — [Source: arxiv-2607.09586 abstract, retrieved 2026-07-13]
