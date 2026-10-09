---
title: "Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents u (CCC K442)"
type: concept
tags: [concept, k442]
keywords: [2610.12360, k442]
related:
  - sources/arxiv-epistemic-humility-knowledge-conflict-2610.12360.md
  - concepts/clarify-before-act-evidence-aligned-close.md
  - concepts/overclaiming-propensity-agent-measurement.md
  - concepts/trajectory-error-lifecycle-attribution.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-09_ccc-k441-k444-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-09
updated: 2026-10-09
---

## Relations

- `@sources/arxiv-epistemic-humility-knowledge-conflict-2610.12360.md`
- `@concepts/clarify-before-act-evidence-aligned-close.md`
- `@concepts/overclaiming-propensity-agent-measurement.md`
- `@concepts/trajectory-error-lifecycle-attribution.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-09_ccc-k441-k444-sip-ready.md`

## Raw Concept

K442: ADOPT eval-methodology (Claude Code harness eval) — arXiv 2610.12360.

## Narrative

**Accuracy and epistemic humility are two different curves.** Defines **epistemic humility (EH)** as three trajectory-level behaviours, **Identify, Solve, Escalate (ISE)**: notice the knowledge gap, act on it with bounded tool use, and tell the user when uncertainty is unresolved. Elicits it through **knowledge conflict** (parametric belief vs. retrieved evidence, or two sources disagreeing) with matched no-conflict controls. Four harnesses evaluated, **one of them Claude Code (Sonnet 4.6, WebSearch/WebFetch/Bash)** alongside Nemotron-ToolOrchestra, OpenHands, and Qwen-Agent. **Three findings:** (1) **higher task accuracy does not imply greater EH** — some high-accuracy configs *identify* the conflict but do not acknowledge unresolved uncertainty in their incorrect final answers; (2) conflict-relevant mentions **peak in the first 10% of execution** then fall — agents detect early but do not follow up; (3) a **one-clause system-prompt intervention raises Escalate while lowering accuracy** (MoNaCo Escalate 1.6 → 60.7 for GPT-5, **13.9 → 60.8 for Claude Code**), landing most configs in the *humble-but-inaccurate* quadrant. Claude Code posts the **highest Identify rate (F1 90.0% on BrowseComp)** yet its wrong finals still do not escalate. **CCC reading:** the paper's recommendation is a **harness affordance** — *expose an explicit abstain-or-escalate action so a conflict raised mid-trajectory survives into the final answer instead of being overwritten by the next tool call*, and score trajectories, not final answers. That is CCC's position on verification gates and on `clarify-before-act`, here measured across four harnesses and shown to be a *system property*, not a model property ('epistemic humility emerges from the interaction among the backbone model, the agent harness, and the evaluation environment'). Pairs `clarify-before-act-evidence-aligned-close`, `overclaiming-propensity-agent-measurement`, `trajectory-error-lifecycle-attribution`. **Phase-0: `KaiserWhoLearns/EpistemicHumilityLLMAgents` Apache-2.0** (1★, pushed 2026-10-09) — released trajectories + per-turn ISE judgments; REFERENCE clone optional. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "See source page for arXiv 2610.12360 locators." [Source: CCC K442 synthesis]
