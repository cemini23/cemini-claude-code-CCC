---
title: "HyperBrowseComp — the bar for browsing agents (CCC k282 route)"
type: concept
tags: [concept, k282, cross-wiki]
keywords: [2610.03574, k282]
related:
  - sources/arxiv-hyperbrowsecomp-browsing-eval-bar-2610.03574.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-05_k282-ccc-agent-eval-route.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@sources/arxiv-hyperbrowsecomp-browsing-eval-bar-2610.03574.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-05_k282-ccc-agent-eval-route.md`

## Raw Concept

Routed from `@osint-wiki` via `@briefs/2026-10-05_k282-ccc-agent-eval-route.md` (arXiv 2610.03574). Canon stays on OSINT.

## Narrative

**423 questions, 13 languages, multimodal.** Strongest configuration reaches **31.68%** accuracy; humans score **15/30**; and **57.68% of failures are shared across configurations**. **CCC reading:** the shared-failure number is the one that matters. When a majority of failures are common to every configuration, **the bottleneck is the task type, not any single model or harness** — which means a better model will not fix it and a better harness may not either. That is a useful ceiling to know before commissioning a browsing-agent eval. The benchmark also **exercises Exa**, the workspace's external-research path, so it is the reference shape if CCC ever builds one. Pairs `@concepts/deep-research-evaluation-prompt.md` / `@concepts/verifiable-search-agent-environment.md` / K426 MCPacific (tool discovery at scale). **No clone, no install.**

## Snippets

> "See source page for arXiv 2610.03574 locators." [Source: CCC k282 synthesis]
