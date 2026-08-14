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
maturity: draft
created: 2026-08-14
updated: 2026-08-14
wire_status: wont_wire
---

## Relations

- @entities/tools/claude-code.md — `claude-ds` (isolated Claude Code) is what `/route` actually runs; dsh does not replace it
- @entities/tools/agent-toolkit.md — `claude-ds.ps1` / `route-task` keep-wrapper host
- @entities/skills/route.md — policy: do not swap `/route` onto dsh (developer preview)
- @entities/tools/opencode.md — sibling Phase-0 (community, provider-agnostic)
- @entities/tools/reasonix.md — sibling Phase-0 (community, DeepSeek-native)
- @concepts/llm-routing-deepseek-openrouter-failover.md

## Raw Concept

What prompted this page: 2026-08-14 Phase-0 audit of the **official** DeepSeek Harness (`deepseek-ai/deepseek-harness`, npm `@deepseek-ai/dsh`), the first-party answer to the same question that prompted the OpenCode / Reasonix audits on 2026-08-12 — "is there a better DeepSeek coding harness than Claude Code pointed at `api.deepseek.com/anthropic`?" Verdict: **NO-GO for the `/route` executor swap; keep `claude-ds`.** This page also fixes the federation wording: agents kept saying the harness was "unreleased" — it is **released as a developer preview** (that is still not adoption-ready).

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

**Hard blockers for a complete laptop+prod `/route` swap:** prod Node 20; RC breaking-change warning; missing PromptFile / Flash-Pro CLI; always-approve is a different permission model (`DSH_PERMISSION_MODE` vs `--dangerously-skip-permissions`); the `/route` hang watchdog + spaced-WorkDir repair + SIP are wrapped around `claude-ds.ps1`, not `dsh`.

### Decision

| Target | Verdict |
|--------|---------|
| `.local/adopts/` REFERENCE clone | **NO-GO** — 80 MB+ RC churn; `/tmp/deepseek-harness-audit` already covers the audit |
| Runtime PATH (`dsh`) | **NO-GO** — do not install a second coding loop on PATH |
| Track A — optional later laptop scratch pilot (not `/route`) | **deferred** — separate binary name (never `claude-ds`), pinned npm tarball + integrity, scratch WorkDir, HITL |
| Track B — production `/route` replacement (laptop **and** prod) | **NO-GO today** — all cutover gates below; no laptop-only "we replaced /route" |

**Keep `/route` on isolated Claude Code 2.1.222 at `~/.deepseek-claude`** (`claude-ds` wrapper). This is the same class of decision as OpenCode / Reasonix (2026-08-12): MIT + headless is not enough for a production `/route` cutover.

### Track B cutover gates (do not execute; revisit only when all pass)

1. `@deepseek-ai/dsh` **non-rc** pin with recorded npm integrity (not only git HEAD — clone was rc.5 while npm was rc.6)
2. Prod Node meets `^22.19.0 || >=24` (Track B cannot skip prod)
3. Headless accepts SIP **PromptFile** as a file path (not `cat` into argv — ARG_MAX/quoting). WorkDir with spaces works
4. First-class Flash vs Pro selection equivalent to `claude-ds -Model`
5. Always-approve mapping proven: noninteractive `danger-full-access` does not hang; opt-out ask-mode still fails closed; hang watchdog still kills stalled runs
6. Adapter may reuse `Invoke-ClaudeDsExecute` internally only after gates 1–5; PATH name `claude-ds` stays until then. Smoke: `test-route-workdir-spaces.ps1` + one mid + one hard SkipGrok on **laptop and prod**
7. HITL GO after GPTSOL/Grok review of the adapter PR

**Wire posture:** `wire_status: wont_wire` for runtime PATH; `policy_wired` for the "keep `claude-ds` / do not second-loop" skill text (route SKILL.md v2.3.1). GPTSOL review (2026-08-14): AGREE keep-wrapper. Residual keep-wrapper risk (Anthropic-compat shim / pinned 2.1.222 aging) = **monitor, not a reason to adopt RC dsh.**

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

- **Full `/route` replacement with official dsh (2026-08-14)** — audited, NO-GO. Prod Node 20 + RC breaking-change warning + missing PromptFile / Flash-Pro CLI + different permission model + watchdog/SIP/WorkDir wrappers all tied to `claude-ds.ps1`. Revisit only via the Track B cutover gates above.
- **"DeepSeek Harness is unreleased" wording in federation pages** — wrong after 2026-08-13 release as developer preview; policy text corrected to developer-preview / keep-wrapper in route SKILL.md v2.3.1 (2026-08-14).
