---
title: "RecToolBench: Benchmarking Recommendation-Specific Tool Orchestration under Fuzzy User Intent (CCC K396)"
type: source
tags: [source, arxiv, k396]
keywords: [2609.30717, k396]
related:
  - concepts/recommendation-tool-orchestration-fuzzy-intent-eval.md
  - briefs/2026-09-28_ccc-k396-k400-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-28
updated: 2026-09-28
---

## Relations

- `@concepts/recommendation-tool-orchestration-fuzzy-intent-eval.md`
- `@briefs/2026-09-28_ccc-k396-k400-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | RecToolBench: Benchmarking Recommendation-Specific Tool Orchestration under Fuzzy User Intent |
| **arXiv** | 2609.30717 (2026-09) |
| **Retrieved** | 2026-09-28 |

## Narrative

**Verdict: ADOPT eval-first.**

**RecToolBench** evaluates **recommendation-specific tool orchestration** when user intent is **fuzzy** — not generic tool-use alone (pairs K316 LifePlanner constraint integration / K259 tool grounding / K318 step-wise routing). Treat rec-domain orchestration as its own harness axis. No clone unless SPDX. Runtime **`wont_wire`**; concept **`policy_wired`**.

**Deep-read note:** RecToolBench is MCP-native with 1200+ fuzzy rec tasks; valid syntax ≠ successful rec — pairs K311 lazy MCP load / K369 closed-world validation.


## Snippets

> "However, existing benchmarks often assume explicit user intent, simplified tool environments, or isolated function calls, leaving realistic tool orchestration for recommendation underexplored." [Source: arXiv 2609.30717 abstract (retrieved 2026-09-28)]

> "RecToolBench contains more than 1,200 executable tasks across three recommendation domains, 13 MCP servers, and 32 tools, spanning single-tool calls, parallel tool calls, sequential tool chains, and hybrid tool orchestration." [Source: arXiv 2609.30717 abstract (retrieved 2026-09-28)]

> "Experiments on representative LLMs show that syntactically valid tool calls do not guarantee successful recommendations." [Source: arXiv 2609.30717 abstract (retrieved 2026-09-28)]

> "Our results identify tool orchestration under fuzzy user intent as a major bottleneck for agentic recommender systems." [Source: arXiv 2609.30717 abstract (retrieved 2026-09-28)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.30717-rectoolbench-benchmarking-recommendation-specifi.pdf` (local inbox pending archive) |
| **Code** | `https://github.com/ShawnChenn/RecToolBench` — **MIT** [CONFIRMED via GitHub API 2026-09-28] |

