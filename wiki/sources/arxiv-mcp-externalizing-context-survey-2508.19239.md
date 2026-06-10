---
title: MCP-inspired adaptive systems survey (arXiv 2508.19239)
type: source
tags: [source, arxiv, mcp, survey, adaptive-systems, k109]
keywords: [2508.19239, mcp, context-externalization, adaptive-transport, taxonomy]
related:
  - concepts/mcp-adaptive-systems-context-survey.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
maturity: draft
read_status: skimmed
created: 2026-06-10
updated: 2026-06-10
---

## Relations

- `@concepts/mcp-adaptive-systems-context-survey.md` — CCC routing stub (prospective MCP deployments)
- `@concepts/mcp-context-optimization.md` — Claude Code cost stack vs transport/adaptive-systems lens
- `@concepts/mcp-server-runtime-fault-taxonomy.md` — runtime fault classes complement protocol survey

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Externalizing Context for Autonomous and Adaptive Systems: A Survey of MCP-Inspired Architectures and Evaluation |
| **Authors** | Chhetri et al. (Texas State University) |
| **arXiv** | 2508.19239v2 [cs.AI] |
| **Venue** | ACM Trans. Autonom. Adapt. Syst. (forthcoming) |
| **Location** | `raw-sources/arxiv-2508.19239-externalizing-context-for-autonomous-and-adaptiv.pdf` |
| **Retrieved** | 2026-06-10 |
| **Read status** | skimmed (abstract, MCP §4, taxonomy framing) |

## Narrative

Survey positions **Model Context Protocol** as a unifying substrate for **context sharing and adaptation** in distributed autonomous systems (transport, IoT, edge AI) — not Claude Code tooling alone. Introduces taxonomy of where adaptation logic resides and how context is represented/exchanged. Compares MCP to REST, message brokers, and domain middleware. Much of the transport/IoT application material is **prospective** rather than deployed MCP.

**CCC relevance:** broadens MCP vocabulary for federation docs; secondary to 2606.05339 fault taxonomy for day-to-day Claude Code reliability.

## Snippets

> "This survey examines the Model Context Protocol (MCP) as a unifying substrate for context sharing and adaptation in distributed autonomous systems."

> "Unless explicitly noted as deployed, the architectures and scenarios should be understood as prospective applications rather than existing MCP deployments."

> — [Source: arxiv-2508.19239-externalizing-context-for-autonomous-and-adaptiv.pdf §4, retrieved 2026-06-10]
