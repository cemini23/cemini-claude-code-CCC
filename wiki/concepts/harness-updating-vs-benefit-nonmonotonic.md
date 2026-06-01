---
title: Harness updating vs harness benefit — non-monotonic agent gains
type: concept
tags: [concept, agent-harness, arxiv, k93]
keywords: [harness-updating, harness-benefit, 2605.30621, evolver, executor]
related:
  - sources/arxiv-harness-updating-not-benefit-2605.30621.md
  - sources/arxiv-continual-harness-self-improving-agents-2605.09998.md
  - concepts/thin-harness-fat-skills-garrytan.md
  - concepts/continual-harness-online-self-improvement.md
  - entities/tools/revfactory-harness.md
  - concepts/subagent-orchestration.md
  - sources/trading-posts-compilation-31-2026-06-01.md
maturity: draft
created: 2026-06-01
updated: 2026-06-01
cross-wiki-source: "@osint-wiki/concepts/harness-updating-vs-benefit-nonmonotonic.md"
---

## Relations

- `@sources/arxiv-harness-updating-not-benefit-2605.30621.md` — primary paper (K93)
- `@sources/arxiv-continual-harness-self-improving-agents-2605.09998.md` — K72 related harness paper
- `@concepts/thin-harness-fat-skills-garrytan.md` — garrytan thread (Posts K93)
- `@concepts/continual-harness-online-self-improvement.md` — prior continual-harness concept
- `@entities/tools/revfactory-harness.md` — harness generator tool
- `@osint-wiki/concepts/harness-updating-vs-benefit-nonmonotonic.md` — OSINT canon

## Raw Concept

arXiv:2605.30621 — separate **harness-updating** (writing good deltas) from **harness-benefit** (using them on tasks). Benefit peaks mid-tier models **`[TENTATIVE]`** — paper claims; not replicated in Cemini prod.

## Narrative

**Design rules for CCC:**

1. Smaller model can run overnight harness mutation; do not default to Opus for evolver only.
2. Executor must **activate** skills/rules — weak-tier failure is usage, not edit quality.
3. Score live task **benefit**, not edit eloquence alone.

**Verdict:** **REFERENCE** — informs harness adoption (revfactory-harness, agents-best-practices cherry-pick).

## Snippets

> "Investing capability budget in the task-solving agent rather than the evolver."
> — [Source: arXiv 2605.30621 via @osint-wiki/sources/arxiv-harness-updating-not-benefit-2605.30621.md]
