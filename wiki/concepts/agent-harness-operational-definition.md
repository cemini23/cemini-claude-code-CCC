---
title: Agent harness operational definition — T1–T4 membership test
type: concept
tags: [concept, agent-harness, definition, k109]
keywords: [2606.10106, T1-T4, agent-loop, tool-interface, context-management, control-mechanisms]
related:
  - sources/arxiv-agent-harness-operational-definition-2606.10106.md
  - concepts/code-as-agent-harness.md
  - concepts/etclovg-harness-layers.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/claude-code.md
  - concepts/progressive-autonomy-incident-resolution.md
  - concepts/self-harness-model-specific-improvement-loop.md
  - sources/arxiv-self-harness-improve-themselves-2606.09498.md
  - sources/arxiv-parthenon-law-self-evolving-legal-agent-2606.04602.md
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/model-harness-six-responsibilities.md
  - sources/arxiv-agent-harness-survey-2606.20683.md
maturity: draft
created: 2026-06-10
updated: 2026-06-24
---

## Relations

- `@sources/arxiv-agent-harness-operational-definition-2606.10106.md` — provenance
- `@concepts/code-as-agent-harness.md` — three-layer survey model (interface / mechanisms / scaling)
- `@concepts/etclovg-harness-layers.md` — seven-layer refinement after membership is established
- `@concepts/agent-completion-verification-gates.md` — T4 control in Cemini workflows
- `@entities/tools/claude-code.md` — reference product in paper application section

## Raw Concept

arXiv **2606.10106** asks: what is an **agent harness** as an instrument, not a slogan? Answer: four runtime conditions that are jointly necessary and sufficient.

## Narrative

### Constitutive definition [CONFIRMED — single primary source]

A system is an **agent harness** iff at runtime it couples to the model:

| ID | Element | Without it |
|----|---------|------------|
| **T1** | Agent loop (reason → act → observe) | One-shot generator, not an agent |
| **T2** | Tool interface (perceive + alter environment) | Model trapped in context window |
| **T3** | Context management (what enters/leaves the window) | Multi-step tasks collapse |
| **T4** | Control mechanisms (limits, verification, deterministic handlers) | Unverifiable “success” claims |

Acts **during** the task — unlike an **eval harness**, which observes afterward.

### Boundary exclusions

Not required: multi-agent, fine-tuning, specific model, or UI. **Framework / SDK / IDE plugin / orchestrator / eval harness** are neighboring concepts with distinct membership tests (paper §5).

### vs ETCLOVG and three-layer survey

| Lens | Use when |
|------|----------|
| T1–T4 (this page) | “Is this product a harness?” |
| Three-layer survey | Map harness onto Claude Code / MCP stack |
| ETCLOVG | Tag which **layer** failed after a trajectory |

### Cemini mapping [TENTATIVE]

| T | Claude Code analogue |
|---|---------------------|
| T1 | Main session + subagent loops, Stop-hook continuation |
| T2 | MCP tools, bash, skills |
| T3 | Progressive disclosure, claude-mem, `hot.md`, lazy-tool |
| T4 | OpenSpec acceptance, `wiki_lint.py`, Tier-1/2 permissions, verification gates |

## Snippets

> "The temporal clause carries a lot of weight: the harness acts during the task."

> — [Source: arxiv-agent-harness-operational-definition-2606.10106.md, retrieved 2026-06-10]
