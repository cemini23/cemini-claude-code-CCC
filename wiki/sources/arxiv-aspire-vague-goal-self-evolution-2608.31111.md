---
title: "Aspire — Can Models Self-Evolve from Vague Goals? (CCC K332)"
type: source
tags: [source, arxiv, self-evolution, vague-goal, harness-evolution, hidden-eval, misevolution, policy, k332]
keywords: [2608.31111, Aspire, vague-goal-driven self-evolution, goal operationalization, hidden evaluation, Qwen-Agent, weight evolution, harness evolution]
related:
  - concepts/vague-goal-self-evolution.md
  - concepts/skill-misevolution.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/stratified-harness-evolution.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@concepts/vague-goal-self-evolution.md`
- `@concepts/skill-misevolution.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md`
- `@concepts/stratified-harness-evolution.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Aspire: Can Models Self-Evolve from Vague Goals? |
| **arXiv** | 2608.31111 (cs.CL, 2026-08-31) |
| **Authors** | ByteDance Seed, Singapore University of Technology and Design, M-A-P, TokenWave.AI (core: Yuhao Wu, Jingyuan Zhang, Jiajun Shi; corresponding: Yuhao Wu, Wenxuan Zhang, Shen Yan, Wenhao Huang, Ge Zhang) |
| **Venue** | arXiv preprint, 23 pages |
| **Code** | Project page only (`self-developing-agents.github.io`); no public repo / no SPDX found → no clone |
| **Retrieved** | 2026-09-01 |

## Narrative

**Verdict: ADOPT policy — vague-goal self-evolution ≠ explicit-task optimization.** Agents complete train/harness-edit loops, but weight gains are sparse; the strongest evolved harness stays below an engineered reference; proxy self-eval fails hidden eval; continued search can erase earlier gains.

Aspire is a benchmark for **vague-goal-driven self-evolution**: the agent receives only a natural-language capability goal while downstream evaluation items remain hidden (520 expert-authored items, six goals: science, humanities, medicine, math, logic/instruction, writing). The agent must **operationalize the goal** — diagnose gaps, decompose sub-goals, construct learning and validation signals — and jointly search over *what* to optimize and *how*.

Findings (the steals):

- **RQ1 (goal specification):** replacing an explicit post-training task with a vague goal **redirects search effort toward goal interpretation** (more goal-definition work) and yields **lower aggregate outcomes** than explicit-task references.
- **RQ2 (weight evolution):** of 30 configuration–goal cells, 28 produce an evaluated checkpoint, 21 an eligible checkpoint, and **only 1 a retained above-base improvement**. A positive within-lineage slope often describes **recovery from training-induced regression**, not above-base gain (math: 0.79 → 1.75 → 2.38 while base is 17.86). **More search ≠ better search:** Sol searched most broadly (33 checkpoints, 76.56 GPU-hours) yet none exceeded base; Terra's math rose to 20.10, fell to 2.78, recovered to 18.17 — continued search can erase earlier gains; **checkpoint selection and rollback are necessary**.
- **RQ3 (harness evolution):** with weights frozen, agents produce executable, behaviorally distinct successor harnesses, but the closest (Sol, 27.22) stays **below the fixed Qwen-Agent reference (28.64)**. **Proxy self-eval fails hidden eval:** Luna raised a self-designed 8-item checklist to 8/8 on its own validation data by adding a template that recasts mechanism/formula questions as study-design problems — validation gain with no hidden-eval gain. Blind continuation (final-only protocol) yields near-zero final checkpoints (0.159 / 2.540 / 0).
- **Conclusion:** "Closing the training loop is not yet the same as closing the capability loop" — judge progress against the **base model**, not only the previous checkpoint.

CCC policy lines: **goal interpretation is the missing search axis**; **local training success ≠ transferable capability**; treat **harness self-edit as high-blast HITL (misevolution)**. **Never auto-evolve `.cursor/skills`.** No public SPDX → no clone; runtime `wont_wire` (project page only). Pairs K162 (bounded self-refinement), K237 (misevolution), K292 (retention checks on held-out packs), K313 (stratified evolution, hidden selection tasks).

| Confidence | `[CONFIRMED]` — results reported in the paper; policy is CCC synthesis |
|------------|------------|

## Snippets

> "Current agents routinely complete training and harness-editing loops, but weight-level gains remain sparse and unstable, and the strongest evolved harness remains below the engineered Qwen-Agent reference." [Source: arXiv 2608.31111 abstract]

> "Agents often train on mismatched data and trust narrow self-evaluations, so local gains fail to transfer to hidden evaluation and continued search and training can erase earlier improvements." [Source: arXiv 2608.31111 abstract]

> "Closing the training loop is not yet the same as closing the capability loop." [Source: arXiv 2608.31111 §6]

> "Of 30 cells, 28 produce an evaluated checkpoint, 21 produce an eligible checkpoint, and one yields a retained improvement." [Source: arXiv 2608.31111 §4 (adaptive-feedback protocol)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.31111-aspire-can-models-self-evolve-from-vague-goals.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
