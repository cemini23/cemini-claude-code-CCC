---
title: cursor-audit (skill) — multi-model Cursor debug and review harness
type: entity
tags: [skill, cursor, multi-model, audit, subagent, glasswing, debugging, SKILL.md, cemini]
keywords: [cursor-audit, multi-model-audit, council-audit, second-opinion-debug, Task-tool, readonly-subagent, role-delegation, premium-models, deliberate-disagreement]
related:
  - entities/skills/super-audit.md
  - entities/skills/free-audit.md
  - entities/tools/claude-code.md
  - concepts/subagent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/tools/council-of-high-intelligence.md
  - entities/skills/tech-debt-audit.md
  - concepts/skill-vetting.md
  - concepts/agent-rubrics-self-correction.md
  - entities/skills/grill-with-docs.md
maturity: validated
created: 2026-06-05
updated: 2026-06-22
cross-wiki-source: "OSINT WORKSPACE .cursor/skills/cursor-audit/ (mirrored 2026-06-05); public distro agent-toolkit-demo/skills/cursor-audit/ (2026-06-06); v1.3.0 role delegation (2026-06-16)"
---

## Relations

- `@entities/skills/super-audit.md` — 5-model extension (3 Cursor + 2 API) for pre-ship prod reviews
- `@entities/skills/free-audit.md` — low-cost Grok-orchestrated council (0 Cursor Task)
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

What prompted this page: debugging session where **codex and opus on the same bug surfaced different errors** — evidence that single-model sessions miss blind spots. User requested a repeatable **cursor audit** skill: three parallel models, **delegated by audit mode and auditor role** (not a fixed triple), synthesized into consensus / unique / conflicts.

## Narrative

### What it does

The **cursor-audit** skill dispatches **three readonly subagents** on **three different model families** via Cursor's **Task** tool. Each auditor receives the same self-contained audit pack (subagents do not see parent chat). The parent synthesizes:

- **Consensus** — ≥2 auditors agree
- **Unique** — single-auditor findings worth investigating
- **Conflicts** — deliberate disagreement before ship (Glasswing gating)
- **Fix order** — prioritized remediation

Origin story [CONFIRMED]: OSINT workspace session 2026-06-05; codex + opus independent review caught errors the drafting model missed. Documented in OSINT `CLAUDE.md` / `ROADMAP.md` and `@osint-wiki/log.md` as the codex independent review pattern.

**v1.3.0 (2026-06-16):** Replaced hardcoded model triples with **role-based premium delegation** — classify mode → resolve three auditor roles → pick highest available premium slug per role from catalog.

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

Files: `SKILL.md`, `reference.md` (role delegation + premium catalog), `examples.md`, `README.md` (public distro only).

`disable-model-invocation: true` — loads only when user names `/cursor-audit`, `cursor audit`, `council audit`, or `multi-model audit`.

**Validate:** `vet skills/cursor-audit/SKILL.md --profile skillmd --strict` ([vet](https://github.com/cemini23/vet)).

### Premium tier + role delegation

Audits are **premium**: flagship reasoning/coding models only. Never default to `composer-2.5-fast`, flash/lite, or economy SKUs. `quick-triage` uses the same premium tier with **narrow scope** (top 3 issues), not cheaper models.

| Auditor role | Optimizes for |
|--------------|---------------|
| **agentic-reasoning** | Root cause, agentic traces, prod judgment |
| **code-implementation** | Patches, test failures, stack traces |
| **third-lens** | Cross-vendor blind spots (Google / xAI / Moonshot) |
| **adversarial** | Exploit paths, attacker model |
| **config-semantics** | YAML/MCP/hooks/deploy wiring |
| **strategic** | Brief GO/NO-GO, displacement, cost claims |

**Procedure:** classify mode → look up three roles in mode → role matrix → resolve each role to premium slug → announce `roles → slugs` before dispatch.

### Audit modes → roles

| Mode | Slot 1 | Slot 2 | Slot 3 | When |
|------|--------|--------|--------|------|
| `code-debug` | code-implementation | agentic-reasoning | third-lens | Stack traces, failing tests (**default**) |
| `security` | agentic-reasoning | adversarial | code-implementation | Auth, injection, secrets |
| `config-infra` | config-semantics | code-implementation | third-lens | MCP, hooks, YAML, CI |
| `brief-plan` | strategic | code-implementation | third-lens | GO/NO-GO briefs, cost claims |
| `architecture` | agentic-reasoning | third-lens | code-implementation | Refactors, module boundaries |
| `quick-triage` | agentic-reasoning | code-implementation | third-lens | Fast pass — premium models, shallow depth |

User override: `models: a, b, c` replaces slots 1–3. Full premium catalog + fallback chains: skill `reference.md`.

> **2026-06-13:** Fable 5 removed — Anthropic withdrew `claude-fable-5-thinking-high` from Cursor subagents.

### Invocation

- `/cursor-audit` or `cursor audit on …`
- `council audit`, `multi-model audit`, `second-opinion debug`
- Options: `mode: security`, `models: a, b, c` (explicit slug override), `quick`

### Cadence (when to run)

| Signal | Run? |
|--------|------|
| Stuck after 2+ fix attempts | Yes |
| Risky diff (auth, money, prod config) pre-merge | Yes |
| Brief with engineering-days + cost commitments | Yes (+ [vet](https://github.com/cemini23/vet) `--profile brief`; OSINT also has `scripts/skill_audit.py`) |
| One-line typo | No |

Cost ≈ **3× premium subagent** — use `quick-triage` when time-sensitive (narrow scope, not downgraded models).

### Relationship to other audit surfaces

| Surface | Scope |
|---------|-------|
| **cursor-audit** | Targeted debug/review; multi-model qualitative (3 auditors) |
| **super-audit** | Pre-ship council; 5 auditors (3 Cursor + 2 API); tailored packs |
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
metadata.version: "1.3.0"
disable-model-invocation: true
---
```
