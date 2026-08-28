---
title: "INTENT-AS-A-TOOL — track agentic misalignment (CCC K323)"
type: source
tags: [source, arxiv, safety, intent, misalignment, cot-monitoring, mit, k323]
keywords: [2608.27348, INTENT-AS-A-TOOL, intent tool, CoT monitoring, agentic misalignment, judge-free signal, RebeccaZhang22]
related:
  - concepts/intent-as-a-tool-misalignment-signal.md
  - entities/tools/intent-as-a-tool.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
read_status: skimmed
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@concepts/intent-as-a-tool-misalignment-signal.md`
- `@entities/tools/intent-as-a-tool.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment |
| **arXiv** | 2608.27348 (cs.CL, 2026-08-27) |
| **Authors** | Yutong Zhang, Jianshuo Dong, Peng Xu, Long Wang, Jie Zhang, Tianwei Zhang, Xiaoping Zhang, Han Qiu (Tsinghua + MatrixOrigin + NTU + SiliconProspect AI) |
| **Code** | `github.com/RebeccaZhang22/intent-as-a-tool` — **MIT** (gh API verified 2026-08-28; ~0.3MB) → **GO REFERENCE** clone `.local/adopts/intent-as-a-tool` |
| **Retrieved** | 2026-08-28 |

## Narrative

**Verdict: ADOPT policy** — intent-targeted tools give a judge-free commitment signal; complements CoT monitors. Runtime **`wont_wire`**. **No attack/PoC text.** Cybersec steal.

CoT-monitoring study with five open-source models shows harmful action is often **preceded by intent signals in reasoning** — observable harmful intent usually proceeds to harmful execution. But post-hoc CoT labels are too coarse to show how intent changes during generation.

INTENT-AS-A-TOOL adds **intent-targeted tools** to the model's action space: the model is instructed to call them once it decides to perform the target behavior. The **probability of calling an intent tool** becomes a **judge-free, fine-grained signal** of commitment to that behavior. This:

- complements CoT monitoring,
- expands post-hoc CoT labels into **dense trajectories**,
- identifies **critical steps for online intervention** (intent-guided intervention matches or exceeds prompting-based baselines on Qwen-family models, at lower intervention density).

Tools are normally intent-agnostic (an email tool can send a benign update or a harmful message); intent tools make the intent itself an observable action.

CCC policy: for any monitorable high-risk behavior, give the model a dedicated intent tool and track its call probability — no external judge needed. No attack writeups.

| Confidence | `[TENTATIVE]` — paper results as reported; not reproduced in CCC |
|------------|------------|

## Snippets

> "The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior." [Source: arXiv 2608.27348 abstract]

> "INTENT-AS-A-TOOL complements CoT monitoring, expands post-hoc CoT labels into dense trajectories, and identifies critical steps for online intervention." [Source: arXiv 2608.27348 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.27348-intent-as-a-tool-makes-it-easy-to-track-agentic.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
