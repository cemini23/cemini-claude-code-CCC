---
title: /route v2.4.3 — say "route as recommended" in any Cursor workspace
type: brief
tags: [brief, route, federation, cursor, deepseek-flash]
created: 2026-09-11
updated: 2026-09-11
---

## Target

Cursor Agent in **any** Cemini federation workspace (Atto, CCC, OSINT, TipDrop, wikis, CeminiSuite). Canon skill `.cursor/skills/route/SKILL.md` v2.4.3 + always-apply rule `~/.cursor/rules/cemini-route-outsource.mdc`. Runtime: private `cemini23/agent-toolkit`.

## Summary

Say **route as recommended**, `/route`, or `route this`. Cursor loads the always-apply rule in every project, classifies easy / mid / hard / money, and shells `route-task` from the **current** project. Do not implement in the parent Cursor session except Cursor Grok fallback. Cheap worker is DeepSeek **V4.1 Flash** (`deepseek-flash`). V4 Pro is **off rotation**. Grok-out hard = Flash then OpenCode.

This brief exists because the skill was already v2.4.3 while the always-apply rule still said "Flash then Pro". Cursor would have followed the stale rule in every workspace.

## Body

### What to type

| You say | Cursor should |
|---------|----------------|
| `route as recommended: <task>` | Classify + shell `route-task` in this project's WorkDir |
| `/route <task>` | Same |
| `route this: <task>` | Same |
| `route as recommended` (no body) | Ask what the task is |

WorkDir = the open project. TipDrop scanner only when the task is clearly scanner/TipDrop work.

### Lanes (must follow)

| Lane | Action |
|------|--------|
| **easy** | OpenRouter free → OpenCode Zen free → claude-ds Flash (`deepseek-flash`). Never Pro. |
| **mid** | Grok CLI plans → OpenCode then Flash execute. Grok usage out / no Plan → Flash plans (never Pro) then cheap execute. |
| **hard** | Cursor premium writes `## Plan` (SIP) → Grok CLI implements. Grok usage out + Plan → **Flash**, then **OpenCode**. Else Cursor Grok. |
| **money** | Same as hard + LIVE OK for live flips. |

### What Cursor must not do

- Implement in the parent Agent session (except fallback / hang takeover).
- Call DeepSeek V4 Pro. Wire id is `deepseek-flash`. Legacy `deepseek-v4-pro` aliases map to Flash.
- Send secrets to free OpenRouter or OpenCode Zen models.
- Rewrite `~/.config/opencode/opencode.json`.
- Treat Grok **auth** fail as usage-out. Print `grok login` (or set `XAI_API_KEY`).

### Always-approve (skill default)

| Executor | Default |
|----------|---------|
| Grok CLI | `--always-approve` |
| OpenCode | `opencode run --auto` |
| claude-ds / dsh | `DSH_PERMISSION_MODE=danger-full-access` |
| Cursor Grok fallback | Auto-run |

Opt out only when the operator asks (`-NoApprove` / `ROUTE_OPENCODE_ASK=1` / `CLAUDE_DS_ASK=1`).

### Why this brief (2026-09-11)

Federation audit after the V4.1 Flash runtime ship:

| Surface | Before | After |
|---------|--------|-------|
| Skill `.cursor/skills/route/SKILL.md` | v2.4.3 (correct) | unchanged |
| Always-apply `cemini-route-outsource.mdc` | Grok-out = Flash then **Pro** then OpenCode; "Pro is audits + hard backup" | Flash then OpenCode; Pro off rotation; trigger phrases in YAML |
| `~/.cursor/rules/` + workspace skills | rule stale; skills already hashed to canon | rule copied via `sync_federation_cursor_skills.sh` |

The always-apply rule is the Cursor-visible contract in **every** project (`alwaysApply: true`). A matching skill is not enough if the rule contradicts it.

### Operator one-liners

```bash
# from any project
route-task -Profile claudio "route as recommended: <task>"

# refresh shims once per machine
pwsh -File ~/Projects/agent-toolkit/scripts/adopt-route-always-approve.ps1

# re-sync federation skills + the always-apply rule
bash "/Users/claudiobarone/Projects/Cemini claude code CCC/scripts/sync_federation_cursor_skills.sh"
```

### Verify (what "correctly set up" means)

1. Skill YAML `metadata.version: "2.4.3"` and `federation: true` in the project `.cursor/skills/route/SKILL.md` **and** `~/.cursor/skills/route/SKILL.md`.
2. `~/.cursor/rules/cemini-route-outsource.mdc` has `alwaysApply: true`, trigger `route as recommended`, and **no** "Flash then Pro".
3. No project copy of `cemini-route-outsource.mdc` except CCC canon (double-load).
4. `route-task` on PATH; `claude-ds` shim → `dsh` with model `deepseek-flash`.

## Sources

- `@ccc-wiki/entities/skills/route.md`
- `@ccc-wiki/entities/tools/agent-toolkit.md`
- `@ccc-wiki/entities/tools/deepseek-harness.md`
- `@ccc-wiki/concepts/llm-routing-deepseek-openrouter-failover.md`
- `@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md`
- DeepSeek docs 2026-09-10: API id `deepseek-flash` is V4.1 Flash; V4.1 Flash beats V4 Pro; `deepseek-v4-pro` routes to Flash from 2026-09-14 04:00 UTC
- Runtime: `~/Projects/agent-toolkit` (`Get-RouteModel.ps1`, `claude-ds.ps1`, `route-task.ps1` `Invoke-HardBackupImplement`)
