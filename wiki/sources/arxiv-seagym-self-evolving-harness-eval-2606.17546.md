---
title: SEAGym — evaluation environment for self-evolving harness (arXiv 2606.17546)
type: source
tags: [source, arxiv, seagym, harness-eval, self-evolving, k117]
keywords: [2606.17546, seagym, harbor, terminal-bench, replay]
related:
  - concepts/seagym-self-evolving-harness-evaluation.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/agent-completion-verification-gates.md
  - concepts/harnessx-composable-evolution-foundry.md
maturity: draft
read_status: read
created: 2026-06-17
updated: 2026-06-17
---

## Relations

- `@concepts/seagym-self-evolving-harness-evaluation.md` — CCC synthesis
- `@concepts/continual-harness-online-self-improvement.md` — harness refinement peer
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — regression/non-monotonic updates
- `@concepts/self-harness-model-specific-improvement-loop.md` — self-harness eval gap

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SEAGym: An Evaluation Environment for Self-Evolving LLM Agents |
| **Authors** | Zheng et al. (Tsinghua) |
| **arXiv** | 2606.17546v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.17546-seagym-an-evaluation-environment-for-self-evolvi.pdf` |
| **Retrieved** | 2026-06-17 |
| **Read status** | read (eval views, Harbor integration, methods compared) |

## Narrative

**SEAGym** evaluates **harness updates** (prompts, memory, tools, middleware, runtime state) — not just final task scores.

**Eval views:** train batches, frozen update-validation, held-out ID/OOD transfer, **replay diagnostics**, snapshot + metric records, cost tracking.

Built on **Harbor** containerized task framework. Converts static benchmarks → dynamic self-evolution task sources. Schedule params: state reset, task reuse, batch size, update timing (single-task, online transfer, epoch batch).

**Instantiated on:** Terminal-Bench 2.0 + HLE. Compares **ACE**, **TF-GRPO**, **AHE** under shared epoch/batch protocol.

**Findings:** frequent updates may fail held-out; useful snapshots may collapse later; source diversity and model backend affect harness reliability.

**Code:** no public repo found (2026-06-17).

## Snippets

> "A self-evolving agent uses task experience to update persistent harness state, and reuses the updated state on later tasks."

> "SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics."
