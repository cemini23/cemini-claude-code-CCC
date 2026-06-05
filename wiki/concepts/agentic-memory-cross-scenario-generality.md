---
title: Agentic memory cross-scenario generality (AutoMEM / 2606.04315)
type: concept
tags: [concept, agent-memory, evaluation, k100, reference]
keywords: [2606.04315, automem, cross-scenario, memory-harness]
related:
  - sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md
  - entities/tools/claude-mem.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/token-economics-and-prompt-caching.md
  - "@osint-wiki/concepts/interaction-native-knowledge-harness.md"
  - "@osint-wiki/concepts/agent-memory-critique.md"
maturity: draft
created: 2026-06-05
updated: 2026-06-05
cross-wiki-source: "@osint-wiki/concepts/agent-memory-cross-scenario-generality.md"
---

## Relations

- `@sources/arxiv-cross-scenario-agentic-generality-2606.04315-2026-06-05.md` — arXiv provenance
- `@entities/tools/claude-mem.md` — laptop passive observation memory
- `@osint-wiki/concepts/interaction-native-knowledge-harness.md` — financial KG harness (OSINT primary)
- `@osint-wiki/concepts/agent-memory-critique.md` — when memory complexity helps

## Raw Concept

arXiv **2606.04315** evaluates eight memory systems + a search agent harness across **five scenarios** (single-turn QA, multi-session chat, agentic-trajectory QA, memory stress tests, long-horizon tasks). Finding: scenario-tuned passive stores underperform; **agent-controlled memory via tool calls** (AutoMEM harness) ranks best on cross-scenario generality [TENTATIVE — paper claims].

## Narrative

### Two failure modes (paper)

1. **Representation failure** — build-time schemas drop step/action-level evidence from agentic trajectories.
2. **Retrieval failure** — passive retrieval cannot surface evidence the store retains.

### CCC steal-from (REFERENCE — not AutoMEM install)

| Insight | Cemini mapping |
|---------|----------------|
| Memory as **tool-managed** flat files beats passive pipeline for agentic work | Prefer claude-mem + explicit `hot.md` + stash over opaque summarization-only |
| Cross-scenario eval required | Do not judge memory design on chat-QA alone |
| Token/latency tracked with accuracy | Aligns with `@concepts/token-economics-and-prompt-caching.md` |

### Routing

**Primary wiki:** `@osint-wiki` (conductor, stash, InKH, financial event memory). **CCC** keeps this stub + claude-mem/hot.md pointers only.

### vs 2606.06324 HarnessFix

| Paper | Focus |
|-------|-------|
| 2606.04315 | **What** to remember and retrieve across scenarios |
| 2606.06324 | **How** to diagnose/repair harness flaws from failed trajectories |

## Snippets

> "Memory performance hinges on giving the agent active control over storage and retrieval rather than on a passive store behind a fixed pipeline."
> — [Source: arxiv-2606.04315 abstract, retrieved 2026-06-05]
