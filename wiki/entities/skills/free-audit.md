---
title: free-audit (skill) — Grok-orchestrated low-cost multi-model audit
type: entity
tags: [skill, cursor, multi-model, audit, grok, openrouter, deepseek, free, SKILL.md, cemini]
keywords: [free-audit, cheap-audit, low-cost-council, grok-orchestrate, openrouter-free, claude-ds, deepseek-v4-flash]
related:
  - entities/skills/cursor-audit.md
  - entities/skills/super-audit.md
  - concepts/subagent-orchestration.md
  - entities/patterns/glasswing-deliberate-disagreement.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/skill-vetting.md
  - "@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md"
maturity: draft
created: 2026-08-01
updated: 2026-08-01
---

## Relations

- `@entities/skills/cursor-audit.md` — 3× Cursor premium Task auditors (higher Cursor cost)
- `@entities/skills/super-audit.md` — 3× Cursor + paid/local API council
- `@concepts/subagent-orchestration.md` — fan-out pattern; free-audit fans out via Grok + HTTP, not Cursor Task
- Federation `/route` skill (`.cursor/skills/route/`) — same always-approve / outsource discipline
- `@entities/patterns/glasswing-deliberate-disagreement.md` — SYNTHESIS conflicts table
- `@entities/patterns/tier1-tier2-agent-model.md` — Tier 1 readonly
- `@concepts/skill-vetting.md` — internal harness skill; track via git + this page
- `@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md` — `OPENROUTER_*` / `DEEPSEEK_*` keys

Skill files: CCC `.cursor/skills/free-audit/` (`federation: true` → autosync).

## Raw Concept

Operator asked for a `/free-audit` that matches cursor-audit / super-audit structure but burns minimal Cursor usage: pack in Cursor → Grok CLI as auditor + orchestrator → claude-ds (DeepSeek V4 Flash) + ≥2 dynamic free OpenRouter models (excluding DeepSeek and Grok) → Glasswing synthesis on disk; Cursor only pastes the SYNTHESIS path.

## Narrative

### Layout

| Slot | Channel | Notes |
|------|---------|-------|
| 1 | Grok CLI | Auditor + orchestrator + synthesizer |
| 2 | DeepSeek API `deepseek-v4-flash` (claude-ds slot) | Headless chat; same model family as claude-ds |
| 3–4 | OpenRouter free (dynamic) | `select_free_or_models.py` — exclude deepseek/grok/x-ai; family diversity |

### Files

`SKILL.md`, `reference.md`, `examples.md`, `prompt-template.md`, `scripts/` (`build_audit_pack.py`, `select_free_or_models.py`, `prepare_free_audit.py`, `run_non_grok_legs.py`, `_env.py`).

`disable-model-invocation: true` — slash / explicit phrases only.

**Validate:** `vet .cursor/skills/free-audit/SKILL.md --profile skillmd --strict` when `vet` is available.

### Cost posture

Free-audit is for cheap multi-opinion triage. Escalate to cursor-audit / super-audit when free council splits on critical severity or money/prod ship is on the line.
