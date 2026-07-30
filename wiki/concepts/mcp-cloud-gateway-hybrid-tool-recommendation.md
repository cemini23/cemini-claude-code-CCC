---
title: MCP cloud gateway — hybrid tool recommendation at the data plane
type: concept
tags: [concept, mcp, gateway, tool-recommendation, hybrid-retrieval, session-affinity, k190]
keywords: [2607.15593, Top-15, lexical+semantic, protocol adaptation, lazy-tool peer]
related:
  - sources/arxiv-scalable-mcp-cloud-gateway-2607.15593.md
  - entities/tools/agentgateway.md
  - entities/tools/lazy-tool.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/mcp-context-optimization.md
  - concepts/slm-agent-orchestration-gateway.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
  - sources/arxiv-agentic-ai-5g6g-survey-2607.16066.md
  - concepts/cost-aware-tool-acquisition-stopping.md
  - sources/arxiv-cam-df-cost-aware-tool-stopping-2607.27083.md
maturity: draft
created: 2026-07-20
updated: 2026-07-30
---

## Relations

- `@sources/arxiv-scalable-mcp-cloud-gateway-2607.15593.md` — provenance
- `@entities/tools/agentgateway.md` — OSS MCP/agent proxy to study (not Alibaba)
- `@entities/tools/lazy-tool.md` — client-side catalog shrink
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — K164 tree routing
- `@concepts/mcp-context-optimization.md` — cost stack
- `@concepts/slm-agent-orchestration-gateway.md` — earlier gateway pattern (K95)

## Raw Concept

K190 — Alibaba production MCP gateway paper. Problem: thousands of tools + stateful replicas. Steal: **hybrid lexical+semantic pre-filter before LLM tool selection**, plus session-aware routing when MCP state lives server-side.

## Narrative

### Problem class

| Layer | Failure without gateway |
|-------|-------------------------|
| Provider | Legacy OpenAPI not MCP; protocol churn |
| Agent | Context window + latency + success drop when mounting huge catalogs |
| Runtime | Body-carried session keys defeat stock L7 balancers |

### Steal checklist (ADOPT pattern)

1. Never dump 1000+ tool schemas into Claude/Cursor turns — pre-filter to Top-k (paper: Top-15 @ 98% recall).
2. Prefer **hybrid** match: MCP tool *names* are lexical gold; embeddings alone miss domain jargon → query rewrite with domain glossary when needed.
3. If MCP backends are stateful multi-replica, pin session at proxy — do not invent client-side replica affinity.
4. Alibaba code: **NO-GO**. Evaluate OSS `agentgateway` as REFERENCE/CONDITIONAL local study only.

### Cemini map

| Surface | Action |
|---------|--------|
| lazy-tool / Cursor multi-MCP | Keep; gateway pattern is fleet-scale sibling |
| TipDrop bots | Cap visible tools per turn; name-aware search before LLM |
| Prod MCP | Session affinity only if stateful servers appear |

| Verdict | **ADOPT** hybrid Top-k + session-affinity checklist; **NO-GO** Alibaba install; **CONDITIONAL-GO** study clone of agentgateway |

## Snippets

> "Tool Recommendation … hybrid matching method combining semantic and lexical matching"
> — [Source: arxiv-2607.15593]
