---
title: Webwright — Microsoft generative UI browser automation (Phase-0 pending)
type: entity
tags: [tool, browser, claude-plugin, adopt-candidate, k88]
keywords: [webwright, microsoft, browser-automation, generative-ui, claude-plugin]
related:
  - entities/tools/claude-code.md
  - concepts/cursor-ide-workspace.md
  - concepts/skill-vetting.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - "@osint-wiki/entities/tools/microsoft-webwright.md"
maturity: draft
created: 2026-05-31
updated: 2026-05-31
cross-wiki-source: "@osint-wiki/entities/tools/microsoft-webwright.md"
---

## Relations

- `@entities/tools/claude-code.md` — `.claude-plugin` host
- `@concepts/cursor-ide-workspace.md` — compare vs built-in browser + Playwright MCP
- `@concepts/skill-vetting.md` — Phase-0 before install
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — K88 v5 Adopt
- `@osint-wiki/entities/tools/microsoft-webwright.md` — OSINT stub (canon summary)

## Raw Concept

K88 v5 **Adopt** — `github.com/microsoft/Webwright`. MIT `[CONFIRMED 2026-05-31]`. Browser automation harness with Claude plugin manifest.

## Narrative

| Check | Status |
|-------|--------|
| License | MIT — GitHub API verified (K88) |
| vs Cursor browser | **CONDITIONAL-GO** — prefer built-in `browser_*` for Anthropic docs; Webwright for Claude Code plugin path |
| vs Playwright MCP | Global fallback only per CCC rules |
| Phase-0 | **PENDING** — plugin sandbox, egress on prod boundary |

**Verdict:** **CONDITIONAL-GO** — Phase-0 audit before `/plugin install`.

## Snippets

> Compare Webwright vs Cursor built-in browser before Adopt.
> — [Source: briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md]
