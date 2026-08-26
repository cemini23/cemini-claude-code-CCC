---
title: "Skill-set selection under budget — BPS set-level, not top-k"
type: concept
tags: [concept, skills, selection, budget, bps, k244]
keywords: [BPS, submodular, monotone, complements, distractors, verification budget]
related:
  - sources/arxiv-k244-harness-skill-selection-cluster.md
  - concepts/skill-misevolution.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - concepts/wayfinder-fog-of-war-planning.md
  - sources/substack-rss-addy-osmani-2026-08-21-software-factory.md
  - entities/skills/skill-set-budget.md
  - concepts/hybrid-mcp-tool-discovery-lazy-catalog.md
maturity: draft
created: 2026-08-21
updated: 2026-08-26
wire_status: policy_wired
wire_target: ".cursor/skills/skill-set-budget/SKILL.md"
---

## Relations

- `@sources/arxiv-k244-harness-skill-selection-cluster.md`
- `@entities/skills/skill-set-budget.md`
- `@concepts/skill-misevolution.md`

## Raw Concept

When a token/context budget forces a choice, which skills should be loaded — and is "best individual skills" the right rule?

## Narrative

**BPS set-level skill select (arXiv 2608.19993, steal-from):** choose a *set* of skills by **monotone submodular benefit − token penalty**, giving a bicriteria guarantee (1−1/e, 1) — instead of picking top-k skills independently. Reported 0.73 vs 0.20–0.52 for baseline routers, with **28% fewer tokens**. Distinguishes **complements** (skills that add signal together) from **distractors** (skills that look useful alone but add none in context).

**Cemini steal (wired 2026-08-21):**

1. Budget selection by marginal-benefit-minus-cost over the *set*, not per-skill rank (pairs token economics — every skill byte is carry cost).
2. Score **complements vs distractors** when auditing the skill library; a skill that never fires in-context is a distractor even if it scores well standalone.
3. Keep a **verification budget** gate (Osmani label discipline) — selection is not verification: a promoted skill still needs an eval gate (pairs skill-misevolution: skills can worsen with practice).

**BPS** = Best Prefix Selection (arXiv 2608.19993). Federation skill: `.cursor/skills/skill-set-budget/`. Policy: `cemini-phase1-policy-wires.mdc`. **No** paper-solver clone.

| Verdict | **ADOPT decision-rule** — skill + policy wired. Algorithm runtime `wont_wire`. |
