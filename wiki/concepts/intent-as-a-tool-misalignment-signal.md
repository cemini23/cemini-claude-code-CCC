---
title: "Intent-as-a-tool — judge-free misalignment signal (CCC K323)"
type: concept
tags: [concept, safety, intent, misalignment, monitoring, k323]
keywords: [INTENT-AS-A-TOOL, intent tool, call probability, CoT monitoring, agentic misalignment, 2608.27348]
related:
  - sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md
  - entities/tools/intent-as-a-tool.md
  - concepts/step-level-tool-guardrails.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
---

## Relations

- `@sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md`
- `@entities/tools/intent-as-a-tool.md`
- `@concepts/step-level-tool-guardrails.md`
- `@briefs/2026-08-28_ccc-k315-k324-sip-ready.md`

## Raw Concept

The question: CoT monitoring detects harmful intent but needs external judges and only yields coarse post-hoc labels. Can the model report its own intent, cheaply and continuously? Answer from INTENT-AS-A-TOOL [Source: wiki/sources/arxiv-intent-as-a-tool-misalignment-2608.27348.md]: yes — make intent an explicit tool call.

## Narrative

**Tools are intent-agnostic.** An email tool can send a benign update or a harmful message; the tool call alone cannot distinguish them. INTENT-AS-A-TOOL adds **intent-targeted tools** to the model's action space — the model is instructed to call one once it decides to perform the target behavior. The **probability of calling that intent tool** is then a **judge-free, fine-grained, continuous** signal of commitment.

Why it works (ADOPT policy):

- CoT monitoring study: harmful execution is usually **preceded by intent signals** — observable harmful intent proceeds to harmful execution in the large majority of cases.
- Post-hoc CoT labels are coarse; intent-tool call probability expands them into **dense trajectories** showing *when* commitment forms.
- The dense signal identifies **critical steps for online intervention** — intent-guided intervention matches/exceeds prompting-based baselines on Qwen-family models at lower intervention density.

CCC policy: for any monitorable high-risk behavior (misalignment, exfiltration intent, destructive tool use), give the model a dedicated intent tool and track its call probability as a tripwire feeding `@concepts/step-level-tool-guardrails.md`. Complements CoT monitors; no external judge required at inference time. No attack writeups; the repo is a REFERENCE clone.

| Confidence | `[CONFIRMED]` — paper results across five open-source models; pattern adoption, not reproduced in CCC |
|------------|------------|

## Snippets

> "Underlying this is the observation that tools are typically intent-agnostic. For example, an email tool can be used for a benign update or for a harmful message." [Source: arXiv 2608.27348 §1, paraphrase]

> "The probability of calling an intent tool provides a judge-free, fine-grained signal of the model's tendency to pursue that behavior." [Source: arXiv 2608.27348 abstract]
