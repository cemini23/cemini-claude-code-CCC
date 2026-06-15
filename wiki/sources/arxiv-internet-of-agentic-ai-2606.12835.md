---
title: Internet of Agentic AI — communication and coordination at scale (arXiv 2606.12835)
type: source
tags: [source, arxiv, ioai, multi-agent, federation, survey, k114]
keywords: [2606.12835, ioai, internet-of-agentic-ai, discovery, trust, controlled-emergence]
related:
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/openagenet-trusted-agent-discovery.md
  - concepts/cross-wiki-routing.md
  - entities/tools/conductor-mcp.md
  - concepts/subagent-orchestration.md
  - entities/mcp-servers/librarian-kb-server.md
maturity: draft
read_status: skimmed
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- `@concepts/internet-of-agentic-ai-ioai.md` — CCC vision survey synthesis
- `@concepts/openagenet-trusted-agent-discovery.md` — trust/discovery layer peer
- `@concepts/cross-wiki-routing.md` — federation routing as bounded IoAI instance
- `@entities/tools/conductor-mcp.md` — laptop cross-wiki query router
- `@concepts/subagent-orchestration.md` — bounded MAS inside harness vs Internet-scale MAS
- `@entities/mcp-servers/librarian-kb-server.md` — federation serving substrate

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Internet of Agentic AI: Communication, Coordination, and Collective Intelligence at Scale |
| **Author** | Quanyan Zhu (NYU Tandon) |
| **arXiv** | 2606.12835v1 [cs.AI] |
| **Location** | `raw-sources/arxiv-2606.12835-the-internet-of-agentic-ai-communication-coordin.pdf` |
| **Retrieved** | 2026-06-13 |
| **Read status** | skimmed — architecture vision, deployment models, trust/interop research agenda |

## Narrative

Vision paper for **Internet of Agentic AI (IoAI)**: heterogeneous agents discover collaborators, negotiate responsibilities, exchange context, invoke tools, and execute workflows across cloud/edge/device/organizational/cyber-physical boundaries — analogous to the Internet's decentralized local-interaction rules.

Core benefits (Table 1): collective intelligence, mission execution, elastic scalability, adaptive coordination, system resilience, **controlled emergence**.

Sections cover: agent deployment models (cloud, edge, on-device, federated, elastic, agent economies); workflow lifecycles; communication protocols and discovery/directory services; semantic interoperability and governance; resource management; trust/security (DID, verifiable credentials, Sybil/registry poisoning); case studies (manufacturing, distributed ops).

Contrasts **centralized orchestration** (single supervisor) with **decentralized agent societies** where collective behavior emerges from local interactions — while still requiring protocols, incentives, and governance bounds.

**CCC mapping:** Cemini federation (conductor + librarian + lazy-tool + seven wikis) is a **private bounded IoAI slice** — not open Internet-scale discovery. Steal vocabulary for OAN evaluation, MCP catalog curation, and cross-org agent handoff briefs. Does not prescribe prod deployment.

## Snippets

> "Controlled emergence: the ability to harness useful system-level behavior arising from local agent interactions while preserving predictability, alignment, robustness, accountability, and operational coherence."

> "IoAI should be studied as a distributed socio-technical and computational ecosystem rather than merely as a collection of stronger individual models."

> — [Source: arxiv-2606.12835-the-internet-of-agentic-ai-communication-coordin.pdf §1,3, retrieved 2026-06-13]
