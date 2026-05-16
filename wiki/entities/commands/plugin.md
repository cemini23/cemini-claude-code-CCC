---
title: /plugin — install + manage Claude Code marketplace plugins
type: entity
tags: [command, slash-command, plugin, marketplace, claude-code, skills]
keywords: [/plugin, /plugin install, /plugin marketplace add, /plugin list, /plugin remove, plugin marketplace, agent skills]
related:
  - entities/tools/claude-code.md
  - entities/mcp-servers/anthropic-skills.md
  - entities/skills/claude-seo-agrici.md
  - entities/skills/marketingskills.md
  - entities/skills/geo-seo-claude.md
  - entities/skills/tech-debt-audit.md
  - concepts/claude-desktop-vs-claude-code.md
  - entities/tools/tech-debt-skill.md
  - entities/tools/claude-for-legal.md
  - entities/tools/skillkit.md
maturity: validated
created: 2026-05-13
updated: 2026-05-16
---

## Relations

- `@entities/tools/claude-code.md` — host harness; `/plugin` is a built-in slash command
- `@entities/mcp-servers/anthropic-skills.md` — the broader skills/marketplace canvas
- `@entities/skills/claude-seo-agrici.md`, `@entities/skills/marketingskills.md`, `@entities/skills/geo-seo-claude.md`, `@entities/skills/tech-debt-audit.md` — examples installed via this command
- `@concepts/claude-desktop-vs-claude-code.md` — `/plugin` is Claude Code-only
- `@entities/tools/claude-for-legal.md` — practice-area plugins install via the `/plugin` marketplace path
- `@entities/tools/skillkit.md` — alternative skill-acquisition path: runtime MCP fetch vs `/plugin` install-time registration

Cross-wiki: `@seo-wiki/concepts/claude-platforms.md` (operator-facing install instructions for the SEO tool stack).

## Raw Concept

Built-in Claude Code slash command for adding marketplaces, installing/removing plugins (skills), and listing what's installed. The most common Cemini-side use is registering a third-party SKILL.md repo and installing one or more skills from it.

## Narrative

`/plugin` isn't one command — it's a small family of subcommands:

| Subcommand | Effect |
|------------|--------|
| `/plugin marketplace add <owner>/<repo>` | Register a GitHub repo as a plugin marketplace |
| `/plugin marketplace list` | Show registered marketplaces |
| `/plugin marketplace remove <name>` | Unregister a marketplace |
| `/plugin install <name>` | Install a plugin (skill or skill bundle) from a registered marketplace |
| `/plugin list` | Show installed plugins |
| `/plugin remove <name>` | Uninstall a plugin |

Plugins land in `~/.claude/plugins/` (user-scoped) or the project's `.claude/plugins/` (project-scoped). Each plugin typically contains one or more SKILL.md files plus optional companion MCP servers.

### Cemini install pattern

```
# in Claude Code:
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install seo

/plugin marketplace add coreyhaines31/marketingskills
/plugin install marketing-skills

/plugin marketplace add zubair-trabzada/geo-seo-claude
/plugin install geo-seo

/plugin marketplace add ksimback/tech-debt-skill
/plugin install tech-debt-audit
```

After install, the skills surface as natural-language-triggered behaviors (the LLM matches user requests against the skill's `description:` field) AND as `/<skill-name>` slash commands when the SKILL.md declares them.

### Permissions interaction

Each new skill may require Bash patterns the project's `.claude/settings.json#permissions.allow` doesn't yet cover. Two policies:

1. **Per-prompt approval** — let the skill request permission live; cheap if rare.
2. **Pre-grant in settings** — add the skill's required Bash patterns to `permissions.allow` before installation; reduces friction.

Cemini defaults to per-prompt approval until a skill earns durability. After 3+ trigger sessions without surprises, pre-grant.

### Marketplace ≠ catalog content (per CCC LESSONS 2026-05-13)

`/plugin marketplace add` registers a repo as an *install source*. The CCC `LESSONS.md` (2026-05-13 entry) flags that catalog content has high churn — `package-security-check` was removed from `instructa/agent-skills` HEAD 12 days after Cemini's K42 eval. Mitigation:

- **Pin to known-good commits** — the marketplace add command resolves to HEAD by default, but you can pin via `--ref <sha>` if the version matters.
- **Don't ingest catalog content as wiki pages** — only ingest skills Cemini operationally depends on (see `@entities/skills/`).

### Where plugins live after install

```
~/.claude/plugins/<plugin-name>/
  SKILL.md          # the skill protocol (frontmatter + body)
  manifest.json     # optional: declares slash commands, MCP servers
  scripts/          # optional: helper scripts the skill calls
```

Editing files inside `~/.claude/plugins/` directly works (instant pickup on next session start) but breaks the marketplace upgrade path — the next `/plugin install --update` overwrites local edits. For lasting customization, fork the marketplace repo.

## Dead Ends

- **Treating `/plugin install` results as durable** — marketplaces churn. Pin commits or fork for anything load-bearing.
- **Editing files in `~/.claude/plugins/` then expecting upgrades to preserve the edit** — they don't. Fork instead.
- **Confusing `/plugin install <name>` with `pip install <name>`** — different ecosystems. Plugins are markdown skills, not Python packages.
