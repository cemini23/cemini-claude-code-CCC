---
name: step-gate
description: >-
  Classify a candidate step as proceed / hold / escalate before a high-blast
  action (StepGuard-style step gate, K312). Use when the operator says step-gate
  / gate this / is this safe / check before you run. Operator CLI, plus an
  optional Claude Code PreToolUse hook that denies only HOLD.
license: MIT
metadata.author: cemini23
metadata.version: "1.1.0"
disable-model-invocation: true
federation: true
---

# Step gate — proceed / hold / escalate (K312)

Canon: CCC `@concepts/step-level-tool-guardrails.md` (arXiv **2608.24777**, K312). Helpers: CCC `scripts/step_gate.py` (CLI) + `scripts/claude_pretooluse_step_gate.py` (Claude Code PreToolUse hook, deny-on-HOLD only). **HITL:** operator-invoked before high-blast steps; hook wired into `~/.claude/settings.local.json` via `scripts/install_pretooluse_step_gate.sh`; do not auto-evolve this skill.

## Procedure

1. State the candidate `(tool, args_summary)`.
2. Run `python3 scripts/step_gate.py check <tool> <args...>`.
3. Act on the verdict:

| Verdict | Meaning | Action |
|---------|---------|--------|
| `HOLD` | Closed high-blast list | Do **not** proceed without explicit operator OK (LIVE Discord, scp to cemini-prod, watches.json, `.cursor/skills` mutation, secrets, `git push --force`) |
| `PROCEED` | Low-blast allowlist | Safe routine action (wiki read, `wiki_lint`, `git status`, local lint) |
| `ESCALATE` | Unknown high-blast / ambiguous | Ask the operator before acting |

Pairs K239 preview-before-effect and `aid-guard-commit` (admission ≠ effect).

## Claude Code hook (optional, machine-local)

`scripts/install_pretooluse_step_gate.sh` wires `claude_pretooluse_step_gate.py` into `~/.claude/settings.local.json` (matcher `Bash|Write|Edit`, timeout 5s). The hook **denies only HOLD**; PROCEED and ESCALATE always allow (denying unknown tools would freeze the session). `STEP_GATE_HOOK=0` disables the gate.

## Selftest

`python3 scripts/step_gate.py selftest` — 12 closed cases must classify correctly (including watches.json HOLD; wiki `token` / `.ssh/config` mentions must not HOLD).
`python3 scripts/claude_pretooluse_step_gate.py selftest` — synthetic PreToolUse payloads (HOLD deny; PROCEED/ESCALATE allow; kill switch).

## NEVER

- Do not deny on ESCALATE — always allow (would freeze the Claude Code session).
- Do not add a `Stop` hook. Do not auto-proceed on HOLD. Do not silent-default an ESCALATE.
- No pipe-to-shell install patterns (`curl` piped to `bash`). No network calls. No secrets in args echoes.
- Do not rewrite `## Verify`. Do not rewrite `route-task.ps1`. Do not edit `~/.claude/settings.json` (use `settings.local.json` only).
