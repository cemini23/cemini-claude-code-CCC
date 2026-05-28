---
title: metatrader-mcp-server — MetaTrader bridge MCP (MIT, scope-limited)
type: entity
tags: [tool, mcp-server, trading, adopt-eligible, k71, cross-wiki-route]
keywords: [metatrader, mcp, ariadng, forex, bridge]
related:
  - entities/mcp-servers/polymarket-mcp-server.md
  - entities/tools/claude-code.md
  - concepts/skill-vetting.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - concepts/k73-phase0-audit-decisions.md
  - entities/tools/tvscreener.md
maturity: draft
created: 2026-05-27
updated: 2026-05-28
cross-wiki-source: "@osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md"
---

## Relations

- `@entities/mcp-servers/polymarket-mcp-server.md` — adjacent market-data MCP pattern
- `@entities/tools/claude-code.md` — harness consumer
- `@concepts/skill-vetting.md` — Phase-0 before prod wiring

Cross-wiki: K71 URL #6 `@osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md`.

## Raw Concept

`ariadng/metatrader-mcp-server` — MCP server bridging **MetaTrader** terminals. K71 cataloged as conditional-go; K73 phase-0 scope review demotes current CCC usage to no-go for Cemini's present Polymarket-focused stack.

## Narrative

### CCC posture

| Check | Status |
|-------|--------|
| License | MIT [CONFIRMED K71 `gh api`] |
| Cemini prod | **Separate brief** — not auto-wired to `/opt/cemini` |
| Verdict | **NO-GO for current Cemini scope** (forex/MT mismatch) |

Forex/MT stack is outside current Polymarket core. Keep as reference only unless scope changes.

## Snippets

> "`metatrader-mcp-server` (MIT): NO-GO for current Cemini scope (forex/MT mismatch)."
> — [Source: briefs/2026-05-28_k73-phase0-audit-ccc-decisions.md]
