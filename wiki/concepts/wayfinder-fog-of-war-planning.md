---
title: "Wayfinder — fog-of-war planning (map / ticket / session)"
type: concept
tags: [concept, planning, fog-of-war, wayfinder, k244]
keywords: [wayfinder, /grill-me, unknown unknowns, map-ticket-session, leading words]
related:
  - sources/newsletter-rss-latent-space-2026-08-20-wayfinder.md
  - concepts/skill-set-selection-under-budget.md
  - concepts/agent-toolkit-routing-research-backlog.md
  - entities/skills/wayfinder.md
  - entities/skills/grill-with-docs.md
maturity: draft
created: 2026-08-21
updated: 2026-08-21
wire_status: runtime_wired
wire_target: ".cursor/skills/wayfinder/SKILL.md"
---

## Relations

- `@sources/newsletter-rss-latent-space-2026-08-20-wayfinder.md`
- `@entities/skills/wayfinder.md`

## Raw Concept

How do you plan when the shape of the work is unknown — the "fog of war" of an open-ended task?

## Narrative

**Wayfinder pattern (steal-from, Latent Space):** make planning explicit under fog of war:

- **Map** — what is known about the space (terrain, constraints, knowns).
- **Tickets** — discrete open questions / subtasks with owners and states.
- **Session** — the live context that binds map + tickets to the current run.

Two entry modes: **`/grill-me`** for one-session, bounded paths (the planner interrogates the operator to converge); **`/wayfinder`** for unknown-unknowns work where the goal itself is fuzzy — surface unknowns first, then plan. **Leading words matter**: the phrasing of the request changes what the planner treats as known vs unknown.

**Cemini steal (wired 2026-08-21):**

1. When a task's requirements are genuinely open, run a fog-of-war pass before committing to a plan — enumerate unknown-unknowns as tickets, not assumptions.
2. Distinguish bounded paths (grill-to-converge) from exploratory paths (map-first) — one prompt shape does not fit both.
3. Federation skill: `.cursor/skills/wayfinder/` (`/wayfinder`). Bounded paths still use `grill-with-docs`.

| Verdict | **ADOPT** opt-in skill — `runtime_wired` (federation sync). |
