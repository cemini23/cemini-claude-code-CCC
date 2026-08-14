---
title: /route skill — easy mid hard money outsource
type: entity
tags: [skill, route, federation]
keywords: [route-task, always-approve, SIP, verify-gate, SHE, failover]
related:
  - entities/tools/agent-toolkit.md
  - concepts/llm-routing-deepseek-openrouter-failover.md
  - entities/skills/phase1-wire.md
  - entities/tools/opencode.md
  - entities/tools/reasonix.md
  - entities/tools/deepseek-harness.md
maturity: validated
created: 2026-07-01
updated: 2026-08-14
---

## Relations

- @entities/tools/agent-toolkit.md
- @concepts/llm-routing-deepseek-openrouter-failover.md
- @entities/tools/opencode.md — Phase-0 NO-GO mid swap
- @entities/tools/reasonix.md — Phase-0 NO-GO mid swap
- @entities/tools/deepseek-harness.md — Phase-0 2026-08-14; official `dsh` developer preview, NO-GO `/route` swap (cutover gates live there)

## Raw Concept

Federation skill `.cursor/skills/route/SKILL.md` (v2.3). Scripts live in private agent-toolkit.

## Narrative

Lanes: easy (OpenRouter free → claude-ds **Flash**), mid (Grok plan → Flash execute), hard/money (Cursor premium plan → Grok implement). **Grok CLI usage out:** Pro plans (mid) / Pro implements (hard + Plan). Always-approve default. One harness; `-Model` selects Flash vs Pro.

v2.1 adds SIP handoff contract (SDR exit 3), post-implement verify gate, mid→hard confidence escalate, `_route_runs/` claim-safe logs. Canon host `@entities/tools/agent-toolkit.md`.

v2.3 (2026-08-12): DeepSeek V4 Pro GA → **Grok CLI stand-in**. `Get-ClaudeDsModel` + `Invoke-ClaudeDsExecute -Model/-Mode`. Flash = easy/mid execute; Pro = mid plan when Grok usage is out, hard implement when Grok usage is out + Plan. Grok **auth** still `grok login`. Keep claude-ds adapter. Overrides: `ROUTE_CLAUDE_DS_FLASH_MODEL` / `ROUTE_CLAUDE_DS_PRO_MODEL`.

v2.3.1 (2026-08-14): policy clarification only — official DeepSeek Harness `dsh` **is** released (developer preview, RC), but remains **NO-GO for the `/route` executor swap**. Keep `claude-ds`; revisit only when Track B cutover gates on `@entities/tools/deepseek-harness.md` pass.

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
| ops 2026-08-12 | OpenCode / Reasonix as DeepSeek coding harness vs claude-ds | **closed** — keep claude-ds 2.1.222; both NO-GO PATH + mid swap (`@entities/tools/opencode.md`, `@entities/tools/reasonix.md`) |
| ops 2026-08-12 | Flash vs Pro in one harness; Pro = Grok CLI usage-out stand-in | **wired** — skill v2.3 + `route-task.ps1` |
| ops 2026-08-14 | Official DeepSeek Harness `dsh` Phase-0; keep-wrapper policy wording | **closed** — NO-GO `/route` swap; developer preview; skill v2.3.1 (`@entities/tools/deepseek-harness.md`) |

Briefs: `briefs/2026-08-11_route-skill-k231-k232-steals.md` · `briefs/2026-08-12_k234-charity-majors-harness-verify.md` · public product working brief: `~/Projects/cursor-route/docs/briefs/WORKING.md`.
