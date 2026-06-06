---
title: cursor-audit (skill) — multi-model Cursor debug and review harness
type: entity
tags: [skill, cursor, multi-model, audit, subagent, glasswing, debugging, SKILL.md, cemini]
keywords: [cursor-audit, multi-model-audit, council-audit, second-opinion-debug, Task-tool, readonly-subagent, codex-opus, deliberate-disagreement]
related:
  - entities/tools/claude-code.md
  - concepts/subagent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/tools/council-of-high-intelligence.md
  - entities/skills/tech-debt-audit.md
  - concepts/skill-vetting.md
  - concepts/agent-rubrics-self-correction.md
maturity: validated
created: 2026-06-05
updated: 2026-06-06
cross-wiki-source: "OSINT WORKSPACE .cursor/skills/cursor-audit/ (mirrored 2026-06-05); public distro agent-toolkit-demo/skills/cursor-audit/ (2026-06-06)"
---

## Relations

- `@entities/tools/claude-code.md` — sibling harness; cursor-audit is **Cursor Task-tool** native (not Claude Code `Agent` tool)
- `@concepts/subagent-orchestration.md` — parallel readonly fan-out discipline
- `@entities/patterns/glasswing-deliberate-disagreement.md` — conflict table gates ship decisions
- `@entities/patterns/tier1-tier2-agent-model.md` — cursor-audit is Tier 1 (readonly auditors)
- `@entities/tools/council-of-high-intelligence.md` — multi-model deliberation kinship; cursor-audit is the lightweight Cursor-native version
- `@entities/skills/tech-debt-audit.md` — whole-repo debt pass; complementary (breadth vs targeted multi-model debug)
- `@concepts/skill-vetting.md` — internal harness skill; not a third-party install candidate
- `@concepts/agent-rubrics-self-correction.md` — multi-model synthesis as rubric pass before ship

Skill files mirrored in OSINT WORKSPACE and CCC at `.cursor/skills/cursor-audit/` (outside wiki tree).

## Raw Concept

What prompted this page: debugging session where **codex and opus on the same bug surfaced different errors** — evidence that single-model sessions miss blind spots. User requested a repeatable **cursor audit** skill: three parallel models, auto-picked for the audit mode, synthesized into consensus / unique / conflicts.

## Narrative

### What it does

The **cursor-audit** skill dispatches **three readonly subagents** on **three different model families** via Cursor's **Task** tool. Each auditor receives the same self-contained audit pack (subagents do not see parent chat). The parent synthesizes:

- **Consensus** — ≥2 auditors agree
- **Unique** — single-auditor findings worth investigating
- **Conflicts** — deliberate disagreement before ship (Glasswing gating)
- **Fix order** — prioritized remediation

Origin story [CONFIRMED]: OSINT workspace session 2026-06-05; codex + opus independent review caught errors the drafting model missed. Documented in OSINT `CLAUDE.md` / `ROADMAP.md` and `@osint-wiki/log.md` as the codex independent review pattern.

### Install path

| Source | Path | Audience |
|--------|------|----------|
| [agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/cursor-audit) | `skills/cursor-audit/` | **Public** — canonical open-source distro; vet CI |
| CCC (this repo) | `.cursor/skills/cursor-audit/` | Federation mirror |
| OSINT WORKSPACE | `.cursor/skills/cursor-audit/` | Private federation mirror |

```bash
# Public install (recommended)
git clone https://github.com/cemini23/agent-toolkit-demo.git
cp -r agent-toolkit-demo/skills/cursor-audit ~/.cursor/skills/

# Or from this repo
cp -r .cursor/skills/cursor-audit ~/.cursor/skills/
```

Files: `SKILL.md`, `reference.md` (model matrix), `examples.md`, `README.md` (public distro only).

`disable-model-invocation: true` — loads only when user names `/cursor-audit`, `cursor audit`, `council audit`, or `multi-model audit`.

**Validate:** `vet skills/cursor-audit/SKILL.md --profile skillmd --strict` ([vet](https://github.com/cemini23/vet)).

### Audit modes

| Mode | Default model triple | When |
|------|---------------------|------|
| `code-debug` | codex · opus · gemini | Stack traces, failing tests (**default**) |
| `security` | opus · codex · grok | Auth, injection, secrets |
| `config-infra` | gemini · gpt-5.5 · sonnet-thinking | MCP, hooks, YAML, CI |
| `brief-plan` | opus · codex · kimi | GO/NO-GO briefs, cost claims |
| `architecture` | opus · gemini · gpt-5.5 | Refactors, module boundaries |
| `quick-triage` | composer · gpt-5.5 · sonnet-thinking | Fast/cheap pass |

Full slug table: skill `reference.md`.

### Invocation

- `/cursor-audit` or `cursor audit on …`
- `council audit`, `multi-model audit`, `second-opinion debug`
- Options: `mode: security`, `models: codex, opus, gemini`, `quick`

### Cadence (when to run)

| Signal | Run? |
|--------|------|
| Stuck after 2+ fix attempts | Yes |
| Risky diff (auth, money, prod config) pre-merge | Yes |
| Brief with engineering-days + cost commitments | Yes (+ [vet](https://github.com/cemini23/vet) `--profile brief`; OSINT also has `scripts/skill_audit.py`) |
| One-line typo | No |

Cost ≈ **3× subagent** — use `quick-triage` when time-sensitive.

### Relationship to other audit surfaces

| Surface | Scope |
|---------|-------|
| **cursor-audit** | Targeted debug/review; multi-model qualitative |
| **tech-debt-audit** | Whole-repo TECH_DEBT_AUDIT.md; single-model skill |
| **vet** / **skill_audit.py** (OSINT) | Static brief veto gates; not multi-model |
| **code-reviewer** subagent | Single second opinion; same model family unless Task `model` set |
| **council-of-high-intelligence** | External multi-model harness; heavier than cursor-audit |

### Glasswing upgrade

cursor-audit implements primitive **#2 deliberate disagreement** from `@entities/patterns/glasswing-deliberate-disagreement.md`: the synthesis **Conflicts** table must be resolved (test, file read, or user decision) before SHIP — no silent merge.

## Snippets

> "The codex review pattern worked well: independent agent reading both briefs catches statistical and cost-cap errors that the original drafter didn't surface."
> — [Source: @osint-wiki/log.md]

```yaml
---
name: cursor-audit
description: Multi-model Cursor audit — three parallel readonly subagents…
license: MIT
metadata.author: cemini23
metadata.version: "1.0.1"
disable-model-invocation: true
---
```
