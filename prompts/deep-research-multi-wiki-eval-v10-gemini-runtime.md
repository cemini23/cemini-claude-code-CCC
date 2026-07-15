# Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v10)

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

Score every URL on **money / value path** (P&L, MRR, conversion, ops time saved, or family-tree personal value). License/ToS = notes only, not tier drivers.

### Priority #1 (prefer routing/tier when ties; name path when claiming fit)

- **XSP killer:** briefs `xsp-*` → `cemini-prod:/opt/cemini/briefs/` → overlap `xsp-killer` → revenue: trading P&L
- **TipDrop:** `tipdrop-workspace-kit/` + David's `cemini23/tipdrop` → overlap `tipdrop` → revenue: David's $97/mo SaaS MRR
- **Family-tree / genealogy:** `Desktop/family/` + `Desktop/family/research/` → overlap `genealogy` → value: archival depth, brick-wall breakthroughs, jure sanguinis docs (no P&L)
- **PM LP canary (K166):** `CeminiSuite/` → `cemini-prod:/opt/cemini/` (`compose.polymarket.canary.yml`, `docs/pm-lp-k166-phase1-canary.md`, briefs `pm-*`) → overlap `pm-canary` → revenue: LP rewards P&L after shadow gates
- **Wikis (always-on):** federation surfaces 2–9 + CCC — stub/route even when no Priority #1 code fit

### Also active — always score & report if research applies (tie-break after #1)

- **Poker arena:** `agents/devfun-poker-arena/examples/cemini_decide.py` → overlap `poker-arena` → revenue: arena prizes — **do not skip** poker/GTO/RL applies
- **CeminiDFS:** `CeminiDFS/src/ceminidfs/pipeline/` → overlap `CeminiDFS` → revenue: contest ROI — **do not skip** NFL/DFS/projection applies

### Ten routing surfaces (YES / PARTIAL / NO — for wiki stubs, not permission gates)

1. Cemini prod bots (**XSP Priority #1**, **PM LP canary Priority #1**, poker arena, world-cup-bot, wc-ticket-monitor)
2. OSINT wiki — **PM LP canary / Kalshi**, LP, XSP research, **genealogy methodology** (K153/K154; family-tree Priority #1)
3. Gambling wiki — retail betting, DFS, poker strategy
4. Cybersec wiki
5. Image-gen wiki
6. SEO wiki
7. 3D-printing wiki
8. Game-dev wiki — hobby game dev (castle-sim legacy — deprioritized)
9. CCC wiki — Cursor/Claude harness, MCP, skills
10. TipDrop.io — David's Discord signals SaaS (**Priority #1**)

### Shipped stacks — default Context/Pass unless named gap + revenue why

Poker arena (7 modules), ceminiDFS (pipeline stages), xsp-killer (4 modules), TipDrop kit (6 modules), **PM LP canary (K166 — shadow compose + markout kills + rebaseline)**, **genealogy (8 modules — archival ladder, Gramps/GEDCOM, FS API, Antenati IIIF, HTR, entity resolution, regional playbook, US census staging)**, world-cup-bot, wc-ticket-monitor — see full v10 canon.

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
- Every fit claim needs a **specific project path** or wiki page.
- Every revenue claim needs a **mechanism** (MRR, P&L, conversion, ops time saved). For **family-tree**: personal **value** (brick-wall breakthrough, hours saved, new generation documented) is valid when revenue confidence is `none`.
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
- Primary lens: revenue + project fit; Priority #1 = XSP + TipDrop + family-tree + PM canary (+ wikis always)
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
- Project fit: [list projects or none]
- Integration play: standalone | combo-with-[X] | wiki-only
- Improvement: ...

- Tier: Integrate | Extract | Watch | Context | Pass | UNAVAILABLE
- Primary fit: [surface name]
- Surfaces: prod=NO osint=NO gambling=NO game=NO cyber=NO image=NO seo=NO print=NO ccc=PARTIAL tipdrop=YES
- Overlaps: tipdrop=... poker-arena=... ceminiDFS=... xsp-killer=... genealogy=... pm-canary=... wc-bot=... wc-tickets=...
- Cross-wiki routing: ...
- Active project routing: [xsp-killer | tipdrop | family-tree | pm-canary | wiki-only | poker-arena | ceminiDFS] (prefer Priority #1)
- Combo plays: ... (or none)
- Reasoning: 2-4 sentences — path + revenue + tier

### Implementation notes (never tier drivers)
- License: [SPDX or NOT FOUND or N/A] — friction only
- Business risk: ... (or none) — TipDrop regulatory/MRR threats
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
- Revenue by project: [counts per project]
- Combo plays: [URL → projects → mechanism]
- Genuine gaps (Extract/Integrate): [list + gap + revenue why]
- Cross-routing batch: [by wiki]
- Implementation friction: [license/business-risk notes only]
```

---

## URLs to evaluate (THIS RUN ONLY — max 20)

[PASTE UP TO 20 URLS HERE — prefix with `URLs as of YYYY-MM-DD:`]
