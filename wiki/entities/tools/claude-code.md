---
title: Claude Code (Anthropic CLI)
type: entity
tags: [tool, anthropic, cli, ide, harness, agentic-coding]
keywords: [claude code, claude-code, anthropic cli, claude-cli, agent harness, opus, sonnet, haiku, fast mode, slow mode, session management, slash commands, hooks, mcp]
related:
  - concepts/context-engineering.md
  - concepts/token-economics-and-prompt-caching.md
  - concepts/subagent-orchestration.md
  - concepts/hooks-for-automation.md
  - entities/tools/claude-mem.md
  - entities/tools/openspec.md
  - entities/tools/exa-mcp.md
  - entities/tools/conductor-mcp.md
  - entities/tools/syncthing.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/patterns/ralph-loop.md
  - entities/patterns/full-prompt-goal-template.md
  - entities/tools/lazy-tool.md
  - entities/tools/claude-code-router.md
  - entities/tools/spec-kit.md
  - entities/tools/ttok.md
  - entities/tools/tech-debt-skill.md
  - entities/tools/cua.md
  - entities/tools/claude-code-ultimate-guide.md
  - entities/commands/plugin.md
  - concepts/claude-desktop-vs-claude-code.md
  - concepts/three-cache-architecture.md
  - concepts/mcp-context-optimization.md
  - entities/tools/alumnium.md
  - entities/tools/polyterm-tui-pattern.md
  - entities/tools/superclaude-framework.md
  - concepts/twelve-rule-claude-md-template.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - entities/tools/open-design.md
  - entities/tools/the-architect.md
  - entities/tools/repomix.md
  - entities/tools/n8n-mcp.md
  - entities/tools/claude-code-tips.md
  - concepts/tools-we-dont-use.md
  - concepts/local-llm-mechanics-primer.md
  - entities/tools/ai-engineering-roadmap.md
  - concepts/claude-code-large-codebase-workflow.md
  - concepts/claude-obsidian-notebooklm-bridge.md
  - concepts/agent-sandbox-unikraft.md
  - concepts/agent-token-discipline-openclaw-hermes.md
  - concepts/five-layer-operator-stack.md
  - concepts/codex-side-fork-workflow.md
maturity: core
hub: true
created: 2026-05-13
updated: 2026-05-30
---

## Relations

- `@concepts/context-engineering.md` — Claude Code is where context-engineering happens day-to-day
- `@concepts/token-economics-and-prompt-caching.md` — the 5-min cache TTL governs how Cemini paces sessions and wake-ups
- `@concepts/subagent-orchestration.md` — Task/Agent tool delegates work to subagents
- `@concepts/hooks-for-automation.md` — `SessionStart`, `Stop`, `UserPromptSubmit` hooks live in `.claude/settings.json`
- `@entities/tools/claude-mem.md` — passive observation memory layered on top
- `@entities/tools/openspec.md` — spec-driven workflow consumed by Claude Code
- `@entities/tools/exa-mcp.md` — primary external-research MCP
- `@entities/tools/conductor-mcp.md` — cross-wiki query routing layer
- `@entities/tools/syncthing.md` — laptop sync for the wiki repos
- `@entities/mcp-servers/anthropic-skills.md` — official Anthropic skills marketplace surface
- `@entities/patterns/ralph-loop.md` — loop-based execution pattern
- `@entities/patterns/full-prompt-goal-template.md` — single-shot meta-prompt template
- `@entities/tools/lazy-tool.md`, `@entities/tools/claude-code-router.md`, `@entities/tools/ttok.md`, `@entities/tools/tech-debt-skill.md`, `@entities/tools/cua.md`, `@entities/tools/spec-kit.md`, `@entities/tools/claude-code-ultimate-guide.md` — surrounding tool stack
- `@entities/commands/plugin.md` — `/plugin marketplace add` + `/plugin install`
- `@entities/tools/superclaude-framework.md` — third-party Claude Code config/automation framework (slash commands + cognitive personas + KNOWLEDGE.md)
- `@concepts/claude-desktop-vs-claude-code.md` — surface distinction
- `@concepts/three-cache-architecture.md` — the cost mechanism behind every Cemini session
- `@concepts/mcp-context-optimization.md` — the four-layer optimization stack
- `@entities/tools/alumnium.md` — AI-native E2E testing wrapper that installs as a Claude Code MCP server
- `@entities/tools/polyterm-tui-pattern.md` — terminal-native UI-design reference for tools built alongside the CLI harness
- `@concepts/code-as-agent-harness.md` — three-layer harness model mapped to Claude Code + MCP
- `@concepts/self-healing-agent-sessions.md` — failure taxonomy and retry budget for long sessions
- `@entities/tools/open-design.md`, `@entities/tools/the-architect.md` — K57 Adopt candidates (steal-from / meta-agent blueprints)
- `@entities/tools/repomix.md`, `@entities/tools/n8n-mcp.md`, `@entities/tools/claude-code-tips.md` — K55-2 ridark high-priority candidates
- `@concepts/tools-we-dont-use.md` — institutional reject register
- `@concepts/local-llm-mechanics-primer.md` — local inference mechanics (K57 Post 1)
- `@entities/tools/ai-engineering-roadmap.md` — external curriculum gap-check (K60, reference-only)

## Raw Concept

Cemini's primary daily driver since K28. Used across all five sibling wikis (OSINT / Cybersecurity / 3D-printing / Image-gen / SEO) and the CeminiSuite dev stack. This page synthesizes what Cemini has settled on after ~6 months of continuous use, not what the docs say in the abstract.

## Narrative

