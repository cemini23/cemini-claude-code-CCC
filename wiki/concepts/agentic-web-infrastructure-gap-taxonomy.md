---
title: Agentic web infrastructure gap taxonomy — Agentverse audit
type: concept
tags: [concept, agentic-web, web4, gap-analysis, infrastructure, k123]
keywords: [2606.20570, agent-cloud-stack, agentverse, memory-cloud, agentdns]
related:
  - sources/arxiv-agentic-web-infrastructure-agentverse-2606.20570.md
  - concepts/agent-first-web-framework.md
  - concepts/internet-of-agentic-ai-ioai.md
  - concepts/system-scaling-harness-agentic-ai.md
  - concepts/mcp-adaptive-systems-context-survey.md
  - sources/arxiv-agent-first-web-redesign-2606.19116.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- `@sources/arxiv-agentic-web-infrastructure-agentverse-2606.20570.md` — Agentverse gap paper
- `@concepts/agent-first-web-framework.md` — application/content layer (ATML, agents.txt)
- `@concepts/internet-of-agentic-ai-ioai.md` — IoAI federation vision peer
- `@concepts/system-scaling-harness-agentic-ai.md` — harness dimensions vs model-only eval

## Raw Concept

What infrastructure gaps block agents from operating reliably at internet scale — and how do we taxonomize them?

## Narrative

**Agent infrastructure gap taxonomy** [TENTATIVE — 2606.20570]: empirical audit of production Agentverse → **8 categories, 62 missing capabilities** (memory, observability, security, economics, orchestration, discovery, etc.).

**Seven-layer Agent Cloud Stack** — reference model for agent-native cloud (analogous to AWS layers for Web2).

**Five evolution paths (steal-for eval prompts):**

| Path | From → To |
|------|-----------|
| Memory | Ephemeral KV → Agent Memory Cloud |
| Discovery | Keyword → semantic trust-weighted Agentdns |
| Protocol | Single → multi-standard agent lingua franca |
| Hosting | Single instance → K8s-scale agent orchestration |
| Economics | Simple tokens → rich agent economic primitives |

**CCC mapping:** federation hub + conductor gaps; claude-mem/stash as partial memory cloud; lazy-tool as discovery proxy.

**Verdict:** **REFERENCE** — taxonomy for v8 eval; **NO-GO** Agentverse platform adopt.

## Snippets

> "We derive a structured Gap Taxonomy—eight categories encompassing 62 distinct missing infrastructure capabilities."
> — [Source: arxiv-2606.20570-infrastructure-for-the-agentic-web-gap-analysis.pdf, retrieved 2026-06-23]
