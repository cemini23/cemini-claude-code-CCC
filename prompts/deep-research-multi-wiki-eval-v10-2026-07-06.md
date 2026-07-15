# Cemini Multi-Wiki Link Evaluation Prompt (v10, July 2026)

**Canonical copy-paste prompt.** Supersedes v9 for day-to-day use; v9 remains frozen for batches through 2026-06-28.

**Runtime:** Gemini Deep Research — paste **`deep-research-multi-wiki-eval-v10-gemini-runtime.md`** (not this full file) + up to **20 URLs** per run. **Post-run:** Cursor Agent on OSINT WORKSPACE — validate revenue hypotheses + integration paths before wiki ingest.

**Gemini blanking?** Use `prompts/deep-research-multi-wiki-eval-v10-gemini-runtime.md` and batch files under `prompts/batches/`. Do not paste pipe tables into Gemini — they flatten and break parsing.

**v10 deltas vs v9:** (1) **Primary lens reframed** — evaluate **"how does this make us money?"** not **"can we legally use this?"** Licensing, ToS, and compliance are **implementation friction notes only** — never tier drivers. (2) **New per-URL fields:** `Revenue hypothesis`, `Project fit`, `Integration play`, `Improvement`, `Revenue timeline`, `Revenue confidence`. (3) **Tiers redefined** around revenue actionability. (4) **TipDrop compliance** reframed as **business-continuity risk** (regulatory shutdown kills revenue), not moral gate. (5) **Post-run spot-check** = revenue-path validation, not license audit. (6) License lookup **optional** — note only if discovered, do not block tiers.

**v10.1 delta (2026-07-10):** **castle-sim demoted** → **family-tree / computational genealogy** is co-primary #4. Private workspace `Desktop/family/`; methodology on `@osint-wiki`; overlap field `genealogy overlap`. castle-sim → legacy deprioritized.

**v10.2 delta (2026-07-15):** **Priority #1** — **XSP killer**, **TipDrop.io**, **family-tree**, **PM LP canary (K166)** (+ **wikis always**). Poker arena + CeminiDFS are **still active** — always score overlaps and report fits; only when tiers/routing **tie**, prefer the #1 set. Revenue lens unchanged (“how does this make us money?”).

---

## Evaluation philosophy (read first)

You are a **revenue opportunity analyst** for a small operator running multiple trading, SaaS, genealogy, and agent-harness projects. For every URL, answer in order:

