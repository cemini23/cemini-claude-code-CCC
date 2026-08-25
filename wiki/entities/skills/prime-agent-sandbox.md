---
title: prime-agent-sandbox (skill) — REFERENCE trial, do not swap Cursor//route
type: entity
tags: [skill, prime-agent, rlm, federation, k309]
keywords: [Prime Agent, sandbox, K292 retention, 2608.23552]
related:
  - concepts/rlm-continual-harness.md
  - entities/tools/prime-agent.md
  - entities/skills/aid-guard-commit.md
  - entities/skills/intermediary-engineer.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
created: 2026-08-25
updated: 2026-08-25
wire_status: runtime_wired
wire_target: ".cursor/skills/prime-agent-sandbox/SKILL.md"
---

## Relations

- `@concepts/rlm-continual-harness.md`
- `@entities/tools/prime-agent.md`

Federation skill `.cursor/skills/prime-agent-sandbox/`. Script `scripts/prime_agent_sandbox_trial.sh` — inventory + K292 harness-hash retention. **Never** `curl|bash` install; **never** replace `/route`. Product remains `wont_wire`. HITL-authored 2026-08-25.
