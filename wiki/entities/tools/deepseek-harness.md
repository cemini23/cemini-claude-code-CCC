---
title: DeepSeek Harness (dsh) — official DeepSeek agent harness
type: entity
tags: [tool, coding-agent, harness, deepseek, mit, phase0]
keywords: [dsh, deepseek-harness, @deepseek-ai/dsh, cordis, headless, developer-preview, claude-ds, DSH_PERMISSION_MODE]
related:
  - entities/tools/claude-code.md
  - entities/tools/agent-toolkit.md
  - entities/skills/route.md
  - entities/tools/opencode.md
  - entities/tools/reasonix.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - "@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md"
  - sources/brief-k237-meta-harness-vero-misevolution-2026-08-14.md
maturity: draft
created: 2026-08-14
updated: 2026-08-15
wire_status: runtime_wired
---

## Relations

- @entities/tools/claude-code.md — isolated Claude Code at `~/.deepseek-claude` is **fallback** (`CLAUDE_DS_FORCE_LEGACY=1`)
- @entities/tools/agent-toolkit.md — `claude-ds.ps1` launches pinned `dsh`; `install-dsh.ps1` pin
- @entities/skills/route.md — v2.3.2: official dsh is the `/route` worker behind PATH name `claude-ds`
- @entities/tools/opencode.md — sibling Phase-0 (community, provider-agnostic)
- @entities/tools/reasonix.md — sibling Phase-0 (community, DeepSeek-native)
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md — OSINT copy of the routing concept; dsh-via-claude-ds worker

## Raw Concept

What prompted this page: 2026-08-14 Phase-0 audit of the **official** DeepSeek Harness (`deepseek-ai/deepseek-harness`, npm `@deepseek-ai/dsh`). Morning verdict was keep-wrapper; **operator GO the same day** to wire official `dsh` as the `/route` worker behind the existing `claude-ds` PATH name (yolo permissions, per-job `--patch` for Flash/Pro, Claude Code fallback). The harness is a **developer preview** (breaking changes expected) — we pin npm and keep the shim so DeepSeek updates land without rewriting `route-task`.

## Narrative

**First-party, unlike OpenCode / Reasonix.** DeepSeek AI's own agent harness. Architecture: **everything is a plugin**, powered by Cordis. npm package `@deepseek-ai/dsh`; CLI bin `dsh`.

### Phase-0 Audit (2026-08-14)

**Method:** GitHub API + LICENSE + clone → `/tmp/deepseek-harness-audit` (HEAD `47f9438` 2026-08-13, ~80 MB). No `npx @deepseek-ai/dsh`, no PATH install, no prod touch.

| Check | Result |
|-------|--------|
| License | **MIT** — `gh api repos/deepseek-ai/deepseek-harness` SPDX + clone `LICENSE` `[CONFIRMED]` |
| Maturity | **87,483★**; last push **2026-08-13**; 0 open issues. README: _developer preview_ — **THERE WILL BE COMPATIBILITY-BREAKING CHANGES** |
| Version skew | Repo `package.json` / `apps/cli/package.json` = **0.1.0-rc.5**; npm registry = **0.1.0-rc.6**. Same-week skew; pin must be npm tarball + integrity |
| Node engines | `^22.19.0 \|\| >=24.0.0` — laptop v24.13.0 OK; **prod v20.20.0 cannot run dsh** |
| Headless | `dsh --profile headless "job"` — positional task only; prints last assistant text; exit 0 if `completed` else 1. **No `-PromptFile`, no `-Model` argv on the shipped headless profile.** Workspace = invoking directory (no `-WorkDir` flag) |
| Permissions | Default preset `workspace-write` + **ask**. `DSH_PERMISSION_MODE=danger-full-access` is the yolo analogue (not `--dangerously-skip-permissions`). Under workspace-write, wider sandbox asks can block headless |
| Models | Headless boots the official DeepSeek route unless patched. Flash vs Pro is **not** `claude-ds -Model`. PTC/`DSH_TOOLS_MODE=code` exists but is not a route-task adapter |
| Surfaces | `apps/` = `cli` + `web` only — **no TUI shipped** as of 2026-08-14. Community README frames it as a framework for building harnesses, not a finished coding-agent drop-in |

