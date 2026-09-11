---
title: agent-toolkit — private /route script host
type: entity
tags: [tool, route, federation, k228-followon]
keywords: [agent-toolkit, route-task, ROUTE_KIT, SIP]
related:
  - entities/skills/route.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - entities/tools/opencode.md
  - entities/tools/reasonix.md
  - entities/tools/deepseek-harness.md
maturity: validated
created: 2026-08-08
updated: 2026-09-11
---

## Relations

- @entities/skills/route.md
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @entities/tools/opencode.md — Phase-0 2026-08-12; NO-GO `/route` swap
- @entities/tools/reasonix.md — Phase-0 2026-08-12; NO-GO `/route` swap
- @entities/tools/deepseek-harness.md — official `dsh` `/route` worker behind `claude-ds` (v2.3.2; pin `install-dsh.ps1`)

## Raw Concept

Private canon host for Cemini `/route` after TipDrop kit retirement (2026-08-08).

## Narrative

- **Repo:** https://github.com/cemini23/agent-toolkit (private)
- **Laptop:** `~/Projects/agent-toolkit`
- **Prod:** `/opt/cemini/agent-toolkit` (`ROUTE_KIT`)
- **Egress:** `/opt/cemini/agent-toolkit` (rsync; no pwsh — bash shims only)
- **Not** public `agent-toolkit-demo` (vet/phase0/wikilint CI)

Scripts: `route-task`, `handoff-to-grok`, `claude-ds`, SIP/verify/escalate libs. Adopt: `pwsh -File scripts/adopt-route-always-approve.ps1`. TipDrop kit keeps redirect stubs only.

**claude-ds (2026-09-11):** PATH name `claude-ds` → official `dsh` (`~/.dsh-cemini`) with `--patch` overlay `{provider: deepseek-official, model: deepseek-flash}`. Isolated Claude Code at `~/.deepseek-claude` is **fallback** (`CLAUDE_DS_FORCE_LEGACY=1`). Wire id **`deepseek-flash`** (DeepSeek V4.1 Flash, native vision). Legacy `deepseek-v4-flash` / `deepseek-v4-pro` aliases map here. V4 Pro is **off rotation**. Subagents: `CLAUDE_CODE_SUBAGENT_MODEL=deepseek-flash`. OpenCode is a Zen-free **sidecar**, not a PATH swap. Reasonix remains NO-GO. Historical 2026-08-14: isolated Claude Code 2.1.222 was the worker; superseded same day by dsh (`@entities/tools/deepseek-harness.md`).
