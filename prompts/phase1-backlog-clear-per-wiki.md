# Phase-1 backlog clear — paste into any Cemini wiki chat

**Use:** open the target wiki folder in Cursor, paste this whole block, send.
**Canon:** CCC `.cursor/skills/phase1-wire/SKILL.md` · `@ccc-wiki/concepts/phase1-adopt-wire.md`
**Skip always:** Image-gen · 3D-printing local wire backlogs

---

```text
/phase1 — clear THIS wiki’s Phase-1 backlog (full sweep)

You are in: <THIS OPEN WORKSPACE / WIKI>. Follow `.cursor/skills/phase1-wire/SKILL.md` (federation).

## Goal
Leave every adopt relevant to THIS surface with `wire_status` ≠ `unwired`. Prefer policy wires. Mark REFERENCE/trainers/OOD as `wont_wire`. Do not stop at inventory — wire until the backlog for this surface is clear or every remaining item is explicit `deferred` with a next action.

## Scope (this chat only)
1. Own this wiki’s entities, CLAUDE.md, `.cursor/rules/`, and any local `.local/adopts/` if present.
2. Also wire **cross-surface** items that THIS wiki owns operationally (e.g. OSINT owns finance/governance tools; Cybersec owns agent-security; Game-dev owns ARC/Tycho-style; TipDrop owns scanner ops; CCC owns harness/meta).
3. Do **not** build Image-gen or 3D-printing local wire backlogs.
4. Do **not** install GRPO trainers, Harbor/Modal fleets, ARC full runners, or `curl | sh`.
5. Ask once before any `~/.cursor/mcp.json` / project MCP / settings.json runtime install; otherwise policy-only.
6. No secrets in rules/handoffs. No LIVE Discord without LIVE OK.

## Procedure
1. Read `phase1-wire` skill + CCC concept `phase1-adopt-wire` if available (`@ccc-wiki/concepts/phase1-adopt-wire.md` or open CCC path).
2. Inventory candidates for THIS surface:
   - If CCC or OSINT: run  
     `python3 "/Users/claudiobarone/Projects/Cemini claude code CCC/scripts/phase1_adopt_inventory.py" --write-brief`  
     then filter rows to this surface + related entities here.
   - Else: grep this wiki for `wire_status: unwired`, missing `wire_status` on ADOPT/GO tool entities, and Phase-0 GO clones under `.local/adopts/` if any.
3. Classify each item → `policy_wired` | `runtime_wired` | `wont_wire` | `deferred`.
4. Wire in batches by theme (one rule file or CLAUDE section per theme — not one rule per arXiv id):
   - Policy: 3–7 agent-facing bullets in `.cursor/rules/*.mdc` (alwaysApply when daily) and/or `CLAUDE.md`.
   - Runtime: only true drop-ins after a single confirmation ask; else leave `deferred` or `wont_wire`.
   - REFERENCE / paper repro / trainer / OOD: set `wont_wire` + one-line reason on the entity.
5. Update every touched entity frontmatter:
   - `wire_status`
   - `wire_target` (path to rule / CLAUDE section / MCP) when wired
6. Append `wiki/log.md` entry: `## [YYYY-MM-DD] phase1 | <wiki> backlog clear` with counts.
7. Lint: `python3 scripts/wiki_lint.py` (or this wiki’s lint). Fix bidirectional gaps you caused.
8. If you edited a federation skill or a rule that should propagate, remind to run CCC sync (post-commit on CCC handles skills; copy local rules as needed).
9. Commit + push only if I already asked for git in this chat; otherwise stop after lint and summarize.

## Success criteria (all must pass before you claim done)
- [ ] Every THIS-surface ADOPT/GO / clone candidate has `wire_status` in {policy_wired, runtime_wired, wont_wire, deferred}
- [ ] No relevant item left `unwired` without explanation
- [ ] Policy wires are reachable (alwaysApply rule or CLAUDE.md)
- [ ] Trainers / Modal / REFERENCE-only marked `wont_wire` with reason
- [ ] Zero Image-gen / 3D local wire attempts
- [ ] `wiki/log.md` updated; lint clean for your edits
- [ ] Final reply: table of Wired / Wont_wire / Deferred counts + paths of new/updated rules

## Output shape
1. One-line plan
2. Classification table (clone/entity → class → target)
3. Then execute wires (don’t wait for approval except MCP/settings)
4. End with counts + “remaining deferred: …”
```

---

## Per-wiki one-liners (optional first line above the block)

| Paste in | Prefill / remind |
|----------|------------------|
| **CCC** | Surface=`ccc`. Run inventory script; wire harness/meta; steal TipDrop/poker bullets only when CCC owns the pattern. |
| **OSINT** | Surface=`osint`. Filter inventory to osint rows; wire finance/governance/OSINT tools into OSINT rules/CLAUDE. |
| **Cybersecurity** | Surface=`cybersec`. Wire agent-security / red-team steals; skip CCC-only harness clones. |
| **Gambling** | Surface=`gambling`. Wire betting/PM-relevant policy only; send harness steals back to CCC as stubs. |
| **Game Dev** | Surface=`game-dev`. Wire ARC/Tycho/sim steals; trainers → `wont_wire`. |
| **SEO** | Surface=`seo`. Wire GEO/adopted-geo-related only. |
| **TipDrop kit/scanner** | Surface=`tipdrop`. Policy bullets in TipDrop `CLAUDE.md` / rules; no LIVE Discord. |
| **Atto / CeminiSuite** | Surface=`atto` or `suite`. Only product-relevant wires; else `wont_wire` / route to CCC. |
| **Image gen / 3D** | Do **not** run this prompt — skip local Phase-1 backlog by policy. |

## Suggested order
1. CCC → 2. OSINT → 3. Cybersec → 4. TipDrop → 5. Game-dev → 6. Gambling → 7. SEO → 8. Atto/Suite as needed.
