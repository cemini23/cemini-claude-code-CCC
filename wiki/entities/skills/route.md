---
title: /route skill — easy mid hard money outsource
type: entity
tags: [skill, route, federation]
keywords: [route-task, always-approve, SIP, verify-gate, SHE, failover]
related:
  - entities/tools/agent-toolkit.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - entities/skills/phase1-wire.md
maturity: validated
created: 2026-07-01
updated: 2026-08-12
---

## Relations

- @entities/tools/agent-toolkit.md
- @concepts/llm-routing-deepseek-openrouter-failover.md

## Raw Concept

Federation skill `.cursor/skills/route/SKILL.md` (v2.2). Scripts live in private agent-toolkit.

## Narrative

Lanes: easy (OpenRouter free → claude-ds), mid (Grok plan → claude-ds), hard/money (Cursor premium plan → Grok implement). Always-approve default.

v2.1 adds SIP handoff contract (SDR exit 3), post-implement verify gate, mid→hard confidence escalate, `_route_runs/` claim-safe logs. Canon host `@entities/tools/agent-toolkit.md`.

v2.2: **Grok-out** (`-SkipGrokPlan` / `ROUTE_GROK_OUT=1`) + usable `## Plan` skips Grok → claude-ds on mid/hard; **claude-ds hang watchdog** (stall/max env) prints parent Cursor takeover; `-HandoffPath` resume. Helpers: `scripts/lib/Test-RoutePlanPresent.ps1`.

### Research → skill improvement backlog (standing)

OSINT daily digest steals for this skill via cluster `cursor-route-harness` (`daily_research_config.yaml`). On match → CCC brief + bump this backlog (HITL before skill/toolkit PR).

| ID | Steal | Status |
|----|-------|--------|
| K232 ops | Grok-out + filled `## Plan` → skip Grok plan, claude-ds execute | **wired** 2026-08-11 — agent-toolkit + skill v2.2 |
| K232 ops | claude-ds hang watchdog → parent Cursor takeover + verify | **wired** 2026-08-11 — `Invoke-PwshScriptNamedArgs -EnableHangWatch` |
| K232 SHE | Trajectory→System Prompt / Rule Bank / Safety Memory / Tool Policy; evolve from `_route_runs/` **HITL only** | open — pattern; `.local/adopts/SHE` REFERENCE (OSINT) |
| K231 smart-ralph | Force research→design→tasks in SIP Plan before mid/hard execute | open — SIP checklist |
| K232 DiffCoop / verify papers | Pressure-test failover paths; accept/reformulate/escalate on verify fail | open — eval habit |
| K233 | SKILLER skill-authoring / SkillLens / MISA-T / opencodex candidate | open — pattern + `/phase1` only for opencodex |
| K234 | Charity Majors: harness > model; verification bottleneck; pets→cattle code | open — reinforce Verify gate; brief `2026-08-12_k234-charity-majors-harness-verify.md` |

Briefs: `briefs/2026-08-11_route-skill-k231-k232-steals.md` · `briefs/2026-08-12_k234-charity-majors-harness-verify.md`.
