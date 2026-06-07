---
title: Retrospective Harness Optimization (RHO) — label-free harness evolution
type: concept
tags: [concept, harness, self-improvement, arxiv, rho]
keywords: [2606.05922, rho, self-preference, dpp-coreset, group-rollout, retro-harness]
related:
  - sources/arxiv-retrospective-harness-optimization-2606.05922.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - entities/tools/retro-harness.md
  - entities/tools/openevolve.md
  - entities/tools/revfactory-harness.md
  - entities/tools/claude-mem.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - concepts/etclovg-harness-layers.md
  - concepts/rl-agent-labs-system-prompt-learning.md
maturity: draft
created: 2026-06-07
updated: 2026-06-07
---

## Relations

- `@sources/arxiv-retrospective-harness-optimization-2606.05922.md` — arXiv 2606.05922 provenance
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix: labeled diagnosis + scoped operators; RHO: unlabeled self-preference
- `@concepts/continual-harness-online-self-improvement.md` — both evolve harness from trajectories
- `@concepts/harness-updating-vs-benefit-nonmonotonic.md` — optimized harness must be followed by executor
- `@entities/tools/retro-harness.md` — MIT reference implementation
- `@entities/patterns/glasswing-deliberate-disagreement.md` — self-consistency via adversarial re-check

## Raw Concept

arXiv **2606.05922** — **RHO**: single-round, **self-supervised** harness optimization from past trajectories using DPP coreset selection, parallel group rollouts, and best-of-N **pairwise self-preference** — no ground-truth validation set.

## Narrative

### Problem

Validation-feedback harness optimizers (DSPy, TextGrad, Meta-Harness, openevolve-style search) need a labeled metric on a held-out set. Deployed agents accumulate **unlabeled trajectories** that encode failure modes — but future task distribution may not match any static validation split.

### RHO pipeline (Algorithm 1)

```text
past trajectories D + harness h₀
  → Stage 1: DPP-GREEDY coreset (difficulty × diversity, k=10, θ=0.7)
  → Stage 2: G parallel rollouts per coreset task
       → rank_val (self-validation: tool errors, false assumptions, early stop)
       → rank_con (self-consistency: plan/tool/answer disagreements)
  → Stage 3: N parallel optimize(h₀, instructions) → candidate harnesses
       → re-solve coreset with each candidate
       → Sj = mean pairwise preference vs baseline rollout
       → accept h_j* iff S_j* > 0 else keep h₀
```

Harness materialized as **workspace folder**: markdown instructions/skills + executable tool scripts (Codex agent setting).

### Results [TENTATIVE — paper claims; Codex/GPT-5.5 setting]

| Benchmark | Vanilla | RHO | Δ |
|-----------|---------|-----|---|
| SWE-Bench Pro | 0.59 | 0.78 | +0.19 |
| Terminal-Bench 2 | 0.71 | 0.76 | +0.05 |
| GAIA-2 | 0.29 | 0.37 | +0.08 |

RHO edits **Skills+Tools**; memory-only baselines gain ≤+0.05.

### vs related CCC patterns

| Method | Labels | Harness surface | Selection gate |
|--------|--------|-----------------|----------------|
| **RHO** (this page) | None | instructions + skills + tools | Self-preference Sj > 0 |
| HarnessFix | Diagnosis records | prompts, hooks, validators (ETCLOVG) | Regression-bounded acceptance |
| SkillAdaptor | Failure/success traces | skill cards in K | Qualifier gate |
| openevolve | Fitness metric | configs/prompts | Evolutionary search |
| K97 rubrics | Operator rubric | in-session behavior | Human/agent checklist |

### Cemini steal-from (no RHO prod install)

| RHO stage | CCC analogue today |
|-----------|-------------------|
| Coreset selection | Tag hard failures in `wiki/log.md` + claude-mem; diversify by ETCLOVG layer |
| Group rollout | Re-dispatch subagent 2–3× on same task spec; compare trajectories |
| Self-validation | Reviewer subagent + `cursor-audit` consensus/conflict synthesis |
| Self-consistency | `@entities/patterns/glasswing-deliberate-disagreement.md` |
| Best-of-N harness | OpenSpec branch candidates; `wiki_lint.py` + smoke test before merge |
| Accept gate (Sj > 0) | Only promote harness edit if held-out flaw class improves without new regressions |

**Verdict:** **REFERENCE** — steal label-free **self-preference over rollouts** + **accept-only-if-positive** gate. **CONDITIONAL-GO** on `@entities/tools/retro-harness.md` after isolated laptop trial.

## Phase-0 Audit (2026-06-07)

| Check | Result |
|-------|--------|
| Repo | `github.com/wbopan/retro-harness` |
| License | **MIT** [CONFIRMED via GitHub API] |
| Maturity | **0★** (new); full tree: `src/`, `tests/`, `configs/`, `pyproject.toml`, `webui` |
| Last push | 2026-06-07 |
| Failure mode | Early-release API drift; Codex-specific harness layout may not map 1:1 to Claude Code |
| vs HarnessFix install | Both NO-GO prod; RHO is **experiment** in throwaway worktree |

**Decision — CONDITIONAL-GO (laptop trial).** Run in isolated temp clone; do not wire to `~/.claude/` prod harness until smoke pass on CCC fixture trajectories.

## Snippets

> "We accept this update only if its score is strictly greater than zero (Sj > 0)."

> "RHO designs specific skills and tools targeting typical failure modes encountered in past tasks."

> — [Source: arxiv-2606.05922-retrospective-harness-optimization-improving-llm.pdf p.4–6, retrieved 2026-06-07]
