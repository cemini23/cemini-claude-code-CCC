---
title: LLM tabular prediction fails at high dimensionality (K241)
type: concept
tags: [concept, tabular, prediction, llm, dimensionality, k241]
keywords: [2608.02412, Garnelo, Czarnecki, CSV, single-pass, classical baselines]
related:
  - sources/arxiv-llms-fail-tabular-prediction-2608.02412.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
  - concepts/geospatial-computation-vs-parametric-knowledge.md
  - sources/arxiv-multiglobeqa-geospatial-reasoning-2608.03882.md
  - entities/tools/multiglobeqa.md
maturity: draft
created: 2026-08-04
updated: 2026-08-05
---

## Relations

- `@sources/arxiv-llms-fail-tabular-prediction-2608.02412.md` — K241 provenance

## Raw Concept

When should operators refuse raw single-pass LLM tabular prediction in favor of classical or tabular-specialized tools?

## Narrative

K241 (arXiv **2608.02412**, Garnelo & Czarnecki): controlled study of pure single-pass LLM over CSV prompts.

### Findings

- Falsifies noise, format, tokenization, and batch-size as primary drivers
- **Dimensionality** decisive: LLM accuracy falls as dimension grows; classical baselines flat or improve
- 2D: LLM behaves like local distance method
- Higher-D: LLM unmatched even by classical+noise

### Cemini policy (ADOPT)

| Do | Don't |
|----|-------|
| Classical ML / stats for tabular predictive analytics | Raw LLM single-pass CSV prediction for high-D tasks |
| Tabular foundation models where appropriate | Assume LLM "understands" spreadsheet structure |

| Verdict | **ADOPT** policy. Concept-only — no entity install. |

### K246 — computation not knowledge (2026-08-05)

MultiGlobeQA generalizes the K241 theme: even with gold facts, geospatial QA plateaus because **computation** (grid indexing, shape) fails — not missing parametric knowledge. See `@concepts/geospatial-computation-vs-parametric-knowledge.md`.

## Dead Ends

- **Prompt-engineering around dimensionality** — paper shows structural failure, not formatting fix
