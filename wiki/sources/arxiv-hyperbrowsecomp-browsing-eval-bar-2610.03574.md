---
title: "HyperBrowseComp — the bar for browsing agents (CCC k282 route)"
type: source
tags: [source, arxiv, k282, cross-wiki]
keywords: [2610.03574, k282]
related:
  - concepts/browsing-agent-eval-bar.md
  - briefs/2026-10-05_k282-ccc-agent-eval-route.md
  - "@osint-wiki/sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md"
maturity: draft
read_status: skimming
cross-wiki-source: "@osint-wiki/sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md"
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@concepts/browsing-agent-eval-bar.md`
- `@briefs/2026-10-05_k282-ccc-agent-eval-route.md`
- `@osint-wiki/sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md` — cross-wiki canon (deep read lives there)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | HyperBrowseComp — the bar for browsing agents |
| **arXiv** | 2610.03574 (2026-10) |
| **Canon** | `@osint-wiki/sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md` |
| **Routed by** | `@briefs/2026-10-05_k282-ccc-agent-eval-route.md` |

## Narrative

**423 questions, 13 languages, multimodal.** Strongest configuration reaches **31.68%** accuracy; humans score **15/30**; and **57.68% of failures are shared across configurations**. **CCC reading:** the shared-failure number is the one that matters. When a majority of failures are common to every configuration, **the bottleneck is the task type, not any single model or harness** — which means a better model will not fix it and a better harness may not either. That is a useful ceiling to know before commissioning a browsing-agent eval. The benchmark also **exercises Exa**, the workspace's external-research path, so it is the reference shape if CCC ever builds one. Pairs `@concepts/deep-research-evaluation-prompt.md` / `@concepts/verifiable-search-agent-environment.md` / K426 MCPacific (tool discovery at scale). **No clone, no install.**

## Snippets

> "shared failure across configs means the bottleneck is the task type, not a single model." [Source: arXiv 2610.03574 via `@osint-wiki/sources/arxiv-2610.03574-hyperbrowsecomp-2026-10-05.md` (retrieved 2026-10-06)]
