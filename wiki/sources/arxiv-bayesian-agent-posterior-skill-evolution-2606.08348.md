---
title: Bayesian-Agent posterior-guided skill evolution (arXiv 2606.08348)
type: source
tags: [source, arxiv, bayesian-agent, skill-evolution, harness, k109]
keywords: [2606.08348, bayesian-agent, posterior, skill-evolution, sop-bench]
related:
  - concepts/bayesian-posterior-guided-skill-evolution.md
  - entities/tools/bayesian-agent.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/muse-autoskill-skill-lifecycle.md
maturity: draft
read_status: read
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@concepts/bayesian-posterior-guided-skill-evolution.md` — posterior rewrite policy synthesis
- `@entities/tools/bayesian-agent.md` — Phase-0 entity (DataArcTech repo)
- `@concepts/continual-harness-online-self-improvement.md` — online harness refinement comparison
- `@concepts/retrospective-harness-optimization-rho.md` — trajectory-based harness optimization sibling
- `@concepts/muse-autoskill-skill-lifecycle.md` — skill lifecycle without explicit posteriors

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Bayesian-Agent: Posterior-Guided Skill Evolution for LLM Agent Harnesses |
| **Authors** | Wu et al. (IDEA Research, HKUST-GZ, DataArcTech) |
| **arXiv** | 2606.08348v1 [cs.CL] |
| **Repo** | https://github.com/DataArcTech/Bayesian-Agent (MIT, ~27★, 2026-06-10) |
| **Datasets** | https://github.com/JinyiHan99/GA-Technical-Report (`datasets/sop_bench`, `lifelong_agentbench`, `realfin_benchmark`) |
| **Location** | `raw-sources/arxiv-2606.08348-bayesian-agent-posterior-guided-skill-evolution.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | read (method, backends, benchmark deltas) |

## Narrative

Treats harness **skills/SOPs as Bayesian hypotheses** under frozen model weights. Records verified trajectory evidence; maintains feature-conditioned categorical posterior per skill; maps belief to inspectable actions: **patch, split, compress, retire, explore**. **Full** mode evolves registry online; **incremental** mode repairs failed tasks from existing runs. Backends: native harness, GenericAgent, mini-swe-agent, **Claude Code**. With deepseek-v4-flash incremental repair: SOP-Bench 80%→95%, Lifelong AgentBench 90%→100%, RealFin-Bench 45%→65%.

**CCC relevance:** CONDITIONAL-GO laptop trial — posterior audit layer above skill-vetting + wiki_lint acceptance.

## Snippets

> "We introduce Bayesian-Agent, a native and cross-harness framework that treats reusable skills and SOPs as hypotheses about whether a frozen model will succeed under a particular prompt, context, and harness environment."

> "The framework includes its own minimal native harness, while GenericAgent, mini-swe-agent, and Claude Code are treated as optional backends behind the same trajectory-evidence boundary."

> — [Source: arxiv-2606.08348-bayesian-agent-posterior-guided-skill-evolution.pdf §1, retrieved 2026-06-10]
