---
title: "DataFlow-Harness — grounded code-agent platform for NL2Pipeline"
type: source
tags: [source, arxiv, harness, mcp, skills, dag, nl2pipeline, k197]
keywords: [2607.16617, DataFlow-Harness, OpenDCAI, typed mutations, DataFlow-Skills]
related:
  - concepts/nl2pipeline-platform-grounded-mutations.md
  - entities/tools/dataflow-opendcai.md
  - concepts/code-as-agent-harness.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/brief-k197-k201-harness-solver-pruner-2026-07-21.md
maturity: draft
created: 2026-07-21
updated: 2026-07-21
---

## Relations

- `@concepts/nl2pipeline-platform-grounded-mutations.md` — synthesized steal
- `@entities/tools/dataflow-opendcai.md` — Apache DataFlow platform peer
- `@concepts/code-as-agent-harness.md` — harness peer
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md` — grounded synthesis peer (K172)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | DataFlow-Harness: A Grounded Code-Agent Platform for Constructing Editable LLM Data Pipelines |
| **Author** | Runming He, Zhen Hao Wong, Hao Liang, et al. (PKU / IAAR / Zhongguancun) |
| **arXiv** | 2607.16617 |
| **Pages** | 13 |
| **Retrieved** | 2026-07-21 |
| **Code** | Paper cites `OpenDCAI/DataFlow-WebUI` (no SPDX on WebUI). Platform peer `OpenDCAI/DataFlow` — **Apache-2.0** |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.16617-dataflow-harness-a-grounded-code-agent-platform.pdf` |

## Narrative

### Thesis

**NL2Pipeline gap:** coding agents emit disposable scripts; production needs persistent, editable, governable DAG artifacts. DataFlow-Harness guides agents via typed incremental mutations + DataFlow-Skills + MCP live operator registry + visual WebUI sync.

### Results [TENTATIVE — single paper]

- 12-task data-engineering bench: **93.3%** end-to-end pass
- vs Vanilla Claude Code: **−72.5%** cost, **−49.9%** latency
- Within **0.9 pp** of Context-Aware Claude Code pass rate at **−42.8%** cost

### CCC steal

Prefer **platform-grounded mutations** (live registry + typed ops) over free-form script generation when the artifact must stay editable. Skills most useful when procedural knowledge is implicit.

## Snippets

> "We call this disconnect the NL2Pipeline gap."
> — Abstract

> "live platform grounding can produce persistent, editable workflow artifacts … with lower measured construction cost and latency"
> — Abstract
