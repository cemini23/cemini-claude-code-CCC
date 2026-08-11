---
title: "The Scaffolding Matters More Than the Interface — MCP vs CLI cost study"
type: source
tags: [source, arxiv, mcp, cli, scaffolding, harness, k262]
keywords: [2608.08654, MCP, CLI, scaffolding, tool-cost]
related:
  - concepts/scaffold-over-tool-interface.md
  - entities/tools/scaffolding-mcp-cli-study.md
  - sources/brief-k261-k265-harness-wave-2026-08-11.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
maturity: draft
created: 2026-08-11
updated: 2026-08-11
---

## Relations

- `@concepts/scaffold-over-tool-interface.md`
- `@entities/tools/scaffolding-mcp-cli-study.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Scaffolding Matters More Than the Interface |
| **arXiv** | 2608.08654 |
| **Authors** | Alier Forment, Casañ Guerrero, García-Peñalvo, Pereira |
| **Code** | No public artifact found at Phase-0 |
| **Retrieved** | 2026-08-11 |

## Narrative

Controlled comparison: one fixed six-op git task × **seven agent scaffoldings** × **five LMs**. Completion verified by repository state (not agent self-report). Dominant cost/success driver = **scaffolding**, not MCP vs CLI interface. Two scaffolds without MCP completed all runs via CLI alone — MCP unnecessary for this task.

| Verdict | **ADOPT** scaffold-over-interface discipline. **NO-GO** code (none). |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.08654-the-scaffolding-matters-more-than-the-interface.pdf`