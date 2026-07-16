---
title: Agent-optimizer compounding and in-loop regression control
type: concept
tags: [concept, harness-optimization, continual-learning, regression, k171]
keywords: [2607.14004, compounding, GEPA, Meta Harness, RELAI-VCL, transfer]
related:
  - sources/arxiv-agent-optimizers-compound-continual-learning-2607.14004.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/agent-completion-verification-gates.md
  - concepts/failure-mode-harness-adaptation-mapping.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/harnessx-composable-evolution-foundry.md
  - entities/tools/relai-continual-learning-terminal-bench.md
  - sources/brief-k171-agent-optimizer-compounding-2026-07-16.md
maturity: draft
created: 2026-07-16
updated: 2026-07-16
---

## Relations

- `@sources/arxiv-agent-optimizers-compound-continual-learning-2607.14004.md` — K171 provenance
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — K169 static eval rigor sibling
- `@concepts/continual-harness-online-self-improvement.md` — continual harness cluster
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — K162 verification hierarchy
- `@concepts/agent-completion-verification-gates.md` — stop/gates for promoted harness edits

## Raw Concept

When is a second round of harness optimization safe — and what fails if regression is only checked after the fact?

## Narrative

### Steal — three questions every optimizer run must answer

1. **Static win?** Does the edit improve the current task set under matched budget (K169)?
2. **Transfer?** Does the optimized agent stay ≥ baseline on tasks **not** in the optimization set?
3. **Compound?** After folding new failures into the objective, does a second budget improve without losing Phase-1 gains?

If (2) or (3) fail, treat the method as **shortcut-prone** for Cemini prod — do not auto-promote.

### Design rule — regression inside the loop

Post-hoc eval / PR review / shadow deploy are necessary but **not sufficient**. The paper's positive case (RELAI-VCL) shapes search with regression constraints **while proposing updates**. Cemini mapping:

| Layer | Practice |
|-------|----------|
| Wiki / hooks / skills | `wiki_lint` + tests must gate harness PRs; refuse LLM-only self-score (K162) |
| Poker / TipDrop bots | Hold-out hand/alert sets across rewrite sessions; never only tune on today's failures |
| Prod agents | Prefer verifiers that can **re-run** the old suite after each harness edit |

### Verdict

**ADOPT** compounding questions + in-loop regression discipline. **REFERENCE** RELAI-VCL product/numbers (`[TENTATIVE]`). **NO-GO** clone of paper artifact repo (no LICENSE).

## Snippets

> "A one-shot benchmark score does not tell us whether an optimizer behaves well under this kind of repeated, recursive application." — §1.1
