---
title: DynAMO — topological multi-agent workflow engine
type: entity
tags: [tool, orchestration, dynamo, industry-4, k120]
keywords: [kushwaha001, dynamo, assetopsbench, apache-2.0]
related:
  - sources/arxiv-dynamo-topological-orchestration-2606.19382.md
  - concepts/plan-then-execute-topological-orchestration.md
  - concepts/skill-vetting.md
  - entities/patterns/scatter-gather.md
maturity: draft
created: 2026-06-20
updated: 2026-06-20
---

## Relations

- `@sources/arxiv-dynamo-topological-orchestration-2606.19382.md` — arXiv 2606.19382
- `@concepts/plan-then-execute-topological-orchestration.md` — pattern synthesis
- `@concepts/skill-vetting.md` — Phase-0 gate
- `@entities/patterns/scatter-gather.md` — parallel scheduling peer

## Raw Concept

`github.com/kushwaha001/DynAMO` — Plan-then-Execute workflow engine for AssetOpsBench industrial agent tasks.

## Narrative

| Field | Value |
|-------|-------|
| **Repo** | `kushwaha001/DynAMO` |
| **License** | Apache-2.0 (API verified 2026-06-20) |
| **Stars** | ~2 (2026-06-20) |
| **Benchmark** | AssetOpsBench (141 queries; IoT/FMSR/TSFM/WO agents) |
| **Model eval** | Llama-4-Maverick-17B (paper appendix) |

### CCC posture

| Verdict | **REFERENCE** — orchestration pattern steal; NO-GO Cemini prod (industrial IoT domain) |

Steal: validated DAG before execution; parallel ready-set scheduling; context pruning per workflow node.

## Snippets

> "Dynamic Asset Management Orchestration via Topological Multi-Agent Scheduling."

> — [Source: arxiv-2606.19382-dynamo-dynamic-asset-management-orchestration-vi.pdf]
