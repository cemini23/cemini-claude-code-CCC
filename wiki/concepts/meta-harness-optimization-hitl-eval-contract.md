---
title: "Meta-harness optimization with HITL / external eval contract (K281)"
type: concept
tags: [concept, meta-harness, self-improving, eval-contract, hitl, k281]
keywords: [2608.13560, AutoDesign, DesignHarness, PosterBench, meta-harness-optimizer, rollout-feedback, no-closed-self-rewrite, k162]
related:
  - sources/arxiv-autodesign-meta-harness-2608.13560.md
  - entities/tools/autodesign.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/brief-k162-rsi-verification-hierarchy-2026-07-14.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - sources/brief-k277-k281-trust-verification-wave-2026-08-14.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/phase1-adopt-wire.md
  - sources/brief-k237-meta-harness-vero-misevolution-2026-08-14.md
  - concepts/black-box-rl-opaque-harness-optimization.md
  - concepts/harness-continual-learning-guarded-evolution.md
  - concepts/task-conditioned-meta-agent-orchestration-eureka.md
  - sources/arxiv-eureka-meta-agent-orchestration-2608.19047.md
  - sources/arxiv-harness-continual-learning-2608.19013.md
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - entities/tools/task-coevolve.md
  - sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md
maturity: draft
created: 2026-08-14
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-autodesign-meta-harness-2608.13560.md`
- `@entities/tools/autodesign.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`

## Raw Concept

A meta-harness optimizer recursively improves the harness from rollout feedback — **but who owns the pass criteria?** If the optimizer can rewrite its own eval contract, improvement is unmeasurable.

## Narrative

AutoDesign: a **meta-harness optimizer guides a code agent to recursively improve the harness** based on rollout feedback, aligned with human design priors. Concrete win on paper-to-poster: learned **DesignHarness** lifts avg PosterBench Score 54.99 → 67.39 (+12.4%) across seven code-agent×model configs; 78.32 vs 70.87 for Claude Design; fully autonomous loop 253 tool calls / 11 editing turns / 40 min / <$3.

### Steal (ADOPT — with the HITL guardrail)

1. **Meta-harness loop over the harness, not the model** — improve the DesignHarness (workflow, prompts, tool ordering), keep the code agent fixed. Harness gains transfer across model configs (+12.4% avg).
2. **Five-component harness audit** (board K237): Context & Memory / Tools & Specs / Execution Runtime / Orchestration / Eval & Feedback — map skills, hooks, MCP, session loop onto those slots.
3. **Rollout feedback as the optimizer's signal** — score + trajectory → harness edits. Recursive but *bounded* improvement. Propose one bounded update per iteration; promote only when train improves **and** hidden-dev does not regress.
4. **External eval contract / HITL (the guardrail, pairs K162).** Pass criteria must NOT be closed self-rewritten by the optimizer. Keep human design priors and an external scoring authority authoritative; the optimizer improves *within* the contract.
5. **Human-aligned priors** — the harness starts from human design priors, not a blank slate. HITL redirection on plateau (brief: autonomous 80.88 → 88.39 with an NL nudge).

### Why this pairs K162

K162's RSI verification hierarchy warns against closed self-eval loops (self-judge without external verification). AutoDesign demonstrates the *effective* version: meta-optimization works **when the eval contract is external** (PosterBench scoring + human study). Without that contract, a self-rewriting pass criterion is the failure mode to ban. `[NEEDS VERIFICATION 2026-08-14]` — the paper reports the external contract; whether the shipped harness enforces it at runtime is not audited in the paper.

### Local adopt

`Yaxin9Luo/AutoDesign` — LICENSE file **MIT** (verify on disk; gh API NOASSERTION). Clone to `.local/adopts/AutoDesign` if repo <500MB (GitHub size ~43MB). Poster/Image-gen runtime **`wont_wire`**.

| Verdict | **Steal** meta-harness loop WITH HITL / external eval contract (pairs K162). Clone if SPDX-clean <500MB; runtime `wont_wire`. |
