---
title: Claude Desktop vs Claude Code — two surfaces, two tool ecosystems
type: concept
tags: [concept, claude-desktop, claude-code, mcp, agent-skills, plugin, distribution]
keywords: [claude desktop, claude code, claude_desktop_config.json, agent skills, plugin marketplace, MCP server, /plugin install, install path]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/mcp-servers/exa.md
  - entities/commands/plugin.md
  - concepts/mcp-context-optimization.md
  - entities/tools/skillkit.md
maturity: validated
created: 2026-05-13
updated: 2026-05-16
---

## Relations

- `@entities/tools/claude-code.md` — Claude Code surface (CLI + IDE extensions)
- `@entities/mcp-servers/anthropic-skills.md` — skills as Claude Code's native extension format
- `@entities/mcp-servers/exa.md` — example MCP server that runs in both surfaces
- `@entities/commands/plugin.md` — `/plugin marketplace add` and `/plugin install` are Claude Code-only
- `@concepts/mcp-context-optimization.md` — applies to both surfaces but settings differ
- `@entities/tools/skillkit.md` — translates skill formats across the Claude-Code vs other-agent surface split (SKILL.md ↔ .mdc)

Cross-wiki: `@seo-wiki/concepts/claude-platforms.md` is the original write-up of this distinction (built for non-coder operators choosing where to install local-SEO tools).

## Raw Concept

Question this page answers: **Cemini's wiki references Claude Desktop and Claude Code interchangeably; what's the actual difference, and which extension format goes where?**

## Narrative

Anthropic ships two consumer surfaces that look related but extend differently:

### Claude Desktop

- macOS / Windows graphical app. The conversational UI most non-technical users start with.
- Extends via the **Model Context Protocol (MCP)** — small server programs that expose tools to the chat (web search, browser automation, filesystem access).
- Config file: `~/Library/Application Support/Claude/claude_desktop_config.json` (macOS).
- Uses the same Anthropic auth as Claude Code, but the two apps install separately.

### Claude Code

- CLI / terminal tool, optionally wrapped in IDE extensions (VS Code, JetBrains).
- Extends via **MCP servers** AND via **Agent Skills** (markdown files with SKILL.md frontmatter).
- Config files:
  - `.claude/settings.json` (project-scoped)
  - `~/.claude/settings.json` (user-scoped)
  - `~/.claude/plugins/` (installed skills)
  - `.mcp.json` (project-scoped MCP wiring) or `~/Library/Application Support/Claude/claude_desktop_config.json` (shared with Desktop)
- Adds a **plugin marketplace** with `/plugin marketplace add <repo>` and `/plugin install <name>` commands.

### Tool-distribution mapping

| Tool type | Works in Desktop | Works in Claude Code | Install where |
|-----------|------------------|----------------------|---------------|
| MCP server (Exa, Brave, Playwright, conductor, claude-mem, …) | Yes | Yes | `claude_desktop_config.json` for Desktop; `.mcp.json` for project-scoped Claude Code |
| Agent Skill (`SKILL.md` files, `/plugin install` packages) | No | Yes | `~/.claude/skills/` or `<project>/.claude/skills/`; or `/plugin marketplace add` then `/plugin install` |
| Slash commands (`/goal`, `/loop`, `/schedule`, `/review`) | No | Yes | Built into Claude Code; user/project commands in `.claude/commands/` |
| Hooks (`SessionStart`, `Stop`, `UserPromptSubmit`) | No | Yes | `.claude/settings.json` |

### Why this matters operationally

When a sibling wiki cites "install this Claude Code skill" — that means the user needs Claude Code installed alongside Claude Desktop. Many of Cemini's tooling adoptions (`@entities/skills/claude-seo-agrici.md`, `@entities/skills/marketingskills.md`, `@entities/skills/geo-seo-claude.md`, `@entities/skills/tech-debt-audit.md`) are Claude Code Agent Skills, not MCP servers. They will not appear in Claude Desktop.

When a sibling wiki cites "install this MCP server" — that means the server runs alongside whichever surface the user prefers. The MCP wiring file differs but the server itself is the same.

### Cemini's working surface

Cemini runs Claude Code as the primary daily driver across all five sibling wikis. Claude Desktop is occasionally used for conversational drafting (briefs, exploratory research) where the GUI is more comfortable. Both authenticate to the same Anthropic account.

### Skill vs MCP — when each matters

- **MCP servers** are best for tools that own state (search engines, browsers, databases). The server keeps the connection; Claude Code or Desktop calls into it.
- **Agent Skills** are best for tools that are workflows or prompts (a code review template, a domain-specific chat persona, a structured-output generator). The skill is a markdown file the LLM reads; no server.
- **Hybrid** — many marketplace entries pair a SKILL.md with companion MCP servers. Installing the skill registers the prompt; the server provides the heavy-lifting tools.

The SEO-wiki audit (`@seo-wiki/sources/github-repo-audit-2026-05-07.md`) found that **4 of 5 GO-tier local-SEO tools were Agent Skills**, not MCP servers. The Local-SEO/GEO tooling community has converged on skills. This is a domain-specific signal; Cemini's other domains may converge differently.

## Dead Ends

- **Trying to use a Claude Code skill in Claude Desktop** — won't appear; skills are Claude Code-only.
- **Editing `claude_desktop_config.json` to add a skill** — wrong file; skills don't go there. Add MCP servers to that file; add skills to `~/.claude/skills/`.
- **Treating the two apps as interchangeable** — they share auth and (some) MCP servers; everything else differs.
