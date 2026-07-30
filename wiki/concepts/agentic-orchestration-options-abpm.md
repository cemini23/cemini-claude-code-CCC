---
title: Agentic orchestration options — OO1–OO4 ABPM framework
type: concept
tags: [concept, orchestration, abpm, process-aware, k136]
keywords: [2606.31518, oo1, oo2, oo3, oo4, mcp, framed-autonomy]
related:
  - sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md
  - concepts/orchestration-option-quantitative-metrics.md
  - concepts/subagent-orchestration.md
  - concepts/plan-then-execute-topological-orchestration.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/etclovg-harness-layers.md
  - concepts/model-harness-six-responsibilities.md
  - entities/patterns/scatter-gather.md
  - entities/tools/simple-agentic-scenario.md
  - sources/brief-k136-agentic-orchestration-options-abpm-2026-07-01.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - concepts/counterfactual-advantage-harness-orchestration.md
maturity: draft
created: 2026-07-01
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-agentic-orchestration-options-abpm-2606.31518.md` — arXiv provenance (2606.31518)
- `@concepts/orchestration-option-quantitative-metrics.md` — quantitative comparison metrics
- `@concepts/subagent-orchestration.md` — CCC delegation patterns

## Raw Concept

How should Cemini choose between single-agent MCP orchestration vs process-framed multi-agent workflows — and what properties trade off?

## Narrative

arXiv **2606.31518** (TUM ABPM) defines **orchestration options** along two axes: who holds the **process frame** (none / prompt / external engine) and whether invoked agents are **process-aware**.

### OO1–OO4 summary

| OO | Name | Autonomy | Traceability | Correctness | CCC default mapping |
|----|------|----------|--------------|-------------|---------------------|
| **OO1** | Process-agnostic agentic orchestration | High | Low | Low | Single Claude/Cursor session + MCP — `@entities/tools/claude-code.md` |
| **OO2** | Process-aware agentic orchestration | High | Medium | Medium | Rules in `CLAUDE.md`, `/goal` prompt, skills — frame in context |
| **OO3** | Orchestration of process-agnostic agents | Medium | Medium (frame) | Higher | Task/subagent scatter-gather + OpenSpec AC + deterministic hooks |
| **OO4** | Orchestration of process-aware agents | Lower | High | Highest | OO3 + subagent prompts carry regulatory/frame constraints |

Transitions between OOs are **fluid** — declarative rule sets blur OO2 vs OO3.

### Qualitative selection criteria (Table 1 steal)

Move toward **OO3/OO4** when:

1. Goal is **complex** (multi-outcome, human oversight)
2. **Constraints** require guarantees (consent withdrawal, audit, compliance)
3. **Human actions** in the loop
4. Agent **decision space must be restricted**
5. **Maintenance** over initial build cost matters

Stay **OO1/OO2** when goal is simple, unconstrained, low oversight, fast bootstrap.

### Implementation lessons (Sect. 3) [CONFIRMED paper]

| Lesson | Harness action |
|--------|----------------|
| Tool wiring restricts action space like traditional workflows | MCP allowlists + lazy-tool proxy |
| Temporal constraints need frames, not LLM timing | Stop hooks, ScheduleWakeup, external cron — not “wait 10 hours in prompt” |
| Agent logging unreliable | `wiki/log.md`, git, claude-mem, CI — **Observability layer** not model |
| Long workflows blow context | Subagents, CPR, self-compacting patterns |
| Less frame → harder debug | Prefer explicit AC + lint over monolithic agent history |

### Regulated scenario pattern (blood donation)

Naive OO1 unacceptable — upload Blood Guide to RAG still risky. **Deterministic parallel services** enforce hard stops (consent abort); LLM agents only for **user Q&A** subtasks. Maps to `@concepts/gatekeeper-layered-agent-evaluation.md` + cybersecurity permission hooks for prod.

## Snippets

> "The transition between the OOs is fluid, especially if the process is declarative and hence consists of a set of rules."
> — [Source: arxiv-2606.31518-design-and-implementation-of-agentic-orchestrati.pdf, retrieved 2026-07-01]
