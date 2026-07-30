---
title: "CAM-DF — cost-aware stopping for tool acquisition"
type: source
tags: [source, arxiv, tools, cost, stopping, k229]
keywords: [2607.27083, CAM-DF, scores-are-not-decisions, tool acquisition]
related:
  - concepts/cost-aware-tool-acquisition-stopping.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md
  - concepts/token-economics-and-prompt-caching.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@concepts/cost-aware-tool-acquisition-stopping.md`
- `@concepts/confidence-aware-tool-orchestration.md`
- `@concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scores Are Not Decisions: Cost-Aware Stopping for Tool Acquisition in LLM Agents |
| **Author** | Feng, Zhang, Cheng, Qi |
| **arXiv** | 2607.27083 |
| **Pages** | 23 |
| **Retrieved** | 2026-07-30 |
| **Code** | no public artifact at Phase-0 — **NO-GO** |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.27083-scores-are-not-decisions-cost-aware-stopping-for.pdf` |

## Narrative

Ranking ≠ acquisition depth. **CAM-DF** learns cost-aware stopping over ranked prefixes (1,343 tasks). Live: **37%** fewer tools vs full access, comparable success. Score-only thresholds suboptimal under heterogeneous costs. **ADOPT** as pre-execution plugin pattern; **NO-GO** code.
