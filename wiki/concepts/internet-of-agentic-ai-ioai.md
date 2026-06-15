---
title: Internet of Agentic AI (IoAI) — vision survey synthesis
type: concept
tags: [concept, ioai, federation, multi-agent, discovery, trust, k114]
keywords: [2606.12835, ioai, controlled-emergence, agent-discovery, semantic-interoperability]
related:
  - sources/arxiv-internet-of-agentic-ai-2606.12835.md
  - concepts/openagenet-trusted-agent-discovery.md
  - concepts/cross-wiki-routing.md
  - entities/tools/conductor-mcp.md
  - concepts/subagent-orchestration.md
  - entities/mcp-servers/librarian-kb-server.md
  - concepts/agents-k1-agent-native-knowledge-orchestration.md
maturity: draft
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- `@sources/arxiv-internet-of-agentic-ai-2606.12835.md` — arXiv 2606.12835 provenance
- `@concepts/openagenet-trusted-agent-discovery.md` — proposed trust/discovery layer below MCP
- `@concepts/cross-wiki-routing.md` — where federation content lives
- `@entities/tools/conductor-mcp.md` — bounded cross-wiki router (not open IoAI)
- `@concepts/subagent-orchestration.md` — harness-local MAS vs Internet-scale MAS
- `@entities/mcp-servers/librarian-kb-server.md` — 24/7 federation knowledge serving
- `@concepts/agents-k1-agent-native-knowledge-orchestration.md` — knowledge substrate for agent networks

## Raw Concept

2606.12835 **IoAI** vision: open ecosystem where heterogeneous agents **discover**, **negotiate**, **coordinate**, and **execute** workflows across organizational and infrastructure boundaries — with **controlled emergence** under trust and governance constraints.

## Narrative

### Layer stack (CCC mapping) [TENTATIVE — vision paper]

| IoAI concern | Cemini federation analog | Gap |
|--------------|---------------------------|-----|
| Discovery / directory | lazy-tool catalog, conductor, MCP server list | Private; no open agent marketplace |
| Semantic interoperability | `@wiki-alias/path` cross-wiki links, kb-server ingest | Human-curated wiki, not agent-native KG |
| Trust / identity | skill-vetting Phase-0, OAN REFERENCE | No production DID/VC layer |
| Resource orchestration | Tier1/Tier2, token economics | Laptop + Hetzner, not elastic agent economies |
| Governance | CLAUDE.md schema, wiki lint, maturity tags | Operator-governed, not on-chain |

### Controlled emergence

Useful collective behavior from local agent interactions **without** sacrificing predictability, alignment, or accountability. Contrasts with both rigid centralized orchestration and unbounded autonomous swarms. Research agenda: incentive-compatible coordination, secure identity, resource-aware orchestration, governance at scale.

### Deployment models (steal-from vocabulary)

Cloud (planner agents), edge (low-latency controllers), on-device (privacy), federated (cross-institution without centralizing raw data), elastic (ephemeral workers), agent economies (market-based compute/data). Cemini already spans **laptop authoring** + **librarian serving** + **prod stack** — a three-tier private IoAI slice.

### Posture

| Scope | Verdict |
|-------|---------|
| CCC meta-wiki | **REFERENCE** — vocabulary for federation briefs, OAN/MCP surveys, trust architecture discussions |
| Cemini prod | **NO-GO** on open agent discovery until trust layer + license audit |
| OSINT / librarian | Monitor Agents-K1 + kb-server scaling as knowledge-layer complement |

IoAI is the **Internet-scale** framing; `@concepts/cross-wiki-routing.md` + conductor is the **operator-scale** implementation today.

## Snippets

> "Just as the Internet transformed isolated computers into a global information infrastructure, IoAI seeks to transform isolated agents and bounded multi-agent systems into a distributed ecosystem of interoperable intelligence."

> "Autonomy and control are not opposites."

> — [Source: arxiv-2606.12835-the-internet-of-agentic-ai-communication-coordin.pdf §1,3, retrieved 2026-06-13]
