---
title: Dual-representation agent memory — text vs code
type: concept
tags: [concept, memory, self-evolving, metis, k124]
keywords: [2606.24151, text-memory, code-memory, crystallization]
related:
  - sources/arxiv-metis-text-code-memory-2606.24151.md
  - concepts/agent-memory-stack-comparison.md
  - entities/tools/claude-mem.md
  - concepts/skillrae-retrieval-augmented-execution.md
  - concepts/procedural-memory-transfer-after.md
  - entities/tools/openspec.md
maturity: draft
created: 2026-06-24
updated: 2026-06-24
---

## Relations

- `@sources/arxiv-metis-text-code-memory-2606.24151.md` — Metis controlled study
- `@concepts/agent-memory-stack-comparison.md` — stack-level comparison

## Raw Concept

Should agent experience be stored as natural-language context injection or as callable code/tools?

## Narrative

**Metis** (2606.24151) controlled comparison — same experiences, two consumption modes:

| Representation | Consumption | Trade-off |
|----------------|-------------|-----------|
| **Text memory** | Read + reason in context | Broad applicability; higher per-step cost |
| **Code memory** | Invoke tool/MCP directly | Execution efficiency; construction cost |

**Metis hierarchy:** text buckets (plans, env facts, pitfalls) + **selective crystallization** of recurring plans into validated tools when reuse justifies cost.

### Cemini mapping

| Metis bucket | CCC layer |
|--------------|-----------|
| Execution plans | `wiki/concepts/`, patterns |
| Environment facts | `CLAUDE.md`, `.cursor/rules/` |
| Common pitfalls | `## Dead Ends`, `LESSONS.md` |
| Crystallized tools | `entities/skills/`, MCP servers |

**Rule:** don't prematurely code-crystallize — wait for AFTER-style reuse evidence (`@concepts/procedural-memory-transfer-after.md`).

## Snippets

> "Neither representation alone is sufficient."
> — [Source: arxiv-2606.24151 abstract, retrieved 2026-06-24]
