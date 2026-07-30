---
title: Cost-aware tool acquisition stopping (scores ≠ decisions)
type: concept
tags: [concept, tools, cost, stopping, k229]
keywords: [CAM-DF, acquisition depth, heterogeneous costs, ranking]
related:
  - sources/arxiv-cam-df-cost-aware-tool-stopping-2607.27083.md
  - concepts/confidence-aware-tool-orchestration.md
  - concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-cam-df-cost-aware-tool-stopping-2607.27083.md`
- `@concepts/confidence-aware-tool-orchestration.md`
- `@concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md`
- `@concepts/token-economics-and-prompt-caching.md`

## Raw Concept

A tool ranking answers priority — not how many tools are worth acquiring under heterogeneous costs.

## Narrative

**CAM-DF** learns stopping over ranked prefixes from the offline gap (stop now vs best continuation). Score-only / fixed thresholds are suboptimal when costs differ. Live result: **37%** fewer tools exposed vs full access with comparable success (1,343 tasks).

**Cemini steal:** After hybrid Top-k recommend (K190), add a **cost-aware depth stop** before binding tools into context. Lazy skill trees (K164) already reduce schema dump — CAM-DF addresses the remaining "how many ranked tools?" decision.

**Verdict:** **ADOPT** pre-execution plugin idea. **NO-GO** code (no artifact).
