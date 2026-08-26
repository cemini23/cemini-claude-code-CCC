---
title: "Recuris — recursive Experiential–Working Memory evolution (CCC K314)"
type: source
tags: [source, arxiv, memory, rsi, skill-memory, long-horizon, k314]
keywords: [2608.24876, Recuris, Gen-Verse, experiential memory, working memory, Meta-Agent, validation-gated, tau2-bench]
related:
  - concepts/experiential-working-memory-coupling.md
  - entities/tools/recuris.md
  - briefs/2026-08-26_ccc-k310-k314-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-26
updated: 2026-08-26
---

## Relations

- `@concepts/experiential-working-memory-coupling.md`
- `@entities/tools/recuris.md`
- `@briefs/2026-08-26_ccc-k310-k314-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Recursive Experiential–Working Memory Evolution for Long-Horizon Agent Harnesses |
| **arXiv** | 2608.24876 |
| **Authors** | Zhaochen Yu, Yingcheng Wu, Zhenfei Yin, Kaiyuan Chen, Zhe Zhao, Mengdi Wang, Shuicheng Yan, Ling Yang (NUS + Stanford + Oxford + Princeton) |
| **Code** | `github.com/Gen-Verse/Recuris` — **Apache-2.0**, ~1.6MB → **GO REFERENCE** clone `.local/adopts/Recuris` (SPDX verified via API + LICENSE on disk) |
| **Retrieved** | 2026-08-26 |

## Narrative

Attacks RSI's long-horizon failure mode — growing histories obscure task state and misalign skill invocation — with a two-memory split:

- **Experiential Memory (EM)** holds accumulated skills/procedures.
- **Working Memory (WM)** tracks current task progress as structured state and **guides which EM skill to invoke**, grounding skill use in present needs instead of full history.

The coupling turns execution into structured evidence that **localizes failures to specific memory components**; a fixed Meta-Agent converts that evidence into localized, **validation-gated** Skill Memory patches, which reshape execution and yield new evidence — a bounded recursive loop.

Results: across four long-horizon benchmarks and ten models, task success improves in 35 of 37 completed model–benchmark pairs. On τ²-Bench: **+17.8** for GPT-5.6 Sol (58.3→76.1), **+15.6** for Claude Opus 5 (→87.9%); +16.6/+13.5 on Qwen3.6 on SkillFlow; advantage widens with horizon to **+32.2** on longest tasks; six failure modes fall 20–86%.

Pairs K309 Prime Agent (persistent cross-trajectory state) and K237/K298/K307 (no unattended self-evolution): the gate is the point — **HITL before any skill self-write**, validation before patch admission.

| Verdict | **ADOPT** EM–WM coupling + validation-gated updates as pattern; Apache-2.0 REFERENCE clone; runtime `wire_status: wont_wire`. HITL before skill self-write. |
|---------|---------|

## Snippets

> "Working Memory tracks task progress and guides skill selection from Experiential Memory, grounding skill use in current needs rather than the full history." [Source: arXiv 2608.24876 abstract]

> "a fixed Meta-Agent turns that evidence into localized, validation-gated updates to Skill Memory … forming a bounded recursive memory-evolution loop." [Source: arXiv 2608.24876 abstract]

> "on 𝜏²-Bench it adds +17.8 points to GPT-5.6 Sol … The advantage widens as the interaction horizon grows, to +32.2 points on the longest tasks." [Source: arXiv 2608.24876 abstract / Fig. 1]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.24876-recursive-experiential-working-memory-evolution.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
