---
title: "SearchOS-V1 — robust open-domain information-seeking agent collaboration"
type: source
tags: [source, arxiv, multi-agent, search, context, harness, k180]
keywords: [2607.15257, SearchOS, SOCM, Evidence Graph, Failure Memory, Ant Group]
related:
  - concepts/searchos-socm-explicit-search-state.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/mcp-multi-agent-graceful-degradation-stack.md
  - concepts/verifiable-search-agent-environment.md
  - entities/tools/searchos.md
  - sources/brief-k180-searchos-socm-2026-07-17.md
maturity: draft
created: 2026-07-17
updated: 2026-07-17
---

## Relations

- `@concepts/searchos-socm-explicit-search-state.md` — synthesized steal
- `@entities/tools/searchos.md` — Phase-0 MIT GO; local adopt `.local/adopts/SearchOS`
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — hierarchical skills peer (K164)
- `@sources/brief-k180-searchos-socm-2026-07-17.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration |
| **Author** | Zhang, Gao, et al. (RUC + Ant Group) |
| **arXiv** | 2607.15257 |
| **Pages** | 27 |
| **Code** | `github.com/antins-labs/SearchOS` — **MIT** |
| **Retrieved** | 2026-07-17 |

## Narrative

Open-domain search agents lose track of progress and loop on failed queries. SearchOS externalizes state via **SOCM** (Search-Oriented Context Management): Frontier Task, Evidence Graph, Coverage Map, Failure Memory. Pipeline-parallel scheduling fills slots with unresolved coverage gaps. **Search Tool Middleware Harness** intercepts model/tool I/O to ground evidence and react to stalls/budget exhaustion. Hierarchical strategy/access skills avoid repeating failed patterns. Leads WideSearch/GISA among evaluated systems.

## Snippets

> "turns fragile, implicit search progress into explicit, persistent, and shared state" — Abstract
