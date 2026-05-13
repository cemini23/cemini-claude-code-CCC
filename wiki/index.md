# CCC Wiki — Index

Content-oriented catalog of every page in this wiki. Update on every new page or major refactor. Pages with `maturity: core` are battle-tested; `validated` is cross-checked; `draft` is bootstrap-quality.

## entities/tools/

| Page | Maturity | Summary |
|------|----------|---------|
| [`claude-code`](entities/tools/claude-code.md) | core | The CLI harness — modes, slash commands, skills, hooks, MCP, agents |
| [`claude-mem`](entities/tools/claude-mem.md) | validated | Passive observation memory; second layer beside `hot.md` |
| [`exa-mcp`](entities/tools/exa-mcp.md) | core | Claude-Code-side wiring of the Exa search MCP |
| [`conductor-mcp`](entities/tools/conductor-mcp.md) | validated | Cross-wiki query router (FastMCP) |
| [`openspec`](entities/tools/openspec.md) | draft | Spec-driven workflow alternative to Ralph and `/goal` |
| [`syncthing`](entities/tools/syncthing.md) | draft | Peer-to-peer file sync underneath Claude Code |

## entities/mcp-servers/

| Page | Maturity | Summary |
|------|----------|---------|
| [`anthropic-skills`](entities/mcp-servers/anthropic-skills.md) | draft | SKILL.md spec + Cemini's catalog-content stance |
| [`exa`](entities/mcp-servers/exa.md) | core | Exa neural search MCP server (paid API) |
| [`librarian-kb-server`](entities/mcp-servers/librarian-kb-server.md) | validated | Hetzner-hosted REST API serving the OSINT wiki |

## entities/patterns/

| Page | Maturity | Summary |
|------|----------|---------|
| [`ralph-loop`](entities/patterns/ralph-loop.md) | draft | File-based memory for autonomous loop iterations |
| [`full-prompt-goal-template`](entities/patterns/full-prompt-goal-template.md) | validated | `/goal` single-shot meta-template (5 sections + 10 ops rules) |

## concepts/

| Page | Maturity | Summary |
|------|----------|---------|
| [`context-engineering`](concepts/context-engineering.md) | validated | The four levers Cemini pulls to manage the model's window |
| [`token-economics-and-prompt-caching`](concepts/token-economics-and-prompt-caching.md) | validated | 5-min cache TTL governs pacing; never sleep 300 s |
| [`subagent-orchestration`](concepts/subagent-orchestration.md) | validated | When to dispatch via the `Agent` tool, when to inline |
| [`cross-wiki-routing`](concepts/cross-wiki-routing.md) | validated | Where new content belongs in the federation; brief vs stub |
| [`hooks-for-automation`](concepts/hooks-for-automation.md) | draft | `.claude/settings.json` hook events, scope, blast radius |

## entities/sources/skills/hooks/commands/people

Currently empty / placeholder. As Cemini ingests Claude Code release notes, conference talks, skill audits, and hook recipes, those subdirectories will populate. See `ROADMAP.md` for the deepening backlog.

## Cross-wiki links from this wiki

| From | To | Reason |
|------|----|--------|
| `entities/tools/openspec.md` | `@osint-wiki/entities/tools/openspec.md` | Audit + verdict canon lives in OSINT |
| `entities/tools/conductor-mcp.md` | `@osint-wiki/concepts/conductor-orchestrator.md` | Architecture history |
| `entities/patterns/ralph-loop.md` | `@osint-wiki/concepts/ralph-autonomous-agent-pattern.md` | Original audit + Steal-from verdict |
| `entities/patterns/full-prompt-goal-template.md` | `@osint-wiki/sources/autonomous-agent-meta-prompt-2026-05.md` | Original source page |
| `entities/mcp-servers/librarian-kb-server.md` | `@osint-wiki/concepts/librarian-server-architecture.md` | Architecture canon |
| `concepts/subagent-orchestration.md` | `@osint-wiki/concepts/conductor-orchestrator.md` | Parallel-fan-out history |
| `concepts/cross-wiki-routing.md` | `@osint-wiki/concepts/librarian-server-architecture.md` | Serving-layer design |
