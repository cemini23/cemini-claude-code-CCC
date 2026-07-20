---
title: "TARS — Theory-of-Mind agent for personalized in-IDE code comprehension"
type: source
tags: [source, arxiv, vscode, theory-of-mind, personalization, rag, k192]
keywords: [2607.15948, TARS, ToM, VS Code, LangGraph, SeSa Lab, leotodisco/tars]
related:
  - concepts/theory-of-mind-personalized-agent-explanations.md
  - entities/tools/tars-vscode.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/agent-skills-progressive-disclosure.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- `@concepts/theory-of-mind-personalized-agent-explanations.md` — synthesized steal
- `@entities/tools/tars-vscode.md` — Phase-0 entity
- `@concepts/client-as-first-order-harness-factor.md` — IDE/client as harness surface (K140)
- `@concepts/agent-skills-progressive-disclosure.md` — depth adaptation peer

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | TARS: A Theory-of-Mind Agent for Personalized In-IDE Code Comprehension |
| **Author** | Leopoldo Todisco, Antonio Della Porta, Stefano Lambiase, Fabio Palomba |
| **arXiv** | 2607.15948 |
| **Pages** | 6 |
| **Retrieved** | 2026-07-20 |
| **Code** | `github.com/leotodisco/tars` — **MIT** [CONFIRMED SPDX] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.15948-tars-a-theory-of-mind-agent-for-personalized-in.pdf` |

## Narrative

### Thesis

Generic LLM explainers ignore *who* is asking and force copy-paste out of the IDE. TARS is a VS Code agent: ToM profiler (expertise, role, style) + RAG over project docs + inline decorations.

### Results [TENTATIVE — n=18 students, Java snippets]

- **26%** faster task completion vs baseline
- Lower reported cognitive load; explanations judged profile-adapted

### CCC steal

**ADOPT** the ToM profiler pattern (short quiz → store mind → adapt depth/tone). **GO** local clone for reference. Do not ship as Cursor extension without a separate Cursor-compatible port — VS Code only today.

## Snippets

> "Participants using TARS completed tasks 26% faster, reported lower cognitive load, and found the explanations meaningfully adapted to their profiles."
> — Abstract

> "Tool repository: https://github.com/leotodisco/tars"
> — Abstract
