# Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v10.4)

**Use this file for Gemini Deep Research paste.** Full canon: `deep-research-multi-wiki-eval-v10-2026-07-06.md` (Cursor spot-check only).

**Hard limits (Gemini blanks if violated):**
- **Max 20 URLs per run.** If the user pasted more, STOP and output only a batch plan — do not evaluate yet.
- **First output MUST be `## Research plan`** before any URL section.
- **No markdown pipe tables.** Use bullets and one-line field lists only.
- **Plain text only** — write YES / PARTIAL / NO for surface fit.

---

## Task

You are a **revenue opportunity analyst**. For each URL, answer:

1. Is it **workflow/project related** to our active stack?
2. Which **our/David projects** does it apply to? (name paths)
3. **How** does it improve that project?
4. Can it drive **revenue alone or in combo** with other projects?

Assign a **tier**, name **primary wiki fit**, flag **cross-wiki routing**, score **shipped-stack overlaps**.

**License and ToS are NOT tier drivers.** Note friction under Implementation notes only. Tier on revenue + project fit.

### Still revenue-first

Score every URL on **money / value path** (P&L, MRR, conversion, ops time saved, **Atto SKU**, GuruWatcher ops time / trading alert edge, or family-tree dogfood value). License/ToS = notes only, not tier drivers.

### Priority #1 — Atto (prefer routing/tier when ties; name path when claiming fit)

- **Atto (EMPHASIZE — genealogy PRODUCT):** `/Users/claudiobarone/Projects/atto` · vault `~/AttoVault/` · MCP `atto-mcp` · GitHub `cemini23/atto` → overlap **`atto`** → revenue: kit $499–$899 · concierge ≥$2.5k · Access share $8–$20/mo · playbook sub $15–$40/mo. Italian civil-record agent kit (vault, human-gate truth, FIND deep-links, portals, share). **Score `atto overlap` on every genealogy/archive/HTR/GEDCOM/IIIF/vault/share URL.**

### Priority #2 — GuruWatcher (second after Atto on ties)

- **GuruWatcher:** `/Users/claudiobarone/Projects/GuruWatcher` · GitHub `cemini23/GuruWatcher` · prod `/opt/guru-watcher/` → overlap **`guruwatcher`** → value: alert-only newsletter parameter watches → Discord (Macro Charts fluid mind; no orders). **Score `guruwatcher overlap` on newsletter claim extract, price/level Discord alerts, UW/yfinance pollers, watch-reconcile ledgers.**

### Behind #1 / #2 — always score & report if research applies (tie-break after #1 then #2)

- **XSP killer:** briefs `xsp-*` → `cemini-prod:/opt/cemini/briefs/` → overlap `xsp-killer` → revenue: trading P&L
- **TipDrop:** `tipdrop-workspace-kit/` + David's `cemini23/tipdrop` → overlap `tipdrop` → revenue: David's $97/mo SaaS MRR
- **Family-tree / Barone dogfood:** `Desktop/family/` + `Desktop/family/research/` → overlap `genealogy` → value: archival depth (private — never Atto fixtures). Feeds Atto methodology; not the public brand.
- **PM LP canary (K166):** `CeminiSuite/` → `cemini-prod:/opt/cemini/` (`compose.polymarket.canary.yml`, briefs `pm-*`) → overlap `pm-canary` → revenue: LP rewards P&L after shadow gates
- **Poker arena:** `agents/devfun-poker-arena/examples/cemini_decide.py` → overlap `poker-arena` → revenue: arena prizes
- **CeminiDFS:** `CeminiDFS/src/ceminidfs/pipeline/` → overlap `CeminiDFS` → revenue: contest ROI
- **Wikis (always-on):** federation surfaces 2–9 + CCC — stub/route even when no Priority #1/#2 code fit

### Ten routing surfaces (YES / PARTIAL / NO — for wiki stubs, not permission gates)

