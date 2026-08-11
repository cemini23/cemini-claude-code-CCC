---
title: Cursor Route Orchestrator — viral public CLI (research + MVP plan)
type: brief
tags: [brief, ccc, product, viral, route, grok, deepseek, k230-adjacent]
created: 2026-08-10
---

## Target

CCC / public GitHub — new open-source product (funnel into Atto · GuruWatcher · Cemini)

## Summary

Ship a **Cursor-native** parallel agent orchestrator that steals the viral shape of `kingbootoshi/codex-orchestrator` and the provider discipline of `awslabs/cli-agent-orchestrator`, but swaps Codex workers for **Grok CLI + claude-ds (DeepSeek)** — with a clean swap slot for DeepSeek’s upcoming native coding harness. Pitch: save tokens/month, keep Cursor as the brain, run implementers you already pay for (X Premium → Grok CLI, DeepSeek → claude-ds).

## Research — competitors

### 1) kingbootoshi/codex-orchestrator (viral archetype)

| Signal | Value |
|--------|--------|
| License | MIT |
| Stars | ~340 (created 2026-01; companion Cartographer ~590★) |
| Stack | Bun CLI + tmux jobs + Claude Code **plugin/skill** |
| Pitch | Claude = strategist; Codex = parallel implementers in tmux |
| UX | `codex-agent start/send/capture/jobs`; live attach; mid-task redirect |
| Growth loop | Claude Code marketplace install → auto-activating skill → hero GIF → “stop coding alone” narrative |

**Why it spreads on X:** one screenshot (Claude spawning N Codex panes) + status-flex (“I shipped with 5 agents”) + ChatGPT/Codex cost drama + Claude Code plugin one-liner. Blog/plugin-hub amplification (“Stop Coding Alone…”) matches the meme, even when original tweets age out of search.

**Steal (patterns only — do not vendor):**
- Thin job CLI + tmux isolation + `send` / `capture` / `jobs --json`
- Orchestrator **skill** that makes the IDE agent default to delegation (not optional)
- Pipeline: Ideation → Research → Synthesis → PRD → Implement → Review → Test
- Optional codebase map injection (`--map`) for fewer exploratory tokens
- Hero visual + 30-second demo GIF as launch assets

### 2) awslabs/cli-agent-orchestrator (CAO) — enterprise reference

| Signal | Value |
|--------|--------|
| License | Apache-2.0 |
| Stars | ~1k · forks ~200 |
| Stack | Python `cao-server` + tmux + MCP handoff/assign/send_message + Web UI |
| Providers | Claude Code, Codex, Kiro, Cursor CLI (`agent`/`cursor-agent`), Copilot, OpenCode, … |
| Pitch | Supervisor–worker fleet; agents stay full CLIs with native auth |

**Steal:**
- Provider adapter interface (swap Grok / claude-ds / future DeepSeek harness without rewriting jobs)
- Explicit **handoff** (sync) vs **assign** (async parallel) vs **send_message**
- Status detectors for TUI CLIs (Cursor CLI docs are a goldmine for Ink/TUI scrape pitfalls)
- Optional Web UI later — **not** MVP

**Avoid for v0:** full CAO weight, Kiro-default bias, AWS-shaped docs. Viral products win on install-in-60s, not portfolio features.

### 3) Cemini private baseline (unfair advantage)

Private `cemini23/agent-toolkit` already has the money-saving brain:

- Lanes: easy (OpenRouter free → claude-ds) · mid (Grok plan → claude-ds) · hard/money (Cursor premium plan → Grok implement)
- Always-approve defaults, SIP handoffs, verify gates, secret deny, WorkDir hygiene

**Public product ≠ paste the private kit.** Extract a **clean, MIT (or Apache-2.0) open core** with the same UX contract; keep Cemini-specific profiles/prod paths private. Funnel README → youratto.com / guruwatcher.com / Cemini.

## Product concept — name LOCKED

**`cursor-route`** CLI + Cursor skill `route-orch` (“`/route` inside Cursor → Grok + DeepSeek army”).

### Fable planning pass (2026-08-10) — locked decisions

| # | Decision |
|---|----------|
| A | TypeScript CLI (Node 20+ / Bun-optional) + `skills/route-orch/` monorepo |
| B | npm primary later; git clone for v0; no pip primary |
| C | v0 supervisor = Cursor Agent skill-only; Cursor CLI = health probe later |
| D | Workers v0 = **grok + claude-ds only** (no OpenRouter) |
| E | Bootoshi-shaped tmux fire-and-forget (`start/send/capture/jobs`); `--no-tmux` for CI |
| F | Uniqueness: Cursor brain + lane-aware Grok/DeepSeek army (not Codex clone, not CAO fleet) |
| G | **MIT** |
| H | Week-1 MUST: health, start, jobs, capture, send, skill, cost table, SECURITY — later: Web UI, `--map`, brew, DeepSeek-native |
| I | Kill risk = broken first demo → `health` is install gate #1 |

Public repo: `~/Projects/cursor-route` → `cemini23/cursor-route` when published.

### One-liner (X)

