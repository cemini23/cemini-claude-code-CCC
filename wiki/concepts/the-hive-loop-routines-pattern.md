---
title: THE HIVE — loops, Routines, and ant cron (K108)
type: concept
tags: [concept, claude-code, loops, hooks, k108]
keywords: [the-hive, av1dlive, bcherny, loop, routines, batch, ant, self-verification]
related:
  - concepts/dynamic-workflow-orchestrator-off-model.md
  - concepts/claude-harness-dynamic-workflows-k88.md
  - concepts/hooks-for-automation.md
  - entities/tools/claude-code.md
  - concepts/skill-vetting.md
  - sources/trading-posts-compilation-8-2026-06-09.md
  - sources/trading-posts-compilation-7-2026-06-09.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: draft
created: 2026-06-09
updated: 2026-06-09
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md"
---

## Relations

- `@concepts/dynamic-workflow-orchestrator-off-model.md` — K107 off-model orchestrator peer
- `@concepts/claude-harness-dynamic-workflows-k88.md` — prior dynamic-workflow cluster
- `@concepts/hooks-for-automation.md` — Stop/SessionStart discipline
- `@entities/tools/claude-code.md` — `/loop`, `/schedule` (Routines) host surface
- `@sources/trading-posts-compilation-8-2026-06-09.md` — K108 Post 2 (@Av1dlive)

## Raw Concept

K108 Post 2 (@Av1dlive): **THE HIVE** — Boris Cherny harness stack: Tier 1 **`/loop`**, Tier 2 **Routines** (scheduled), Tier 3 **`/batch`** + dynamic workflows + **ant** headless cron for CI/glue.

## Narrative

### Three tiers [TENTATIVE — X post synthesis]

| Tier | Mechanism | CCC mapping |
|------|-----------|-------------|
| **1** | `/loop` slash command | `@entities/tools/claude-code.md` recurring/self-paced loops |
| **2** | Routines (scheduled) | LaunchAgent / `com.cemini.daily-research-digest` cadence peer |
| **3** | `/batch` + dynamic workflows + **ant** | Off-model glue (`brew install anthropics/tap/ant`) |

### Monday→Friday on-ramp (brief steal-first)

1. `brew install anthropics/tap/ant` — headless cron/CI glue
2. `.claude/commands/` + `.claude/agents/` + one **verification skill** with runnable script
3. Loop three commands (`/babysit`, `/slack-feedback`, `/pr-pruner`) before overnight Routines
4. **Boris tip 5:** self-verification skill before unattended Opus — without it, overnight runs are coin flips

**Boundaries:** do not enable auto-permissions on unattended runs; start with **3 loops + 2 Routines**, not "thousands of agents overnight" promo scale.

**Verdict:** **REFERENCE** — extends K107; no new third-party install beyond optional `ant` + existing Claude Code surface.

## Snippets

> "My job is to write loops." [Source: Posts.docx K108, @Av1dlive Post 2 — Boris Cherny via Acquired]
