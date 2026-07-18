---
title: adopted-geo-tools — federation Cursor skill (SEO domain)
type: entity
tags: [entity, skill, cursor, geo, seo, federation]
keywords: [adopted-geo-tools, E-GEO, geo-optimizer, wondelai, federation-sync]
related:
  - entities/skills/goal.md
  - entities/skills/to-issues.md
  - entities/skills/grill-with-docs.md
  - "@seo-wiki/entities/tools/e-geo.md"
  - "@seo-wiki/entities/tools/geo-optimizer-skill.md"
  - "@seo-wiki/entities/tools/wondelai-skills.md"
maturity: validated
created: 2026-07-18
updated: 2026-07-18
---

## Relations

- `@entities/skills/goal.md` — sibling federation skill
- `@seo-wiki/entities/tools/e-geo.md` — E-GEO adopt + rewrite helper
- `@seo-wiki/entities/tools/geo-optimizer-skill.md` — GEO audit CLI
- `@seo-wiki/entities/tools/wondelai-skills.md` — CRO / improve-website skills

## Raw Concept

Domain Cursor skill for locally adopted SEO/GEO tooling. Canon lives in the SEO wiki (not CCC) because the on-disk clones and scripts are SEO-repo paths. Synced federation-wide so agents in OSINT, tipdrop, gambling, etc. can still invoke the helpers via absolute `SEO_ROOT`.

## Narrative

| Field | Value |
|-------|-------|
| **Canon** | `/Users/claudiobarone/Projects/SEO:GEO B&M Business/.cursor/skills/adopted-geo-tools/SKILL.md` |
| **User-global** | `~/.cursor/skills/adopted-geo-tools/SKILL.md` |
| **Sync** | `scripts/sync_federation_cursor_skills.sh` → `DOMAIN_SKILL_DIRS` |
| **Triggers** | service-page GEO rewrite, site GEO audit, local B&M conversion / wondelai CRO |

**Deploy:** edit SEO canon, then run sync from CCC. Do not duplicate the skill body inside CCC.

## Snippets

```bash
bash "/Users/claudiobarone/Projects/Cemini claude code CCC/scripts/sync_federation_cursor_skills.sh"
```
