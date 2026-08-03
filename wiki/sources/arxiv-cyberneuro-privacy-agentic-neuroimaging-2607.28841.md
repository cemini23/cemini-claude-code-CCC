---
title: "CyberNeuro — privacy-preserving agentic neuroimaging workbench"
type: source
tags: [source, arxiv, mcp, multi-agent, local-first, neuroimaging, k234]
keywords: [2607.28841, CyberNeuro, WandaMind, NeuroBench, HITL, skill DAG]
related:
  - concepts/local-first-mcp-multi-agent-workbench.md
  - entities/tools/cyberneuro.md
  - concepts/mcp-app-hitl-approval-gap.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
maturity: draft
created: 2026-08-03
updated: 2026-08-03
---

## Relations

- `@concepts/local-first-mcp-multi-agent-workbench.md`
- `@entities/tools/cyberneuro.md`
- `@concepts/mcp-app-hitl-approval-gap.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CyberNeuro: A Privacy-Preserving Agentic Workbench for Neuroimaging |
| **Author** | (Wanda / neuroimaging team — arXiv metadata) |
| **arXiv** | 2607.28841 |
| **Pages** | 25 |
| **Retrieved** | 2026-08-03 |
| **Code/Availability** | No public CyberNeuro repo; product site https://wanda-cyberbench.com (HTTP 401 at fetch). Cited Wanda core `github.com/MEKOMIKU/cc-haha` → 404. NeuroClaw MIT `github.com/CUHK-AIM-Group/NeuroClaw` (~60MB) is a *different* baseline — REFERENCE pointer only; **not cloned** |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.28841-cyberneuro-a-privacy-preserving-agentic-workbenc.pdf` |

## Narrative

Privacy-preserving, **local-first** agentic neuroimaging workbench — no outbound network by default. Four agents (Planner, Validator, Dispatcher, Reporter) over a secure MCP bridge with pinned execution. Skills via SKILL.md + typed contracts compile to a task DAG. HITL verification panel for biomedical QC.

**Results:** NeuroBench held-out domain accuracy 40%→69%; local WandaMind ~10.6% token usage vs NeuroClaw baseline; cloud ~61.7% of NeuroClaw tokens.

**Domain:** Neuroimaging is OOD for Cemini ops.

| Verdict | **ADOPT** local-first MCP multi-agent + skill-DAG + HITL panel patterns. **NO-GO** product install (gated site; no public code). Code adopt: none |