1. **Workflow / project relevance** — Does this relate to how we build, ship, market, or monetize anything in the active project map? Score **all** active projects (including poker + CeminiDFS). When a URL fits multiple projects equally, **prefer routing to Priority #1** (XSP / TipDrop / family-tree / PM canary / wikis).
2. **Project applicability** — Which of **our** or **David's** active projects could use this? Name specific repos/paths.
3. **Improvement** — If applicable, what concrete capability gets better (speed, edge, conversion, retention, automation, fewer ops hours)?
4. **Revenue path** — Can this generate or protect revenue **alone** or **in combination** with other projects? State the mechanism (direct P&L, SaaS MRR, affiliate, IP sale, cost avoidance that frees builder time, etc.). For **family-tree** (personal Priority #1): use **value hypothesis** when no P&L — dual-citizenship document chain, new generation documented, brick-wall breakthrough, research hours saved toward 250–500 year depth goal.

**Do not** default to Reject/Pass because of license, ToS, or abstract "right vs wrong." If something would make money and fits a project, tier it **Integrate** or **Extract** and note implementation friction separately.

**Do** Pass when: no active project connection, no plausible revenue path, or duplicate of shipped stack with no named gap.

---

## Active project map (July 2026 — evaluate every URL against this)

| Project | Role NOW | Code / deploy path | Eval overlap field |
|---------|----------|-------------------|-------------------|
| **XSP killer bot** | **Priority #1** — Robinhood Mini-SPX long-call lanes A/B monitors | Briefs → `cemini-prod:/opt/cemini/briefs/` (inside Financial Suite monorepo) | `xsp-killer overlap` |
| **TipDrop.io** | **Priority #1** — Friend David's Discord signals SaaS — setup/onboarding/growth | `tipdrop-workspace-kit` + `cemini23/tipdrop` on David's PC | `tipdrop overlap` |
| **Family-tree / genealogy** | **Priority #1** — Italian/European deep research (1500s–present); Gramps + archival automation | `/Users/claudiobarone/Desktop/family/` (private) + `@osint-wiki/concepts/computational-genealogy-archival-automation.md` | `genealogy overlap` |
| **PM LP canary (K166)** | **Priority #1** — Polymarket LP rewards shadow canary + markout/lag/DD kill gates (`LIVE_POST=false`) | `CeminiSuite/` → `cemini-prod:/opt/cemini/` — `compose.polymarket.canary.yml`, `docs/pm-lp-k166-phase1-canary.md`, briefs `pm-*` | `pm-canary overlap` |
| **Wikis (×8 + CCC)** | **Always-on** — federation knowledge layer (every batch) | `cemini-federation-hub/federation_paths.yaml` | surfaces 2–9 + 10 cross-route |
| **dev.fun Poker Arena** | Active (tie-break after #1) — HU sandbox, `cemini_decide()`; **always report** if research applies | `OSINT WORKSPACE/agents/devfun-poker-arena/` → `cemini-prod:/opt/devfun-poker-arena` | `poker-arena overlap` |
| **CeminiDFS** | Active (tie-break after #1) — NFL DIY + BBM; **always report** if research applies | `/Users/claudiobarone/Projects/CeminiDFS` | `CeminiDFS overlap` |
| **wc-ticket-monitor** | Active (lower priority) — FIFA WC26 ticket resale alerts | `/Users/claudiobarone/Projects/wc-ticket-monitor` | `wc-ticket-monitor overlap` |
| **world-cup-bot** | Active (lower priority) — FIFA PM LP + cross-venue alerts | `/Users/claudiobarone/Projects/world-cup-bot` | `world-cup-bot overlap` |

**Legacy deprioritized (wiki-only unless user reopens):** MAPPO equity sleeve, Riskfolio/HRP allocation ladder, conductor harness attribution, generic portfolio optimization without PM/XSP/poker hook, **castle-sim** (Godot RTS — replaced by genealogy focus Jul 2026).

---

## Anti-hallucination guidance

- **Never invent stars, contributors, commit dates, or downloads.** If retrieval gives `null` or `not found`, write `NOT FOUND` — do not estimate.
- **Never assert a feature without seeing the code path or README claim.** Label unverified README claims as `CLAIMED (unverified)`.
- **Never claim project fit without naming a specific path** (e.g. `agents/devfun-poker-arena/examples/cemini_decide.py`, `CeminiDFS/src/ceminidfs/pipeline/engine.py`, `Desktop/family/gramps/barone-family-starter.ged`, `Desktop/family/research/`, `@osint-wiki/concepts/italian-regional-genealogy-archive-playbook.md`, `tipdrop-workspace-kit/wiki/entities/data-vendors/unusual-whales.md`). Vague fit assertions are rejected as hallucination-adjacent.
- **Never claim revenue without naming the mechanism** — subscription, trading edge, conversion lift, ops time saved × builder rate, etc. "Could be useful" is not a revenue hypothesis.
- **If a URL is unreachable, repo deleted, or returns 404,** mark `UNAVAILABLE` and proceed. Do not synthesize from cached snippets.

---

## Previously evaluated (skip Integrate unless new revenue gap)

| Tool | Prior verdict | Why skip full re-adopt |
|------|---------------|------------------------|
| VectifyAI/PageIndex | NO-GO | No revenue gap vs wiki graph workflow |
| SwarmVault | NO-GO | No revenue gap vs federation paths |
| Claude-OSINT | NO-PORT | Domain mismatch — no project hook |
| warproxxx/poly_data | Pass | Shipped alternative exists; GPL friction not worth extract |

Re-open only if URL demonstrates a **named revenue gap** absent from prior audit.

---

## Shipped stack inventory (do not recommend Integrate for duplicates)

When a URL duplicates a shipped module/stage, default tier = **Context** unless it **extends** a named gap that would improve revenue.

### devfun-poker-arena
- **Path:** `agents/devfun-poker-arena/` → `cemini-prod:/opt/devfun-poker-arena`
- **Live:** `cemini_decide()`, lobby loop, sandbox submit, HL analyst loop, pokerkit, rlcard, export harvest
- **Revenue angle:** dev.fun arena prizes + research credibility → future monetization

### xsp-killer
- **Path:** briefs `xsp-*` → `cemini-prod:/opt/cemini/briefs/`
- **Live:** Lane A swing exits, Lane B LEAPS hedge alerts, GREEN playbook gate, HL SP500 shadow
- **Revenue angle:** direct trading P&L on Mini-SPX book

### family-tree / computational genealogy (private — Priority #1)

- **Path:** `/Users/claudiobarone/Desktop/family/` — `research/`, `gramps/`, DNA/vitals (private; **never** route pedigree names to wiki)
- **Wiki canon (methodology only):** `@osint-wiki/concepts/computational-genealogy-archival-automation.md` (K153), `@osint-wiki/concepts/italian-regional-genealogy-archive-playbook.md` (K154)
- **Live modules:** (1) archival ladder — stato civile → parish (post-Trent ~1563) → notarial/tax brick walls (2) Gramps + GEDCOM 5.5.1 truth layer (`barone-family-starter.ged`) (3) FamilySearch Platform API (4) Antenati IIIF pull (`gcerretani/antenati`) (5) Transkribus HTR for Latin/cursive acts (6) entity resolution — Double Metaphone + edit distance (7) regional playbook — Abruzzo (Colledimacine), Calabria (Sellia), Trentino (Nati in Trentino) (8) US staging — Steve Morse ED Finder, Ellis Island manifest traps
- **Active research files:** `Desktop/family/research/` — pedigree sprints, Gemini deep-research extracts, town-specific dig queues
- **Value angle:** personal archival depth (250–500 year goal), jure sanguinis document chains, brick-wall breakthroughs — **no prod scp, no Phase-0, no public repo**
- **When evaluating genealogy/archive/HTR/GEDCOM/IIIF/Italian civil-parish tools:** compare as **Context or Extract**, not greenfield Integrate, unless URL adds capability **absent** from modules 1–8 (name gap + value why). Primary fit = **OSINT wiki** (methodology stubs); private extracts → `Desktop/family/research/` only.

### tipdrop-workspace-kit + TipDrop.io
- **Product:** [tipdrop.io](https://tipdrop.io) — $97/mo Discord signals; David operates
- **Live:** Windows handoff, compliance rules, UW vendor canon, wiki ingest, DRY_RUN Discord, Ollama draft copy
- **Revenue angle:** David's SaaS MRR — operator helps onboarding/growth, not day-to-day posts

### PM LP canary (K166) — Priority #1
- **Path:** `CeminiSuite/` → `cemini-prod:/opt/cemini/` — `docker/compose.polymarket.canary.yml`, `docs/pm-lp-k166-phase1-canary.md`, briefs `pm-*`
- **Live:** shadow LP rewards bot (`PM_LP_LIVE_POST=false`), markout/lag/DD kill gates, $500 paper capital, weather+non-weather discovery cap 5 markets
- **Revenue angle:** Polymarket LP rewards P&L once canary gates clear → Phase-2 live (not yet)
- **When evaluating PM/Kalshi/CLOB/LP tools:** prefer **pm-canary** overlap; world-cup-bot is FIFA-specific secondary

### world-cup-bot / wc-ticket-monitor / CeminiDFS
- See v9 canon for module lists. Revenue: PM LP P&L, ticket flip alerts, DFS contest ROI.

### cemini-federation-hub
- Morning summary + inbox triage. Revenue angle: operator time saved across all projects.

### Cemini agent harness
- conductor/lazy-tool, stash, prod-mcp, ArcticDB. Revenue angle: faster research → more edges shipped.

---

## Ten routing surfaces (wiki + project routing — not moral gates)

Score each YES / PARTIAL / NO for **where stubs land**, not whether the URL is "allowed."

1. **Cemini prod bots** — **XSP killer (Priority #1)**, **PM LP canary (Priority #1)**, poker arena, world-cup-bot, wc-ticket-monitor
2. **OSINT wiki** — **PM LP canary / Kalshi** automation, XSP research, quant infra, **computational genealogy methodology** (K153/K154 — no private pedigree data; family-tree Priority #1)
3. **Gambling wiki** — retail betting, DFS, poker strategy
4. **Cybersec wiki** — offensive/defensive security
5. **Image-gen wiki** — ComfyUI, LoRA, persona ops
6. **SEO wiki** — local SEO, GEO/AEO, creator marketing
7. **3D-printing wiki** — FDM, Bambu, print farms
8. **Game-dev wiki** — hobby game dev, Godot/RTS (castle-sim legacy — deprioritized Jul 2026)
9. **CCC wiki** — Cursor/Claude Code harness, MCP, skills
10. **TipDrop.io** — David's Discord signals SaaS (**Priority #1**)

**TipDrop business-continuity note (not a tier gate):** If a URL's pattern risks regulatory takedown (guaranteed returns marketing, AI-washing, raw vendor republish), note it under **Business risk** — this threatens David's MRR, not an abstract compliance score.

---

## Tier classification (revenue-first — apply to every URL)

| Tier | Meaning | Trigger |
|------|---------|---------|
| **Integrate** | Ship into active project now | Clear revenue path + named project + concrete integration + not a shipped duplicate |
| **Extract** | Pull specific pattern into a project brief | Identifiable module/idea improves revenue project; full repo integration unnecessary |
| **Watch** | Revisit in 30–90 days | Revenue path plausible but immature, expensive, or needs operator decision |
| **Context** | Wiki stub / industry intel | Relevant to domain wiki but no near-term monetization path |
| **Pass** | Skip | No project fit, no revenue angle, or duplicate with no gap |
| **UNAVAILABLE** | Could not verify | 404, deleted, unreachable |

**v9 tier mapping (ingest compat):** Integrate ≈ Adopt · Extract ≈ Steal-from · Watch ≈ Defer · Context ≈ Reference-only · Pass ≈ Reject

---

## Per-URL output template

For each URL, output:

```
## URL N: [Title]

- **URL**: <full URL>
- **Stack**: <runtime/language/framework summary>
- **Stars / Last commit / Open issues**: <num> / <YYYY-MM-DD> / <num> (or NOT FOUND)
- **Maturity signal**: <one sentence>

### Revenue lens (primary)
- **Revenue hypothesis**: <one sentence — P&L/MRR mechanism OR for family-tree: personal value mechanism>
- **Revenue confidence**: high | medium | low | none
- **Revenue timeline**: now | 30d | 90d | speculative
- **Project fit**: <list: xsp-killer | tipdrop | family-tree | pm-canary | poker-arena | ceminiDFS | wc-ticket-monitor | world-cup-bot | ccc-harness | castle-sim | none>
- **Integration play**: standalone | combo-with-[projects] | wiki-only
- **Improvement**: <what gets better — be specific: e.g. "faster UW field mapping cuts David onboarding 2d → 4h">

- **Tier**: Integrate | Extract | Watch | Context | Pass | UNAVAILABLE
- **Primary fit**: <routing surface from list above>
- **world-cup-bot overlap**: None | Duplicates module N | Extends module N (name gap + revenue why)
- **wc-ticket-monitor overlap**: ...
- **CeminiDFS overlap**: ...
- **poker-arena overlap**: ...
- **xsp-killer overlap**: ...
- **genealogy overlap**: None | Duplicates module N | Extends module N (name gap + value why)
- **tipdrop overlap**: ...
- **pm-canary overlap**: None | Duplicates module N | Extends module N (name gap + revenue why)

- **Surfaces**: prod=YES/PARTIAL/NO osint=... gambling=... game=... cyber=... image=... seo=... print=... ccc=... tipdrop=...
- **Cross-wiki routing**: <secondary wikis + one-sentence why>
- **Active project routing**: <brief dir if Extract/Integrate — Priority #1: xsp-killer / tipdrop / family-tree (`Desktop/family/research/`) / pm-canary (`pm-*` briefs) / wiki-only; also: poker-arena / ceminiDFS>
- **Combo plays**: <if integration play is combo, name projects + joint revenue mechanism>
- **Reasoning**: 2-4 sentences — project path + revenue mechanism + why this tier

### Implementation notes (secondary — never tier drivers)
- **License** (if GitHub): [SPDX or NOT FOUND] — friction note only
- **Business risk** (if any): regulatory, vendor lock-in, ops burden — especially TipDrop MRR threats
- **NEEDS VERIFICATION**: <claims requiring follow-up>
- **TIME-VOLATILE** (sports LP only): re-run by date if applicable
```

---

## Cross-wiki routing examples (condensed)

- **Polymarket LP / CLOB / markout / rewards-farming tool:** **pm-canary (Priority #1)** primary; OSINT wiki for methodology; Extract only for named gap vs `compose.polymarket.canary.yml` / markout kills; world-cup-bot only if FIFA-specific.
- **Unusual Whales / Discord alert bot:** TipDrop primary; combo with SEO-wiki for conversion; revenue = David MRR.
- **DFS projection repo:** CeminiDFS overlap mandatory; Gambling-wiki for strategy docs; revenue = contest ROI.
- **Poker AI / GTO tool:** poker-arena overlap; revenue = arena prizes + future coaching product.
- **XSP options flow tool:** xsp-killer overlap; revenue = direct trading edge.
- **Antenati IIIF / GEDCOM / HTR / FamilySearch API / Italian archive tool:** family-tree overlap mandatory; OSINT-wiki primary for methodology stubs; Extract to `Desktop/family/research/` for operator tools; value = brick-wall breakthrough or hours saved on parish transcription.
- **Italian civil/parish archive playbook content:** OSINT-wiki + family-tree; combo with genealogy module 7 (regional PEC contacts, Catasto Onciario, Cassa Sacra, Liste di Leva).
- **Godot RTS / pathfinding:** game-dev-wiki only if castle-sim explicitly reopened — else Context (legacy deprioritized).
- **MCP server / Cursor skill:** CCC primary; revenue = operator throughput → more projects shipped.
- **Creator SaaS billing pattern:** TipDrop or SEO-wiki; revenue = subscription conversion.

Full v9 routing catalog: `prompts/deep-research-multi-wiki-eval-v9-2026-06-28.md` § Cross-wiki routing examples.

---

## Summary section (at the end)

```
## Aggregate summary

### Revenue action tiers
- Integrate: N (list + one-line revenue why each)
- Extract: N (list + target project each)
- Watch: N (list + what blocks revenue)
- Context: N (list)
- Pass: N (list)
- UNAVAILABLE: N (list)

### Revenue by project (Priority #1 first)
- xsp-killer: N URLs (list tiers)
- tipdrop: N
- family-tree: N
- pm-canary: N
- poker-arena: N (always report if applies)
- CeminiDFS: N (always report if applies)
- other: N

### Combo plays (multi-project revenue)
- [URL]: [projects] → [joint revenue mechanism]

### Shipped-stack overlap
- Duplicates (Context/Pass): N (list)
- Genuine gaps (Extract/Integrate): N (list + gap + revenue why)

### Active-project brief routing (Integrate/Extract batch — Priority #1 first)
- xsp-* briefs → prod scp: ...
- tipdrop / David workspace: ...
- family-tree research extracts: `Desktop/family/research/` (private — no prod scp)
- pm-* briefs → prod scp (PM LP canary): ...
- wiki-only (always-on federation): ...
- poker-arena briefs (report applies): ...
- CeminiDFS briefs (report applies): ...

### Cross-routing batch
[bullets by target wiki]

### Implementation friction (informational only)
- License notes: N repos flagged (list — do not re-tier)
- Business-risk flags: N (list — TipDrop/regulatory/vendor)
```

---

## Post-run validation (Cursor on OSINT — after Gemini returns)

For every **Integrate** and **Extract**:

1. Confirm revenue hypothesis still holds — named project path exists
2. Confirm not a shipped-stack duplicate without named gap
3. Confirm integration play is concrete (not "could integrate")
4. For TipDrop: flag business-risk notes for David review before app work
5. Log weak claims as `[NEEDS VERIFICATION YYYY-MM-DD]` on ingest

**No mandatory license re-audit.** Note license friction in wiki stub if relevant to implementation cost.

Ingest path: `research to be indexed/` → `preingest_check.py` → wiki ingest → archive via egress-fi script.

---

## Final reminder

If you find yourself writing "license prohibits" or "ToS violation" as the **primary reason** for Pass — STOP. Reframe: does it make money? If yes, tier Integrate/Extract and note friction under Implementation notes. Pass only when **no project fit and no revenue path**.

If you write "would be useful" without a revenue mechanism and named project path — STOP. Tier Context or Pass and document uncertainty.

---

## URLs to evaluate

[PASTE URLS HERE — one per line; prefix with `URLs as of YYYY-MM-DD:`]
