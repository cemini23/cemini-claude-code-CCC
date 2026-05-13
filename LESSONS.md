# Lessons — CCC Wiki

A running log of lessons learned while operating the CCC meta-wiki and Claude Code itself. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## 2026-05-13 — Catalog content has higher churn than schema content; pin to spec, not catalog

K42 follow-up in OSINT (see `@osint-wiki/LESSONS.md` 2026-05-13 entry) recommended adopting Axis A (SKILL.md spec format) but explicitly rejecting Axis B (catalog content dependency). The Anthropic / instructa skills catalogs see significant churn — `package-security-check` was removed from `instructa/agent-skills` HEAD on 2026-05-12, 12 days after Cemini's eval. **12-day-half-life on a catalog entry is too short for a wiki page to depend on it.**

Applied to CCC at bootstrap: this wiki documents the SKILL.md *spec* and our internal skill use, not third-party catalog entries. Catalog entries are referenced by URL in source pages, not modeled as entities. Same posture for MCP server marketplace entries — we document servers we've actually adopted, not the marketplace as a catalog.

*Apply:* when tempted to add an `entities/skills/<third-party-skill>.md` page, ask whether the skill is in active Cemini use. If no, write a source page citing the URL and move on. The skill page only earns a slot when we depend on it operationally.

---

## 2026-05-13 — Bootstrap a new wiki by copying the closest sibling's CLAUDE.md, not designing from scratch

The Cybersecurity wiki's CLAUDE.md is the cleanest laptop-only schema in the federation — explicit three-layer architecture, no server-sync sections, complete ops loop. Copying it as the base for CCC and adapting the domain-specific sections (folder layout, entity categories, page-type quick reference, related-wikis table) took ~15 minutes; designing a new schema from scratch would have taken hours and produced subtle drift from the federation conventions (which is what the cross-wiki lint check exists to catch).

Cross-wiki conventions worth preserving verbatim:
- `## Relations` / `## Raw Concept` / `## Narrative` / `## Snippets` / `## Dead Ends` body sections, in that order
- `[CONFIRMED]` / `[TENTATIVE]` / `[NEEDS VERIFICATION YYYY-MM-DD]` / `[RETRACTED]` confidence tags
- Bidirectional `@path` cross-links
- `wiki/index.md` content-oriented catalog + `wiki/log.md` chronological append-only ledger
- Session-start ritual (read `hot.md`, then inbox check)

Domain-specific sections to swap:
- Folder layout (entity categories)
- Page-type quick reference (which entity categories matter, with examples)
- External-research MCP table (which tools matter for this domain)
- Related Wikis table (this wiki's alias entry on top, sibling paths relative to *this* CLAUDE.md location)
- Phase-0 audit pattern (failure-mode bullets specific to the tool classes this wiki adopts)

*Apply:* future sibling-wiki bootstraps should follow the same pattern — copy Cybersecurity-wiki's CLAUDE.md, swap domain sections, run the lint script, fix any errors. Don't redesign the schema; it's been calibrated across 4 wikis.

---
