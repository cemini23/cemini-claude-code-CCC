---
title: step-gate (skill) — closed high-blast proceed/hold/escalate classifier + PreToolUse hook
type: entity
tags: [skill, step-gate, guardrail, federation, k312, pretooluse]
keywords: [step-gate, proceed, hold, escalate, PreToolUse, high-blast, step guardrails]
related:
  - concepts/step-level-tool-guardrails.md
  - entities/skills/aid-guard-commit.md
  - concepts/hooks-for-automation.md
  - briefs/2026-08-28_ccc-k315-k324-sip-ready.md
  - briefs/2026-08-31_ccc-pretooluse-scout-bm25-sip-ready.md
maturity: draft
created: 2026-08-28
updated: 2026-08-31
wire_status: runtime_wired
wire_target: ".cursor/skills/step-gate/SKILL.md"
---

## Relations

- `@concepts/step-level-tool-guardrails.md`
- `@entities/skills/aid-guard-commit.md`
- `@concepts/hooks-for-automation.md`

K312 leftover shipped 2026-08-28 as operator-invoked skill; **real Claude Code PreToolUse hook shipped 2026-08-31**. Closed classifier `(tool, args_summary)` → `proceed` | `hold` | `escalate`. **hold:** LIVE Discord, `scp` to cemini-prod, `watches.json` write, `.cursor/skills` mutation, `.env`/secrets, `git push --force`. **proceed:** wiki read, `wiki_lint`, `git status`, local lint. **escalate:** unknown high-blast / ambiguous.

Helpers: `scripts/step_gate.py` (operator CLI, `selftest`) + `scripts/claude_pretooluse_step_gate.py` (PreToolUse hook, `selftest`) wired by `scripts/install_pretooluse_step_gate.sh` into `~/.claude/settings.local.json` (matcher `Bash|Write|Edit`, timeout 5s). The hook **denies only HOLD** (`permissionDecision: deny`, "Operator OK required"); PROCEED/ESCALATE always allow (deny-on-ESCALATE would freeze the session); `STEP_GATE_HOOK=0` kill switch. Federation skill: `federation: true`, `disable-model-invocation: true`. Operator-invoked before high-blast (pairs K239); no Stop hook.
