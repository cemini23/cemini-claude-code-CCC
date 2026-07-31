---
title: phase1-wire — federation Cursor skill (adopt-wire)
type: entity
tags: [entity, skill, phase-1, federation, cursor]
keywords: [phase1-wire, /phase1, wire_status, adopt]
related:
  - concepts/phase1-adopt-wire.md
  - concepts/skill-vetting.md
  - concepts/k73-phase0-audit-decisions.md
  - entities/skills/goal.md
  - entities/skills/route.md
maturity: draft
created: 2026-07-31
updated: 2026-07-31
wire_status: runtime_wired
wire_target: .cursor/skills/phase1-wire/SKILL.md
---

## Relations

- `@concepts/phase1-adopt-wire.md`
- `@concepts/skill-vetting.md`
- `@entities/skills/goal.md`

## Raw Concept

Federation skill that closes the gap between Phase-0 REFERENCE clones and daily harness behavior.

## Narrative

| Field | Value |
|-------|-------|
| Canon | CCC `.cursor/skills/phase1-wire/SKILL.md` |
| Invoke | `/phase1`, “wire adopts”, end-of-ingest propose |
| Inventory | `scripts/phase1_adopt_inventory.py` |
| Deploy | `federation: true` → auto-discovered by `sync_federation_cursor_skills.sh`; CCC post-commit autosyncs |

**Verdict:** **ADOPT** as standard post-ingest step. Not a Phase-0 replacement.
