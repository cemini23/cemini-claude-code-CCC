---
title: "CASCADE — agentic regulatory network MCP with claim-level validation"
type: source
tags: [source, arxiv, mcp, langgraph, bioinformatics, k259]
keywords: [2608.05359, CASCADE, jab57, ARACNe, patient-data-validation, tool-grounding]
related:
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - entities/tools/cascade-mcp.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - concepts/canary-tools-mcp-selection-diagnosis.md
  - sources/brief-k259-cascade-mcp-claim-validation-2026-08-08.md
  - briefs/2026-08-08_ccc-handoff-k259-cascade-ingest.md
maturity: draft
created: 2026-08-08
updated: 2026-08-08
---

## Relations

- `@concepts/mcp-claim-validation-and-parameter-grounding.md`
- `@entities/tools/cascade-mcp.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CASCADE: An Agentic Regulatory Network Framework for Patient-Data-Validated Downstream Perturbation Prediction |
| **arXiv** | 2608.05359 |
| **Author** | Jose A. Bird |
| **Repo** | `jab57/CASCADE` — MIT SPDX; Zenodo DOI 10.5281/zenodo.21774774 |
| **Domain** | Cancer systems biology + LangGraph/MCP agent harness |
| **Retrieved** | 2026-08-08 |

## Narrative

LangGraph-orchestrated MCP server predicts downstream transcriptional effects of gene perturbation via ARACNe networks. Central Cemini steal is methodological: validate the **directional claim an MCP tool would surface** against real patient genotype–expression proxies (not curated membership lists). Separate eval: NL → MCP parameter grounding (35 queries) — schema failures model-size-dependent; aliases fixed server-side; confident wrong defaults on ambiguous queries resist server-side “unset” guards.

Bio product **OOD** for CCC runtime. Clone REFERENCE without optional DepMap (~413MB) / model download.

| Verdict | **ADOPT** claim-level MCP validation + parameter-grounding failure taxonomy. **GO** MIT REFERENCE `.local/adopts/CASCADE` (~352MB shallow). **wont_wire** runtime. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.05359-cascade-an-agentic-regulatory-network-framework.pdf` (archived 2026-08-08).
