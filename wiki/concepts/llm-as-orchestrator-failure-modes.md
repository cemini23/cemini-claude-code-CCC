---
title: LLM-as-orchestrator failure modes — structural harness limits
type: concept
tags: [concept, react, control-flow, harness, k116]
keywords: [token-explosion, control-flow-hallucination, react-loop]
related:
  - concepts/llm-as-code-agentic-programming.md
  - sources/arxiv-llm-as-code-agentic-programming-2606.15874.md
  - concepts/agent-completion-verification-gates.md
  - concepts/long-thread-context-decay.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
maturity: draft
created: 2026-06-16
updated: 2026-06-16
---

## Relations

- `@concepts/llm-as-code-agentic-programming.md` — proposed alternative
- `@sources/arxiv-llm-as-code-agentic-programming-2606.15874.md` — KDD 2026 AgenticSE paper
- `@concepts/agent-completion-verification-gates.md` — verifier-before-done mitigation
- `@concepts/long-thread-context-decay.md` — context rot sibling
- `@concepts/dynamic-workflow-orchestrator-off-model.md` — code-owned orchestration fix

## Raw Concept

What breaks when the model owns the agent loop on long-horizon tasks?

## Narrative

Catalog from **2606.15874** — symptoms of **LLM-as-orchestrator** (ReAct-style), architectural not fixable by prompt alone:

| Symptom | Mechanism | CCC mitigation |
|---------|-----------|----------------|
| Token explosion | Context grows every step | pruning (`@concepts/tool-response-context-pruning-summarization.md`), subagent isolation |
| Control-flow hallucination | Reports success before verifier | `@concepts/agent-completion-verification-gates.md`, OpenSpec |
| Unreliable completion | Abandons prior correct state | `/goal` envelopes, Stop-hook, program-owned loops |

**Verdict:** REFERENCE checklist for harness flaw records (ETCLOVG Execution + Verification layers).

## Snippets

> "These are the long-horizon coherence failures … putting a probabilistic model in charge of control flow that must be deterministic."
