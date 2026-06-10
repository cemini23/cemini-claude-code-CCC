---
title: Agent harness operational definition (arXiv 2606.10106)
type: source
tags: [source, arxiv, agent-harness, definition, k109]
keywords: [2606.10106, agent-harness, T1-T4, inclusion-test, coding-agent]
related:
  - concepts/agent-harness-operational-definition.md
  - concepts/code-as-agent-harness.md
  - concepts/etclovg-harness-layers.md
  - concepts/agent-completion-verification-gates.md
  - entities/tools/claude-code.md
maturity: draft
read_status: read
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@concepts/agent-harness-operational-definition.md` — CCC synthesis + Cemini mapping
- `@concepts/code-as-agent-harness.md` — three-layer survey vs T1–T4 constitutive test
- `@concepts/etclovg-harness-layers.md` — finer runtime taxonomy once membership is established
- `@concepts/agent-completion-verification-gates.md` — control mechanisms (T4) in practice
- `@entities/tools/claude-code.md` — cited product harness in application section

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | What makes a harness a harness: necessary and sufficient conditions for an agent harness |
| **Author** | Sanderson Oliveira de Macedo (Federal Institute of Goiás) |
| **arXiv** | 2606.10106v1 [cs.SE] |
| **Location** | `raw-sources/arxiv-2606.10106-what-makes-a-harness-a-harness-necessary-and-suf.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | read (definition, boundary, six-harness application) |

## Narrative

Conceptual analysis paper — not a benchmark — delivering an **operational membership test** for “agent harness.” Reconstructs genealogy (horse tack → test harness → ML eval harness → agent harness). Proposes four **necessary and sufficient** runtime conditions (T1–T4): agent loop, tool interface, context management, control mechanisms (limits, verification, deterministic actions). Distinguishes harness from framework, SDK, IDE plugin, eval harness, and orchestrator. Applies test to Claude Code, Codex CLI, Aider, Cline, OpenHands, SWE-agent.

**CCC relevance:** vocabulary anchor for ETCLOVG layer tagging, Phase-0 tool class decisions, and “is this a harness?” routing in cross-wiki evals.

## Snippets

> "An agent harness is the runtime engineering layer that wraps one or more language models and turns them into an agent able to accomplish tasks over an external environment."

> "A system is an agent harness if and only if it instantiates the four elements above at runtime."

> "Claude Code is the harness, and Claude is the model inside it."

> — [Source: arxiv-2606.10106-what-makes-a-harness-a-harness-necessary-and-suf.pdf §4, retrieved 2026-06-10]
