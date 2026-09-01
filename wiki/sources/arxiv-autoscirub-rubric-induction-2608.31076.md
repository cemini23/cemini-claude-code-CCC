---
title: "AutoSciRub — Learning to Evaluate Before Improving: Automatic Rubric Induction (CCC K331)"
type: source
tags: [source, arxiv, rubric-induction, evaluation-first, research-agents, executable-rubric, eval-contract, k331]
keywords: [2608.31076, AutoSciRub, zjunlp, rubric induction, criterion-level verification, ResearchClawBench, AstaBench, evaluation-first, external eval contract]
related:
  - concepts/evaluation-first-rubric-induction.md
  - entities/tools/autoscirub.md
  - concepts/validation-ratchet-skill-evolution.md
  - concepts/seagym-self-evolving-harness-evaluation.md
  - concepts/stratified-harness-evolution.md
  - briefs/2026-09-01_ccc-k328-k332-sip-ready.md
maturity: draft
read_status: read
created: 2026-09-01
updated: 2026-09-01
---

## Relations

- `@concepts/evaluation-first-rubric-induction.md`
- `@entities/tools/autoscirub.md`
- `@concepts/validation-ratchet-skill-evolution.md`
- `@concepts/seagym-self-evolving-harness-evaluation.md`
- `@concepts/stratified-harness-evolution.md`
- `@briefs/2026-09-01_ccc-k328-k332-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic Research Agents |
| **arXiv** | 2608.31076 (cs.CL, 2026-08-31) |
| **Authors** | Xuehai Wang, Haowei Qin, Tongxin Liu, Junkai Li, Buqiang Xu, Jintian Zhang, Yijun Chen, Zirui Xue, Shumin Deng (Zhejiang University et al.) |
| **Venue** | arXiv preprint, 20 pages |
| **Code** | `github.com/zjunlp/AutoSciRub` — **MIT** (gh SPDX verified 2026-09-01) → GO REFERENCE clone |
| **Retrieved** | 2026-09-01 |

## Narrative

**Verdict: ADOPT evaluation-first — induce a task-specific *executable rubric* before research execution; use it to guide, verify, and revise.**

Open-ended research tasks hide success criteria: agents miss important analyses, use inappropriate methods, or draw conclusions insufficiently supported by evidence. Existing rubrics in scientific-agent benchmarks are **post-hoc evaluation instruments**; AutoSciRub treats the rubric as an **intermediate scientific specification** — make implicit requirements explicit and connect task interpretation, execution, verification, and iterative revision.

Two stages:

1. **Automatic Rubric Induction** — (a) *Rubric Skeleton Induction*: decompose the underspecified instruction into atomic scientific goals (traceable, non-overlapping; no methods/metrics yet); (b) *Scientific Literature Grounding*: per goal, query concepts/methods/metrics/protocols over task literature + arXiv/OpenAlex/Semantic Scholar/Tavily, retain 5–7 core papers (blocklist-filtered, never used as experimental evidence); (c) *Task-Data Exploration*: lightweight profile of available files/datasets/fields/units/conditions (planning only); (d) *Criterion Synthesis*: combine into a task-specific executable rubric — each criterion links to goals and specifies data sources, required experiments/analyses, metrics/comparisons, expected evidence artifacts, and a satisfaction condition.
2. **Rubric-Guided Iterative Revision** — a verifier checks each criterion against the artifact (satisfied / remaining evidence gap), producing targeted feedback (missing experiment, incomplete comparison, unsupported claim); the agent revises; stop when all criteria pass or the revision budget is reached.

Results (all gains transfer across harnesses with frozen backbone):

- **ResearchClawBench** (40 tasks, 10 domains): +2.08 avg across three backbone LLMs (GPT-5.4 / GLM-5.2 / MiniMax-M3) under the fixed Codex harness; **+2.95** across three agent harnesses (Claude Code / OpenClaw / OpenScience) with fixed DeepSeek-V4-Flash backbone.
- **AstaBench E2E Discovery** (20-task subset): avg **+16.8** points across three agent configs; Claude Code and Codex task counts 18/20 → 20/20.
- **Ablation:** skeleton +0.36, grounded rubric +1.06, full (revision) **+3.11**; rubric-guided revision ≈ **2.7×** the cumulative improvement of rubric-free self-refinement (2.05 vs 0.77) — repeated rewriting alone does not explain the gain.
- **Limitation:** improves operationalization, not scientific framing — scientific-core coverage slightly decreases (3.35 → 3.07); higher-level framing judgment stays with the backbone model.

**CCC policy lines:** evaluation-first rubric is the **control surface**; keep the **external eval contract** — do not let the agent rewrite pass criteria (**do not rewrite `## Verify`**). Pairs K162 (verification hierarchy), K281 (meta-harness HITL / eval contract), K289 (evidence-tree eval), K298 (validation-task selection). Entity runtime `wont_wire`; concept `policy_wired`. Clone is REFERENCE only.

| Confidence | `[CONFIRMED]` — results reported in the paper; clone license verified via GitHub API |
|------------|------------|

## Snippets

> "Open-ended research tasks often do not clearly specify the analyses, methods, and success criteria required … a reliable research agent should learn to evaluate before improving." [Source: arXiv 2608.31076 abstract, §1]

> "Rubrics in existing scientific-agent benchmarks are predominantly treated as post-hoc evaluation instruments … rubrics should instead serve as intermediate scientific specifications." [Source: arXiv 2608.31076 §1]

> "Rubric-guided revision improves the score monotonically to 20.36 … achieving approximately 2.7 times the cumulative improvement of rubric-free self-refinement." [Source: arXiv 2608.31076 §4.4]

> "AutoSciRub is more effective at translating an identified scientific direction into concrete and verifiable requirements than at revising the underlying framing of the research problem." [Source: arXiv 2608.31076 §4.4]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.31076-learning-to-evaluate-before-improving-automatic.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
