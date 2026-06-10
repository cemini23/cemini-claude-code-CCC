---
title: Bayesian posterior-guided skill evolution — harness-side belief over skills
type: concept
tags: [concept, bayesian-agent, skill-evolution, harness, k109]
keywords: [2606.08348, posterior, patch-split-compress-retire, incremental-repair]
related:
  - sources/arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md
  - entities/tools/bayesian-agent.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/muse-autoskill-skill-lifecycle.md
  - concepts/skilladaptor-step-level-skill-adaptation.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/skill-vetting.md
maturity: draft
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@sources/arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md` — paper + benchmark deltas
- `@entities/tools/bayesian-agent.md` — DataArcTech reference implementation
- `@concepts/continual-harness-online-self-improvement.md` — reset-free harness refinement
- `@concepts/retrospective-harness-optimization-rho.md` — trajectory-based harness optimization (frequentist preference)
- `@concepts/muse-autoskill-skill-lifecycle.md` — skill lifecycle without explicit posteriors

## Raw Concept

arXiv **2606.08348** — treat harness **skills/SOPs as hypotheses**; maintain categorical posterior from **verified** trajectories; rewrite via **patch / split / compress / retire / explore**.

## Narrative

Frozen model \(M_\theta\); inference environment \(C_t\) (prompt, tools, memory, verifier). Skill \(h_k\) reliability:

\[
p_{k,t} = P(y_t=1 \mid M_\theta, C_t, h_k, z_t)
\]

where \(z_t\) features extracted from verified trajectory \(e_t\).

**Modes:**

| Mode | Behavior |
|------|----------|
| **full** | Evolve skill registry online from scratch |
| **incremental** | Import existing run; repair failed tasks only |

**Backends:** native harness, GenericAgent, mini-swe-agent, **Claude Code** — shared trajectory-evidence boundary.

### vs RHO / Continual Harness

| Approach | Evidence | Decision |
|----------|----------|----------|
| RHO | DPP coreset + self-preference | Best-of-N harness proposal |
| Continual Harness | Trajectory refiner | Reset-free prompt/skill updates |
| Bayesian-Agent | Categorical posterior per skill | Auditable patch/split/retire policy |

### Cemini mapping [TENTATIVE]

Posterior audit layer above `@concepts/skill-vetting.md` Phase-0 — rank which installed skills to patch vs retire from `wiki/log.md` harness flaw records. Laptop trial via `@entities/tools/bayesian-agent.md`.

## Snippets

> "Skill evolution is best viewed as posterior-guided harness optimization rather than uncalibrated prompt accumulation."

> — [Source: arxiv-bayesian-agent-posterior-skill-evolution-2606.08348.md §1, retrieved 2026-06-10]
