---
title: SEAGym — self-evolving harness evaluation environment
type: concept
tags: [concept, harness-eval, self-evolving, seagym, k117]
keywords: [2606.17546, seagym, replay, harbor, forgetting]
related:
  - sources/arxiv-seagym-self-evolving-harness-eval-2606.17546.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/agent-completion-verification-gates.md
  - concepts/gatekeeper-layered-agent-evaluation.md
maturity: draft
created: 2026-06-17
updated: 2026-06-21
---

## Relations

- `@sources/arxiv-seagym-self-evolving-harness-eval-2606.17546.md` — Tsinghua paper
- `@concepts/continual-harness-online-self-improvement.md` — online harness refinement
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — non-monotonic harness benefit
- `@concepts/self-harness-model-specific-improvement-loop.md` — held-in/held-out harness promotion
- `@concepts/harnessx-composable-evolution-foundry.md` — harness evolution with seesaw gate
- `@concepts/agent-completion-verification-gates.md` — verifier-backed eval views

## Raw Concept

How do we evaluate harness self-evolution beyond a single final accuracy number?

## Narrative

**SEAGym eval checklist** [TENTATIVE — 2606.17546] for CCC harness changes (skills, hooks, prompts):

| View | Question |
|------|----------|
| Train batches | Does update learn from batch? |
| Frozen validation | Held-out during update window |
| ID / OOD transfer | Generalizes beyond source tasks? |
| **Replay** | Old tasks regress after update? |
| Cost / snapshots | Token spend + intermediate checkpoint quality |

**Findings to internalize:** frequent harness edits can hurt held-out; good intermediate snapshots may collapse; replay diagnostics catch forgetting static benchmarks miss.

**CCC mapping:** apply replay view when promoting harness edits from Self-Harness / HarnessX / Bayesian-Agent — re-run prior `wiki_lint.py` + sample ingest smoke after each harness promotion.

**Harbor dependency:** builds on Harbor containerized eval — REFERENCE until SEAGym repo ships.

**Verdict:** REFERENCE eval methodology; steal replay + OOD transfer for harness flaw records.

## Snippets

> "Evaluating self-evolution requires more than reporting whether a final agent scores higher on a task set."

> "Useful intermediate snapshots may collapse later."