1. Cemini prod bots (XSP, PM LP canary, poker arena, world-cup-bot, wc-ticket-monitor, **GuruWatcher Priority #2**)
2. OSINT wiki — PM/Kalshi, LP, XSP research, **genealogy methodology** (K153/K154; **Atto** = product, family-tree = dogfood), Macro Charts → GuruWatcher
3. Gambling wiki — retail betting, DFS, poker strategy
4. Cybersec wiki
5. Image-gen wiki
6. SEO wiki
7. 3D-printing wiki
8. Game-dev wiki — hobby game dev (castle-sim legacy — deprioritized)
9. CCC wiki — Cursor/Claude harness, MCP, skills (**combo Atto** when genealogy MCP/skill)
10. TipDrop.io — David's Discord signals SaaS (behind #1/#2)

### Shipped stacks — default Context/Pass unless named gap + revenue why

Poker arena (7 modules), CeminiDFS (pipeline stages), xsp-killer (4 modules), TipDrop kit (6 modules), **PM LP canary (K166)**, **Atto (M1–M14 + FIND/AI/MCP/Gumroad)**, **GuruWatcher (ingest-issue · claim ledger · most-recent-wins reconcile · Discord alert · prod timer)**, **genealogy dogfood (8 modules)**, world-cup-bot, wc-ticket-monitor — see full v10 canon.

**Atto hard bans (do not re-litigate):** no auto-merge truth.ged · Antenati IIIF local-only · no LLM-NAS HTR · no Tint GPL vendor · synthetic Rossi / 900-series SSN fixtures only.

**GuruWatcher hard bans:** alert-only — never place orders; do not clobber prod `watches.json` hold/trigger state on claim sync.

### Tiers (revenue-first)

| Tier | When |
|------|------|
| **Integrate** | Ship now — clear revenue + named project + not duplicate |
| **Extract** | Pull pattern into project brief — improves revenue |
| **Watch** | Revenue plausible but blocked (immature, costly, needs decision) |
| **Context** | Wiki intel — no near-term monetization |
| **Pass** | No project fit, no revenue angle, or duplicate with no gap |
| **UNAVAILABLE** | 404 / deleted / unreachable |

### Anti-hallucination

- Stars / commits / issues: NOT FOUND if unverified — never estimate.
- Unverified features: CLAIMED (unverified).
- Every fit claim needs a **specific project path** or wiki page (`Projects/atto/...`, `Projects/GuruWatcher/...`, or `Desktop/family/...`).
- Every revenue claim needs a **mechanism** (MRR, P&L, conversion, ops time saved, **Atto SKU**, GuruWatcher alert edge). For **family-tree dogfood**: personal **value** is valid when revenue confidence is `none`.
- 404: UNAVAILABLE, skip deep analysis.

---

## Required output order

### Step 1 — Research plan (MANDATORY FIRST)

```
## Research plan
- URLs received: N
- URLs to evaluate this run: N (max 20)
- Deferred to next batch: [list or none]
- Batch theme: [e.g. Discord alert bots + TipDrop revenue plays]
- Evaluation order: [numbered URL list]
- Primary lens: revenue + project fit; Priority #1 = Atto; Priority #2 = GuruWatcher; everything else behind (+ wikis always)
```

### Step 2 — Per URL

```
## URL N: [repo name]

- URL: ...
- Stack: ...
- Stars / Last commit / Issues: ... / ... / ... (or NOT FOUND)

### Revenue lens
- Revenue hypothesis: ...
- Revenue confidence: high | medium | low | none
- Revenue timeline: now | 30d | 90d | speculative
- Project fit: [list projects or none — include atto and/or guruwatcher and/or family-tree when relevant]
- Integration play: standalone | combo-with-[X] | wiki-only
- Improvement: ...

- Tier: Integrate | Extract | Watch | Context | Pass | UNAVAILABLE
- Primary fit: [surface name]
- Surfaces: prod=NO osint=NO gambling=NO game=NO cyber=NO image=NO seo=NO print=NO ccc=PARTIAL tipdrop=YES
- Overlaps: tipdrop=... poker-arena=... ceminiDFS=... xsp-killer=... atto=... guruwatcher=... genealogy=... pm-canary=... wc-bot=... wc-tickets=...
- Cross-wiki routing: ...
- Active project routing: [atto | guruwatcher | xsp-killer | tipdrop | family-tree | pm-canary | wiki-only | poker-arena | ceminiDFS] (prefer #1 Atto then #2 GuruWatcher; genealogy productizable → atto)
- Combo plays: ... (or none)
- Reasoning: 2-4 sentences — path + revenue + tier

### Implementation notes (never tier drivers)
- License: [SPDX or NOT FOUND or N/A] — friction only
- Business risk: ... (or none) — TipDrop regulatory/MRR threats; Atto PII/share perimeter; GuruWatcher webhook/key hygiene
- NEEDS VERIFICATION: ... (or none)
```

### Step 3 — Aggregate summary

```
## Aggregate summary
- Integrate: N — [list + revenue why]
- Extract: N — [list + target project]
- Watch: N — [list + blocker]
- Context: N — [list]
- Pass: N — [list]
- UNAVAILABLE: N — [list]
- Revenue by project: [counts — include atto, guruwatcher, and family-tree separately]
- Combo plays: [URL → projects → mechanism]
- Genuine gaps (Extract/Integrate): [list + gap + revenue why]
- Cross-routing batch: [by wiki]
- Implementation friction: [license/business-risk notes only]
```

---

## URLs to evaluate (THIS RUN ONLY — max 20)

[PASTE UP TO 20 URLS HERE — prefix with `URLs as of YYYY-MM-DD:`]
