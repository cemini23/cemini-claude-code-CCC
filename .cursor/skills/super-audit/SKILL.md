---
name: super-audit
description: >-
  Five-model super audit — three Cursor readonly subagents plus two cheaper
  OpenAI-compatible API auditors (OpenRouter, DeepSeek, ADVISOR_*). Tailor a
  domain prompt and audit pack before each run; synthesize consensus, unique
  findings, and conflicts. Use when the user says super audit, /super-audit,
  5-model audit, council super audit, pre-ship multi-opinion review, or wants
  cursor-audit depth with extra API-backed opinions before prod GO/NO-GO.
license: MIT
metadata.author: cemini23
metadata.version: "1.2.0"
disable-model-invocation: true
---

# Super audit (5-model)

**cursor-audit + 2 API legs.** Five independent opinions before high-stakes ship (prod bots, conviction configs, tournament deploys, adoption briefs). Pattern proven on poker Tournament S1 and WC bot prod reviews.

**Tier 1 only** — all auditors are readonly; they report, they do not edit.

## When to run

| Signal | Run? |
|--------|------|
| GO/NO-GO with engineering + money on the line | Yes |
| cursor-audit ran but user wants more coverage / cheaper extra opinions | Yes |
| Pre-prod deploy (bot, config matrix, conviction.yaml) | Yes |
| Trivial fix or single-file typo | No — use cursor-audit or direct edit |
| User says "quick" | Yes — use `quick` tailoring (3 cursor + 1 API only) |

## vs cursor-audit

| | cursor-audit | super-audit |
|---|-------------|-------------|
| Auditors | 3 Cursor Task | 3 Cursor Task + 2 HTTP API |
| Cost | 3× subagent | 3× subagent + ~2 cheap API calls |
| Prep | Audit pack in chat | Audit pack on disk + domain prompt template |
| Best for | Bugs, infra, quick triage | Pre-ship council, prod posture, domain strategy |

Read [cursor-audit](../cursor-audit/SKILL.md) for shared synthesis rules and Glasswing conflict gating.

## Workflow (parent agent)

```
Super audit progress:
- [ ] 0. Tailor — domain prompt, mission, artifact list, output extras
- [ ] 1. Scope — target, question, constraints, ruled-out hypotheses
- [ ] 2. Mode — classify; pick 3 Cursor models (reference.md)
- [ ] 3. Pack — build_audit_pack.py → audit_prompt.md + PACK_INDEX.md
- [ ] 4a. Cursor leg — 3× Task in ONE message, readonly
- [ ] 4b. API leg — discover keys → run_api_auditors.py (parallel slots 4–5)
- [ ] 5. Synthesize — 5-model consensus / unique / conflicts / fix order
- [ ] 6. Act — report only unless user says fix; offer re-audit after large changes
```

Announce before dispatch:

> Super audit — mode: `{mode}` · Cursor: `{m1, m2, m3}` · API: `{api1, api2}` · pack: `{path}`

### Step 0 — Tailor (required every run)

Copy [prompt-template.md](prompt-template.md) to the project audit folder (e.g. `prompts/{slug}_super_audit.md` or `reports/audit/prompt.md`). Fill:

1. **Mission** — one sharp question (single sentence)
2. **Domain context** — tables, version state, env toggles, prior audit bullets
3. **Code/data paths** — absolute paths auditors must read
4. **Output extras** — mode-specific sections (deploy recommendation, env list, metrics to avoid, etc.)
5. **`{{MODEL_SLOT}}`** — leave placeholder; scripts substitute per auditor

Confirm tailoring with user when stakes are high (prod deploy, cost claims).

**Artifact manifest** — list files to copy into the pack (metrics jsonl, configs, briefs, status script output). Parent runs `build_audit_pack.py` with `--artifact path:alias` or a small manifest JSON.

### Step 1 — Scope

Same as cursor-audit: target, question, constraints, ruled-out hypotheses. Add:

- **Ship deadline** — P0 vs P1 backlog labels
- **Regime boundaries** — what comparisons are invalid (e.g. playground ≠ tournament)
- **Synthesis output path** — where to write rollup brief (e.g. `briefs/YYYY-MM-DD_{slug}-super-audit-synthesis.md`)

### Step 2 — Mode + model pick

Classify mode (see [reference.md](reference.md)). Default **5-auditor split**:

| Slot | Channel | Default | Role |
|------|---------|---------|------|
| 1 | Cursor Task | `claude-opus-4-8-thinking-high` | Agentic reasoning / root cause |
| 2 | Cursor Task | `gpt-5.3-codex` | Implementation / patches |
| 3 | Cursor Task | `gemini-3.1-pro` | Third family / alt structure |
| 4 | HTTP API | `x-ai/grok-4.3` @ OpenRouter | Adversarial / exploit paths |
| 5 | HTTP API | `deepseek-reasoner` @ DeepSeek | Cheap deep reasoning |

