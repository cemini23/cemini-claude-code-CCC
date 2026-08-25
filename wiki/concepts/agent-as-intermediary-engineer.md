---
title: "Agent as intermediary engineer — train small specialists instead of forecasting with the LLM"
type: concept
tags: [concept, time-series, meta-harness, delegation, forecasting, k308]
keywords: [metacaster, intermediary engineer, lightweight forecaster, few-shot, agentic data generation, 2608.23473]
related:
  - sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md
  - entities/tools/metacaster.md
  - entities/skills/intermediary-engineer.md
  - entities/tools/autodesign.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@sources/arxiv-metacaster-meta-harness-tsf-2608.23473.md`
- `@entities/tools/metacaster.md`
- `@entities/skills/intermediary-engineer.md`
- `@entities/tools/autodesign.md` (K281 pair)
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

Question answered: in domains where running an LLM per prediction is uneconomical, what is the agent's role? Source: arXiv 2608.23473 (CCC K308). Pairs K281 AutoDesign.

## Narrative

Two failure modes exist for LLM+time-series: LLM-as-forecaster (expensive per call, weak at numeric extrapolation) and skipping agents entirely (lightweight forecasters starve without data). MetaCaster's answer: the agent is an **intermediary engineer** — a meta-harness optimizes the agent's harness so it can generate training data, select and train a compact specialized forecaster from few examples + textual context, and hand off a deployable artifact. The optimized harness transfers across LLM providers.

Generalized principle for CCC: when a production surface needs cheap, high-frequency decisions (alerts, screeners, watchers), point the agent at **building and maintaining the small specialist**, not at serving each decision itself. Keep the meta-harness's external evaluation honest — the agent may optimize everything except the pass criteria (K281/K162).

## Snippets

> "agents act not as forecasters but as intermediary engineers that prepare efficient, task-specific forecasters for deployment" [Source: arXiv 2608.23473 abstract]
