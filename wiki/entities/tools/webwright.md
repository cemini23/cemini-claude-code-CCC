---
title: Webwright — Microsoft generative UI browser automation (Phase-0 pending)
type: entity
tags: [tool, browser, claude-plugin, adopt-candidate, k88]
keywords: [webwright, microsoft, browser-automation, generative-ui, claude-plugin]
related:
  - entities/tools/claude-code.md
  - concepts/cursor-ide-workspace.md
  - concepts/skill-vetting.md
  - sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md
  - "@osint-wiki/entities/tools/microsoft-webwright.md"
  - concepts/cross-wiki-tool-adoption-routing.md
  - concepts/agent-first-web-framework.md
  - sources/arxiv-agent-first-web-redesign-2606.19116.md
maturity: draft
created: 2026-05-31
updated: 2026-06-19
cross-wiki-source: "@osint-wiki/entities/tools/microsoft-webwright.md"
---

## Relations

- `@entities/tools/claude-code.md` — `.claude-plugin` host
- `@concepts/cursor-ide-workspace.md` — compare vs built-in browser + Playwright MCP
- `@concepts/skill-vetting.md` — Phase-0 before install
- `@sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md` — K88 v5 Adopt
- `@osint-wiki/entities/tools/microsoft-webwright.md` — OSINT stub (canon summary)

## Raw Concept

K88 v5 **Adopt** — `github.com/microsoft/Webwright`. MIT `[CONFIRMED 2026-05-31]`. Browser automation harness with Claude plugin manifest.

## Narrative

| Check | Status |
|-------|--------|
| License | MIT — GitHub API verified (K88) |
| vs Cursor browser | **CONDITIONAL-GO** — prefer built-in `browser_*` for Anthropic docs; Webwright for Claude Code plugin path |
| vs Playwright MCP | Global fallback only per CCC rules |
| Phase-0 | **DONE** 2026-06-04 — see `## Phase-0 Audit` |

**Verdict:** **CONDITIONAL-GO** — Claude Code plugin path only; Cursor sessions use built-in browser first.

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + README skim (`gh api repos/microsoft/Webwright/readme`). No install.

| Check | Result |
|-------|--------|
| License | **MIT** — API + root `LICENSE` [CONFIRMED] |
| Maturity | **5,020★**; last push **2026-06-03** — actively maintained |
| Stack | Python ≥3.10, Playwright chromium, httpx/pydantic/typer; ~1.5k LoC core |
| Plugin | `.claude-plugin` manifest; install via `/plugin install webwright@webwright` |
| Failure mode | **Egress + API keys** — OpenAI/Anthropic/OpenRouter backends; browser automation outside CCC sandbox defaults |

**Overlap:** Cursor built-in `browser_*` preferred for Anthropic docs per `@concepts/cursor-ide-workspace.md`; global Playwright MCP is fallback only. Webwright adds Claude Code/Codex/Hermes skill path and Task2UI HTML artifacts — not a Cursor default.

**Decision — CONDITIONAL-GO.** Safe to trial in isolated Claude Code profile with network allowlist review. **Do not** install on prod-boundary sessions until egress policy documented. **NO-GO** as replacement for Cursor built-in browser in this workspace.

## Adoption trial (2026-06-04)

| Step | Result |
|------|--------|
| `pip install` from `microsoft/Webwright` git clone | **PASS** — CLI `webwright doctor`: 4/6 (Python, Playwright, Chromium, screenshot) |
| API key | **FAIL** — `OPENAI_API_KEY` unset (Anthropic backend available via env instead) |
| Claude plugin | **FAIL** — `claude plugin install webwright@webwright` SSH clone error; marketplace registered |
| Project skill | **PASS** — copied `skills/webwright/` → `.claude/skills/webwright/`; `skill-scanner`: SAFE |

**Posture:** **ADOPTED (project skill + pip CLI)** — use in Claude Code sessions on this repo; Cursor continues built-in browser. Retry plugin install when GitHub HTTPS clone path works.

## Snippets

> Compare Webwright vs Cursor built-in browser before Adopt.
> — [Source: briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md]
