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
maturity: draft
created: 2026-05-27
updated: 2026-06-21
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md"
---

## Relations

- `@concepts/claude-premortem-skill.md` — pre-ship review; this page is **runtime completion** proof
- `@entities/patterns/full-prompt-goal-template.md` — explicit done criteria in `/goal` envelopes
- `@entities/tools/openspec.md` — acceptance criteria before merge
- `@concepts/subagent-orchestration.md` — parent must verify subagent return, not assume success

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

**K111 channel fracture:** cross-agent memory/cron delivery must use **receiver-side proof** (read-back at target store) — writer tool success is insufficient; see `@concepts/channel-fracture-cross-agent-memory-delivery.md` CADVP CC-0 veto.

| Verdict | **REFERENCE (adopt in rules/skills)** |

## Snippets

> "Agent completion proof / stop babysitting."
> — [Source: briefs/2026-05-27_k72-ccc-workflows-from-osint.md, Post 0]
