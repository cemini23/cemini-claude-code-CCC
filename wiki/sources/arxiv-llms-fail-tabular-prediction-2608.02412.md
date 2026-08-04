---
title: "Why LLMs Fail at Tabular Prediction"
type: source
tags: [source, arxiv, tabular, prediction, llm, k241]
keywords: [2608.02412, Garnelo, Czarnecki, dimensionality, CSV]
related:
  - concepts/llm-tabular-prediction-dimensionality-failure.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
maturity: draft
created: 2026-08-04
updated: 2026-08-04
---

## Relations

- `@concepts/llm-tabular-prediction-dimensionality-failure.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Why LLMs Fail at Tabular Prediction |
| **Authors** | Marta Garnelo, Wojciech M. Czarnecki |
| **arXiv** | 2608.02412 |
| **Code** | No code artifact required |
| **Retrieved** | 2026-08-04 |

## Narrative

Controlled study: pure single-pass LLM over CSV prompt. Falsifies noise/format/tokenization/batch-size hypotheses. **Dimensionality** decisive — LLM accuracy falls as dimension grows while classical baselines flat/improve. In 2D behaves like local distance method; higher-D unmatched by classical+noise.

| Verdict | **ADOPT** policy — do not use raw LLM single-pass for tabular predictive analytics; prefer classical / tabular foundation models / tools. Concept-only (no entity). |
