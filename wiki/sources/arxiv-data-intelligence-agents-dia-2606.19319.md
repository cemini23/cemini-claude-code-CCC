---
title: Data Intelligence Agents — enterprise data via autonomous coding (arXiv 2606.19319)
type: source
tags: [source, arxiv, dia, text-to-sql, autonomous-coding-agent, k123]
keywords: [2606.19319, data-interpreter, schema-creator, query-generator, c3-ai]
related:
  - concepts/autonomous-coding-agents-enterprise-data.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/code-as-agent-harness.md
  - concepts/agent-completion-verification-gates.md
  - concepts/claim-drift-automated-research.md
maturity: draft
read_status: read
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- `@concepts/autonomous-coding-agents-enterprise-data.md` — DIA synthesis
- `@concepts/llm-as-code-agentic-programming.md` — ACA as control abstraction peer

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Data Intelligence Agents: Interpreting, Modeling, and Querying Enterprise Data via Autonomous Coding Agents |
| **Authors** | Vyas et al. (C3 AI) |
| **arXiv** | 2606.19319v1 [cs.MA] |
| **Location** | `raw-sources/arxiv-2606.19319-data-intelligence-agents-interpreting-modeling-a.pdf` |
| **Retrieved** | 2026-06-23 |
| **Read status** | read (architecture, benchmarks, ACA abstraction) |

## Narrative

**DIA** — three agents on a shared workspace, each realized as an **Autonomous Coding Agent (ACA)**: generate, execute, validate, repair **concrete artifacts** (not text-only handoffs).

| Agent | Role |
|-------|------|
| Data Interpreter | Discover and understand raw enterprise data |
| Schema Creator | Structure validated schemas |
| Query Generator | SQL generation, debugging, conversational interaction |

**Key thesis:** ACA (coder + LLM + sandbox) is the central abstraction — adaptation via natural-language instructions, shared memory for experience reuse, domain expert review at each artifact stage.

**Eval:** Query Generator in fully autonomous mode — matches or beats best published on **seven** SQL benchmarks (BIRD, Spider2 variants, LiveSQLBench) across four dialects without fine-tuning.

**CCC relevance:** steal artifact-grounded execution + shared memory pattern for ingest/OpenSpec; **REFERENCE** for C3 AI product stack (not Cemini prod).

## Snippets

> "Rather than emitting text, the agents generate, execute, validate, and repair concrete artifacts."
> — [Source: arxiv-2606.19319-data-intelligence-agents-interpreting-modeling-a.pdf, retrieved 2026-06-23]
