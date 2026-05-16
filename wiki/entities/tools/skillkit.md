---
title: "skillkit — universal translation/management bridge for AI-agent skills across 46 agents"
type: entity
tags: [entity, tool, skill-management, skill-translation, mcp-server, marketplace, session-memory, p2p-mesh, adopt, ccc-primary-fit, cross-wiki-route-2026-05-16]
keywords: [skillkit, skill-format-translation, claude-skill-md, cursor-mdc, skillkit-mcp, runtime-skill-discovery, claude-skills-directory, session-memory, p2p-mesh-distribution, apache-2-license, rohitg00]
related:
  - entities/mcp-servers/anthropic-skills.md
  - entities/commands/plugin.md
  - entities/tools/claude-mem.md
  - concepts/claude-desktop-vs-claude-code.md
maturity: draft
created: 2026-05-16
updated: 2026-05-16
cross-wiki-source: "@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md"
---

## Relations

- @entities/mcp-servers/anthropic-skills.md — skillkit governs the same `.claude/skills/` surface the SKILL.md spec defines; it is a management/translation layer on top of that spec
- @entities/commands/plugin.md — alternative skill-acquisition path: where `/plugin` installs from a marketplace, skillkit's MCP server fetches capabilities at runtime
- @entities/tools/claude-mem.md — skillkit's session memory captures transient architectural insights, conceptually adjacent to claude-mem's passive observation layer
- @concepts/claude-desktop-vs-claude-code.md — format translation (SKILL.md ↔ .mdc) spans the Claude-Code vs other-agent surface split
- @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md — cross-wiki source (tool-eval ingest verdict)

## Raw Concept

Cross-routed from OSINT workspace tool-eval ingest 2026-05-16. `skillkit` is a universal translation and management bridge for AI-agent skills, spanning 46 agents (Claude Code, Cursor, Devin, and others). Apache-2.0; ~1,100 stars / last commit 2026-04-21 / 12 open issues. Stack: TypeScript / Node.js. K-cycle tool-eval verdict: **ADOPT**, CCC primary fit — skillkit operates directly on the `.claude/skills/` directory Cemini already uses, and its MCP server is a clean runtime-discovery layer.

URL: https://github.com/rohitg00/skillkit

## Narrative

skillkit sits one layer above the SKILL.md spec (`@entities/mcp-servers/anthropic-skills.md`): where that spec defines what a skill *is*, skillkit manages how skills are *acquired, translated, and discovered* across agents.

### Capabilities

1. **Cross-agent skill translation** — auto-translates skill formats between agents: Claude's `SKILL.md` ↔ Cursor's `.mdc`, and across the 46-agent set. A skill authored once is usable everywhere. For CCC this is the bridge that lets a Cemini-authored skill leave the Claude Code surface without a rewrite.

2. **Skill marketplace (400,000+ skills)** — indexes a marketplace of 400k+ skills sourced from GitHub repos and Gists. Note Cemini's standing stance per `@entities/mcp-servers/anthropic-skills.md`: adopt the spec, do not depend on catalog content. The same caution applies to skillkit's marketplace — it is a discovery surface, not a source of truth, and a 400k-skill catalog carries proportionally large supply-chain surface. Phase-0 audit any skill before install.

3. **MCP server for runtime skill discovery** — ships `npx @skillkit/mcp`, an MCP server that lets agents fetch capabilities (e.g. PDF processing) at runtime without pre-installation. This is the most CCC-relevant piece: it converts skill acquisition from an install-time step into a runtime fetch, adjacent in spirit to the lazy-tool MCP-discovery-proxy pattern (`@entities/tools/lazy-tool.md`).

4. **Session memory + P2P mesh distribution** — captures transient architectural insights during a session (conceptually parallel to claude-mem's passive observation, `@entities/tools/claude-mem.md`), and distributes learned patterns across teammates over a peer-to-peer mesh.

5. **Governs `.claude/skills/`** — operates directly on the directory Cemini already uses for project- and user-scoped skills.

### Verdict

ADOPT for CCC. The MCP runtime-discovery server (`npx @skillkit/mcp`) and the cross-agent translation layer are the high-value pieces; Apache-2.0, ~1,100 stars, and a recent commit (2026-04-21) clear the maturity bar. Treat the 400k-skill marketplace as discovery-only — never auto-install. The session-memory + P2P-mesh feature should be evaluated separately and is **not** part of the adopt recommendation pending the security question below; CCC is a laptop-only workspace with no team-distribution requirement, so the P2P mesh has no current use case here.

### Open questions

- `[NEEDS VERIFICATION 2026-05-16]` — security of the P2P mesh in firewalled / zero-trust subnets: whether the peer-to-peer pattern-distribution mesh can operate (or should be disabled) inside a firewalled zero-trust subnet is unverified. Since CCC is laptop-only with no team mesh need, default to disabling P2P distribution; resolve the security question before any networked deployment.

## Snippets

> skillkit ships an MCP server (`npx @skillkit/mcp`) for runtime skill discovery — agents fetch capabilities like PDF processing without pre-installation. It auto-translates skill formats (Claude SKILL.md ↔ Cursor .mdc) across 46 agents and indexes a marketplace of 400,000+ skills from GitHub and Gists.
[Source: @osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md]
