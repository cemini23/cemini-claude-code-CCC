---
title: "Scalable LLM Agent Tool Access in the Cloud — MCP gateway (Alibaba)"
type: source
tags: [source, arxiv, mcp, gateway, tool-recommendation, cloud, k190]
keywords: [2607.15593, MCP gateway, hybrid retrieval, Top-15, session affinity, Alibaba Cloud]
related:
  - concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md
  - entities/tools/agentgateway.md
  - entities/tools/lazy-tool.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/mcp-context-optimization.md
  - sources/brief-k190-k194-mcp-gateway-toolverse-tars-2026-07-20.md
maturity: draft
created: 2026-07-20
updated: 2026-07-20
---

## Relations

- `@concepts/mcp-cloud-gateway-hybrid-tool-recommendation.md` — synthesized steal
- `@entities/tools/agentgateway.md` — open-source peer cited by paper (not Alibaba code)
- `@entities/tools/lazy-tool.md` — client-side lazy tool surface peer
- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — K164 hierarchy peer
- `@concepts/mcp-context-optimization.md` — four-layer MCP cost stack

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Scalable LLM Agent Tool Access in the Cloud |
| **Author** | Mingxin Li, Enge Song, Yueshang Zuo, et al. (Nanjing U / Alibaba Cloud / Fudan / …) |
| **arXiv** | 2607.15593 |
| **Pages** | 20 |
| **Retrieved** | 2026-07-20 |
| **Code** | Alibaba gateway proprietary — **NO-GO**. Related OSS: `agentgateway/agentgateway` (Apache-2.0) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.15593-scalable-llm-agent-tool-access-in-the-cloud.pdf` |

## Narrative

### Thesis

MCP at cloud scale breaks direct-connect assumptions: legacy OpenAPI is not MCP-callable, protocol churn hurts providers, agents cannot mount thousands of tools in-context, and stateful MCP replicas need session affinity that L7 balancers do not see (routing keys live in HTTP body).

### System

Gateway on the data plane: protocol adaptation (legacy API ↔ MCP + variant bridging), auth offload, **hybrid lexical+semantic tool recommendation**, session-aware routing across replicas.

### Results [TENTATIVE — single production deployment paper]

- Hybrid retrieval: **98% Top-15 recall**
- Scales agent tool access to **3,000+** tools
- Tool selection time **8.9×** faster; token usage **23.8×** lower vs mounting full catalogs

### CCC steal

Prefer **gateway- or proxy-side pre-filter** (hybrid name+embedding) before the LLM sees tools — same problem class as lazy-tool / K164, solved one hop closer to the fleet. Do not adopt Alibaba's proprietary stack.

## Snippets

> "Hybrid retrieval sustains 98% Top-15 recall; it scales agent tool access to 3,000+ with high tool selection accuracy, and reduces tool selection time by 8.9× and token usage by 23.8×"
> — Abstract

> "traditional L7 load balancers cannot be directly applied to MCP"
> — Conclusion
