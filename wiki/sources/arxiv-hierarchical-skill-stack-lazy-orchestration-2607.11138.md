---
title: Hierarchical skill architecture — stack execution + lazy discovery (2607.11138)
type: source
tags: [source, arxiv, orchestration, hierarchy, lazy-loading, stack, k164]
keywords: [2607.11138, hierarchical skill, LIFO stack, lazy manifest, capability fencing, UPI Help, pushdown automaton]
related:
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - entities/tools/lazy-tool.md
  - concepts/mcp-context-optimization.md
  - concepts/subagent-orchestration.md
  - sources/brief-k164-hierarchical-skill-stack-lazy-orchestration-2026-07-14.md
maturity: draft
read_status: read
created: 2026-07-14
updated: 2026-07-14
phase_0_verdict: "REFERENCE 2026-07-14 — production UPI Help blueprint; no public product repo; adopt tree+stack+lazy-manifest patterns; David adopt for TipDrop multi-vendor routing"
---

## Relations

- `@concepts/hierarchical-skill-stack-lazy-orchestration.md` — CCC synthesis
- `@entities/tools/lazy-tool.md` — Cemini lazy MCP sibling

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery |
| **Author** | Prashant Devadiga et al. (UPI Help / payments-support product context) |
| **arXiv** | 2607.11138 (Jul 2026) |
| **Type** | Architecture + controlled benchmarks + production-adjacent eval |
| **Code** | None public at Phase-0 — paper is formalization of internal system |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.11138-a-formal-hierarchical-architecture-for-agentic.pdf` |
| **Retrieved** | 2026-07-14 |

## Narrative

Replaces flat tool registries with a **capability tree**: decision-making skills (orchestrators) vs executable skills (deterministic leaves). Runtime = single-step loop on a **LIFO stack** (pushdown / nested return semantics). **Manifest-driven lazy discovery** loads only immediate children. **Capability fencing** + localized frames reduce prompt-injection persistence.

Key empirical claims (generated catalogs, rich schemas): flat routing hits context limit at N=256–512; hierarchy stays feasible with ~constant schema tokens/call (~138–1111 vs tens of thousands). Under workflow noise, hierarchy matches ~0.73 success while cutting prompt size ~10×. Accuracy depends on **non-overlapping top-level domains** — overlapping domains cause first-depth wrong-branch errors.

| Verdict | **REFERENCE** — steal architecture checklist; no clone |

## Snippets

> "hierarchical routing bounds visible schema tokens per LLM call and remains context-feasible at N=512 with rich schemas, where flat routing fails"
> — [Source: arxiv-2607.11138 conclusion]

> "Choose hierarchical routing when tool catalogs may grow, schemas are rich, multi-step workflows matter, and domain categories can be kept mutually exclusive."
> — [Source: arxiv-2607.11138 §9.8]
