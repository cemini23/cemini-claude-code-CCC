# Lessons — CCC Wiki

A running log of lessons learned while operating the CCC meta-wiki and Claude Code itself. Each entry is dated and kept short. Write an entry when an assumption broke, a workflow changed, or something surprising came up — not for every session.

Newest entries on top.

---

## 2026-05-13 — Cross-wiki deep-dive paid for itself in 1 session; OSINT carries most of the Claude Code material

Dispatched two parallel Explore agents (one OSINT-focused, one for the four laptop-only siblings) and inventoried every page touching Claude Code workflow. The OSINT wiki carried 48 high-signal entries; SEO + Cybersec each carried ~10 substantial pages; 3D-printing + Image-gen had less Claude Code-specific material (just root CLAUDE.md cross-references).

**Key surprise — most of CCC's missing coverage was already written elsewhere.** The 16 seed pages from bootstrap covered the conceptual surface but not the concrete tools and skills. Specifically:

- The SEO wiki's `entities/tools/claude-code-tool-stack.md` was the densest single page Cemini owned on the subject — it documents lazy-tool / claude-code-router / claude-mem / ttok / tech-debt-skill / spec-kit + the 3-cache architecture + the install priority order. CCC didn't have any of that as standalone pages.
- The Cybersec wiki's `concepts/llm-pentest-automation.md` + `entities/tools/pentest-ai-agents.md` + `entities/tools/cua.md` documented the Tier 1/Tier 2 agent-orchestration pattern operationally — CCC's `subagent-orchestration.md` had the abstract concept but no scope-enforcement model.
- The OSINT wiki's `concepts/mcp-context-optimization.md` carried the full 4-layer methodology (lazy-loading proxy / routing / caching / context-budget audit) — CCC had pieces in `token-economics-and-prompt-caching.md` but no consolidated page.

**Outcome**: 16 new CCC pages + 8 deepened existing pages + 10 sibling-wiki backlinks added in one batch. CCC went from 16 to 32 pages, 58 to 179 outbound edges, 8/8 to 36/36 cross-wiki refs resolving. Lint stayed clean throughout.

**Apply**: when bootstrapping the next sibling wiki (or when a sibling wiki accumulates material on a topic CCC owns), run a deep-dive sweep BEFORE writing CCC content from scratch. The federation-as-a-whole is denser than any single wiki; treating CCC as a synthesis layer over the federation is cheaper than treating it as a standalone authority. The cost: ~2 hours of Explore-agent inventory + 2 hours of synthesis. The savings: writing 16 well-grounded pages with real cross-wiki citations vs. 16 hand-wave pages.

**Operating-rule update**: future Phase-0 audits on Claude Code tooling should *first* check whether any sibling wiki has already done the audit (especially OSINT — densest). Skipping this step risks duplicate work and missing the operator-facing context the sibling wiki captured.

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
