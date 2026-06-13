---
title: super-audit (skill) — five-model pre-ship council with API leg
type: entity
tags: [skill, cursor, multi-model, audit, subagent, glasswing, openrouter, deepseek, prod-ship, SKILL.md, cemini]
keywords: [super-audit, five-model-audit, council-super-audit, cursor-audit, OpenRouter, DeepSeek, ADVISOR, pre-ship, readonly-subagent, deliberate-disagreement]
related:
  - entities/skills/cursor-audit.md
  - entities/tools/claude-code.md
  - concepts/subagent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/tools/council-of-high-intelligence.md
  - entities/skills/tech-debt-audit.md
  - concepts/skill-vetting.md
  - concepts/agent-rubrics-self-correction.md
  - "@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md"
maturity: validated
created: 2026-06-09
updated: 2026-06-13
cross-wiki-source: "OSINT WORKSPACE .cursor/skills/super-audit/ (2026-06-09); public distro agent-toolkit-demo/skills/super-audit/ (commit 40b97db)"
---

## Relations

- `@entities/skills/cursor-audit.md` — 3-model baseline; super-audit extends with 2 HTTP API auditors
- `@entities/tools/claude-code.md` — Cursor Task-tool native (not Claude Code `Agent` tool)
- `@concepts/subagent-orchestration.md` — parallel readonly fan-out + separate API leg
- `@entities/patterns/glasswing-deliberate-disagreement.md` — 5-model conflict table gates ship
- `@entities/patterns/tier1-tier2-agent-model.md` — Tier 1 readonly (Cursor + API report only)
- `@entities/tools/council-of-high-intelligence.md` — heavier external deliberation; super-audit is Cursor-native + cheap API slots
- `@entities/skills/tech-debt-audit.md` — whole-repo sweep; complementary
- `@concepts/skill-vetting.md` — internal harness; track via git + wiki, not Phase-0
- `@concepts/agent-rubrics-self-correction.md` — five-model synthesis before prod GO/NO-GO
- `@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md` — `OPENROUTER_*` / `DEEPSEEK_*` / `ADVISOR_*` key contract

Skill files mirrored in OSINT WORKSPACE and CCC at `.cursor/skills/super-audit/` (outside wiki tree).

## Raw Concept

What prompted this page: **cursor-audit** (3 models) proved valuable on poker bot debug and adoption briefs; pre-prod ship decisions (Tournament S1 poker, WC conviction bot) needed **more opinions without 5× Cursor subagent cost**. Pattern: keep 3 premium Cursor Task auditors + add 2 cheaper OpenAI-compatible API calls (Grok @ OpenRouter, DeepSeek reasoner) with per-run tailored prompt packs.

## Narrative

### What it does

The **super-audit** skill runs a **5-model council**:

| Slot | Channel | Default |
|------|---------|---------|
| 1–3 | Cursor Task (readonly) | **opus** · codex · gemini |
| 4–5 | HTTP API | grok-4.3 @ OpenRouter · deepseek-reasoner |

Each auditor receives the same **audit pack** on disk (`audit_prompt.md` + `PACK_INDEX.md`). Parent synthesizes:

- **Consensus** (≥3 auditors) and **strong consensus** (≥4)
- **Unique** single-auditor angles
- **Conflicts** — Glasswing gating before SHIP
- **Ranked patch backlog** — domain-specific (from tailored prompt)

**Proven runs [CONFIRMED]:** poker Tournament S1 super audit (2026-06-09, 5 models); WC bot prod posture reviews use same pattern with `ADVISOR_*` overrides.

### Install path

| Source | Path | Audience |
|--------|------|----------|
| [agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/super-audit) | `skills/super-audit/` | **Public** — canonical open-source distro; `vet-super-audit` CI |
| CCC (this repo) | `.cursor/skills/super-audit/` | Federation mirror |
| OSINT WORKSPACE | `.cursor/skills/super-audit/` | Private federation mirror |

```bash
# Public install (recommended)
git clone https://github.com/cemini23/agent-toolkit-demo.git
cp -r agent-toolkit-demo/skills/super-audit ~/.cursor/skills/

# Or from this repo
cp -r .cursor/skills/super-audit ~/.cursor/skills/
```

Files: `SKILL.md`, `reference.md`, `examples.md`, `prompt-template.md`, `auditors.default.json`, `scripts/` (`build_audit_pack.py`, `discover_api_keys.py`, `run_api_auditors.py`), `README.md`.

`disable-model-invocation: true` — loads when user names `/super-audit`, `super audit`, `5-model audit`, or `council super audit`.

**Validate:** `vet skills/super-audit/SKILL.md --profile skillmd --strict` ([vet](https://github.com/cemini23/vet)) — PASS 100/100 (2026-06-09).

### Tailoring (every run)

1. Copy `prompt-template.md` → domain prompt (mission, context tables, regime boundaries)
2. `build_audit_pack.py` — artifacts + `PACK_INDEX.md`
3. `discover_api_keys.py` — probe `~/.cemini/llm-routing.env`, `.env`, `ADVISOR_*`
4. Cursor leg — 3× parallel Task
5. `run_api_auditors.py` — optional custom `auditors.json` (e.g. WC: Gemini advisor + DeepSeek v4)

### Audit modes

Inherits cursor-audit modes for slots 1–3; adds **`prod-ship`** default for bot/config deploys. See skill `reference.md` for API slot overrides.

### Invocation

- `/super-audit` or `super audit on …`
- `5-model audit`, `council super audit`
- Options: `mode: prod-ship`, `quick` (3 Cursor + 1 API), `prompt: path`, `pack: path`

### Cadence (when to run)

| Signal | Run? |
|--------|------|
| Pre-prod deploy (bot, conviction.yaml, tournament) | Yes |
| GO/NO-GO with engineering + money on the line | Yes |
| cursor-audit insufficient / want API-backed extra opinions | Yes |
| Trivial one-line fix | No — cursor-audit or direct edit |

Cost ≈ **3× Cursor subagent + 2 API calls** — API leg is cheaper than a fourth Cursor subagent.

### Relationship to other audit surfaces

| Surface | Scope |
|---------|-------|
| **cursor-audit** | 3-model; fast targeted debug |
| **super-audit** | 5-model; pre-ship council + tailored packs + API leg |
| **tech-debt-audit** | Whole-repo TECH_DEBT_AUDIT.md |
| **vet** | Static brief veto; REJECT overrides multi-model SHIP |
| **council-of-high-intelligence** | External harness; heavier |

### Glasswing

Same primitive **#2** as cursor-audit: **Conflicts** table must be resolved before SHIP. Super-audit adds **strong consensus** threshold (≥4) for critical findings.

## Snippets

> Five independent opinions before high-stakes ship — 3 Cursor Task + 2 HTTP API (OpenRouter/DeepSeek).
> — [Source: agent-toolkit-demo/skills/super-audit/SKILL.md]

```yaml
---
name: super-audit
description: Five-model super audit — three Cursor readonly subagents plus two cheaper API auditors…
license: MIT
metadata.author: cemini23
metadata.version: "1.2.0"
disable-model-invocation: true
---
```
