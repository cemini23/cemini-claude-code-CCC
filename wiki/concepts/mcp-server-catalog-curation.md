---
title: MCP server catalog curation — USB-C mental model (K98)
type: concept
tags: [concept, mcp, catalog, curation, k98]
keywords: [explorax, mcp-servers, usb-c, lazy-tool, phase-0, catalog]
related:
  - entities/tools/lazy-tool.md
  - concepts/mcp-context-optimization.md
  - concepts/skill-vetting.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - sources/k67-explorax-100-repos-reference.md
  - sources/trading-posts-compilation-18-2026-06-04.md
  - entities/tools/conductor-mcp.md
  - concepts/seclaw-agent-security-evaluation.md
  - "@osint-wiki/sources/trading-posts-compilation-18-2026-06-04.md"
maturity: draft
created: 2026-06-04
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-18-2026-06-04.md"
---

## Relations

- `@entities/tools/lazy-tool.md` — defer full MCP enumeration until invoke time
- `@concepts/mcp-context-optimization.md` — four-layer cost stack
- `@concepts/skill-vetting.md` — Phase-0 before any catalog GO
- `@concepts/cross-wiki-tool-eval-inventory.md` — dedupe against existing rows
- `@sources/k67-explorax-100-repos-reference.md` — prior @exploraX_ 100-repo queue (K67)
- `@sources/trading-posts-compilation-18-2026-06-04.md` — K98 Post 10 (@exploraX_)
- `@concepts/seclaw-agent-security-evaluation.md` — security eval before expanding write tools

## Raw Concept

K98 Post 10 (@exploraX_): viral **50 MCP servers** catalog for Claude/Codex/Gemini. CCC treats as **curation workflow**, not install list — USB-C metaphor (one protocol, many devices) maps to stdio MCP + global `~/.cursor/mcp.json` policy.

## Narrative

### Curation pipeline [CONFIRMED via existing CCC discipline]

1. **Preingest** — `python3 scripts/preingest_check.py` on any new repo URL
2. **Dedupe** — `@concepts/cross-wiki-tool-eval-inventory.md` + OSINT `entities/tools/*`
3. **Phase-0** — license API, transport, credentials, rate limits, failure mode per tool class
4. **Cost gate** — if ≥5 MCP servers active → `@entities/tools/lazy-tool.md` (OSINT folder)
5. **Security gate** — SeClaw eval or `@entities/tools/defenseclaw.md` patterns before write-capable MCP

### vs K67 exploraX list

| Batch | Scope | CCC action |
|-------|-------|------------|
| K67 Post 36 | 100 OSS repos | `@sources/k67-explorax-100-repos-reference.md` audit queue |
| K98 Post 10 | 50 MCP servers | Same queue discipline; MCP-specific Phase-0 |

**Verdict:** **REFERENCE** — mine posts for discovery URLs; **no bulk MCP install** from social catalogs.

## Snippets

> exploraX 50 MCP servers — USB-C mental model for Claude/Codex/Gemini tool surfaces. [TENTATIVE — Posts.docx K98 Post 10]
