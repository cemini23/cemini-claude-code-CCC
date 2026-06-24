---
title: BioInsight multi-agent biomedical evidence UI (arXiv 2606.20997)
type: source
tags: [source, arxiv, multi-agent, biomedical, k124]
keywords: [2606.20997, evidence-artifacts, interactive-dashboard]
related:
  - concepts/multi-agent-evidence-artifact-layers.md
  - concepts/subagent-orchestration.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/cross-wiki-routing.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@concepts/multi-agent-evidence-artifact-layers.md` — evidence/synthesis/interface layer pattern (CCC steal-from)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | BioInsight: Multi-Agent Orchestration for Interactive Biomedical Knowledge Discovery |
| **Authors** | Wang et al. (PKU, UIUC, UPenn, Purdue, Stanford) |
| **arXiv** | 2606.20997v1 [cs.AI] |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2606.20997-bioinsight-multi-agent-orchestration-for-interac.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (architecture + typed artifacts) |

## Narrative

**BioInsight** — multi-agent harness producing **typed intermediate artifacts** (pathways, literature packets, reasoning notes, citation-grounded reports, dashboard schemas, rendered UI) from disease + protein association inputs.

Three functional layers: **Evidence** (search/retrieval), **Synthesis** (reasoning + summarization agents), **Interface** (visualization agent → interactive dashboard). Deterministic citation normalization; same structured evidence feeds report and UI.

**Cross-wiki routing:** domain content is biomedical — **not CCC prod**. Steal the **evidence → synthesis → explorable artifact** decomposition for wiki/deep-research deliverables (canvas, structured briefs). **REFERENCE** only.

## Snippets

> "BioInsight organizes disease-specific evidence through typed intermediate artifacts, including ranked pathways, literature evidence packets, protein-level reasoning notes, citation-grounded reports, dashboard schemas, and rendered interactive interfaces."
> — [Source: arxiv-2606.20997-bioinsight-multi-agent-orchestration-for-interac.pdf abstract, retrieved 2026-06-24]
