---
title: Self-Harness — model-specific harness self-improvement loop
type: concept
tags: [concept, self-harness, harness-improvement, regression-gate, k110]
keywords: [2606.09498, weakness-mining, harness-proposal, held-out-validation]
related:
  - sources/arxiv-self-harness-improve-themselves-2606.09498.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-harness-operational-definition.md
  - concepts/harness-updating-vs-benefit-nonmonotonic.md
  - concepts/skillhone-continual-skill-decision-history.md
  - sources/arxiv-skillhone-continual-skill-evolution-2606.08671.md
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - sources/arxiv-seagym-self-evolving-harness-eval-2606.17546.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - entities/tools/areal.md
  - sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md
maturity: draft
created: 2026-06-11
updated: 2026-07-07
---

## Relations

- `@sources/arxiv-self-harness-improve-themselves-2606.09498.md` — arXiv provenance
- `@concepts/continual-harness-online-self-improvement.md` — reset-free online refinement
- `@concepts/retrospective-harness-optimization-rho.md` — unlabeled trajectory self-preference
- `@concepts/failed-trajectory-harness-repair.md` — HarnessFix scoped operators
- `@concepts/bayesian-posterior-guided-skill-evolution.md` — skill-level posteriors vs harness edits
- `@concepts/agent-completion-verification-gates.md` — held-out regression gate analogue

## Raw Concept

arXiv **2606.09498** — **Self-Harness**: fixed model proposes **bounded harness edits** to itself from verifier-grounded failure clusters, without a stronger external meta-agent.

## Narrative

### Loop (three stages)

| Stage | Input | Output |
|-------|--------|--------|
| Weakness mining | Held-in task runs + verifier | Failure pattern clusters |
| Harness proposal | Evidence bundle + current harness | K minimal edits on named surfaces |
| Proposal validation | Held-in + held-out re-eval | Promote iff no split degradation |

**Promotion rule [CONFIRMED]:** accept candidate \(h'\) only if \(\Delta_{\text{in}} \geq 0\), \(\Delta_{\text{ho}} \geq 0\), and \(\max(\Delta_{\text{in}}, \Delta_{\text{ho}}) > 0\).

### vs other harness optimizers

| Method | Who proposes | Validation |
|--------|--------------|------------|
| Human harness engineering | Human | Manual |
| Meta-Harness / RHO | External search or self-preference | Benchmark rollouts |
| HarnessFix | Diagnosis operators | Regression acceptance |
| Bayesian-Agent | Posterior on **skills** | Verified trajectories |
| **Self-Harness** | **Same model** under current harness | Held-in + held-out pass counts |

### Cemini mapping [TENTATIVE]

- Pair promotion rule with OpenSpec acceptance + `wiki_lint.py` on harness artifact edits  
- Log rejected proposals in `wiki/log.md` harness flaw records (audit lineage)  
- **REFERENCE only** — no public repo (2026-06-11); do not install until code + license appear

## Snippets

> "Self-Harness can evolve an initial harness into model-specific ones better suited to different base models."

> — [Source: arxiv-self-harness-improve-themselves-2606.09498.md, retrieved 2026-06-11]
