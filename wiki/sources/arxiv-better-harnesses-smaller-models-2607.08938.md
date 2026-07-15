---
title: "Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation"
type: source
tags: [source, arxiv, harness-adaptation, slm, cost-efficiency, k168]
keywords: [2607.08938, small language models, harness optimizer, meta-agent, failure modes, gepa, cmu]
related:
  - concepts/failure-mode-harness-adaptation-mapping.md
  - entities/tools/migration-analysis-replication-package.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/retrospective-harness-optimization-rho.md
  - concepts/agent-harness-operational-definition.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - sources/brief-k168-slm-harness-adaptation-2026-07-15.md
  - sources/brief-k169-harness-adaptation-evaluation-rigor-prod-2026-07-15.md
maturity: draft
created: 2026-07-15
updated: 2026-07-15
---

## Relations

- `@concepts/failure-mode-harness-adaptation-mapping.md` — synthesized framework from this paper
- `@entities/tools/migration-analysis-replication-package.md` — repo Phase-0 (replication package, NO-GO adopt)
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — paired K169 paper questioning harness-evolution ROI
- `@concepts/harnessx-composable-evolution-foundry.md` — sibling harness-evolution search-space design
- `@concepts/retrospective-harness-optimization-rho.md` — sibling label-free harness optimizer
- `@sources/brief-k168-slm-harness-adaptation-2026-07-15.md` — prod brief stub

## Raw Concept

