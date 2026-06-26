---
title: WorldMemArena — multimodal agent memory evaluation framework
type: concept
tags: [concept, agent-memory, evaluation, arxiv]
keywords: [worldmemarena, 2605.29341, memory-write, memory-retrieval]
related:
  - sources/arxiv-worldmemarena-agent-memory-2605.29341.md
  - entities/tools/claude-mem.md
  - entities/mcp-servers/stash.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - "@osint-wiki/concepts/agent-memory-pipeline-eval-rubric.md"
  - concepts/hidden-user-state-recovery-audit.md
  - sources/arxiv-memprobe-hidden-user-state-recovery-2606.24595.md
  - concepts/agent-rubrics-self-correction.md
  - entities/tools/memprobe.md
maturity: draft
created: 2026-06-02
updated: 2026-06-26
---

## Relations

- `@sources/arxiv-worldmemarena-agent-memory-2605.29341.md` — arXiv 2605.29341
- `@entities/tools/claude-mem.md` — passive observation memory
- `@entities/mcp-servers/stash.md` — episodic recall MCP
- `@concepts/agent-memory-stack-comparison.md` — stack comparison

## Raw Concept

arXiv **2605.29341** — evaluates long-horizon **multimodal** agent memory via action-world loops, scoring memory pipeline stages separately.

## Narrative

| Arena stage | CCC analogue |
|-------------|--------------|
| Write | claude-mem observations, wiki ingest |
| Maintenance | `hot.md`, maturity bumps, stale `[NEEDS VERIFICATION]` |
| Retrieval | conductor, stash recall, wiki index |
| Use | session tool choice + rules |

| Recovery audit | MemProbe dump_all + top-k | hidden user-state reconstruction vs ground truth |

**Verdict:** **REFERENCE** — steal evaluation rubric for memory MCP/skill audits; multimodal scope beyond current CCC harness. Pair with `@concepts/hidden-user-state-recovery-audit.md` for behavioral vs artifact scoring.

## Snippets

> "Memory must track an evolving world, revise what has gone stale, and surface the right evidence at decision time."
> — [Source: arxiv-2605.29341-worldmemarena-evaluating-multimodal-agent-memory.pdf]
