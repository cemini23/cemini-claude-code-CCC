---
title: Metis dual-representation agent memory (arXiv 2606.24151)
type: source
tags: [source, arxiv, self-evolving, memory, metis, k124]
keywords: [2606.24151, text-memory, code-memory, mcp-tools]
related:
  - concepts/dual-representation-agent-memory.md
  - concepts/agent-memory-stack-comparison.md
  - entities/tools/claude-mem.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/continual-harness-online-self-improvement.md
maturity: draft
read_status: read
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@concepts/dual-representation-agent-memory.md` — text vs code memory trade-off synthesis

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Metis: Bridging Text and Code Memory for Self-Evolving Agents |
| **Authors** | Dai et al. (CUHK, Huawei, Wuhan U) |
| **arXiv** | 2606.24151v1 [cs.CL] |
| **Location** | `raw-sources/arxiv-2606.24151-pdf-metis-bridging-text-and-code-memory-for-self.pdf` |
| **Retrieved** | 2026-06-24 |
| **Read status** | read (controlled comparison + hierarchical memory) |

## Narrative

Controlled study isolating **text memory** (NL injected into context) vs **code memory** (callable tools/MCP). Neither alone sufficient — complementary trade-offs in construction cost, execution efficiency, transferability.

**Metis** — hierarchical dual-representation: text organized as execution plans, environment facts, common pitfalls; recurring plans **crystallized** into validated callable tools when reuse justifies generation cost.

**AppWorld results [TENTATIVE]:** +20.6% accuracy vs ReAct, −22.8% execution cost; better accuracy/efficiency/cost balance than representative self-evolving systems.

**CCC mapping:** wiki pages = text memory; SKILL.md + MCP tools = code memory; promote repeated wiki patterns to skills when AFTER-style reuse evidence exists. **REFERENCE** — no Metis repo in paper (work in progress).

## Snippets

> "We distinguish by how the agent consumes the stored experience rather than by its surface content."
> — [Source: arxiv-2606.24151-pdf-metis-bridging-text-and-code-memory-for-self.pdf, retrieved 2026-06-24]

> "Metis selectively crystallizes recurring plans into validated callable tools."
> — [Source: arxiv-2606.24151-pdf-metis-bridging-text-and-code-memory-for-self.pdf, retrieved 2026-06-24]
