---
title: goal — Cursor /goal single-shot meta-prompt skill
type: entity
tags: [entity, skill, cursor, goal, k124]
keywords: [goal, full-prompt, cursor-skill, single-shot]
related:
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/claude-code.md
  - sources/brief-k122-k126-federation-cursor-harness-adoptions-2026-06-25.md
  - sources/brief-k132-local-adoptions-cursor-federation-prod-2026-06-27.md
maturity: validated
created: 2026-06-24
updated: 2026-06-29
---

## Relations

- `@entities/patterns/full-prompt-goal-template.md` — wiki canon for envelope structure
- `@entities/tools/claude-code.md` — Claude Code `/goal` + Stop-hook variant

## Raw Concept

Cursor Agent skill deployed federation-wide (2026-06-24). Invoke with **`/goal <task>`** in chat.

## Narrative

| Location | Path |
|----------|------|
| Project | `.cursor/skills/goal/SKILL.md` |
| User-global | `~/.cursor/skills/goal/SKILL.md` |
| Rule | `.cursor/rules/cemini-goal-skill.mdc` |
| Sync script | `scripts/sync_federation_cursor_skills.sh` (goal + to-issues + grill-with-docs) |
| Legacy alias | `scripts/sync_goal_skill_to_workspaces.sh` |
| Prod briefs | `scripts/scp_harness_briefs_to_prod.sh` → `cemini-prod:/opt/cemini/briefs/` |

**Deploy:** run `sync_federation_cursor_skills.sh` from CCC repo after editing canonical skills. Covers federation wikis, OSINT, CeminiSuite, castle-sim, ticket monitors, etc. (18 workspaces + user-global).

**Cursor vs Claude Code:** Cursor has no Stop hook — agent must enforce success-criteria check (rule 10) before ending turn.

## Snippets

```
/goal Phase-0 audit foo/bar — GO/NO-GO with gh license proof
```
