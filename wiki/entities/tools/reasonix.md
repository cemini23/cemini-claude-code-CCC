---
title: Reasonix — community DeepSeek-native coding agent
type: entity
tags: [tool, coding-agent, harness, deepseek, mit, phase0]
keywords: [reasonix, DeepSeek-Reasonix, esengine, deepseek-v4-flash, prefix-cache, claude-ds]
related:
  - entities/tools/claude-code.md
  - entities/tools/agent-toolkit.md
  - entities/skills/route.md
  - entities/tools/opencode.md
  - entities/tools/deepseek-harness.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - "@osint-wiki/entities/tools/reasonix.md"
  - "@osint-wiki/entities/infrastructure/deepseek-api.md"
maturity: draft
created: 2026-08-12
updated: 2026-08-14
wire_status: wont_wire
---

## Relations

- @entities/tools/claude-code.md — current `/route` mid (`claude-ds`)
- @entities/tools/agent-toolkit.md
- @entities/skills/route.md — do not swap mid-lane onto Reasonix
- @entities/tools/opencode.md — sibling Phase-0 (provider-agnostic)
- @entities/tools/deepseek-harness.md — official `dsh` `/route` worker behind `claude-ds` (v2.3.2); Reasonix stays NO-GO
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @osint-wiki/entities/tools/reasonix.md — OSINT stub
- @osint-wiki/entities/infrastructure/deepseek-api.md

## Raw Concept

What prompted this page: 2026-08-12 claude-ds harness refresh. Reasonix (`esengine/DeepSeek-Reasonix`) is the strongest **DeepSeek-native** coding CLI (listed on `deepseek-ai/awesome-deepseek-agent`). It talks to `api.deepseek.com` directly (OpenAI / Responses), not via Anthropic translation.

## Narrative

**Not first-party DeepSeek.** Community project (GitHub user `esengine`). `awesome-deepseek-agent` listing ≠ official product. Homebrew tap email `reasonix@deepseek.com` is branding, not affiliation.

### Phase-0 Audit (2026-08-12)

**Method:** GitHub API + LICENSE + shallow clone `--depth 1` → `/tmp/reasonix-audit` (`730454e`, CLI `v1.25.0`). No `npm i -g reasonix`. No PATH install.

| Check | Result |
|-------|--------|
| License | **MIT** — GitHub license API + clone `LICENSE` `[CONFIRMED]` |
| Maturity | **34,217★**; last push **2026-08-13**; ~1,021 open issues + 350 PRs; daily 1.x releases |
| Clone size | **63 MB** shallow |
| Headless | `reasonix run --yolo --dir "$WorkDir" --model deepseek/deepseek-v4-flash -p < "$PromptFile"` — **no `run --prompt-file`**. Default headless Ask **fails closed** on writes |
| DeepSeek | Native `kind=openai` `https://api.deepseek.com`; default **Flash**; Pro via `--model deepseek-v4-pro`. Anthropic-compat preset exists but is **hidden** from new-provider lists. Keys via `DEEPSEEK_API_KEY` / `~/.reasonix/.env` (`api_key_env`), not TOML |
| Always-approve | `--yolo` ≡ `--dangerously-skip-permissions`. Weaker `--auto`/`-y`. YOLO still honors deny/sandbox/plan-confirm |
| Failure mode | Not a drop-in for `claude-ds`. Cache-first “leave it running” thesis **does not help** one-shot `/route` SIP jobs. `npm i -g reasonix` pulls **unhashed prebuilt binaries**. In-app `reasonix upgrade`. Bot/serve/MCP product surface. Stale awesome-list docs (`npx reasonix code`, JSON config) vs current Go `config.toml` |

**Decision**

| Target | Verdict |
|--------|---------|
| REFERENCE clone | **CONDITIONAL-GO** — research shelf for native-DeepSeek / prefix-cache; sparse (drop `desktop/`, `site/`). `/tmp/reasonix-audit` already covers the audit |
| Runtime PATH | **NO-GO** — prebuilt npm/Homebrew binary, updater, telemetry/bot surfaces, overlap with isolated `claude-ds` |
| `/route` mid-executor swap | **NO-GO** — keep `claude-ds`. Sidecar (`REASONIX_HOME` isolated, telemetry off, `--yolo`, stdin handoff) only if Anthropic-shim hangs persist after the 2.1.222 bump |

Differentiator vs updated `claude-ds`: native OpenAI/Responses (no Anthropic translation) + prefix-cache for **long** sessions. That is not the `/route` mid job shape.

## Snippets

> Default non-interactive Ask fails closed. `--yolo` is the closest always-approve analogue. [Source: `/tmp/reasonix-audit/docs/TOOL_APPROVAL_MODES.md` (retrieved 2026-08-12)]
