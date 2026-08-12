---
title: Model–harness six runtime responsibilities
type: concept
tags: [concept, harness-engineering, survey, k124]
keywords: [2606.20683, observation, context, control, action, state, verification]
related:
  - sources/arxiv-agent-harness-survey-2606.20683.md
  - concepts/code-as-agent-harness.md
  - concepts/etclovg-harness-layers.md
  - concepts/agent-harness-operational-definition.md
  - entities/tools/claude-code.md
  - concepts/system-scaling-harness-agentic-ai.md
  - entities/tools/awesome-agent-engineering.md
  - entities/patterns/full-prompt-goal-template.md
  - sources/brief-k124-harness-memory-research-cluster-2026-06-24.md
  - concepts/agentic-orchestration-options-abpm.md
  - sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md
  - concepts/distributed-harness-security-controls.md
  - concepts/scaffold-over-tool-interface.md
  - concepts/agentic-configuration-management-acm.md
maturity: draft
created: 2026-06-24
updated: 2026-08-12
---

## Relations

- `@sources/arxiv-agent-harness-survey-2606.20683.md` — arXiv provenance
- `@concepts/etclovg-harness-layers.md` — CCC seven-layer refinement
- `@concepts/code-as-agent-harness.md` — three-layer survey model parent

## Raw Concept

What are the coupled runtime responsibilities of an LLM agent execution harness, and how do they map to Claude Code?

## Narrative

arXiv **2606.20683** decomposes the execution harness into **six coupled responsibilities**:

| Responsibility | Scope | Claude Code / Cemini mapping |
|----------------|-------|------------------------------|
| **Observation** | What the agent can perceive each step | Tool outputs, MCP results, browser snapshots |
| **Context** | Window, summaries, retrieval, injection policy | `hot.md`, claude-mem, lazy-tool, progressive disclosure |
| **Control** | Planning, branching, retries, termination | Subagents, Stop hooks, `/goal`, conductor |
| **Action** | Tool invocation, sandbox boundaries | Tier 1/2, MCP allowlists, Bash permissions |
| **State** | Persistent task/project memory | `wiki/log.md`, stash, git, lifecycle records |
| **Verification / governance** | Checks, eval, safety, audit | OpenSpec AC, `wiki_lint.py`, defenseclaw, skill-vetting |

### vs ETCLOVG

| Six-responsibility | ETCLOVG layers (approx.) |
|--------------------|--------------------------|
| Observation + Action | Execution + Tool Interface |
| Context + State | Context & Memory |
| Control | Lifecycle & Orchestration |
| Verification/governance | Verification + Governance |
| (cross-cutting) | Observability spans all |

**K136:** ABPM **OO1–OO4** maps Control + Observability trade-offs — OO1 single-agent MCP vs OO3/OO4 external process frame with framed subagents; see `@concepts/agentic-orchestration-options-abpm.md`.

Use the six-responsibility checklist for **survey-aligned** discussions; use ETCLOVG for **failure localization** (`## Dead Ends`, HarnessFix records).

## Snippets

> "Agent quality emerges from the interaction between model capability, runtime infrastructure, task structure, and evaluation design."
> — [Source: arxiv-2606.20683, retrieved 2026-06-24]
