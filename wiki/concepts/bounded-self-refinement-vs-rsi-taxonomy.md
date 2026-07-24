---
title: Bounded self-refinement vs RSI — taxonomy and verification hierarchy
type: concept
tags: [concept, self-improvement, rsi, verification, taxonomy, harness, k162]
keywords: [2607.07663, verification hierarchy, bounded refinement, recursive self-improvement, self-evaluation, loop closure]
related:
  - sources/arxiv-recursive-self-improvement-survey-2607.07663.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/agent-completion-verification-gates.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - concepts/skillhone-continual-skill-decision-history.md
  - concepts/verifiable-search-agent-environment.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/claim-drift-automated-research.md
  - concepts/trustx-agent-risk-classification.md
  - sources/brief-k162-rsi-verification-hierarchy-2026-07-14.md
  - briefs/2026-07-14_ccc-handoff-rsi-hierarchical-orchestration-ingest.md
  - concepts/agent-completion-verification-gates.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/agent-optimizer-compounding-and-regression-control.md
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - concepts/toolverse-gust-turn-aware-agentic-rl.md
  - concepts/businesscasebench-rubric-from-expert-solutions.md
  - sources/arxiv-businesscasebench-knowledge-work-2607.16057.md
  - sources/arxiv-toolverse-long-horizon-mcp-rl-2607.15660.md
  - concepts/solver-grounded-agent-numerics.md
  - concepts/measurement-gated-agent-harness-optimization.md
  - sources/arxiv-flashrt-agent-harness-realtime-2607.18171.md
  - sources/arxiv-smart-grids-agentic-tutorial-2607.18147.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/production-agent-deployment-checklist.md
  - sources/arxiv-biosecbench-surveillance-2607.19262.md
  - concepts/hybrid-slm-ensemble-orchestration.md
  - concepts/offensive-agent-ethics-oversight-posture.md
  - sources/arxiv-ethics-offensive-autonomous-agents-2607.20255.md
  - concepts/harness-native-agent-rl-training.md
maturity: draft
created: 2026-07-14
updated: 2026-07-24
---

## Relations

- `@sources/arxiv-recursive-self-improvement-survey-2607.07663.md` — K162 provenance
- `@concepts/continual-harness-online-self-improvement.md` — Cemini harness-evolution cluster (deployment-time cell)
- `@concepts/agent-completion-verification-gates.md` — prefer stronger verification rungs

## Raw Concept

K162 arXiv **2607.07663** — survey of ~1250 papers mapping “self-X” vocabulary onto a two-axis grid so **bounded industrial loops** are not confused with **open-ended RSI**.

## Narrative

### Two axes

| Axis | Values |
|------|--------|
| **What improves** | Deployment behavior (outputs / TTT / harness·skills) · Training policy · Evaluator · Research process |
| **Loop closure** | Human-in-the-loop · Human-on-the-loop · Closed |

Almost all surveyed work is **human-on-the-loop** bounded refinement. Closed loops that also rewrite the evaluator are the RSI / safety-relevant niche.

### Verification hierarchy (steal for Cemini) [CONFIRMED from survey framing]

| Strength | Signal | Cemini mapping |
|----------|--------|----------------|
| Strongest | Formal verifiers (proofs, types) | Rare — typed configs, schema checks |
| High | Execution feedback (tests, compilers, benchmarks) | `wiki_lint`, unit tests, OpenSpec AC, deploy smoke |
| Mid | Process/reward models, LLM judges, rubrics | `/super-audit`, rubric evals — treat as advisory |
| Weakest | Intrinsic self-assessment (“looks good”) | Never sole stop criterion |

**Failure modes at weak rungs:** self-confirming loops, model collapse, diversity collapse. Survey claim: demonstrated self-improvement strength tracks this hierarchy.

### Bottleneck = research direction-setting

Anthropic RSI continuum (essay used as frame, not evidence): execution is increasingly automated; **choosing which problems matter** stays human. Same as verification bottleneck for non-checkable tasks.

### Cemini operating rule

- **ADOPT** hierarchy language in briefs / `/goal` verification sections
- **ADOPT** prefer execution/formal gates over LLM-judge-only Stop hooks
- **NO-GO** closed self-reward loops that edit their own success criteria without human review
- Pair with `@concepts/trustx-agent-risk-classification.md` before raising autonomy

| Verdict | **REFERENCE** — taxonomy + checklist; cited GitHub 404 at Phase-0 |

## Snippets

> "Self-improvement strength tracks this hierarchy … characteristic failure modes (self-confirming loops, model collapse, diversity collapse) follow from its violations"
> — [Source: arxiv-2607.07663 abstract]
