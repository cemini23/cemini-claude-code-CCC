---
name: cursor-audit
description: >-
  Multi-model Cursor audit — dispatches three parallel readonly subagents on
  different models to debug code, configs, plans, or briefs and synthesize
  consensus vs unique findings. Use when the user says cursor audit,
  /cursor-audit, multi-model audit, council audit, second-opinion debug, or
  wants independent model reviews before fixing or shipping.
license: MIT
metadata.author: cemini23
metadata.version: "1.0.0"
disable-model-invocation: true
---

# Cursor audit (multi-model)

Independent opinions from **three different models** catch bugs, bad assumptions, and blind spots a single session misses. Pattern: codex + opus on the same bug surfaced different errors — repeat that deliberately.

**Tier 1 only** — subagents are `readonly: true`; they report, they do not edit.

## When to run

| Signal | Run? |
|--------|------|
| Stuck on a bug after 2+ fix attempts | Yes |
| GO/NO-GO on brief with engineering + cost claims | Yes |
| Pre-merge on risky diff (auth, money, prod config) | Yes |
| Trivial typo / one-line fix | No — direct edit |
| User says "quick audit" | Yes — use `quick-triage` mode |

## Workflow (parent agent)

Copy this checklist and track progress:

```
Cursor audit progress:
- [ ] 1. Scope — target, question, constraints, files/links
- [ ] 2. Mode — classify audit type; pick 3 models (see reference.md)
- [ ] 3. Audit pack — one self-contained brief (subagents see ONLY this)
- [ ] 4. Dispatch — 3× Task in ONE message, parallel, readonly
- [ ] 5. Synthesize — consensus / unique / conflicts / fix order
- [ ] 6. Act — implement only if user asks; re-audit after large fixes
```

### Step 1 — Scope

State explicitly:

- **Target** — file paths, error text, URL, or brief path
- **Question** — what must be answered ("why does X fail?", "is this brief shippable?")
- **Constraints** — no prod writes, time budget, models to exclude
- **Known ruled-out** — hypotheses already disproven (saves subagent time)

If scope is vague, ask one clarifying question before dispatch.

### Step 2 — Mode + model pick

Classify into one mode, then read [reference.md](reference.md) for the default triple.

| Mode | Use when |
|------|----------|
| `code-debug` | Stack traces, failing tests, runtime errors, logic bugs (**default**) |
| `security` | Auth, injection, secrets, trust boundaries |
| `config-infra` | YAML, MCP, hooks, CI, deploy scripts, env wiring |
| `brief-plan` | Adoption briefs, GO/NO-GO, cost/stat claims |
| `architecture` | Module boundaries, refactors, multi-file design |
| `quick-triage` | User asked for fast/cheap pass |

**Selection rules:**

1. Always **three models from three provider families** when possible (OpenAI / Anthropic / Google or xAI or Moonshot).
2. Never dispatch three variants of the same base model.
3. If the user names models, use those (still aim for diversity).
4. If a slug is unavailable, substitute from the same column in reference.md and note the swap.
5. Announce the chosen triple to the user before dispatch:

   > Cursor audit — mode: `code-debug` · models: codex, opus, gemini

### Step 3 — Audit pack (shared prompt body)

Every subagent gets the **same facts** plus the mode-specific lens. Subagents do **not** see parent chat — paste everything they need.

Required sections in each Task `prompt`:

```markdown
## Role
You are auditor {N}/3 in a multi-model cursor audit. Model: {model}. Be adversarial — try to disprove the current hypothesis.

## Target
{paths, error output, or brief excerpt}

## Question
{single sharp question}

## Constraints
{readonly, no edits, time budget}

## Already ruled out
{bullets or "none"}

## Required output format
Return ONLY this structure:

### Verdict
PASS | WARN | FAIL — one line why

### Findings
| Severity | Finding | Evidence (file:line or quote) | Fix |
|----------|---------|----------------------------------|-----|
| critical/warn/info | ... | ... | ... |

### Root cause (if debugging)
One paragraph — or "insufficient evidence" with what to inspect next

### Confidence
high | medium | low — and what would change your mind

### Unique angle
One thing you suspect other models might miss
```

Mode-specific extra lens (append one line to Role):

- `code-debug` — trace execution paths; check edge cases and error handling
- `security` — assume attacker model; hunt trust-boundary violations
- `config-infra` — validate wiring, defaults, and failure modes at startup
- `brief-plan` — pressure-test cost, timeline, and "Cemini already has this" displacement
- `architecture` — coupling, duplication, wrong abstraction level
- `quick-triage` — top 3 issues only; skip deep dives

### Step 4 — Dispatch

Use the **Task** tool three times in **one message**:

```text
subagent_type: generalPurpose
readonly: true
run_in_background: false
model: <slug from reference.md>
description: cursor-audit-{1|2|3}-{short-label}
prompt: <audit pack from step 3>
```

Do **not** serialize audits unless one audit depends on another (rare). Parallel is the point.

**File access:** subagents can Read/Grep the workspace. Include absolute paths in the audit pack when the target is known.

### Step 5 — Synthesize (parent delivers)

Merge the three reports using this template:

```markdown
# Cursor audit — {target summary}

**Mode:** {mode} · **Models:** {m1}, {m2}, {m3}

## Consensus (≥2 auditors agree)
- ...

## Unique (single auditor — still investigate)
- [{model}] ...

## Conflicts (deliberate disagreement — resolve before ship)
| Topic | {m1} | {m2} | {m3} | Resolution |
|-------|------|------|------|------------|
| ... | ... | ... | ... | ... |

## Recommended fix order
1. ...
2. ...

## Verdict rollup
| Model | Verdict |
|-------|---------|
| ... | PASS/WARN/FAIL |

**Overall:** SHIP | SHIP-WITH-FIXES | REWORK | REJECT — one paragraph
```

**Conflict rule (Glasswing):** if two auditors disagree on root cause or severity, do **not** silently pick one. Flag in Conflicts; propose a concrete test or file read to break the tie.

### Step 6 — Act

- Default: report only. User decides whether to fix.
- If user says "fix it": parent implements; offer **re-audit** after substantive changes.
- For OSINT briefs: cross-check with `@osint-wiki/scripts/skill_audit.py` static pass — cursor audit is complementary, not a replacement.

## Invocation phrases

User can trigger with any of:

- `/cursor-audit` or `cursor audit`
- `multi-model audit on …`
- `council audit`
- `get three model opinions on …`

Optional args in the same message:

- `mode: security`
- `models: codex, opus, gemini` (override)
- `quick` → `quick-triage`
- `files: path/a, path/b`

## Cost discipline

- Full audit ≈ 3× subagent cost. Use `quick-triage` when the user is time-sensitive.
- Do not re-run full audit on every tiny edit — only after meaningful changes or persistent failure.

## Related patterns

- `@entities/patterns/glasswing-deliberate-disagreement.md` — disagreement gating
- `@concepts/subagent-orchestration.md` — parallel Task dispatch
- `@entities/skills/cursor-audit.md` — CCC wiki canonical page
- `@osint-wiki/scripts/skill_audit.py` — static brief veto gates (OSINT workspace)

## Additional resources

- Model matrix + fallbacks: [reference.md](reference.md)
- Worked examples: [examples.md](examples.md)
