---
title: "MidTool — mid-training data synthesis for agentic tool use"
type: source
tags: [source, arxiv, mid-training, tool-use, mcp, k299]
keywords: [2608.20314, MidTool, MidTool-Mix, 20.3B tokens, affordance, argument grounding]
related:
  - concepts/mid-training-tool-use-affordance-grounding.md
  - entities/tools/midtool.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
maturity: draft
read_status: read
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@concepts/mid-training-tool-use-affordance-grounding.md`
- `@entities/tools/midtool.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MidTool: Mid-training Data Synthesis for Agentic Tool Use |
| **arXiv** | 2608.20314 |
| **Authors** | Jiang, Wang, Liu, Wang, Xu, Yao, Poovendran, He (UW / Snowflake / UNC) |
| **Code** | HF collection `MidTool/midtool-release` — **skip download** |
| **Retrieved** | 2026-08-21 |

## Narrative

First open **mid-training** pipeline/corpus for *general tool use*: **MidTool-Mix, a 20.3B-token mixture** built from four source families (web via FineWeb dumps, PDFs via FinePDFs, code, structured tool artifacts — real APIs + MCP skills) and two synthesis branches: **context-grounded trajectory augmentation** (grounding: tool boundaries, parameter inference, workflow recovery from messy docs) and **native agentic trajectory synthesis** (execution: multi-turn planning, clarification, recovery with explicit validation of schema grounding / turn order / required args / tool-response consistency). Teaches: recognize tool affordances, ground arguments from context, compose tool workflows, recover from incomplete information.

Mid-training Qwen3-4B-Base / Qwen3-8B-Base on MidTool-Mix then applying the same downstream SFT (+RL) **consistently improves** BFCL, τ²-Bench, and MCP Universe vs SFT-only baselines; gains largest on harder multi-turn/interactive settings; RL compounds. Capability boundary: benefits strongest for broad tool-use capability/transfer — specialized exploratory behaviors (deep search) need dedicated mid-training beyond a general tool-use mix.

| Verdict | **WATCH** — model-choice awareness only: dedicated tool-use mid-training beats leaving tool use to post-training. Runtime **`wont_wire`**; **do not download** HF `MidTool/midtool-release` weights/datasets. Pairs K259 (claim validation + parameter grounding). |

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.20314-midtool-mid-training-data-synthesis-for-agentic.pdf` |