Override slots 4–5 in `auditors.json` (see reference) when tailoring (e.g. WC bot: `ADVISOR_MODEL` on OpenRouter).

**Quick mode:** slots 1–3 Cursor + slot 5 API only (skip Grok).

### Step 3 — Build audit pack

From repo root or project subfolder:

```bash
python3 .cursor/skills/super-audit/scripts/build_audit_pack.py \
  --prompt prompts/{slug}_super_audit.md \
  --out reports/audit/pack-{slug} \
  --artifact reports/hl-loop/deploys.jsonl \
  --artifact reports/hl-loop/state.json
```

Outputs:

- `PACK_INDEX.md` — read order for auditors
- `audit_prompt.md` — rendered prompt (`{pack_index}` replaced)
- copied artifacts + `meta.json`

Subagents and API script read **only** the pack — not parent chat.

### Step 4a — Cursor leg (3 parallel)

Use **Task** three times in **one message** — same pattern as cursor-audit. Inject into each prompt:

- Path to `audit_prompt.md` (absolute)
- `You are auditor {N}/5 — slot: {model_slug}. Read the pack index first.`
- Required output format from template
- `readonly: true`

```text
subagent_type: generalPurpose
readonly: true
run_in_background: false
model: <cursor slug>
description: super-audit-{1|2|3}-{short-label}
prompt: <pointer to pack + role line + output format>
```

### Step 4b — API leg (2 parallel)

Discover keys first (parent or script):

```bash
python3 .cursor/skills/super-audit/scripts/discover_api_keys.py
```

Then run API auditors (after pack exists):

```bash
python3 .cursor/skills/super-audit/scripts/run_api_auditors.py \
  --pack reports/audit/pack-{slug} \
  --out reports/audit/premium-{slug}
```

Optional: `--auditors path/to/auditors.json` to override default Grok + DeepSeek.

Script writes `{label}_{timestamp}.md` per model + `meta_{timestamp}.json`. On missing keys: report which slots skipped; continue with Cursor-only synthesis if user accepts.

**Do not** paste API keys into chat. Keys load from env files only.

### Step 5 — Synthesize (5-model)

Use this template (extends cursor-audit):

```markdown
# Super audit — {target summary}

**Mode:** {mode} · **Pack:** `{pack path}` · **Built:** {ts}

| Slot | Channel | Model | Verdict |
|------|---------|-------|---------|
| 1 | cursor | {m1} | PASS/WARN/FAIL |
| 2 | cursor | {m2} | … |
| 3 | cursor | {m3} | … |
| 4 | api | {api1} | … |
| 5 | api | {api2} | … |

## Consensus (≥3 auditors) 
- ...

## Strong consensus (≥4 auditors)
- ...

## Unique (single auditor — still investigate)
- [{model}] ...

## Conflicts (resolve before ship)
| Topic | {m1} | {m2} | {m3} | {api1} | {api2} | Resolution |
|-------|------|------|------|--------|--------|------------|

## Domain recommendation (from tailoring extras)
- Deploy target / config / env toggles / numeric targets

## Ranked patch backlog
| P | Patch | Effort | Expected lift |
|---|-------|--------|---------------|

## Recommended fix order
1. ...

**Overall:** SHIP | SHIP-WITH-FIXES | REWORK | REJECT — one paragraph
```

**Conflict rule:** ≥2 auditors disagree on root cause or deploy commit → flag in Conflicts; propose concrete test before ship.

Write synthesis to the path chosen in Step 1 (briefs/ or reports/).

### Step 6 — Act

- Default: synthesis brief only.
- Prod briefs: run `python3 scripts/skill_audit.py` on handoff brief if applicable.
- Re-audit after substantive deploy or when user says still failing.

## Invocation phrases

- `/super-audit` or `super audit on …`
- `5-model audit` / `council super audit`
- `super audit before prod ship`
- Optional: `mode: brief-plan`, `quick`, `pack: path`, `prompt: path`

## Cost discipline

- API legs ≈ fraction of one Cursor subagent when using DeepSeek + OpenRouter.
- Full super audit ≈ 3× Cursor + 2 API. Use **quick** when time-sensitive.
- Do not re-run full super audit on every tiny edit.

## Related

- [cursor-audit](../cursor-audit/SKILL.md) — 3-model baseline
- [reference.md](reference.md) — API key discovery, auditors.json, mode matrix
- [examples.md](examples.md) — poker Tournament S1, WC bot
- [agent-toolkit-demo/skills/super-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/super-audit) — public open-source distro
- `@ccc-wiki/entities/skills/super-audit.md` — wiki canonical page
- `@ccc-wiki/entities/patterns/glasswing-deliberate-disagreement.md`
- `config/llm-routing.env.example` — canonical key locations
- `agents/devfun-poker-arena/` — reference implementation (domain-specific scripts)
