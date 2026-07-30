---
title: Orchestration reward modeling — Orch-RM for MAS
type: concept
tags: [concept, reward-model, multi-agent, orchestration, k116]
keywords: [2606.13598, orch-rm, best-of-n, bradley-terry]
related:
  - sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598.md
  - concepts/subagent-orchestration.md
  - entities/tools/conductor-mcp.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/agent-completion-verification-gates.md
  - concepts/retrospective-harness-optimization-rho.md
  - sources/brief-k116-orchrm-harnessx-llm-as-code-prod-2026-06-16.md
  - concepts/counterfactual-advantage-harness-orchestration.md
  - sources/arxiv-chill-harness-counterfactual-learning-2607.25825.md
maturity: draft
created: 2026-06-16
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-orch-rm-multi-agent-orchestration-2606.13598.md` — Rutgers + Salesforce paper
- `@concepts/subagent-orchestration.md` — scatter-gather orchestration target
- `@entities/tools/conductor-mcp.md` — cross-wiki orchestrator
- `@concepts/agent-rubrics-self-correction.md` — scalar reward from traces
- `@concepts/agent-completion-verification-gates.md` — verifier scores for pairs
- `@concepts/retrospective-harness-optimization-rho.md` — trajectory-level preference learning peer

## Raw Concept

How do we score orchestration quality without human labels or full sub-agent rollout cost?

## Narrative

**Orch-RM** [TENTATIVE — 2606.13598]: self-supervised **orchestration-level** reward model. Win-lose pairs from MAS training artifacts; Bradley-Terry training. Scores **workflow plans** and agent coordination — not individual sub-agent outputs at rollout depth.

| Use | CCC steal-from |
|-----|----------------|
| Test-time BoN | Pick best conductor/subagent fan-out plan vs majority vote |
| Continued training | Reward signal for orchestrator prompt/policy updates |

**Efficiency claim:** ~10× token reduction vs rollout-based orchestrator training; +3–8% accuracy on scaling.

**Repo:** `Wang-ML-Lab/OrchRM` **404** (2026-06-16) — REFERENCE until release + license.

**Verdict:** steal BoN-at-orchestration-level for multi-subagent wiki queries; do not wait on Orch-RM install for conductor (use rubric + verification gates today).

## Snippets

> "Operating directly at the orchestration level … ~10× less token used with improved accuracy."

> "Selects higher-quality rollouts than majority voting under best-of-N evaluation."
