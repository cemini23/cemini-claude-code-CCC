---
title: CCC handoff — Robust-TO confidence orchestration ingest
type: brief
tags: [brief, ccc-handoff, mcp-eval, tool-confidence]
created: 2026-07-02
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/confidence-aware-tool-orchestration.md
updated: 2026-07-03
---

## Target

Claude Desktop / lazy-tool | prod MCP harness design

## Summary

Cybersec-wiki ingest 2026-07-02: arXiv **2606.26904** Robust-TO — confidence-aware tool orchestration (video CV origin; steal pattern for MCP). Phase-0 **Reference** (no public code).

## Body

### Why CCC cares

Tier-2 lazy-tool workers currently lack a standard **tool-output trust signal**. Robust-TO's **Blind Trust Problem** generalizes: agents fail silently when MCP returns degraded data but the planner proceeds at full confidence.

### Pattern to adopt

- `(result, confidence)` on every MCP wrapper
- Tiered evidence fusion before side effects
- Pair with ToolBench-X hazard eval (`@cybersecurity-wiki/concepts/tool-environment-unreliability-eval.md`)

Wiki: `@cybersecurity-wiki/concepts/confidence-aware-tool-orchestration.md`

### Eval stack (unchanged security lane)

| Layer | Wiki |
|-------|------|
| Security trajectories | `@cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md` |
| Tool hazards | `@cybersecurity-wiki/concepts/tool-environment-unreliability-eval.md` |
| Confidence calibration | **NEW** `@cybersecurity-wiki/concepts/confidence-aware-tool-orchestration.md` |

### Staged briefs

- `2026-07-02_robust-to-confidence-aware-tool-routing-handoff.md`
- `2026-07-02_prod-mcp-tool-confidence-contract-checklist.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2606-26904-confidence-aware-tool-orchestration-robust-to.md
- @cybersecurity-wiki/concepts/confidence-aware-tool-orchestration.md
