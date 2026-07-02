---
title: Metamemory — scaffold vs proficiency training for agent memory
type: concept
tags: [concept, memory, metamemory, harness, k137]
keywords: [2607.01224, automem, scaffold, memory-proficiency, file-system-memory]
related:
  - sources/arxiv-automem-metamemory-cognitive-skill-2607.01224.md
  - entities/tools/automem-stanford-cognitive-skill.md
  - concepts/agent-memory-stack-comparison.md
  - concepts/agentic-memory-cross-scenario-generality.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/long-thread-context-decay.md
  - concepts/self-compacting-adaptive-context.md
  - entities/tools/claude-mem.md
  - concepts/multi-factor-agentic-memory-value-model.md
  - sources/brief-k137-automem-metamemory-cognitive-skill-2026-07-02.md
maturity: draft
created: 2026-07-02
updated: 2026-07-02
---

## Relations

- `@sources/arxiv-automem-metamemory-cognitive-skill-2607.01224.md` — arXiv provenance (2607.01224)
- `@entities/tools/claude-mem.md` — laptop session memory (passive observation)
- `@concepts/agentic-memory-cross-scenario-generality.md` — related AutoMEM eval paper (2606.04315 — different work)

## Raw Concept

How should Cemini improve agent memory on long-horizon tasks — by revising harness structure, training model proficiency, or both?

## Narrative

arXiv **2607.01224** (Stanford **AutoMem**) frames **metamemory** as a learnable skill with two improvement axes:

| Axis | What changes | Cemini mapping |
|------|--------------|----------------|
| **Structure** | Prompts, file schemas, action vocabulary, validation hooks | `CLAUDE.md`, `hot.md` layout, claude-mem capture rules, wiki page templates |
| **Proficiency** | Model's parametric ability to choose memory ops well | Fine-tuning out of scope; steal **behavioral** discipline via rules/skills |

### Inner-loop pattern: memory-as-file-system

Each step runs **LOG** (what to record?) and **PLAN** (what to recall?) before world/task actions. Memory ops share the action space with task tools — every decision is traceable.

**CCC analog:** explicit `Write`/`Read` to `hot.md`, wiki ingest fan-out to durable pages, claude-mem search-before-append — not opaque context summarization alone.

### Outer-loop #1 — scaffold optimization

Meta-LLM reads **complete episode traces** (thousands of steps), diagnoses memory failure patterns, revises agent scaffold. Acceptance gate: progression must strictly improve on fixed eval seeds.

Example scaffold wins (NetHack): coordinate-keyed `<|UPSERT_MAP|>` dedup vs append-only duplicates; auto-sync inventory/status from observation; pre-populated strategy reference.

**CCC steal:** periodic meta-review of ingest trajectories → revise `hot.md` schema, SessionStart hooks, claude-mem filters — pairs with `@concepts/failed-trajectory-harness-repair.md`.

### Outer-loop #2 — memory proficiency training

After scaffold converges, collect traces on disjoint seeds; meta-LLM curates SFT + LoRA config for a **memory specialist**; gameplay model stays frozen. Inference: specialist handles LOG + PLAN retrieval; base model commits task action.

**CCC steal:** **REFERENCE only** — no local LoRA pipeline. Adopt **search-before-write** ratio as eval metric for memory hygiene.

### Results [TENTATIVE — single paper]

| Stage | Crafter | MiniHack | NetHack |
|-------|---------|----------|---------|
| v0 base | 25.0% | 7.5% | 0.42% |
| + scaffold | 47.3% | 27.5% | 1.57% |
| + proficiency | 51.4% | 30.0% | 1.85% |

Scaffold alone beat Qwen2.5-72B — **well-structured external memory > raw scale** on these long-horizon tasks.

### Disambiguation

| Name | arXiv / repo | Role |
|------|--------------|------|
| AutoMem (this page) | 2607.01224, autoLearnMem/AutoMem | Metamemory training framework |
| AutoMEM eval harness | 2606.04315 | Cross-scenario memory benchmark |
| AutoMem MCP service | verygoodplugins/automem (MIT) | Production graph-vector memory — separate product |

## Snippets

> "Both axes resist manual optimization: episodes in long-horizon tasks run for thousands of steps, and a single memory mistake can hide long before it surfaces."
> — [Source: arxiv-2607.01224-automem-automated-learning-of-memory-as-a-cognit.pdf, retrieved 2026-07-02]
