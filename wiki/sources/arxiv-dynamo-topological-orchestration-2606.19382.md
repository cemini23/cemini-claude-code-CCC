---
title: DynAMO — topological multi-agent scheduling for asset ops (arXiv 2606.19382)
type: source
tags: [source, arxiv, dynamo, orchestration, industry-4, k120]
keywords: [2606.19382, plan-then-execute, assetopsbench, dag-scheduling]
related:
  - concepts/plan-then-execute-topological-orchestration.md
  - entities/tools/dynamo-orchestration.md
  - entities/patterns/scatter-gather.md
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/subagent-orchestration.md
  - concepts/tool-response-context-pruning-summarization.md
maturity: draft
read_status: read
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- `@concepts/plan-then-execute-topological-orchestration.md` — harness synthesis
- `@entities/tools/dynamo-orchestration.md` — reference repo
- `@entities/patterns/scatter-gather.md` — parallel fan-out peer pattern

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DynAMO: Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling |
| **Authors** | Kushwaha et al. (Gati Shakti Vishwavidyalaya); Patel (IBM Research) |
| **arXiv** | 2606.19382v1 [cs.SE] |
| **Repo** | `github.com/kushwaha001/DynAMO` (Apache-2.0) |
| **Location** | `raw-sources/arxiv-2606.19382-dynamo-dynamic-asset-management-orchestration-vi.pdf` |
| **Retrieved** | 2026-06-20 |
| **Read status** | read (Plan-then-Execute, DAG schedulers, AssetOpsBench eval) |

## Narrative

**DynAMO** — deployment-oriented **Plan-then-Execute** engine for industrial asset workflows:

1. **Schema-constrained planning** → verifiable task DAG before execution
2. **Topological engine** — `SequentialWorkflow` (strict topo order) vs `ParallelWorkflow` (dependency-aware concurrency)

**Eval (AssetOpsBench — 141 industrial IoT queries):** median **1.6×** latency reduction (up to 1.8× parallelizable); LLM reasoning >90% of wall time after tool-I/O instrumentation; structured context pruning ~30% inference latency reduction; graceful degradation under fault injection.

**CCC relevance:** steal DAG scheduling + plan-before-execute for scatter-gather / off-model orchestrator — **REFERENCE** for Industry 4.0 domain code.

## Snippets

> "Schema-constrained planning to generate verifiable task graphs before execution."

> "ParallelWorkflow dynamically schedules tasks whose dependencies are satisfied."
