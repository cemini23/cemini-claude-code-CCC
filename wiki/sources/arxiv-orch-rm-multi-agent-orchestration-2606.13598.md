---
title: Orch-RM — orchestration reward modeling for MAS (arXiv 2606.13598)
type: source
tags: [source, arxiv, orch-rm, multi-agent, reward-model, k116]
keywords: [2606.13598, orch-rm, mas-orchestra, bradley-terry, best-of-n]
related:
  - concepts/orchestration-reward-modeling-orch-rm.md
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - concepts/agent-rubrics-self-correction.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- `@concepts/orchestration-reward-modeling-orch-rm.md` — CCC synthesis
- `@concepts/subagent-orchestration.md` — MAS orchestration target
- `@entities/tools/conductor-mcp.md` — federation orchestrator analogue
- `@concepts/agent-rubrics-self-correction.md` — reward-guided selection parallel

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Reward Modeling for Multi-Agent Orchestration |
| **Authors** | Tsang et al. (Rutgers); Ke, Joty, Yavuz (Salesforce AI Research) |
| **arXiv** | 2606.13598v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.13598-2606-13598v1-reward-modeling-for-multi-agent-orc.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (self-supervised pairs, BoN, continued training) |

## Narrative

**Orch-RM (Orchestration Reward Modeling)** — self-supervised Bradley-Terry reward model for **orchestration quality** without human labels. Builds win-lose pairs from intermediate MAS-Orchestra checkpoints and trajectories via multi-faceted grouping.

Operates at **orchestration level** (not full sub-agent rollout scoring) → ~**10×** fewer tokens vs rollout-based training; up to **~8%** accuracy gain on test-time scaling vs baselines.

**Uses:**

1. **Inference:** best-of-N (BoN) rollout selection beats majority voting
2. **Training:** reward-guided continued orchestrator training improves MAS-Orchestra checkpoint; scratch training approaches RL teacher

Domains: math reasoning, web QA, multi-hop reasoning.

**Code:** promised at `github.com/Wang-ML-Lab/OrchRM` — **404** on GitHub 2026-06-16 [NEEDS VERIFICATION 2026-06-16].

## Snippets

> "Orch-RM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling."

> "Intermediate artifacts from MAS-Orchestra training … construct diverse win-lose pairs of orchestration trajectories."
