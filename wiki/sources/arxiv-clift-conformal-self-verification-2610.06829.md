---
title: "CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling (CCC K428)"
type: source
tags: [source, arxiv, k428]
keywords: [2610.06829, k428]
related:
  - concepts/conformal-self-verification-certified-bank.md
  - briefs/2026-10-06_ccc-k426-k430-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@concepts/conformal-self-verification-certified-bank.md`
- `@briefs/2026-10-06_ccc-k426-k430-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | CLIFT: Conformal Self-Verification for Web Agent Training and Test-Time Scaling |
| **arXiv** | 2610.06829 (2026-10) |
| **Retrieved** | 2026-10-06 |

## Narrative

**Verdict: ADOPT pattern.**

**CLIFT — turn the judge's feedback into a verifier the agent carries with it.** The problem is the verifier bottleneck for agent RL: a binary success signal is too sparse (when every rollout in a GRPO group scores alike, the advantage collapses), while a frontier judge is too expensive to call per step **and cannot be assumed available at deployment**. CLIFT's object is not a new model but a **calibrated question bank**: natural-language verification questions, each with a **URL scope** and a **polarity sign** (does YES mean progress or failure?). A **Compositional Conformal Certifier** keeps only questions whose URL-conditional evidence agrees with a training-time judge, assigns **signed trust weights** by polarity-aware lift, and blends the score into per-step rewards **asymmetrically — it can only add evidence on top of the judge baseline, never subtract**, which prevents the reward-collapse failure of earlier linear blends. At test time the same bank is **frozen** and reused as **Conformal Trajectory Selection**: sample a greedy rollout plus retries, summarise each URL trace, and apply a **conservative majority rule** to decide whether to swap — **no external judge called**. Three results: SOTA open-source web agent on WebArena Infinity; **a bank trained on open Gemma-4 transfers to GPT-5.5** and reaches SOTA under the canonical harness on VisualWebArena; and on Online Mind2Web, **no agent is trained on the benchmark** — the question bank alone transfers and lifts a live-web agent. **CCC relevance:** this is the strongest version of a pattern CCC already holds — **the verifier should be explicit, cheap, and reusable**, not an expensive oracle called at runtime. The certified-bank idea generalises K407 (judge variance) and K424 (graded ladder): make the grading signal deterministic, transferable, and auditable. Pairs K423 TPRS / `@concepts/verifiable-deterministic-agent-benchmarking.md` / `@concepts/agent-completion-verification-gates.md` / K406 Assay. **No repo stated.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "The policy is often not the only limiting object; the way we score and select its rollouts can dominate the observed success rate." [Source: arXiv 2610.06829 (retrieved 2026-10-06)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.06829-clift-conformal-self-verification-for-web-agent.pdf` |
