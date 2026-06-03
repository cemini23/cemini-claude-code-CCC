---
title: Runtime harness adaptation (LIFE-HARNESS) — arXiv 2605.22166
type: source
tags: [source, arxiv, agent-harness, k95]
keywords: [2605.22166, life-harness, runtime-harness, interface-adaptation, frozen-llm]
related:
  - concepts/runtime-harness-interface-adaptation.md
  - concepts/code-as-agent-harness.md
  - concepts/system-scaling-harness-agentic-ai.md
  - entities/tools/life-harness.md
maturity: draft
read_status: skimmed
created: 2026-06-03
updated: 2026-06-03
---

## Relations

- `@concepts/runtime-harness-interface-adaptation.md` — CCC synthesis
- `@concepts/code-as-agent-harness.md` — three-layer harness mapping
- `@entities/tools/life-harness.md` — upstream code artifact

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents |
| **Author** | Tianshi Xu, Huifeng Wen, Meng Li (Peking University) |
| **arXiv** | 2605.22166 |
| **Retrieved** | 2026-06-03 |
| **Read status** | skimmed |
| **Location** | `raw-sources/arxiv-2605.22166-adapting-the-interface-not-the-model-runtime-har.pdf` |
| **Code** | LIFE-HARNESS (GitHub — see paper) |

## Narrative

Proposes **LIFE-HARNESS**: evolve the runtime harness (environment contracts, procedural skills, action realization, trajectory regulation) from training trajectories while **keeping LLM weights fixed**. Targets deterministic, rule-governed agent benchmarks (τ-bench, τ²-bench, AgentBench). Claims 88.5% average relative improvement across 126 model–environment settings; harnesses trained on one backbone transfer to 17 other models — evidence that interface-side structure is reusable.

## Snippets

> "Many failures in deterministic, rule-governed domains stem from mismatches at the model–environment interface."
> — [Source: arxiv-2605.22166-adapting-the-interface-not-the-model-runtime-har.pdf p.1]

> "LIFE-HARNESS keeps LLM weights fixed and evolves reusable interface interventions from training trajectories."
> — [Source: arxiv-2605.22166-adapting-the-interface-not-the-model-runtime-har.pdf p.1]
