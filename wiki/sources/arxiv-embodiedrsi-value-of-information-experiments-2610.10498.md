---
title: "EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution (CCC K440)"
type: source
tags: [source, arxiv, k440]
keywords: [2610.10498, k440]
related:
  - concepts/value-of-information-experiment-selection.md
  - briefs/2026-10-08_ccc-k436-k440-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-08
updated: 2026-10-08
---

## Relations

- `@concepts/value-of-information-experiment-selection.md`
- `@briefs/2026-10-08_ccc-k436-k440-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution |
| **arXiv** | 2610.10498 (2026-10) |
| **Repo** | `Geeksongs/agentic_robotics` |
| **Retrieved** | 2026-10-08 |

## Narrative

**Verdict: REFERENCE (cross-domain; pattern transfers).**

**Spend the experiment on the hypothesis it can actually settle.** A self-evolving agentic harness for robot learning where the model stays frozen and the **harness** improves. The organising structure is a **Hypothesis Graph** holding competing code and skill hypotheses, and the selection rule is the transferable part: **Value-of-Information Experiment Selection** picks the physical experiment that can *distinguish between the live hypotheses* — rather than the experiment that seems most promising, which the paper argues is why prior self-evolving harnesses use robot trials inefficiently. Outcomes then drive **Code–Skill Co-Evolution**; a slow system builds **Hierarchical Memory**, and **Reward-Grounded Memory Learning** keeps the memories worth keeping for later fast-system improvement. RoboCasa365: **77.0% overall, 71.3% on Composite-Unseen, against 40.1% for the best baseline**; LIBERO-Pro 86.8%; zero-shot transfer to a real robot 71.3%. **CCC reading:** the harness shape is general even though the domain is not. **Choose the next action by what it would disambiguate, not by what looks best** is the same question K434 raised from the other side — K434 asked whether history predicts when a context operation will *hurt* and found little signal; VoI asks which operation would *tell you the most* and is an answer to that kind of failure. Also note the **memory that earns its place** framing: hierarchical memory with a reward-grounded retention rule, which is K429's budgeting question with a learning rule attached. Pairs K416/K419/K429/K434. **Phase-0: `Geeksongs/agentic_robotics` and `Einsia/EmbodiedRSI` both return no licence** → **no clone**. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "Value-of-Information Experiment Selection chooses physical experiments that can distinguish these hypotheses." [Source: arXiv 2610.10498 (retrieved 2026-10-08)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.10498-embodiedrsi-active-continual-robot-learning-thro.pdf` |
