---
title: Runtime context — MCP + file refs vs agent guessing (K97)
type: concept
tags: [concept, context-engineering, mcp, k97]
keywords: [ericzakariasson, runtime-context, file-refs, mcp, grounding]
related:
  - concepts/context-engineering.md
  - concepts/mcp-context-optimization.md
  - entities/tools/claude-code.md
  - entities/tools/lazy-tool.md
  - concepts/claude-harness-dynamic-workflows-k88.md
  - sources/trading-posts-compilation-17-2026-06-03.md
maturity: draft
created: 2026-06-03
updated: 2026-06-03
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md"
---

## Relations

- `@concepts/context-engineering.md` — parent discipline for what enters the window
- `@concepts/mcp-context-optimization.md` — lazy MCP + static prompt layers
- `@entities/tools/claude-code.md` — Read/Grep/MCP tool surface
- `@entities/tools/lazy-tool.md` — defer MCP catalog until needed
- `@concepts/claude-harness-dynamic-workflows-k88.md` — dynamic workflow routing complements explicit refs
- `@sources/trading-posts-compilation-17-2026-06-03.md` — K97 Post 4 (@ericzakariasson)

## Raw Concept

K97 Post 4 (@ericzakariasson): **runtime context** pattern — wire **MCP tools + explicit file references** into the harness so the agent reads ground truth instead of guessing repo layout or API shapes from stale training.

## Narrative

### Anti-pattern vs pattern

| Anti-pattern | Pattern |
|--------------|---------|
| "Find the auth module" (no path) | `@wiki/index.md` → follow `@relations`; `@path/to/file.md` in prompt |
| Enumerate all MCP tools in system prompt | `@entities/tools/lazy-tool.md` + ToolSearch / on-demand MCP |
| Re-describe project structure each turn | `CLAUDE.md` + `.cursor/rules/` static layer |
| Ask model to recall Anthropic doc behavior | Fetch via Exa/Brave or `@docs` citation with retrieval date |

### Cemini defaults [CONFIRMED via existing stack]

- Session start: read `CLAUDE.md` + `hot.md` (CCC ritual)
- Wiki queries: `@wiki/index.md` → target pages → `@relations`
- OOD: MCP search before fabricating harness behavior
- Cross-wiki: `@wiki-alias/path` syntax per federation table

**Verdict:** **REFERENCE** — aligns with `@concepts/context-engineering.md`; no new tooling.

## Snippets

> Runtime context vs agent guessing — MCP + file refs over vague prompts. [TENTATIVE — @ericzakariasson, Posts.docx K97 Post 4]