Claude Code is Anthropic's official CLI harness — the same model API plus a tool sandbox (Bash, Read, Edit, Write, Grep, etc.), settings-driven hooks, MCP-server pluggability, and a slash-command/skill surface. It also ships as a desktop app (Mac/Windows), a web app (claude.ai/code), and IDE extensions (VS Code, JetBrains). Cemini runs the CLI in a macOS Apple-Silicon terminal.

The harness is built around **session-scoped context windows**. The model has a hard window (1M tokens on Opus 4.7 / Sonnet 4.6 long-context); the harness summarizes prior messages when nearing the limit. The economics of running a session are dominated by two factors: prompt-caching (5-minute TTL — see `@concepts/token-economics-and-prompt-caching.md`) and subagent delegation (offload heavy reads to a subagent and only ingest its summary — see `@concepts/subagent-orchestration.md`).

**Key surfaces Cemini uses every session:**

- **Slash commands** — `/goal` (auto-set goal-condition for self-checking session), `/loop` (recurring or self-paced loops), `/schedule` (cron routines), `/review`, `/security-review`, plus user-authored commands. See `@entities/commands/` (folder reserved for per-command pages).
- **Skills** (SKILL.md-compliant) — plain markdown + YAML frontmatter; triggered by description match. User skills in `~/.claude/skills/`, project skills in `.claude/skills/`, plus skills bundled by plugins like `claude-mem`.
- **Hooks** — `SessionStart`, `Stop`, `UserPromptSubmit`, `PreToolUse`, `PostToolUse`. Configured in `.claude/settings.json` (project) or `~/.claude/settings.json` (user). Misconfigured `Stop` hooks can loop the session indefinitely — see `@concepts/hooks-for-automation.md`.
- **MCP servers** — wired via `~/Library/Application Support/Claude/claude_desktop_config.json` (Desktop app) or per-project `.mcp.json`. Cemini-adopted: Exa, Brave, Playwright, claude-mem, stash-librarian, conductor.
- **Agents** — `Agent` tool spawns isolated subagent runs. Built-in types: `general-purpose`, `Explore`, `Plan`, `code-reviewer`, `statusline-setup`. Cemini-authored agents inherit the same tool surface unless restricted.
- **Modes** — `/fast` toggles fast-mode (Opus 4.7 with faster output, not a model downgrade). Plan-mode (`EnterPlanMode`) is read-only with `ExitPlanMode` to approve.

**Fast vs Opus pricing model**: at the time of writing Cemini runs on `claude-opus-4-7[1m]` for primary sessions, with Sonnet 4.6 for cheaper subagents and Haiku 4.5 for high-throughput orchestration jobs. Models change rapidly; verify against the current `--model` flag rather than relying on this page.

## Snippets

`.claude/settings.json` skeleton Cemini reuses across wikis:

```json
{
  "hooks": {
    "SessionStart": [{"matcher": "startup", "hooks": [{"type": "command", "command": "claude-mem hook session-start"}]}],
    "Stop": [{"matcher": "*", "hooks": [{"type": "command", "command": "claude-mem hook stop"}]}]
  },
  "permissions": {
    "allow": ["Bash(ls *)", "Bash(git status)", "Bash(python3 scripts/*.py)"],
    "deny": ["Bash(rm -rf *)", "Bash(git push --force *)"]
  }
}
```

### Surrounding tool stack (Cemini's adopted + documented)

| Tool | Role | Cemini posture |
|------|------|----------------|
| `@entities/tools/lazy-tool.md` | MCP-catalog lazy-loading proxy | CONDITIONAL-GO (≥5 MCP) |
| `@entities/tools/claude-code-router.md` | Multi-provider routing + caching headers | Documented, not adopted |
| `@entities/tools/ttok.md` | Token-counter CLI for cost preview | Adopted (cheap) |
| `@entities/tools/tech-debt-skill.md` | Whole-repo tech-debt audit skill | Adopted (`@entities/skills/tech-debt-audit.md`) |
| `@entities/tools/spec-kit.md` | GitHub spec-driven dev CLI | Documented, not adopted |
| `@entities/tools/cua.md` | M-series Mac VM sandbox | Documented, candidate for Tier-2 isolation |
| `@entities/tools/claude-code-ultimate-guide.md` | 24k-line CC reference + 28-CVE catalog + 655 malicious-skill patterns | Reference-only (CC-BY-SA caveat) |

### Two surfaces — Desktop vs Code

See `@concepts/claude-desktop-vs-claude-code.md` for the full distinction. Short version:
- **Claude Desktop** — graphical app; MCP only; config in `claude_desktop_config.json`
- **Claude Code** — CLI/IDE; MCP + Agent Skills + slash commands + hooks; config in `.claude/`
- Skills (SKILL.md) are Claude Code-only. Marketplaces are added via `/plugin marketplace add`; skills installed via `/plugin install`. See `@entities/commands/plugin.md`.

### Cost discipline (load-bearing)

The cost model lives in `@concepts/three-cache-architecture.md` (mechanism) + `@concepts/token-economics-and-prompt-caching.md` (the rules) + `@concepts/mcp-context-optimization.md` (the four-layer stack). Cemini's defaults: static-at-start prompts; 60-270s active polls; 1200-1800s idle waits; never 300s.

## Dead Ends

- **Long single-context sessions past ~400K tokens** — context degrades; switch to the Ralph loop pattern (`@entities/patterns/ralph-loop.md`) for multi-iteration work
- **Per-prompt MCP-server enumeration** — listing every MCP tool in the prompt envelope wastes tokens; let the harness discover via `ToolSearch` (deferred-tool pattern), and consider `@entities/tools/lazy-tool.md` if MCP-server count exceeds 5
- **Treating Claude Desktop and Claude Code as interchangeable** — see `@concepts/claude-desktop-vs-claude-code.md`
