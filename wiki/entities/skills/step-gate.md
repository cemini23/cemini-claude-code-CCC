---
title: step-gate (skill) — closed high-blast proceed/hold/escalate classifier
type: entity
tags: [skill, step-gate, guardrail, federation, k312]
keywords: [step-gate, proceed, hold, escalate, PreToolUse, high-blast, step guardrails]
related:
  - concepts/step-level-tool-guardrails.md
  - entities/skills/aid-guard-commit.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-28
wire_status: runtime_wired
wire_target: ".cursor/skills/step-gate/SKILL.md"
---

## Relations

- `@concepts/step-level-tool-guardrails.md`
- `@entities/skills/aid-guard-commit.md`

K312 leftover shipped 2026-08-28 as operator-invoked skill: closed classifier `(tool, args_summary)` → `proceed` | `hold` | `escalate`. **hold:** LIVE Discord, `scp` to cemini-prod, `watches.json` write, `.cursor/skills` mutation, `.env`/secrets, `git push --force`. **proceed:** wiki read, `wiki_lint`, `git status`, local lint. **escalate:** unknown high-blast / ambiguous. Helper `scripts/step_gate.py` (`selftest`). Federation skill: `federation: true`, `disable-model-invocation: true`. **Not** a Claude Code hook install — operator-invoked before high-blast (pairs K239).
