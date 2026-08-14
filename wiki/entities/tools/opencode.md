---
title: OpenCode — provider-agnostic terminal coding agent
type: entity
tags: [tool, coding-agent, harness, deepseek, mit, phase0]
keywords: [opencode, sst/opencode, anomalyco/opencode, opencode-ai, deepseek-v4-flash, claude-ds]
related:
  - entities/tools/claude-code.md
  - entities/tools/agent-toolkit.md
  - entities/skills/route.md
  - entities/tools/reasonix.md
  - entities/tools/deepseek-harness.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - "@osint-wiki/entities/tools/opencodex.md"
  - "@osint-wiki/entities/tools/opencode.md"
maturity: draft
created: 2026-08-12
updated: 2026-08-14
wire_status: wont_wire
---

## Relations

- @entities/tools/claude-code.md — current `/route` mid executor (`claude-ds` = this CLI + DeepSeek Anthropic-compat)
- @entities/tools/agent-toolkit.md — `claude-ds.ps1` / `route-task` host
- @entities/skills/route.md — do not swap mid-lane onto OpenCode
- @entities/tools/reasonix.md — sibling Phase-0 (DeepSeek-native CLI)
- @entities/tools/deepseek-harness.md — official DeepSeek Harness `dsh`; developer preview, NO-GO `/route` swap (2026-08-14)
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @osint-wiki/entities/tools/opencodex.md — **different tool** (`lidge-jun/opencodex` provider proxy)
- @osint-wiki/entities/tools/opencode.md — OSINT stub

## Raw Concept

What prompted this page: 2026-08-12 claude-ds harness refresh. Operator asked whether a better DeepSeek-API coding harness exists than Claude Code pointed at `api.deepseek.com/anthropic`. OpenCode (`sst/opencode` → canonical `anomalyco/opencode`) is the strongest general alternative DeepSeek documents (`awesome-deepseek-agent`).

## Narrative

**Name collision:** this is **OpenCode the coding agent**, not `@osint-wiki/entities/tools/opencodex.md` (K233 provider proxy).

### Phase-0 Audit (2026-08-12)

**Method:** GitHub API + LICENSE file + shallow clone `--depth 1 --filter=blob:none` → `/tmp/opencode-audit` (`cc4b456`, tag `v1.18.18`, branch `dev`). No bun/npm install. No PATH install.

| Check | Result |
|-------|--------|
| License | **MIT** — `gh api repos/sst/opencode/license` + clone `LICENSE` `[CONFIRMED]` (docs often say Apache-2.0; **wrong**) |
| Maturity | **196,635★**; last push **2026-08-13**; **5,128** open issues; daily `dev` releases |
| Clone size | **223 MB** blobless (GitHub size ~440 MB) |
| Headless | `opencode run --auto --dir "$WorkDir" --model deepseek/deepseek-v4-flash "$(cat "$PromptFile")"` — **no PromptFile flag**; `-p` is `--password`, not Claude `-p` |
| DeepSeek | OpenAI-compat `https://api.deepseek.com` (not Anthropic `/anthropic`). Models `deepseek/deepseek-v4-flash` + `deepseek/deepseek-v4-pro`. Prefer `DEEPSEEK_API_KEY` env; `/connect` writes `~/.local/share/opencode/auth.json` |
| Always-approve | `--auto` (aliases `--yolo`, `--dangerously-skip-permissions`). Without it, `external_directory` / `doom_loop` default **ask** and can hang headless |
| Failure mode | Not a drop-in for `claude-ds`. Protocol swap (OpenAI vs Anthropic-compat). No isolated home like `~/.deepseek-claude`. README first install is **`curl \| bash`**. Share URLs (`opncd.ai`) unless `"share": "disabled"`. Skills bleed from `~/.claude` unless `OPENCODE_DISABLE_CLAUDE_CODE=1`. High churn (`dev` + 5k issues) |

**Decision**

| Target | Verdict |
|--------|---------|
| REFERENCE clone `.local/adopts/opencode` | **CONDITIONAL-GO** — docs/CLI only; keep blobless; **do not** bun install; pin a release tag not `dev`. `/tmp/opencode-audit` already covers the audit; skip shelf unless needed |
| Runtime PATH | **NO-GO** — curl\|sh hard stop; overlaps Claude Code; no isolated install dir |
| `/route` mid-executor swap | **NO-GO** — keep `claude-ds`. Sidecar smoke later only if Anthropic-shim hangs persist after the 2.1.222 bump |

Keep mid-lane on updated `claude-ds` (Claude Code **2.1.222**, default `deepseek-v4-flash`, `-Model deepseek-v4-pro` for harder work).

## Snippets

> `opencode run --auto --dir <workdir> --model deepseek/deepseek-v4-flash` — closest headless analogue; prompt on argv or stdin. [Source: `/tmp/opencode-audit/packages/web/src/content/docs/cli.mdx` (retrieved 2026-08-12)]
