# Cursor audit — model matrix

Use these defaults unless the user overrides. Slugs must match Cursor Task `model` parameter exactly.

## Anthropic slot — Opus default

| Use case | Preferred | Fallback (same family) |
|----------|-----------|------------------------|
| Agentic code, bugs, architecture, prod-ship, security (code paths) | `claude-opus-4-8-thinking-high` | `claude-4.6-sonnet-medium-thinking` |
| Adoption briefs, strategic GO/NO-GO, narrative displacement | `claude-opus-4-8-thinking-high` | `claude-4.6-sonnet-medium-thinking` |

User override `models: opus` or `models: sonnet` swaps only the Anthropic leg; keep three provider families.

> **2026-06-13:** `claude-fable-5-thinking-high` removed — Anthropic withdrew Fable 5 from Cursor subagents. Opus is the Anthropic default for all modes.

## Default triples by mode

| Mode | Model 1 | Model 2 | Model 3 | Why this spread |
|------|---------|---------|---------|-----------------|
| **code-debug** | `gpt-5.3-codex` | `claude-opus-4-8-thinking-high` | `gemini-3.1-pro` | Codex: implementation + test failures; Opus: agentic trace + logic; Gemini: third family |
| **security** | `claude-opus-4-8-thinking-high` | `gpt-5.3-codex` | `grok-4.3` | Agentic reasoning + exploit paths + non-OpenAI/Anthropic lens |
| **config-infra** | `gemini-3.1-pro` | `gpt-5.5-medium` | `claude-4.6-sonnet-medium-thinking` | Config semantics + practical fixes + structured thinking |
| **brief-plan** | `claude-opus-4-8-thinking-high` | `gpt-5.3-codex` | `kimi-k2.5` | Strategic holes + technical feasibility + third vendor |
| **architecture** | `claude-opus-4-8-thinking-high` | `gemini-3.1-pro` | `gpt-5.5-medium` | Agentic design depth + alt structure + engineering pragmatism |
| **quick-triage** | `composer-2.5-fast` | `gpt-5.5-medium` | `claude-4.6-sonnet-medium-thinking` | Lower latency; still three families |

## Available slugs (Cursor subagents)

If a slug fails at dispatch, substitute within the same **family column**:

| Family | Slugs |
|--------|-------|
| OpenAI | `gpt-5.3-codex`, `gpt-5.5-medium` |
| Anthropic | `claude-opus-4-8-thinking-high`, `claude-4.6-sonnet-medium-thinking` |
| Google | `gemini-3.1-pro` |
| xAI | `grok-4.3`, `grok-build-0.1` |
| Moonshot | `kimi-k2.5` |
| Cursor | `composer-2.5-fast` |

**Fallback order when a slug is unavailable:** same-mode row → next row with closest intent → never duplicate family in the triple.

## Mode classification heuristics

| User language | Mode |
|---------------|------|
| test fail, exception, traceback, bug, doesn't work | `code-debug` |
| XSS, SQLi, auth bypass, secret leak, CVE | `security` |
| mcp.json, hook, yaml, workflow, tunnel, deploy | `config-infra` |
| brief, adopt, GO/NO-GO, phase 0, rollout | `brief-plan` |
| refactor, design, module split, API shape | `architecture` |
| quick, fast, triage, skim | `quick-triage` |

## Audit pack checklist

Before dispatch, verify the pack includes:

- [ ] Absolute file paths or pasted error output
- [ ] Single primary question
- [ ] Ruled-out hypotheses (even if empty)
- [ ] Required output format block
- [ ] Readonly constraint stated

## Synthesis severity rollup

Map subagent severities to parent action:

| Pattern | Overall verdict |
|---------|-----------------|
| Any **critical** with consensus | FAIL → REJECT or REWORK |
| **critical** from one auditor only | WARN → investigate before ship |
| All PASS | SHIP (still note unique warns) |
| Split root cause | REWORK until conflict resolved |

## Integration with static brief audit

For files under `briefs/`:

1. Run cursor audit (multi-model, qualitative)
2. Run `python3 scripts/skill_audit.py briefs/<file>.md` or `vet briefs/<file>.md --profile brief` (mechanical veto gates)

Static REJECT overrides multi-model SHIP.
