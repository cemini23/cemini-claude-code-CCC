---
title: awesome-cursorrules — CC0 catalog for .cursor/rules patterns
type: entity
tags: [tool, cursor, rules, reference, cross-wiki-route]
keywords: [awesome-cursorrules, patrickjs, cursor-rules, cc0, pattern-library]
related:
  - concepts/cursor-ide-workspace.md
  - concepts/twelve-rule-claude-md-template.md
  - concepts/cross-wiki-routing.md
  - entities/tools/open-design.md
  - concepts/cross-wiki-tool-eval-inventory.md
maturity: validated
created: 2026-05-24
updated: 2026-05-21
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md"
---

## Relations

- `@concepts/cursor-ide-workspace.md` — primary consumer: cherry-pick into project `.cursor/rules/`
- `@concepts/twelve-rule-claude-md-template.md` — persistent CLAUDE.md vs Cursor rules files
- `@concepts/cross-wiki-routing.md` — per-wiki rules differ (OSINT vs CCC vs CeminiSuite)
- `@entities/tools/open-design.md` — modular skill Markdown patterns (parallel authoring discipline)

Cross-wiki: `@osint-wiki/entities/tools/awesome-cursorrules.md`; K63 URL #11.

## Raw Concept

`PatrickJS/awesome-cursorrules` — community **rules catalog** for Cursor (~40k★). CC0-1.0 [CONFIRMED 2026-05-24]. K63 **Adopt** as **pattern library**, not blind copy-paste.

## Narrative

### CCC use

1. **Curated import landed** (2026-05-21): `.cursor/rules/ccc-*.mdc` + `.cursor/curated-rules/README.md` — patterns from catalog, not bulk copy.
2. **Do not** mirror the full catalog — churn + irrelevant domains (per LESSONS.md spec-only posture).
3. Pair with `~/.cursor/rules/cemini-projects.mdc` global rule for SSH/MCP map.

### Adoption posture

| Check | Status |
|-------|--------|
| License | CC0-1.0 [CONFIRMED] — public domain dedication |
| Phase-0 | Light — review each rule file before import |
| Verdict | **GO — adopted** [CONFIRMED 2026-05-21] |

## Snippets

> "rules catalog for `.cursor/rules`; CCC Adopt as pattern library (not blind copy)."
> — [Source: briefs/2026-05-24_k63-ccc-cursor-agent-tooling-from-osint.md]
