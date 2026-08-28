---
title: scout-tool-search (skill) — local skill frontmatter top-k search
type: entity
tags: [skill, scout, tool-search, federation, k311]
keywords: [scout-tool-search, SKILL.md frontmatter, top-k, term overlap, tool_search]
related:
  - concepts/hybrid-mcp-tool-discovery-lazy-catalog.md
  - entities/skills/route.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
wire_status: runtime_wired
wire_target: ".cursor/skills/scout-tool-search/SKILL.md"
---

## Relations

- `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md`
- `@entities/skills/route.md`

K311 leftover shipped 2026-08-28 as operator-invoked skill: indexes **local** `.cursor/skills/*/SKILL.md` name + description (plus optional one-line from the body's first heading), returns keyword / term-overlap **top-k (k≈5)** with `name`, `path`, `score`, one-line why. `execute` = read the SKILL.md — **not** a live MCP invoke, not a catalog dump. Helper `scripts/scout_tool_search.py` (`selftest`). Federation skill: `federation: true`, `disable-model-invocation: true` — no `/route` rewrite, no `curl|bash`.
