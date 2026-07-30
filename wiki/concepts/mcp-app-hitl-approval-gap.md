---
title: MCP app HITL approval gap (empirical)
type: concept
tags: [concept, mcp, hitl, empirical, k223]
keywords: [MCPAppTax, blocking approval, 37.2%, 1723]
related:
  - sources/arxiv-empirical-mcp-applications-hitl-2607.25635.md
  - concepts/production-agent-deployment-checklist.md
  - concepts/enterprise-mcp-adoption-practice.md
  - concepts/acp-mcp-three-layer-human-agent-execution.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - sources/brief-k221-k229-mcp-harness-security-ingest-2026-07-30.md
maturity: draft
created: 2026-07-30
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-empirical-mcp-applications-hitl-2607.25635.md`
- `@concepts/production-agent-deployment-checklist.md`
- `@entities/patterns/tier1-tier2-agent-model.md`

## Raw Concept

How often do real MCP-consuming apps gate tool execution behind a blocking human approval step?

## Narrative

Across **1,723** GitHub MCPApps: file config 85.2%, official SDK 81.1%, logging 90.8%, enable/disable 77.2%, but **blocking approval only 37.2%**. Most apps let any enabled tool run unconditionally.

**Cemini steal:** Logging ≠ control. Prefer Cursor/Claude Code approval modes + Tier-2 gates for write/network/secret-touching tools. Treat "enable/disable server" as insufficient alone.

**Verdict:** **ADOPT** default blocking gate for consequential tools. Study only — **NO-GO** install.
