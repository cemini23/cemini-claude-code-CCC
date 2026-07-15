---
title: Multi-agent evidence artifact layers
type: concept
tags: [concept, multi-agent, evidence, deliverables, k124]
keywords: [2606.20997, evidence-layer, synthesis-layer, interface-layer]
related:
  - sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md
  - concepts/subagent-orchestration.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/deep-research-evaluation-prompt.md
  - concepts/cross-wiki-routing.md
  - concepts/subagent-orchestration.md
  - sources/brief-k124-harness-policy-hands-on-2026-06-24.md
  - concepts/web-scale-scientific-collaboration-infrastructure.md
  - sources/arxiv-clarus-scientific-collaboration-infrastructure-2606.30246.md
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - sources/arxiv-large-cancer-assistant-lca-2607.06531.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
maturity: draft
created: 2026-06-24
updated: 2026-07-15
---

## Relations

- `@sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md` — BioInsight provenance (biomedical domain)
- `@concepts/cross-wiki-routing.md` — domain routing; biomedical content stays in source page

## Raw Concept

How should multi-agent research systems structure outputs so users can inspect evidence, not just read final prose?

## Narrative

From **BioInsight** (2606.20997) — three-layer decomposition applicable beyond biomedicine:

| Layer | Agent role | CCC analogue |
|-------|------------|--------------|
| **Evidence** | Retrieve, rank, normalize citations | Exa/Brave fetch → `wiki/sources/` |
| **Synthesis** | Reason, summarize, hypothesis notes | Ingest discussion → concept pages |
| **Interface** | Render explorable artifact | Canvas (`.canvas.tsx`), structured briefs |

**Steal-from for CCC ingest:** typed intermediate artifacts (source page draft, entity stubs, lint matrix) before final narrative — mirrors BioInsight's separation of retrieval from reasoning from presentation.

**K150 SIP:** LCA's Standardized Intermediate Payload is the clinical-domain instance of the same boundary — typed payload between orchestration and volatile downstream (`@concepts/algorithmic-impermeability-model-agnostic-orchestration.md`).

**Verdict:** **REFERENCE** pattern — domain-specific biomedical tooling **NO-GO** for CCC prod.

## Snippets

> "Biomedical AI systems should move beyond text-only and static reports toward provenance-preserving, interactive evidence artifacts."
> — [Source: arxiv-2606.20997 abstract, retrieved 2026-06-24]
