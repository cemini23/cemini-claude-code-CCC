---
title: Agent completion verification gates — stop babysitting agent runs
type: concept
tags: [concept, claude-code, verification, harness, k72]
keywords: [ericosiu, completion-proof, verification-gate, agent-babysitting, done-criteria]
related:
  - concepts/claude-premortem-skill.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/openspec.md
  - concepts/subagent-orchestration.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/continual-harness-online-self-improvement.md
  - concepts/enterprise-auto-mode-telemetry-rollout.md
  - concepts/claude-code-subagent-templates.md
  - concepts/nine-stage-agent-team-production.md
  - concepts/agentic-pm-review-artifacts.md
  - concepts/system-scaling-harness-agentic-ai.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/agent-five-gate-org-chart.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/agent-harness-operational-definition.md
  - concepts/progressive-autonomy-incident-resolution.md
  - sources/arxiv-agent-harness-operational-definition-2606.10106.md
  - sources/arxiv-autonomous-hyperscale-incident-resolution-2606.09122.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - sources/arxiv-self-harness-improve-themselves-2606.09498.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - sources/arxiv-channel-fracture-cross-agent-memory-2606.04896.md
  - concepts/perspectivegap-orchestration-prompting.md
  - sources/arxiv-perspectivegap-multi-agent-orchestration-2606.08878.md
  - concepts/llm-as-orchestrator-failure-modes.md
  - concepts/orchestration-reward-modeling-orch-rm.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - sources/arxiv-seagym-self-evolving-harness-eval-2606.17546.md
  - concepts/specification-driven-scientific-workflow-management.md
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
  - concepts/handoff-validity-agent-harness.md
  - sources/arxiv-agentic-eda-handoff-2606.19795.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - sources/arxiv-gatekeepers-layered-eval-quantum-vqe-2606.18422.md
  - concepts/claim-drift-automated-research.md
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - concepts/externalized-research-synthesis-validation.md
  - entities/tools/xcientist.md
  - concepts/autonomous-coding-agents-enterprise-data.md
  - sources/arxiv-data-intelligence-agents-dia-2606.19319.md
  - concepts/scalable-cua-training-pipeline.md
  - sources/arxiv-fara-scalable-cua-environments-2606.20785.md
  - concepts/recoverable-tool-reliability-hazards.md
  - sources/arxiv-toolbench-x-tool-environment-unreliability-2606.25819.md
  - concepts/orchestration-option-quantitative-metrics.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/client-as-first-order-harness-factor.md
  - concepts/agent-data-injection-attacks.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md
  - concepts/hierarchical-bounded-agent-memory.md
  - concepts/modular-instruction-memory-learnable-selection.md
  - concepts/trustx-agent-risk-classification.md
  - concepts/verifiable-search-agent-environment.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - sources/arxiv-recursive-self-improvement-survey-2607.07663.md
  - concepts/agent-optimizer-compounding-and-regression-control.md
  - concepts/solver-grounded-agent-numerics.md
  - sources/arxiv-smart-grids-agentic-tutorial-2607.18147.md
maturity: draft
created: 2026-05-27
updated: 2026-07-21
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@concepts/claude-premortem-skill.md` — pre-ship review; this page is **runtime completion** proof
- `@entities/patterns/full-prompt-goal-template.md` — explicit done criteria in `/goal` envelopes
- `@entities/tools/openspec.md` — acceptance criteria before merge
- `@concepts/subagent-orchestration.md` — parent must verify subagent return, not assume success
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — K162 verification hierarchy for self-improve loops
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — K164 tree routing (orthogonal to stop gates)

Cross-wiki: K72 Post 0 (@ericosiu).

## Raw Concept

K72 — **agent completion proof**: operators should not babysit every tool call; harness must expose verifiable **done** signals (tests green, lint clean, artifact exists) before the session claims completion.

## Narrative

### Pattern [TENTATIVE]

| Gate | Example |
|------|---------|
| Objective test | `pytest`, `wiki_lint.py`, build |
| Artifact check | file path + hash in response |
| Human checkpoint | only for irreversible prod writes |

### CCC fit

Pair with `@concepts/claude-premortem-skill.md` (what could fail) and `@entities/patterns/full-prompt-goal-template.md` (what done looks like).

**K151 Prebind Assurance (CAGE-1):** complements completion gates — prove control **before each binding action** (prod write, trade, send), not only at session end. See `@concepts/cage-1-enterprise-agent-governance-eval.md`.

**K111 channel fracture:** cross-agent memory/cron delivery must use **receiver-side proof** (read-back at target store) — writer tool success is insufficient; see `@concepts/channel-fracture-cross-agent-memory-delivery.md` CADVP CC-0 veto.

**K122 claim drift:** completion gates must prove the **claimed mechanism** survived implementation — not only that tests/lint passed; see `@concepts/claim-drift-automated-research.md` (semantic / experimental / mechanistic subtypes).

**K138 substrate constraints:** objective gates (`wiki_lint.py`, pytest, build) prove **session done**; **substrate constraints** (linters, types, module-local `Invariants:` docstrings) make agent output **auditable** before those gates run — small reviewer recall 54.5% → 90.9% with substrate + docs CLI (`@concepts/substrate-constraints-coding-agent-oversight.md`).

**K162 verification hierarchy (RSI survey):** when the session *is* a self-improvement loop, place the stop signal on this ladder and refuse weaker-only gates:

| Strength | Signal | Session-done example |
|----------|--------|----------------------|
| Strongest | Formal | schema / type / OpenSpec AC |
| High | Execution | `wiki_lint.py`, pytest, deploy smoke |
| Mid | Judges / rubrics | `/super-audit`, LLM rubric — advisory |
| Weakest | Intrinsic | “looks good” — never sole stop |

**NO-GO:** closed self-reward that rewrites its own pass criteria without a human. See `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`.

| Verdict | **REFERENCE (adopt in rules/skills)** |

## Snippets

> "Agent completion proof / stop babysitting."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 0]
