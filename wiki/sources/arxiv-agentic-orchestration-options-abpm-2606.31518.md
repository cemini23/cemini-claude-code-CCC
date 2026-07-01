---
title: Agentic orchestration options — ABPM classification (arXiv 2606.31518)
type: source
tags: [source, arxiv, abpm, orchestration, k136]
keywords: [2606.31518, oo1, oo2, oo3, oo4, agentic-bpm, process-aware]
related:
  - concepts/agentic-orchestration-options-abpm.md
  - concepts/orchestration-option-quantitative-metrics.md
  - entities/tools/simple-agentic-scenario.md
  - concepts/subagent-orchestration.md
  - concepts/etclovg-harness-layers.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/model-harness-six-responsibilities.md
  - concepts/plan-then-execute-topological-orchestration.md
  - entities/patterns/scatter-gather.md
  - sources/brief-k136-agentic-orchestration-options-abpm-2026-07-01.md
maturity: draft
read_status: read
created: 2026-07-01
updated: 2026-07-01
---

## Relations

- `@concepts/agentic-orchestration-options-abpm.md` — OO1–OO4 synthesis
- `@concepts/orchestration-option-quantitative-metrics.md` — M/ABC/F1 metrics
- `@entities/tools/simple-agentic-scenario.md` — reference implementation repo

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Design and Implementation of Agentic Orchestrations and Orchestration of Agents |
| **Authors** | Rinderle-Ma et al. (TUM) |
| **arXiv** | 2606.31518v1 [cs.AI] |
| **Implementation** | https://github.com/JohannesLbck/SimpleAgenticScenario |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.31518-design-and-implementation-of-agentic-orchestrati.pdf` |
| **Retrieved** | 2026-07-01 |
| **Read status** | read (classification, light-sensing eval, blood-donation sketch) |

## Narrative

TUM ABPM paper classifying **four orchestration options (OO1–OO4)** for LLM agents combined with process technology:

| OO | Pattern | Frame | Agent process-awareness |
|----|---------|-------|-------------------------|
| **OO1** | Process-agnostic agentic orchestration | None | Agent orchestrates via MCP/A2A |
| **OO2** | Process-aware agentic orchestration | In prompt/context | Agent aware of rules/docs |
| **OO3** | Orchestration of process-agnostic agents | External process engine | Agents black-box in workflow |
| **OO4** | Orchestration of process-aware agents | External process + agent frame | Highest traceability/correctness |

Evaluated on predictive **light sensing** (REST + MCP + cpee.org orchestration) with metrics for task specificity (cyclomatic **M**, **ABC**), correctness (**P/R/F1**), reactivity, traceability. **Blood donation** case argues regulated domains require OO3/OO4 — deterministic enforcement for consent withdrawal, LLM only where Q&A needed.

**CCC relevance:** maps Claude Code default (OO1) vs OpenSpec/`/goal` AC + hooks (OO3) vs framed subagent prompts (OO4). Steal selection table + “do not rely on agent logging” + temporal constraints need frames.

## Snippets

> "OO1 Process-agnostic Agentic Orchestration: One agent orchestrates multiple work steps, using, for example, protocols such as MCP … The agent is not aware of any explicit process frame or logic."
> — [Source: arxiv-2606.31518-design-and-implementation-of-agentic-orchestrati.pdf, retrieved 2026-07-01]

> "Relying on agents for logging is generally not recommended, even when logging tools are provided."
> — [Source: arxiv-2606.31518-design-and-implementation-of-agentic-orchestrati.pdf Sect. 3, retrieved 2026-07-01]

> "Any temporal constraints are challenging to enforce, as the reasoning times of LLMs are unpredictable, so they require frames/tools to enforce temporal relationships."
> — [Source: arxiv-2606.31518-design-and-implementation-of-agentic-orchestrati.pdf Sect. 3, retrieved 2026-07-01]
