# Cursor audit — examples

## Example 1 — User invocation (code bug)

**User:**

> cursor audit — MCP server shows red; tool search returns empty

**Parent:**

1. Scope: `.cursor/mcp.json`, MCP catalog, error = empty search
2. Mode: `config-infra`
3. Models: gemini-3.1-pro, gpt-5.5-medium, claude-4.6-sonnet-medium-thinking
4. Dispatch 3 parallel readonly Tasks with shared audit pack
5. Synthesize: consensus on stale catalog + disabled UI toggle; unique finding from one model on config path mismatch

**Sample synthesis excerpt:**

```markdown
## Consensus (≥2 auditors agree)
- MCP catalog stale or server disabled in UI — reindex + enable toggle

## Unique (single auditor — still investigate)
- [gemini] config path mismatch vs mcp.json cwd

## Overall:** SHIP-WITH-FIXES — reindex first; if still empty, fix config path
```

---

## Example 2 — Brief GO/NO-GO

**User:**

> /cursor-audit mode brief-plan on briefs/2026-06-01_adoption-brief.md

**Parent:**

1. Read brief; paste Summary + Body + cost claims into audit pack
2. Mode: `brief-plan`
3. Models: opus, codex, kimi
4. Lens: displacement vs existing tooling, statistical claims, phase 1 scope
5. Run `vet briefs/2026-06-01_adoption-brief.md --profile brief` after synthesis

**Conflict example:**

| Topic | codex | opus | kimi |
|-------|-------|------|------|
| Backtest sample size | n too small | acceptable with caveats | insufficient detail |

Resolution: parent proposes adding explicit n and regime disclosure before ship.

---

## Example 3 — Security pass

**User:**

> council audit on the new auth middleware in src/middleware/

**Parent:**

1. Mode: `security`
2. Models: opus, codex, grok
3. Audit pack lists all files in scope + threat model (session fixation, header injection)

---

## Example 4 — Quick triage

**User:**

> quick cursor audit on scripts/deploy.sh

**Parent:**

1. Mode: `quick-triage`
2. Models: composer-2.5-fast, gpt-5.5-medium, claude-4.6-sonnet-medium-thinking
3. Subagents return top 3 issues only

---

## Example 5 — After fix loop

**User:**

> you fixed it but still failing — cursor audit again

**Parent:**

1. Re-scope with **Already ruled out** filled from prior audit
2. Same mode unless evidence shifted (e.g. code-debug → config-infra)
3. Optionally swap one model for fresh eyes (e.g. replace gemini with grok)
