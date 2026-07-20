---
title: to-issues (skill) — vertical-slice issue decomposition
type: entity
tags: [skill, mattpocock, issue-tracker, vertical-slice, k126]
keywords: [to-issues, tracer-bullet, milestone-decomposition, SKILL.md]
related:
  - entities/tools/mattpocock-skills.md
  - entities/patterns/full-prompt-goal-template.md
  - concepts/claim-drift-automated-research.md
  - "@osint-wiki/entities/tools/mattpocock-skills.md"
  - sources/brief-k122-k126-federation-cursor-harness-adoptions-2026-06-25.md
  - sources/brief-k132-local-adoptions-cursor-federation-prod-2026-06-27.md
  - entities/skills/adopted-geo-tools.md
maturity: draft
created: 2026-06-22
updated: 2026-07-20
license_verified: MIT
cross-wiki-source: "github.com/mattpocock/skills skills/engineering/to-issues"
---

## Relations

- `@entities/tools/mattpocock-skills.md` — parent library (K126 Adopt)
- `@entities/patterns/full-prompt-goal-template.md` — `/goal` plans decomposed into grabbable issues
- `@osint-wiki/entities/tools/mattpocock-skills.md` — canonical eval

Skill files at `.cursor/skills/to-issues/` (MIT, mattpocock/skills). **Federation deploy:** `scripts/sync_federation_cursor_skills.sh` (18 workspaces + user-global).

## Raw Concept

Transplanted **2026-06-22** per `briefs/2026-06-22_k126-nvidia-mattpocock-skills-adopt.md` — break plans/specs into independently grabbable tracer-bullet issues.

## Narrative

| Field | Value |
|-------|-------|
| **Source** | `mattpocock/skills` → `skills/engineering/to-issues` |
| **License** | MIT [CONFIRMED gh api 2026-06-22] |
| **Install** | `.cursor/skills/to-issues/` |
| **Use** | castle-sim milestone decomposition; federation ingest task breakdown |

**Phase-0:** `scripts/adopt_k126_phase0.sh`

## Snippets

> "Break a plan, spec, or PRD into independently-grabbable issues on the project issue tracker using tracer-bullet vertical slices."
> — [Source: mattpocock/skills to-issues SKILL.md]