**Morning Phase-0 blockers (still true as raw facts, now wrapped):** prod system Node is v20 (sidecar Node 24, do **not** replace trading-host Node); RC breaking-change warning (pin npm); no first-class `-PromptFile` / `-Model` on shipped headless (shim writes a prompt-file task + `--patch`); permission flag is `DSH_PERMISSION_MODE` not `--dangerously-skip-permissions`; hang watchdog / SIP / spaced-WorkDir stay on `claude-ds.ps1`.

### Decision (operator GO 2026-08-14 — same-day override)

| Target | Verdict |
|--------|---------|
| `.local/adopts/` REFERENCE clone | **NO-GO** — 80 MB+ RC churn; `/tmp/deepseek-harness-audit` covers the audit |
| Runtime PATH name `dsh` | **NO-GO** — do not steal PATH; pin lives in `~/.dsh-cemini` |
| `/route` worker behind `claude-ds` | **GO / runtime_wired** — `install-dsh.ps1` pin `@deepseek-ai/dsh@0.1.0-rc.6`; yolo `danger-full-access`; `-Model` → `--patch`; PromptFile by path; Claude Code fallback |
| Prod | **GO** with Node **24 sidecar** (`~/.local/node24`); system `node` stays v20.20.0 |

**Install:** `pwsh -File ~/Projects/agent-toolkit/scripts/install-dsh.ps1` then `adopt-route-always-approve.ps1`. Opt out to old wrapper: `CLAUDE_DS_FORCE_LEGACY=1`. Ask mode: `CLAUDE_DS_ASK=1`.

**Residual:** developer-preview RC (pin + retest on bump). `settings.yaml` sticky GUI default is overridden per job by `--patch`. Hang watchdog still wraps `claude-ds.ps1`, not raw `dsh`.

### Track B cutover gates (historical — morning list; adapter now implements 3–6 via shim)

1. Non-rc npm pin — still RC; we pin **0.1.0-rc.6** anyway (operator GO)
2. Prod Node — **sidecar**, not system upgrade
3. PromptFile as file path — shim task text points at the UTF-8 file
4. Flash vs Pro — `--patch` on `agent-default-model`
5. Always-approve — `DSH_PERMISSION_MODE=danger-full-access` (operator: do not stall on "dangerous")
6. PATH name `claude-ds` stays; `Invoke-ClaudeDsExecute` unchanged
7. HITL GO — **operator 2026-08-14** (this page)

**Wire posture:** `wire_status: runtime_wired`. Route SKILL.md **v2.3.2**. OpenCode / Reasonix remain NO-GO.

## Snippets

> DeepSeek Harness (`dsh`) is an open-source agent harness developed by DeepSeek AI. It uses an architecture where **everything is a plugin**, and is powered by Cordis… DeepSeek Harness is currently in _developer preview_ and is iterating rapidly. **THERE WILL BE COMPATIBILITY-BREAKING CHANGES.** [Source: `/tmp/deepseek-harness-audit/README.md` (retrieved 2026-08-14)]

> `dsh --profile headless "job"` — Run one fresh persisted session, print the final answer, and exit. … The invoking directory is the default workspace root. [Source: `/tmp/deepseek-harness-audit/apps/cli/README.md` (retrieved 2026-08-14)]

```jsonc
// apps/cli/package.json — repo pin lags npm
{ "name": "@deepseek-ai/dsh", "version": "0.1.0-rc.5", "bin": { "dsh": "lib/bin.js" }, "license": "MIT" }
// npm registry: 0.1.0-rc.6
```

> `workspace-write` permits writes under the workspace root…; `danger-full-access` bypasses confinement. [Source: `/tmp/deepseek-harness-audit/docs/subsystems/sandbox.md` (retrieved 2026-08-14)]

## Dead Ends

- **Morning keep-wrapper (2026-08-14)** — Phase-0 NO-GO `/route` swap. **Superseded same day** by operator GO: official dsh behind `claude-ds`, yolo permissions, Node sidecar on prod. Skill v2.3.1 keep-wrapper text replaced in v2.3.2.
- **"DeepSeek Harness is unreleased" wording** — wrong after 2026-08-13; corrected in v2.3.1, then v2.3.2 made it the worker.
