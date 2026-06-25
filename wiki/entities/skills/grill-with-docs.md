---
title: grill-with-docs (skill) — plan interview + ADR/glossary docs
type: entity
tags: [skill, mattpocock, review, adr, k126]
keywords: [grill-with-docs, grill-me, pre-ship-review, SKILL.md]
related:
  - entities/tools/mattpocock-skills.md
  - entities/skills/cursor-audit.md
  - entities/skills/super-audit.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/claim-drift-automated-research.md
  - "@osint-wiki/entities/tools/mattpocock-skills.md"
maturity: draft
created: 2026-06-22
updated: 2026-06-22
license_verified: MIT
cross-wiki-source: "github.com/mattpocock/skills skills/engineering/grill-with-docs"
---

## Relations

- `@entities/tools/mattpocock-skills.md` — parent library (K126 Adopt)
- `@entities/skills/cursor-audit.md` — multi-model audit; grill-with-docs is interview-style plan sharpening
- `@entities/skills/super-audit.md` — pre-ship prod reviews
- `@concepts/claim-drift-automated-research.md` — claim-boundary audit before ship

Skill files at `.cursor/skills/grill-with-docs/`. **Federation deploy:** `scripts/sync_federation_cursor_skills.sh`. Briefs refer to **grill-me**; mattpocock repo ships **grill-with-docs** (same role).

## Raw Concept

Transplanted **2026-06-22** per K126 brief — relentless interview to sharpen plans/designs while producing ADRs and glossary entries.

## Narrative

| Field | Value |
|-------|-------|
| **Source** | `mattpocock/skills` → `skills/engineering/grill-with-docs` |
| **License** | MIT [CONFIRMED gh api 2026-06-22] |
| **Install** | `.cursor/skills/grill-with-docs/` |
| **Use** | Pre-submit poker arena review; pre-ship plan hardening |

**Phase-0:** `scripts/adopt_k126_phase0.sh`

## Snippets

> "A relentless interview to sharpen a plan or design, which also creates docs (ADR's and glossary) as we go."
> — [Source: mattpocock/skills grill-with-docs SKILL.md]