- **Title:** Better Harnesses, Smaller Models: Building 90% Cheaper Agents via Automated Harness Adaptation
- **Author:** Chenyang Yang, Xinran Zhao, Tongshuang Wu, Christian Kästner (Carnegie Mellon University)
- **Type:** arXiv preprint, cs.SE
- **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.08938-building-90-cheaper-agents-via-automated-harness.pdf`
- **Retrieved:** 2026-07-15
- **arXiv ID:** 2607.08938v1, submitted 9 Jul 2026
- **Pages:** 12
- **Read status:** read (full text, including Table I/II, RQ1–RQ4 results)
- **Public code:** `github.com/malusamayo/migration-analysis` (replication package only — see entity page)

## Narrative

### Thesis

For **routine, repetitive business tasks** (not open-ended coding), small open-weight language models (SLMs, 3B–30B active params) can match frontier-LLM agent performance at ~4–10% of the cost — **if** paired with a harness (prompts, tools, hooks, sub-agents) that has been specifically adapted to the SLM's weaknesses. The paper's core contribution is a **framework mapping agent failure modes to harness-adaptation strategies**, plus an automated **harness optimizer** (meta-agent) that discovers these adaptations without manual engineering.

### Failure-mode → adaptation framework (Section II)

Five capability-indexed failure modes: **tool-use**, **instruction-following**, **knowledge**, **long-context**, **planning/reasoning**. Three adaptation categories, each with two named strategies:

| Category | Strategies |
|----------|-----------|
| Context adaptations | A1 add contexts (demonstrate, reinforce, externalize, plan) · A2 manage contexts (reveal progressively, compress/summarize) |
| Tool adaptations | T1 create tools (wrap, enforce, encode) · T2 manage tools (filter, adapt schema) |
| Agent-loop adaptations | L1 instrument code (hooks/guardrails) · L2 orchestrate agents (split roles) |

Each strategy trades new capability for a new failure risk (e.g., adding contexts fixes knowledge gaps but risks long-context/instruction-following failures) — there is **no free lunch**, adaptation must be targeted per observed failure.

### Harness optimizer (Section III)

A GEPA-style ([Agrawal et al. 2607.19457] genetic/Pareto-front search) meta-agent loop: (1) sample harness from pool, evaluate on training batch, log full raw-JSON trajectories; (2) meta-agent (frontier LLM, e.g. gemini-3.1-pro-preview) diagnoses failures against current harness + search-memory of past edits, proposes a harness edit; (3) sanity-check, then validate on held-out validation batch, add to pool if improved. Search space = editable surface of `software-agent-sdk` (OpenHands): system prompts/skills, primitive + custom tools, hooks, context management, sub-agents. Budget: **$20 per task-model pair** (amortized after ~13 production runs given per-run savings).

### Results (Table I, Table II)

7 curated business tasks (attendance-auditing, budget-approval, stock-alert, anomaly-detection, playwright-testing, website-management, code-refactoring) × 3 SLMs (gemma-4-26b-a4b, qwen3-coder-30b-a3b, ministral-3-8b) vs. gemini-3.1-pro-preview baseline (89.7% avg accuracy, $1.735/query):

- **16 of 21** task-SLM pairs significantly improved by harness optimization; **7 pairs** close the SLM-LLM gap entirely.
- Best case: gemma-4-26b-a4b + optimized harness recovers **89.7%→80.2% avg accuracy at $0.071/query (4% of LLM cost)**, with 25% latency reduction. Single best pair (budget-approval): 98.3% accuracy at 8% of cost.
- Adaptation is **more effective for less-diverse tasks** (Spearman ρ = −0.96 between task-diversity and optimized-harness score; diversity-controlled variant: 89.1%→68.0% as templates go 3→20).
- Adaptation is **more effective for stronger-base-capability SLMs** (+48.8% for capable SLMs vs. +15.5% for weak ones) — harnesses absorb difficulty but cannot substitute for missing core capability.
- Dominant failure modes addressed: instruction-following (81%), knowledge (81%), tool-use (62%), long-context (33%). Dominant strategies: add contexts (86%), create tools (43%), manage tools (29%). **No successful sub-agent-orchestration adaptations observed** — current SLMs (and/or the meta-agent) can't yet manage sub-agent coordination well.
- **Different SLMs need different adaptations** — harness optimization does not transfer across models; must re-run per model migration.

### Worked example (Fig. 1, Fig. 4) — budget-approval task

Generic harness: broad MCP tool set + simple system prompt → SLM (gemma-4-26b-a4b) scores 75.0% vs LLM 97.3%. After 23 optimizer iterations: filtered tool set (6→5 MCP tools), explicit step-by-step workflow prompt, and a custom `anti_loop_hook.py` that denies repeated identical `send_message` calls with an explanatory rejection message. Result: SLM reaches 98.3% at 8% of LLM cost — a textbook L1 (instrument code) + T2 (filter tools) + A1 (reinforce instructions) combo.

### Lessons for building harness optimizers (Section V-A)

1. **Diagnosis quality beats iteration count.** Raw JSON trajectories (unsummarized) diagnose better than markdown-condensed traces — condensation loses details the meta-agent needs. Downgrading the meta-agent model (gemini-3.1-pro→flash) for more iterations produced worse harnesses net.
2. **Exploration diversity over quantity.** Keep search memory of prior attempts to avoid rediscovering the same fix; run several independent search chains rather than one long chain.
3. A strong frontier meta-agent given faithful failure evidence + an editable harness does **not** need hand-holding heuristics (manually-written failure→fix rules did not help further).

### Implications flagged by authors

- Agent developers: benchmark-score SLM capability (Artificial Analysis index) is a useful proxy for how much harness adaptation will help — correlate before committing.
- Future work direction: **mixtures-of-harnesses** (per-instance routing among specialized harnesses) for tasks too diverse for one harness; online monitoring for task-distribution drift.
- Reproducibility caveat (author-stated): closed-source frontier APIs (used as the meta-agent) drift/deprecate — exact replication risk over time.

### CCC caution — read alongside K169 companion paper

This paper searches for and reports the **best** validated harness per task-model pair using **the same task distribution for search and final test-set evaluation** (20/20/60 train/val/test split, same benchmark family). `@sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md` (companion ingest, same day) argues this exact evaluation shape systematically overstates harness-evolution gains vs. simple test-time-scaling baselines, and that gains often don't generalize to held-out task distributions. This paper's numbers are plausible and its framework is independently useful as a **failure-mode taxonomy**, but its magnitude claims (89.7%/96% cost reduction) should carry a `[NEEDS VERIFICATION 2026-07-15]` tag pending a parallel-sampling / sequential-refinement baseline comparison — which this paper does not run.

## Snippets

> "The best SLM agent recovering 89.7% of LLM performance at 4% of the cost." — Abstract

> "There is no one-size-fits-all solution when we create harnesses for SLMs. Instead, we need to create harnesses specialized to the task contexts and observed failures." — §II-B

> "We found that the meta-agent performs better when it receives high-fidelity failure evidence rather than aggressively summarized traces." — §V-A Lesson 1

> — [Source: arxiv-2607.08938-building-90-cheaper-agents-via-automated-harness.pdf, retrieved 2026-07-15]