> Cursor plans. Grok + DeepSeek build — in parallel tmux panes. Same workflow whether you live in Cursor, X (Grok CLI), or DeepSeek. Save tokens. Ship faster.

### Audience

1. Daily Cursor users (premium for plan / Composer)
2. X Premium users with **Grok CLI** already installed
3. DeepSeek users on **claude-ds** today → native DeepSeek harness when it ships
4. People burned by Claude-only or Codex-only bills

### Funnel

```
Star / install cursor-route
  → use free/cheap implementers
  → README “Also from Cemini”: Atto (genealogy) · GuruWatcher (alerts) · CCC skills
  → Discord / waitlist soft CTA (no hard sell in README body)
```

## Architecture (MVP)

```
┌─────────────────────────────┐
│  Cursor Agent / Cursor CLI  │  ← orchestrator (premium plan when hard)
│  skill: route-orch          │
└──────────────┬──────────────┘
               │ spawn jobs
               ▼
┌─────────────────────────────┐
│  cursor-route CLI (public)  │  jobs · send · capture · attach · health
│  tmux session per worker    │
└──────────────┬──────────────┘
               │ adapters
     ┌─────────┴─────────┐
     ▼                   ▼
┌──────────┐      ┌─────────────┐
│ Grok CLI │      │ claude-ds   │  ← DeepSeek via Claude Code harness
│ plan /   │      │ implement   │     (swap → deepseek-harness later)
│ implement│      └─────────────┘
└──────────┘
     optional: OpenRouter free for easy drafts
```

### Worker matrix (v0)

| Lane | Orchestrator | Worker(s) |
|------|--------------|-----------|
| easy | Cursor skill or CLI | OpenRouter free → claude-ds |
| mid | Cursor packs context | Grok `-PlanOnly` → claude-ds execute |
| hard | Cursor premium writes Plan | Grok `--always-approve` implement |
| parallel | Cursor skill fans out | N× Grok and/or claude-ds in tmux |

### DeepSeek transition (explicit)

- **Now:** `claude-ds` adapter (DeepSeek behind Claude Code harness) — document as “DeepSeek via claude-ds”.
- **Later:** `deepseek` adapter when native coding harness ships — same job CLI, one provider file swap.
- Do **not** market “Claude Code required forever.”

## Viral launch mechanics (copy the Bootoshi playbook)

1. **Hero:** one GIF — Cursor chat → 3 tmux panes (Grok / claude-ds / Grok) completing parallel tasks.
2. **Install path A:** Cursor rule/skill (federation sync) — “add skill → say route this”.
3. **Install path B:** `brew`/`npm`/`uv` one-liner for `cursor-route` CLI (no `curl|bash` as primary — AgentBaiting).
4. **Tweet thread:** (1) pain = Cursor alone serial + $$$ (2) demo GIF (3) install (4) “Grok CLI + DeepSeek = workers you already have” (5) star link.
5. **Social proof:** token cost table vs Claude-only / Codex-only for a fixed 3-file task.
6. **Companion later:** lightweight codebase map (steal Cartographer idea; don’t ship 589★ clone day one).

## Non-goals (v0)

- Not a fork of CAO or codex-orchestrator (license + brand clarity).
- Not exposing private `agent-toolkit` secrets, prod WorkDirs, or TipDrop.
- Not LIVE trading / Discord automations in demos.
- Not requiring AWS, Kiro, or Codex.

## Success criteria (MVP ship)

1. Public repo MIT or Apache-2.0 with LICENSE + SECURITY.md.
2. `cursor-route health` detects `grok`, `claude-ds`/`deepseek-claude`, `tmux`, optional `agent` (Cursor CLI).
3. `cursor-route start --worker grok|claude-ds "…"` returns job id; `jobs --json` / `capture` / `send` work.
4. Cursor skill: on “route this” / coding tasks, prefer spawn workers over doing all edits in Composer when lane ≥ mid.
5. README cost table + 60s install + funnel footer (Atto / GuruWatcher).
6. One demo GIF + sample `_route_runs`-style log committed as fixture (no secrets).

## Risks

| Risk | Mitigation |
|------|------------|
| Grok CLI ToS / rate limits | Document X Premium requirement; fallback claude-ds |
| claude-ds = Claude Code dependency | Honest README; DeepSeek-native adapter roadmap |
| CAO already supports Cursor CLI | Differentiate on **cheap workers + /route lanes**, not “also Cursor” |
| Supply-chain (`curl|bash`) | Prefer npm/uv/brew; pin versions |
| Cannibalize private kit | Public core subset; Cemini profiles stay private |

## Sources

- https://github.com/kingbootoshi/codex-orchestrator (MIT; README + plugin hub writeups, retrieved 2026-08-10)
- https://github.com/awslabs/cli-agent-orchestrator (Apache-2.0; README + `docs/cursor-cli.md`, retrieved 2026-08-10)
- https://github.com/kingbootoshi/cartographer (companion map pattern)
- https://prompts.brightcoding.dev/blog/stop-coding-alone-codex-orchestrator-spawns-parallel-ai-agents (amplification narrative)
- Cemini private `agent-toolkit` `/route` skill contract (not for public paste)
