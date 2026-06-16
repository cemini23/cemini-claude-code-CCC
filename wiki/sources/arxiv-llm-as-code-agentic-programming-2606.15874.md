---
title: LLM-as-Code — agentic programming for agent harness (arXiv 2606.15874)
type: source
tags: [source, arxiv, llm-as-code, agentic-programming, kdd, k116]
keywords: [2606.15874, llm-as-code, control-flow, dag-context, react]
related:
  - concepts/llm-as-code-agentic-programming.md
  - concepts/code-as-agent-harness.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/agentic-programming-full-stack-thesis.md
  - concepts/llm-as-orchestrator-failure-modes.md
maturity: draft
read_status: read
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- `@concepts/llm-as-code-agentic-programming.md` — CCC synthesis
- `@concepts/code-as-agent-harness.md` — harness control-flow axis
- `@concepts/dynamic-workflow-orchestrator-off-model.md` — program-owned orchestration
- `@concepts/agentic-programming-full-stack-thesis.md` — agentic programming framing

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | LLM-as-Code: Agentic Programming for Agent Harness |
| **Authors** | Qi et al. (CityU HK); Wu (Tencent Jarvis Lab) |
| **arXiv** | 2606.15874v1 [cs.AI] |
| **Venue** | KDD 2026 Workshop on Agentic Software Engineering (AgenticSE) |
| **Location** | `raw-sources/arxiv-2606.15874-llm-as-code-agentic-programming-for-agent-harnes.pdf` |
| **Retrieved** | 2026-06-16 |
| **Read status** | read (paradigm, DAG context, computer-use case study) |

## Narrative

Critiques **LLM-as-orchestrator** (ReAct loop in AutoGen, OpenHands, MetaGPT): token explosion, control-flow hallucination, unreliable completion are **architectural** — probabilistic model assigned deterministic looping/branching/sequencing.

**Agentic Programming** alternative:

- **Program** owns control flow (loops, branches, sequencing, completion)
- **LLM-as-Code** — adaptive component invoked only for reasoning/generation steps
- Context = **DAG** from execution call tree; context length scales with **call depth**, not step accumulation
- Multi-agent collaboration = functions over that graph
- Self-programmed evolution commits improvements as durable code

Case study: computer-use agents — improved stability on long visual operation sequences.

**CCC relevance:** aligns with K107 off-model orchestrator + OpenSpec acceptance gates; contrasts with pure ReAct Claude Code default loop. No public framework repo found 2026-06-16.

## Snippets

> "Token explosion, control-flow hallucination, and unreliable completion are not implementation bugs but architectural consequences of assigning deterministic work to a probabilistic system."

> "Within each call the model keeps full flexibility, but it cannot alter the program's execution path."
