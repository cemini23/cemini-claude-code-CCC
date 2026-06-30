---
title: LLM-as-Code — program-owned control flow for agents
type: concept
tags: [concept, agentic-programming, control-flow, dag-context, k116]
keywords: [2606.15874, llm-as-code, react-critique, kdd-agenticse]
related:
  - sources/arxiv-llm-as-code-agentic-programming-2606.15874.md
  - concepts/code-as-agent-harness.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/agentic-programming-full-stack-thesis.md
  - concepts/llm-as-orchestrator-failure-modes.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/openspec.md
  - concepts/specification-driven-scientific-workflow-management.md
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
  - concepts/executable-user-memory-user-as-code.md
  - sources/arxiv-user-as-code-executable-memory-2606.16707.md
  - concepts/plan-then-execute-topological-orchestration.md
  - concepts/autonomous-coding-agents-enterprise-data.md
  - sources/arxiv-data-intelligence-agents-dia-2606.19319.md
  - sources/brief-k116-orchrm-harnessx-llm-as-code-prod-2026-06-16.md
maturity: draft
created: 2026-06-16
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-llm-as-code-agentic-programming-2606.15874.md` — CityU + Tencent Jarvis paper
- `@concepts/code-as-agent-harness.md` — harness vs model responsibilities
- `@concepts/dynamic-workflow-orchestrator-off-model.md` — orchestrator in code, zero-token glue
- `@concepts/agentic-programming-full-stack-thesis.md` — full-stack agent workflows
- `@concepts/llm-as-orchestrator-failure-modes.md` — symptom catalog (this page's thesis)
- `@entities/patterns/full-prompt-goal-template.md` — explicit program-shaped done criteria
- `@entities/tools/openspec.md` — deterministic acceptance before stop

## Raw Concept

Should the LLM run the agent loop, or should the program run the loop and call the LLM at reasoning nodes?

## Narrative

**LLM-as-Code / Agentic Programming** [TENTATIVE — 2606.15874]: rejects **LLM-as-orchestrator** (ReAct default). Deterministic steps (loop, branch, sequence, bind, error handling) belong in **code**; LLM invoked only for probabilistic steps (understand, summarize, generate, judge).

**DAG context:** execution history forms a call tree; each LLM call's context bounded by **depth**, not cumulative step length — addresses token explosion without infinite windows.

**Three structural failures of LLM orchestrator:**

1. Token explosion — history grows per step
2. Control-flow hallucination — claims done before verifier runs
3. Unreliable completion — abandons correct earlier diagnosis

**CCC alignment:** K107 off-model orchestrator, Ralph `/goal` envelopes, OpenSpec gates, Stop-hook completion proof — program owns flow; model owns reasoning inside nodes.

**Verdict:** **REFERENCE** — strengthen rules that completion checks and branch logic live in hooks/scripts/skills, not model discretion alone.

## Snippets

> "A better prompt or a stronger model cannot guarantee the reliability of the LLM agent."

> "The program governs all control flow, and the LLM is itself part of it … invoked only where a task calls for reasoning or generation."
