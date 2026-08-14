---
title: /route v2.3 — claude-ds Flash vs Pro (Grok CLI stand-in)
type: brief
created: 2026-08-12
updated: 2026-08-14
---

## Target

CCC operators + agent-toolkit. Not a prod scp.

## Summary

One isolated Claude Code harness (`claude-ds` / `~/.deepseek-claude`). DeepSeek V4 Pro GA (2026-08-12, API id `deepseek-v4-pro`) is the **Grok CLI stand-in when usage is out**. Flash stays the cheap execute worker. Do not swap to OpenCode/Reasonix. **2026-08-14:** official DeepSeek Harness `dsh` is now a developer-preview RC — still **NO-GO** as the `/route` worker; keep this adapter (`entities/tools/deepseek-harness.md`).

## Body

| Role | Model | Lane |
|------|-------|------|
| Easy fallback + mid execute | `deepseek-v4-flash` | easy / mid |
| Mid plan when Grok CLI usage is out | `deepseek-v4-pro` | mid SkipGrok / Credits-RateLimit-Network |
| Hard implement when Grok CLI usage is out | `deepseek-v4-pro` | hard SkipGrok+Plan |
| Hard plan | Cursor premium | quality gate — Pro does not replace this |

Grok **auth** (`grok login`) is not usage-out. Official Claude Code recipe (DeepSeek api-docs coding_agents): Pro as Opus/Sonnet, Flash as Haiku + `CLAUDE_CODE_SUBAGENT_MODEL`. Two models, **one** process.

Env overrides: `ROUTE_CLAUDE_DS_FLASH_MODEL` / `ROUTE_CLAUDE_DS_PRO_MODEL`.

## Sources

- agent-toolkit `scripts/route-task.ps1` v2.3
- `.cursor/skills/route/SKILL.md` v2.3.0
- https://api-docs.deepseek.com (coding_agents; retrieved 2026-08-12)
