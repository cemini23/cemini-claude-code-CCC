---
title: Plan-then-execute topological orchestration — DynAMO pattern
type: concept
tags: [concept, orchestration, dag, plan-execute, k120]
keywords: [2606.19382, dynamo, parallel-workflow, schema-constrained-planning]
related:
  - sources/arxiv-dynamo-topological-orchestration-2606.19382.md
  - entities/tools/dynamo-orchestration.md
  - entities/patterns/scatter-gather.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/llm-as-code-agentic-programming.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/tool-response-context-pruning-summarization.md
  - concepts/subagent-orchestration.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- `@sources/arxiv-dynamo-topological-orchestration-2606.19382.md` — DynAMO paper
- `@entities/tools/dynamo-orchestration.md` — Apache-2.0 reference engine
- `@entities/patterns/scatter-gather.md` — parallel fan-out without DAG validation
- `@concepts/graphflow-verifiable-agent-workflows.md` — verifiable workflow graphs
- `@concepts/dynamic-workflow-orchestrator-off-model.md` — off-model orchestration patterns
- `@concepts/llm-as-code-agentic-programming.md` — plan in code vs ReAct loop
- `@concepts/handoff-validity-agent-harness.md` — DAG edges as handoff contracts
- `@concepts/tool-response-context-pruning-summarization.md` — context pruning peer (30% latency claim)
- `@concepts/subagent-orchestration.md` — Task tool dispatch mapping

## Raw Concept

How do we orchestrate multi-agent workflows with safety and latency guarantees?

## Narrative

**Plan-then-Execute** [TENTATIVE — 2606.19382 DynAMO]: separate **planning** (schema-constrained DAG generation) from **execution** (topological scheduling with optional parallelism).

| Scheduler | Behavior | CCC analogue |
|-----------|----------|--------------|
| SequentialWorkflow | Fixed topological order | Single-threaded ingest pipeline |
| ParallelWorkflow | Ready-set dispatch when deps satisfied | scatter-gather with explicit dependency graph |

**Key findings:** parallelism helps when branches are independent; **LLM inference remains dominant cost** (>90% after realistic tool latency); structured context pruning reduces inference time ~30%.

### Steal-for CCC harness

1. **Plan DAG before fan-out** — OpenSpec/`/goal` acceptance criteria as graph edges
2. **Dependency-aware parallel** — only scatter-gather when tasks are provably independent
3. **Prune context per node** — align with tool-response pruning (K115)

**Domain:** Industry 4.0 asset ops — **not** Cemini prod. Repo `kushwaha001/DynAMO` — CONDITIONAL-GO reference only.

## Snippets

> "Enforces schema-constrained planning to generate verifiable task graphs before execution."

> — [Source: arxiv-2606.19382-dynamo-dynamic-asset-management-orchestration-vi.pdf]
