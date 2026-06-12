---
title: Self-Harness — harnesses that improve themselves (arXiv 2606.09498)
type: source
tags: [source, arxiv, self-harness, harness-improvement, k110]
keywords: [2606.09498, self-harness, weakness-mining, proposal-validation, terminal-bench]
related:
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/agent-harness-operational-definition.md
  - concepts/agent-completion-verification-gates.md
maturity: draft
read_status: read
created: 2026-06-11
updated: 2026-06-11
---

## Relations

- `@concepts/self-harness-model-specific-improvement-loop.md` — CCC synthesis
- `@concepts/continual-harness-online-self-improvement.md` — online harness refinement sibling
- `@concepts/retrospective-harness-optimization-rho.md` — external trajectory optimization
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix diagnosis + scoped repair
- `@concepts/agent-completion-verification-gates.md` — regression gate parallel

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Self-Harness: Harnesses That Improve Themselves |
| **Authors** | Zhang et al. (Shanghai AI Laboratory) |
| **arXiv** | 2606.09498v1 [cs.CL] |
| **Location** | `raw-sources/arxiv-2606.09498-self-harness-harnesses-that-improve-themselves.pdf` |
| **Retrieved** | 2026-06-11 |
| **Read status** | read (loop, validation rule, Terminal-Bench-2.0 results) |

## Narrative

**Self-Harness** — same fixed model improves **its own harness** (prompts, tools, verification, orchestration) without human engineers or a stronger external meta-agent. Three-stage loop:

1. **Weakness mining** — run on held-in tasks; cluster failed traces into failure patterns  
2. **Harness proposal** — K parallel minimal edits mapped to editable harness surfaces  
3. **Proposal validation** — promote only if Δheld-in ≥ 0, Δheld-out ≥ 0, and max(Δ) > 0 (no split tradeoffs)

Evaluated on Terminal-Bench-2.0 (64-case subset) with MiniMax M2.5, Qwen3.5-35B-A3B, GLM-5. Held-out pass rates: +21.4pp (MiniMax), +14.3pp (Qwen), +14.2pp (GLM) absolute.

**CCC relevance:** steal-from regression promotion rule + evidence bundle for harness flaw records; distinct from RHO (self-preference) and Bayesian-Agent (skill posteriors). No public code repo found (2026-06-11).

## Snippets

> "Unlike recent approaches that use stronger external agents to improve the harnesses of weaker ones, Self-Harness seeks to internalize this improvement loop within the target agent itself."

> "A candidate is accepted only if it improves at least one split without degrading the other."

> — [Source: arxiv-2606.09498-self-harness-harnesses-that-improve-themselves.pdf §3.4, retrieved 2026-06-11]
