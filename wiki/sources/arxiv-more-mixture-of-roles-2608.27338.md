---
title: "MoRe — one model, many minds (CCC K322, WATCH)"
type: source
tags: [source, arxiv, mixture-of-roles, steering-vector, multi-agent, watch, k322]
keywords: [2608.27338, MoRe, mixture of roles, steering vector, query-aware router, GRPO, token cost]
related:
  - concepts/query-aware-role-fusion.md
  - concepts/context-engineering.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/query-aware-role-fusion.md`
- `@concepts/context-engineering.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | One Model, Many Minds: Unlocking Multi-Agent Synergy in a Single Agent via Mixture of Roles |
| **arXiv** | 2608.27338 (2026-08-27) |
| **Authors** | Zhichen Zeng, Huiyuan Chen, Jingru Cheng, Juan Zha, Ming Liu, Ying Chen, Xiyuan Yang, Chaosheng Dong, Haiyang Zhang, Hanghang Tong (UIUC + Amazon) |
| **Code** | None found (WATCH — no clone) |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: WATCH** — query-aware steering-vector fusion vs spawning N agents; frozen backbone; GRPO **`wont_wire`**. No clone.

MoRe adaptively composes multiple specializations into a **single steering vector** for single-turn inference: a diversified **codebook of steering vectors** (each encoding a latent role) + a **query-aware router** that fuses the codebook into one composed vector, steering a frozen backbone LLM for multi-perspective reasoning in one pass. Trained via three-stage SFT curriculum + GRPO post-training.

Results: outperforms single-agent baselines by **2.2% on average**, on par with MAS while reducing **token cost by 20×**.

CCC steal: **do not auto-spawn N agents for multi-perspective work** — a single model can carry multiple roles via composed steering; MAS's multi-turn fusion inflates context and cost. Reinforces K311/K164 lazy-context discipline.

| Confidence | `[TENTATIVE]` — paper results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "MoRe enables multi-perspective specialization in a single-agent, single-turn inference process." [Source: arXiv 2608.27338 abstract]

> "MoRe … achieves performance on par with MAS while reducing token cost by 20×." [Source: arXiv 2608.27338 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.27338-one-model-many-minds-unlocking-multi-agent-syner.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
