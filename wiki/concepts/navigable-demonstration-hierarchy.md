---
title: "Recursive Video In-Context Learning for Agentic Robot (CCC K430)"
type: concept
tags: [concept, k430]
keywords: [2610.06843, k430]
related:
  - sources/arxiv-rv-icl-navigable-demonstration-hierarchy-2610.06843.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-06_ccc-k426-k430-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@sources/arxiv-rv-icl-navigable-demonstration-hierarchy-2610.06843.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-06_ccc-k426-k430-sip-ready.md`

## Raw Concept

K430: REFERENCE (cross-domain; pattern transfers) — arXiv 2610.06843.

## Narrative

**RV-ICL — let the agent navigate the demonstration, do not paste it into the prompt.** Agentic robot harnesses improve across episodes through **text memory**, which records *what the agent did* but not *how the task is done*. A demonstration video shows the how, and fits badly into context three ways, each named precisely: **the full video slows every turn**; **fixed keyframes lose the contact detail that decides whether a grasp holds**; and **what the agent needs shifts** — task structure while planning, frames around each contact while executing. RV-ICL's answer is architectural: turn the demonstration into **a hierarchy the agent navigates rather than a prompt it receives**. Levels run coarse-to-fine — whole-task keyframes → phases → moments → short clips — built from the demonstration's **sub-events** (grasps, releases), and exposed through **read-only tools**. The agent reads coarse levels before planning, **re-enters the hierarchy whenever a step needs more detail**, and loads **only the clip of its current sub-goal**. Training-free. One demonstration per task suffices. On RPent: LIBERO-PRO **92.6% → 96.5%**, LIBERO-Plus **86.7% → 95.8%**. **CCC relevance is direct and it is the same argument as K419 VISTA, made one level more explicit:** do not pre-decide what context matters — **expose it as a navigable structure and let the agent pull what it needs, when it needs it**. Where VISTA gives lossless retention plus inspection over frames, RV-ICL gives lossless retention plus a *pre-indexed semantic hierarchy*, so retrieval is cheaper than search. Pairs K419 / K311 lazy MCP / `@concepts/context-engineering.md` / `@concepts/progressive-skill-discovery-access-control.md` (progressive disclosure, earned by capability). Cross-domain (robotics) so REFERENCE, but the pattern is harness-general. **Phase-0: no public repo confirmed.** Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.06843 locators." [Source: CCC K430 synthesis]
