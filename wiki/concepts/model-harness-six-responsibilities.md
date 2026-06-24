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
maturity: draft
created: 2026-06-24
updated: 2026-06-24
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

Use the six-responsibility checklist for **survey-aligned** discussions; use ETCLOVG for **failure localization** (`## Dead Ends`, HarnessFix records).

## Snippets

> "Agent quality emerges from the interaction between model capability, runtime infrastructure, task structure, and evaluation design."
> — [Source: arxiv-2606.20683, retrieved 2026-06-24]
