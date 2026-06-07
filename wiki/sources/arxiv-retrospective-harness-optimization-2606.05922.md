---
title: Retrospective Harness Optimization — RHO (arXiv 2606.05922)
type: source
tags: [source, arxiv, harness, self-improvement, rho, microsoft]
keywords: [2606.05922, rho, retrospective-harness, self-preference, retro-harness]
related:
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/code-as-agent-harness.md
  - concepts/agent-rubrics-self-correction.md
  - entities/tools/retro-harness.md
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - concepts/self-healing-agent-sessions.md
  - concepts/etclovg-harness-layers.md
maturity: draft
read_status: read
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- `@concepts/retrospective-harness-optimization-rho.md` — CCC synthesis
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix uses labeled diagnosis; RHO uses unlabeled self-preference
- `@concepts/continual-harness-online-self-improvement.md` — continual harness peer
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — executor must follow harness deltas
- `@entities/tools/retro-harness.md` — reference implementation

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Retrospective Harness Optimization: Improving LLM Agents via Self-Preference over Trajectory Rollouts |
| **Authors** | Wenbo Pan, Shujie Liu, Chin-Yew Lin, Jingying Zeng, Xianfeng Tang, Xiangyang Zhou, Yan Lu, Xiaohua Jia |
| **Affiliation** | City University of Hong Kong; Microsoft Research Asia |
| **arXiv** | 2606.05922v1 [cs.AI] |
| **Code** | https://github.com/wbopan/retro-harness |
| **Project** | https://paper-rho.wenbo.io |
| **Location** | `raw-sources/arxiv-2606.05922-retrospective-harness-optimization-improving-llm.pdf` |
| **Retrieved** | 2026-06-07 |
| **Read status** | read (abstract, method, benchmarks, ablations) |

## Narrative

**RHO** optimizes the **full agent harness** (instructions, skills, executable tools) from **unlabeled past trajectories** — no validation-set grading. Three stages: (1) **DPP coreset** — difficulty-diverse subset of past tasks (θ=0.7, k=10); (2) **group rollout** — G parallel re-solves per coreset task, extracting **self-validation** (within-trajectory faults) and **self-consistency** (cross-trajectory disagreements); (3) **best-of-N harness proposal** — N candidate harnesses, pairwise **self-preference** vs baseline rollouts, accept iff aggregate score Sj > 0.

Evaluated on Codex agent (GPT-5.5, high reasoning). Held-out pass rates after one RHO round vs Vanilla Codex: SWE-Bench Pro **0.59→0.78** (+19), Terminal-Bench 2 **0.71→0.76**, GAIA-2 **0.29→0.37**. Beats memory-only baselines (Dynamic Cheatsheet, ReasoningBank, Sleep-time Compute). Optimized harnesses add domain-specific tools/skills targeting prior failure modes (e.g. `check_build_and_lint`, diff-hygiene skills).

**CCC relevance:** label-free harness evolution from session logs — complements HarnessFix (diagnosis-first repair) and SkillAdaptor (skill-card-only edits).

## Snippets

> "RHO departs from this paradigm, requiring no validation feedback and improving the harness in a single retrospective pass over unlabeled past trajectories."

> "By running a single round of retrospective harness optimization on software-engineering trajectories, we improve the pass rate on SWE-Bench Pro from 59% to 78%, without depending on grading against a validation set."

> "RHO instead optimizes the full harness, including executable tools and instructions, rather than memory alone."

> — [Source: arxiv-2606.05922-retrospective-harness-optimization-improving-llm.pdf p.1–6, retrieved 2026-06-07]
