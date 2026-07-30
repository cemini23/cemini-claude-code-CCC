---
title: "MTGuard — hybrid analysis for secure MCP tool use"
type: source
tags: [source, arxiv, mcp, security, hybrid-analysis, k221]
keywords: [2607.25297, MTGuard, static-dynamic, co-analysis, tool poisoning]
related:
  - concepts/hybrid-static-dynamic-mcp-tool-security.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - concepts/mcp-session-sequential-attack-detection.md
  - concepts/schema-bound-mcp-tool-surface.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@concepts/hybrid-static-dynamic-mcp-tool-security.md`
- `@concepts/mcp-security-signals-vs-runtime-evidence.md`
- `@concepts/mcp-session-sequential-attack-detection.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Hybrid Analysis for Secure MCP Tool Use in LLM Agents |
| **Author** | Ping He, Yuexiang Xie, Yaliang Li, Shouling Ji (ZJU / Alibaba) |
| **arXiv** | 2607.25297 |
| **Pages** | 13 |
| **Retrieved** | 2026-07-30 |
| **Code** | no public MTGuard repo at Phase-0 (`antgroup/` org only) — **NO-GO** |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.25297-hybrid-analysis-for-secure-mcp-tool-use-in-llm-a.pdf` |

## Narrative

Static-only MCP defenses miss lifecycle mismatch (benign-looking call ≠ executed behavior). **MTGuard** = lifecycle-aware static–dynamic co-analysis. Avg FPR **3.7%** across six agent/model configs. **ADOPT** hybrid co-analysis checklist; **NO-GO** code until SPDX'd artifact.
