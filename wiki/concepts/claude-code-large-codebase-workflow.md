---
title: Claude Code on large codebases — navigation and context discipline
type: concept
tags: [concept, claude-code, monorepo, context, k69]
keywords: [bibryam, large-codebase, repomix, subagents, codebase-navigation]
related:
  - entities/tools/claude-code.md
  - concepts/context-engineering.md
  - concepts/mcp-context-optimization.md
  - concepts/subagent-orchestration.md
  - entities/tools/lazy-tool.md
  - entities/tools/repomix.md
  - entities/tools/ttok.md
  - sources/trading-posts-compilation-20-2026-05-27.md
  - concepts/agent-backpressure-loop.md
  - sources/trading-posts-compilation-19-2026-06-07.md
maturity: draft
created: 2026-05-27
updated: 2026-06-07
cross-wiki-source: "@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md"
---

## Relations

- @entities/tools/claude-code.md — primary harness
- @concepts/context-engineering.md — window budgeting on million-line repos
- @concepts/mcp-context-optimization.md — MCP catalog + lazy-tool stack for heavy sessions
- @concepts/subagent-orchestration.md — fan-out per module/service instead of one mega-context
- @entities/tools/lazy-tool.md — deferred MCP tool discovery
- @entities/tools/repomix.md — one-shot pack; stale after edits
- @entities/tools/ttok.md — measure paste cost before bulk context
- @sources/trading-posts-compilation-20-2026-05-27.md — Post 9 (@bibryam)

## Raw Concept

K69 Post 9 (@bibryam): practices for **Claude Code on large codebases** — scoped exploration, incremental context, subagent/module boundaries, avoiding whole-repo dumps.

## Narrative

### Workflow shape [TENTATIVE]

1. **Map before edit** — directory-level recon; `@entities/tools/repomix.md` or targeted grep, not full tree in one prompt.
2. **Subagent boundaries** — align with `@concepts/subagent-orchestration.md` (scatter-gather per package).
3. **MCP hygiene** — `@concepts/mcp-context-optimization.md` + `@entities/tools/lazy-tool.md` to avoid 50-tool schema upfront.
4. **Token preview** — `@entities/tools/ttok.md` before pasting logs or generated packs.

### Cemini alignment [CONFIRMED pattern]

Matches existing CeminiSuite posture: conductor for cross-repo wiki facts; Claude Code for repo edits; `hot.md` for session pin — same discipline at wiki + app scale.

### Non-actions

- No "index entire monorepo into one CLAUDE.md" — violates `@concepts/twelve-rule-claude-md-template.md` spirit.

## Snippets

> Claude Code on large codebases — scoped navigation and context discipline. [TENTATIVE — @bibryam, Posts.docx K69 Post 9]
