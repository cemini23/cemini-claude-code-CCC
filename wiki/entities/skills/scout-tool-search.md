---
title: scout-tool-search (skill) — local skill frontmatter BM25 top-k search
type: entity
tags: [skill, scout, tool-search, federation, k311]
keywords: [scout-tool-search, SKILL.md frontmatter, top-k, BM25, tool_search]
related:
  - concepts/hybrid-mcp-tool-discovery-lazy-catalog.md
  - entities/skills/route.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
  - briefs/2026-08-31_ccc-pretooluse-scout-bm25-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-31
wire_status: runtime_wired
wire_target: ".cursor/skills/scout-tool-search/SKILL.md"
---

## Relations

- `@concepts/hybrid-mcp-tool-discovery-lazy-catalog.md`
- `@entities/skills/route.md`

K311 leftover shipped 2026-08-28 as operator-invoked skill; **BM25-lite scoring shipped 2026-08-31**. Indexes **local** `.cursor/skills/*/SKILL.md` name + description (plus optional one-line from the body's first heading), returns **BM25-lite** (k1=1.5, b=0.75, IDF from the local corpus, small substring bonus) **top-k (k≈5)** with `name`, `path`, `score`, one-line why. No pip, no HF, no vector DB. `execute` = read the SKILL.md — **not** a live MCP invoke, not a catalog dump. Helper `scripts/scout_tool_search.py` (`selftest`: ≥3 federation skills, `route` → route, `step` → step-gate in top-k). Federation skill: `federation: true`, `disable-model-invocation: true` — no `/route` rewrite, no `curl|bash`.
