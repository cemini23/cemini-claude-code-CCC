---
title: Hybrid static–dynamic MCP tool security (MTGuard)
type: concept
tags: [concept, mcp, security, hybrid-analysis, k221]
keywords: [MTGuard, lifecycle co-analysis, tool poisoning, FPR]
related:
  - sources/arxiv-mtguard-hybrid-mcp-tool-security-2607.25297.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
  - concepts/mcp-session-sequential-attack-detection.md
  - concepts/schema-bound-mcp-tool-surface.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-mtguard-hybrid-mcp-tool-security-2607.25297.md`
- `@concepts/mcp-security-signals-vs-runtime-evidence.md`
- `@concepts/mcp-session-sequential-attack-detection.md`
- `@concepts/schema-bound-mcp-tool-surface.md`

## Raw Concept

When is static MCP inspection enough, and when must runtime behavior co-analyze the tool-invocation lifecycle?

## Narrative

**Problem:** Poisoned/compromised MCP tools can look benign in prompts/descriptions while executing harmful side effects. Static-only defenses (prompt/output inspection) are brittle.

**Pattern (MTGuard):** Lifecycle-aware **static–dynamic co-analysis** — static view supplies semantic context of the declared call; dynamic view observes executed behavior; mismatches trigger deny. Reported avg FPR **3.7%** across six agent/model configs.

**Cemini steal:** Pair FlowGuard-style evidence (K189) + session sequential detection (K206) with a **declared-vs-executed** mismatch gate before irreversible host actions. Prefer execution evidence over description heuristics.

**Verdict:** **ADOPT** checklist. **NO-GO** MTGuard code (no public SPDX artifact).

## Snippets

> MTGuard … lifecycle-aware static-dynamic co-analysis. [Source: arXiv 2607.25297]
