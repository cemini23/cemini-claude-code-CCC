---
title: "Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI (CCC K409)"
type: source
tags: [source, arxiv, k409]
keywords: [2609.38143, k409]
related:
  - concepts/meta-skill-bank-harness-construction.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- `@concepts/meta-skill-bank-harness-construction.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI |
| **arXiv** | 2609.38143 (2026-09) |
| **Repo** | `qiancheng-apodex/MetaSkill-AI4AI` |
| **Retrieved** | 2026-09-30 |

## Narrative

**Verdict: ADOPT pattern; NO-GO clone (null SPDX).**

**Learning meta-skills for harness design.** A **Builder** constructs execution environments for a **Target**; both sets of model weights stay **frozen**. A **meta-skill** is a three-field principle: **`when`** (observable trigger), **`provide`** (capability or resource to supply), **`use`** (how the Target should employ it, and which judgments stay its own). The Builder learns these from Target execution feedback on a development set, then **freezes the bank** and uses it to build harnesses for unseen tasks. Full-bank meta-skills beat no-skill construction by **8.95 points** and beat **delivering the same bank directly to the Target** by 12.02 points — **teaching the Builder beats teaching the Target**. When one model plays both roles, scores rise 18.71 points. **Phase-0: `qiancheng-apodex/MetaSkill-AI4AI` returns null SPDX** (no license file) → **NO-GO on clone**, watch only. Pairs K404 harness learning / `harness-as-eval-artifact` / `thin-harness-fat-skills-garrytan` / `skill-set-selection-under-budget` / `progressive-skill-discovery-access-control`. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "Teaching the Builder to translate experience into executable support can therefore be more beneficial than directly teaching the Target additional task skills." [Source: arXiv 2609.38143 (retrieved 2026-09-30)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2609.38143-learning-meta-skills-for-agent-harness-design-in.pdf` |
