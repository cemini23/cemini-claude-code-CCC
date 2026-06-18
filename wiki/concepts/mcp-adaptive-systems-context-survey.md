---
title: MCP as adaptive-systems context substrate — transport/IoT survey lens
type: concept
tags: [concept, mcp, survey, adaptive-systems, k109]
keywords: [2508.19239, context-externalization, adaptive-transport, prospective-deployments]
related:
  - sources/arxiv-mcp-externalizing-context-survey-2508.19239.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
  - concepts/specification-driven-scientific-workflow-management.md
  - sources/arxiv-specification-to-execution-scientific-workflow-2606.18425.md
maturity: draft
created: 2026-06-10
updated: 2026-06-18
---

## Relations

- `@sources/arxiv-mcp-externalizing-context-survey-2508.19239.md` — ACM survey provenance
- `@concepts/mcp-context-optimization.md` — Claude Code four-layer cost stack (primary CCC MCP page)
- `@concepts/mcp-server-runtime-fault-taxonomy.md` — runtime fault classes for deployed MCP servers

## Raw Concept

arXiv **2508.19239** — survey framing MCP as **context externalization** substrate for autonomous/adaptive systems (transport, IoT, edge), with taxonomy of adaptation logic placement and context exchange.

## Narrative

Distinct from laptop Claude Code MCP wiring:

- Emphasizes **session semantics**, capability negotiation, multi-transport (stdio vs Streamable HTTP)
- Compares MCP to REST, MQTT/AMQP brokers, domain middleware
- Many scenarios are **prospective** — not documented production MCP deployments

**CCC use:** background when explaining MCP to non-CLI audiences; day-to-day harness work stays on `@concepts/mcp-context-optimization.md` + `@concepts/mcp-server-runtime-fault-taxonomy.md`.

## Snippets

> "We introduce a taxonomy that organizes MCP-inspired designs by where adaptation logic resides and how context is represented and exchanged."

> — [Source: arxiv-mcp-externalizing-context-survey-2508.19239.md, retrieved 2026-06-10]
