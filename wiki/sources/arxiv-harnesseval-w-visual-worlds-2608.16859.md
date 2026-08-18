---
title: "HarnessEval-W — agentifying the evaluation of visual worlds"
type: source
tags: [source, arxiv, world-model, evaluation, agentified-benchmark, evidence-tree, k289]
keywords: [2608.16859, HarnessEval-W, agentified eval, evidence tree, world model benchmark, sub-agent routing, visual worlds]
related:
  - concepts/agentified-eval-evidence-tree-harness.md
  - entities/tools/harnesseval-w.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - sources/brief-k285-k289-harness-wave-2026-08-18.md
  - briefs/2026-08-18_ccc-handoff-k285-k289-ingest.md
maturity: draft
created: 2026-08-18
updated: 2026-08-18
---

## Relations

- `@concepts/agentified-eval-evidence-tree-harness.md`
- `@entities/tools/harnesseval-w.md`
- `@concepts/bounded-self-refinement-vs-rsi-taxonomy.md` — K162 verification hierarchy (no closed self-eval)
- `@concepts/measurement-integrity-mcp-security-eval.md` — K277 measurement integrity

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | HarnessEval-W: Agentifying the Evaluation of Visual Worlds |
| **arXiv** | 2608.16859 |
| **Authors** | Weiliang Chen, Haowen Sun, Jun Gao, Jiawei Chi, Hanyang Wang, Qiyu Dai, Yihao Li, Hao Li, Jingnan Gao, Yi-Hsin Hung, Xingzhuo Guo, Shangchen Miao, Zhiyuan Shi, Xiang Li, Fengrui Tian, Weihua Du, Ziqi Huang, Shenyuan Gao, Siqiao Huang, Mingyu Liu, Yifei Li, Shizun Wang, Xi Wang, Tianqi Zhang, Xue Luo, Xiyin Ren, Jinshan Ren, Xiaoyang Shen, Xiaobo Hu, Zhiyang Dou, Mingyu Ding, Yichao Yan, Xinchao Wang, Yizhou Wang, Shilong Liu, Wenzhao Zheng, Yueqi Duan, Yuan Gong, Ziwei Liu, Ming-Yu Liu, Jialong Wu, Jiangran Lyu, Fangfu Liu |
| **Code** | `github.com/mirros-lab/harnesseval-w` — **NO-GO clone** (null SPDX, no LICENSE in pyproject) |
| **Retrieved** | 2026-08-18 |

## Narrative

Brings the **harness paradigm** from the LLM ecosystem to world-model benchmarking. The claim: a benchmark should deliver more than a scalar score — what makes an evaluation trustworthy is the reasoning that justifies the score. Existing world-model metrics are brute-force computed with no inspectable reasoning chain.

**HarnessEval-W** is an agentified evaluation pipeline that, for each of 330 evaluation cases across 18 representative world models:
1. **Interprets the context** of the case and routes it to appropriate **skills** (from a growing skill library) that can legitimately evaluate it;
2. **Decomposes** the evaluation question into measurable subproblems;
3. **Spawns specialized sub-agents**, each equipped with tailored context + diagnostic tools (e.g., bounding-box tracking, temporal-intersection verification, velocity estimation) to reason over its own subproblem;
4. The **parent agent validates** the gathered evidence before merging it into the final verdict.

The outcome is a **transparent evidence tree** — what was tested, which tool supplied the visual grounding, and the complete logical chain justifying the score — not a scalar-only rubric. Cases are organized around three world-model functions: Observation Quality, Transition Correctness, World Persistence, authored by an agentic construction pipeline (scene taxonomy sampling → action grounding → case validation).

**Results.** Judgment ordering aligns with human preferences; provides verifiable, fine-grained diagnoses. Analysis shows adapting a video generator into a world model **redistributes** capability across settings rather than uniformly improving it.

| Verdict | **ADOPT** agentified eval harness: decompose case → specialized sub-agents + tools → validated evidence tree (not scalar-only rubric). `mirros-lab/harnesseval-w` **NO-GO** clone (null SPDX). `policy_wired`. Pairs K162 verification hierarchy, K277 measurement integrity. |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.16859-harnesseval-w-agentifying-the-evaluation-of-visu.pdf` |
