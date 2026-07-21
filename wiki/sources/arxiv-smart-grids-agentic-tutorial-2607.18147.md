---
title: "LLMs and agentic AI for smart grids — solver-grounded tutorial (energy OOD)"
type: source
tags: [source, arxiv, survey, smart-grid, solver-grounded, verification, k199]
keywords: [2607.18147, solver-grounded, UCSD, power systems, CVXPY]
related:
  - concepts/solver-grounded-agent-numerics.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/agent-completion-verification-gates.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- `@concepts/solver-grounded-agent-numerics.md` — CCC steal (energy body OOD)
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — verification hierarchy peer
- `@concepts/agent-completion-verification-gates.md` — completion gates peer
- Prefer brief/concept over deep energy pages

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LLMs and Agentic AI Systems for Smart Grids: A Tutorial on Architectures and Applications |
| **Author** | Daniela Rojas et al. (UCSD / Alberta) |
| **arXiv** | 2607.18147 |
| **Pages** | 33 |
| **Retrieved** | 2026-07-21 |
| **Code** | `d2rojas/LLMs-Agents-For-SmartGrids-Code` — **no SPDX** → **NO-GO** install |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.18147-llms-and-agentic-ai-systems-for-smart-grids-a-tu.pdf` |

## Narrative

**Solver-grounded design:** report a numerical result only when it originates from a trusted tool and passes explicit verification. Four case studies (forecasting, EV scheduling, power flow, contingency) show LLM-as-interface + solver-as-truth beats LLM-as-computer.

**CCC routing:** keep the principle; do not deepen smart-grid content here. Case-study repo lacks LICENSE — pattern only.

## Snippets

> "a numerical result is reported only when it originates from a trusted tool and passes explicit verification"
> — Abstract / design principle
