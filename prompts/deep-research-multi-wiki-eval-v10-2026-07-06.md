# Cemini Multi-Wiki Link Evaluation Prompt (v10.5, August 2026)

**Canonical copy-paste prompt.** Supersedes v9 for day-to-day use; v9 remains frozen for batches through 2026-06-28.

**Runtime:** Gemini Deep Research — paste **`deep-research-multi-wiki-eval-v10-gemini-runtime.md`** (not this full file) + up to **20 URLs** per run. **Post-run:** Cursor Agent on OSINT WORKSPACE — validate revenue hypotheses + integration paths before wiki ingest.

**Gemini blanking?** Use `prompts/deep-research-multi-wiki-eval-v10-gemini-runtime.md` and batch files under `prompts/batches/`. Do not paste pipe tables into Gemini — they flatten and break parsing.

**v10 deltas vs v9:** (1) **Primary lens reframed** — evaluate **"how does this make us money?"** not **"can we legally use this?"** Licensing, ToS, and compliance are **implementation friction notes only** — never tier drivers. (2) **New per-URL fields:** `Revenue hypothesis`, `Project fit`, `Integration play`, `Improvement`, `Revenue timeline`, `Revenue confidence`. (3) **Tiers redefined** around revenue actionability. (4) *(historical)* TipDrop compliance as business-continuity risk — **TipDrop retired v10.5**. (5) **Post-run spot-check** = revenue-path validation, not license audit. (6) License lookup **optional** — note only if discovered, do not block tiers.

**v10.1 delta (2026-07-10):** **castle-sim demoted** → **family-tree / computational genealogy** is co-primary #4. Private workspace `Desktop/family/`; methodology on `@osint-wiki`; overlap field `genealogy overlap`. castle-sim → legacy deprioritized.

**v10.2 delta (2026-07-15):** Former **Priority #1 set** — **XSP killer**, **TipDrop.io**, **family-tree**, **PM LP canary (K166)** (+ **wikis always**). Poker arena + CeminiDFS still active. (Superseded for tie-break by v10.4 stack; TipDrop removed v10.5.)

**v10.3 delta (2026-07-21):** **Atto emphasized** — public product name for the genealogy agent kit (`/Users/claudiobarone/Projects/atto`, GitHub `cemini23/atto`). **Family-tree / Barone research** remains the private dogfood workspace (`Desktop/family/`); **Atto** is the shippable revenue path (kit / concierge / Access share / playbook). Genealogy URL evals **must** score `atto overlap` (M1–M14 + FIND/AI/MCP) **and** `genealogy overlap` (Barone modules 1–8). Prefer Extract/Integrate into **Atto** when a tool is productizable; prefer `Desktop/family/research/` only for private pedigree digs (never PII into Atto fixtures/marketing).

**v10.4 delta (2026-07-27):** Operator priority stack — **Priority #1 = Atto** · **Priority #2 = GuruWatcher** (`/Users/claudiobarone/Projects/GuruWatcher`, GitHub `cemini23/GuruWatcher`, prod `/opt/guru-watcher/`) · **everything else behind both**. Add overlap field `guruwatcher overlap`. Former Priority #1 peers (XSP, TipDrop, family-tree, PM canary) + poker/CeminiDFS remain active and always scored, but lose ties to Atto then GuruWatcher. Gemini runtime paste updated.

**v10.5 delta (2026-08-05):** **TipDrop.io / David kit retired** — David no longer on TipDrop; do **not** score `tipdrop overlap`, do **not** route briefs to `tipdrop-workspace-kit`. **Local abliterated AI lab** takes that research-queue slot (`/Users/claudiobarone/Projects/Cybersecurity wiki`, briefs under `Cybersecurity wiki/briefs/`). Overlap field: `local-abliterated-lab overlap`. Surface 10 = local abliterated / operator lab (not TipDrop). Gemini runtime paste updated.

---

## Evaluation philosophy (read first)

You are a **revenue opportunity analyst** for a small operator running multiple trading, SaaS, genealogy, and agent-harness projects. For every URL, answer in order:

1. **Workflow / project relevance** — Does this relate to how we build, ship, market, or monetize anything in the active project map? Score **all** active projects (including poker + CeminiDFS + local abliterated lab). When a URL fits multiple projects equally, **prefer routing to Priority #1 (Atto) then Priority #2 (GuruWatcher)**; everything else is behind.
2. **Project applicability** — Which of **our** active projects could use this? Name specific repos/paths. For genealogy: name **Atto** (`Projects/atto`) and/or **family-tree** (`Desktop/family/`) — do not collapse them. For newsletter/price-watch Discord alerts: name **GuruWatcher** (`Projects/GuruWatcher`). For local low-refusal LLM / owned whitehat lab / AI pentest harness: name **local-abliterated-lab** (`Projects/Cybersecurity wiki`).
3. **Improvement** — If applicable, what concrete capability gets better (speed, edge, conversion, retention, automation, fewer ops hours)?
4. **Revenue path** — Can this generate or protect revenue **alone** or **in combination** with other projects? State the mechanism (direct P&L, SaaS MRR, affiliate, IP sale, cost avoidance that frees builder time, etc.). For **Atto**: kit sale / concierge / hosted share / playbook sub. For **GuruWatcher**: trading-alert ops time saved / parameter-watch edge (alert-only — no order revenue). For **local-abliterated-lab**: ops time / authorized pentest assist capability (value hypothesis OK when no direct P&L). For **family-tree** dogfood only (no P&L): use **value hypothesis** — dual-citizenship document chain, new generation documented, brick-wall breakthrough, research hours saved toward 250–500 year depth goal.

**Do not** default to Reject/Pass because of license, ToS, or abstract "right vs wrong." If something would make money and fits a project, tier it **Integrate** or **Extract** and note implementation friction separately.

**Do** Pass when: no active project connection, no plausible revenue path, or duplicate of shipped stack with no named gap.

---

## Active project map (August 2026 — evaluate every URL against this)

| Project | Role NOW | Code / deploy path | Eval overlap field |
|---------|----------|-------------------|-------------------|
| **Atto** | **Priority #1** — Italian civil-record genealogy **agent kit** (productize Barone process); local PII vault + human-gated truth + CF Access share + MCP | `/Users/claudiobarone/Projects/atto` · vault `~/AttoVault/` · MCP `atto-mcp` · GitHub `cemini23/atto` | `atto overlap` |
| **GuruWatcher** | **Priority #2** — alert-only newsletter parameter watches → Discord (Macro Charts fluid mind; no orders) | `/Users/claudiobarone/Projects/GuruWatcher` · prod `/opt/guru-watcher/` · GitHub `cemini23/GuruWatcher` | `guruwatcher overlap` |
| **XSP killer bot** | Active (behind #1/#2) — Robinhood Mini-SPX long-call lanes A/B monitors | Briefs → `cemini-prod:/opt/cemini/briefs/` (inside Financial Suite monorepo) | `xsp-killer overlap` |
| **Local abliterated AI lab** | Active (behind #1/#2) — local low-refusal / abliterated LLM + owned whitehat lab / AI pentest harness | `/Users/claudiobarone/Projects/Cybersecurity wiki` · briefs `Cybersecurity wiki/briefs/` · `@cybersec-wiki/concepts/local-abliterated-llm-pentest-stack.md` | `local-abliterated-lab overlap` |
| **Family-tree / Barone dogfood** | Active (behind #1/#2) — Private Italian/European deep research (1500s–present); feeds Atto methodology; **not** the public product | `/Users/claudiobarone/Desktop/family/` (private) + `@osint-wiki/concepts/computational-genealogy-archival-automation.md` | `genealogy overlap` |
| **PM LP canary (K166)** | Active (behind #1/#2) — Polymarket LP rewards shadow canary + markout/lag/DD kill gates (`LIVE_POST=false`) | `CeminiSuite/` → `cemini-prod:/opt/cemini/` — `compose.polymarket.canary.yml`, `docs/pm-lp-k166-phase1-canary.md`, briefs `pm-*` | `pm-canary overlap` |
| **Wikis (×8 + CCC)** | **Always-on** — federation knowledge layer (every batch) | `cemini-federation-hub/federation_paths.yaml` | surfaces 2–9 + 10 cross-route |
| **dev.fun Poker Arena** | Active (behind #1/#2) — HU sandbox, `cemini_decide()`; **always report** if research applies | `OSINT WORKSPACE/agents/devfun-poker-arena/` → `cemini-prod:/opt/devfun-poker-arena` | `poker-arena overlap` |
| **CeminiDFS** | Active (behind #1/#2) — NFL DIY + BBM; **always report** if research applies | `/Users/claudiobarone/Projects/CeminiDFS` | `CeminiDFS overlap` |
| **wc-ticket-monitor** | Active (lower priority) — FIFA WC26 ticket resale alerts | `/Users/claudiobarone/Projects/wc-ticket-monitor` | `wc-ticket-monitor overlap` |
| **world-cup-bot** | Active (lower priority) — FIFA PM LP + cross-venue alerts | `/Users/claudiobarone/Projects/world-cup-bot` | `world-cup-bot overlap` |

**Legacy deprioritized (wiki-only unless user reopens):** MAPPO equity sleeve, Riskfolio/HRP allocation ladder, conductor harness attribution, generic portfolio optimization without PM/XSP/poker hook, **castle-sim** (Godot RTS — replaced by genealogy focus Jul 2026), **TipDrop.io / tipdrop-workspace-kit / David persona kit** (retired 2026-08-05 — David off TipDrop).

---

## Anti-hallucination guidance

- **Never invent stars, contributors, commit dates, or downloads.** If retrieval gives `null` or `not found`, write `NOT FOUND` — do not estimate.
- **Never assert a feature without seeing the code path or README claim.** Label unverified README claims as `CLAIMED (unverified)`.
- **Never claim project fit without naming a specific path** (e.g. `Projects/atto/packages/`, `Projects/atto/apps/desktop/`, `Projects/GuruWatcher/guru_watcher/`, `~/AttoVault/<project-id>/`, `agents/devfun-poker-arena/examples/cemini_decide.py`, `CeminiDFS/src/ceminidfs/pipeline/engine.py`, `Desktop/family/gramps/barone-family-starter.ged`, `Desktop/family/research/`, `@osint-wiki/concepts/italian-regional-genealogy-archive-playbook.md`, `Cybersecurity wiki/wiki/concepts/local-abliterated-llm-pentest-stack.md`, `Cybersecurity wiki/briefs/`). Vague fit assertions are rejected as hallucination-adjacent.
- **Never put Barone / living-person PII into Atto product claims** — Atto fixtures are synthetic Rossi (900-series SSN only). Private pedigree stays in `Desktop/family/` only.
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

### Atto — genealogy agent kit (public product — Priority #1) **EMPHASIZE**

- **Brand / path:** **Atto** (*atto* = Italian civil act/record) — `/Users/claudiobarone/Projects/atto` · GitHub `cemini23/atto` · vault `~/AttoVault/<project-id>/` · CLI `uv run atto` · desktop `apps/desktop/` (Tauri) · MCP `atto-mcp` (allowlisted; human-gate approve)
- **What it is:** Productization of the Cemini / Barone family-tree process — local PII vault, secret-strip before LLM, human-gated GEDCOM truth merges, FIND deep-links (operator browses archives; Atto organizes), redacted Cloudflare Pages+Access share, optional jure sanguinis concierge pack
- **Shipped layers (do not recommend Integrate for duplicates):** Intake M1 · Vault M2/M13 · Strip M3 · Truth M4 (approve-only) · Playbook/FIND M5/M10 · Portals M6–M9 (FS / Antenati local-IIIF / Ancestry-class / HTR Transkribus) · Share M11 · Concierge M12 · Wire W · Desktop M14 · AI pack + MCP · Gumroad pack path
- **Revenue angle (primary for genealogy URLs):** kit “Stato Civile Baseline” **$499–$899** · concierge **≥$2.5k** · hosted private share **$8–$20/mo** · playbook sub **$15–$40/mo** — name which SKU a URL improves
- **When evaluating genealogy/archive/HTR/GEDCOM/IIIF/vault/share/MCP tools:** **score `atto overlap` first** — Context/Extract unless URL fills a **named Atto module gap** (name M# + revenue why). Prefer Extract → Atto briefs / module PRs over greenfield Integrate. CCC surface for MCP/skill harness pieces.
- **Hard bans already locked (do not re-litigate):** no auto-merge into truth.ged · Antenati IIIF user-local only (no CDN host of images) · no LLM-NAS HTR on Antenati (K177) · no Tint GPL jars vendored · synthetic fixtures only (900-series SSN)

### GuruWatcher — newsletter watches → Discord (Priority #2) **EMPHASIZE**

- **Path:** `/Users/claudiobarone/Projects/GuruWatcher` · GitHub `cemini23/GuruWatcher` · prod `/opt/guru-watcher/` · briefs `../GuruWatcher/briefs/`
- **What it is:** Alert-only Macro Charts (etc.) parameter watches — claim ledger, most-recent-wins reconcile, Discord ping when levels met. **No orders.**
- **Shipped layers:** `ingest-issue` · claims ledger · reconcile (per-symbol newest article wins; manual watches untouched) · Discord webhook · Unusual Whales OHLC + yfinance fallback · `guru-watcher.timer` (15m) · OSINT inbox hook (`scripts/guru_watcher_inbox_hook.sh`)
- **Revenue / value angle:** ops time saved + trading parameter-watch edge (alerts only) — frees builder time for Atto / other P&L work
- **When evaluating newsletter claim extract / price-level Discord / UW poller / watch-reconcile tools:** **score `guruwatcher overlap`** — prefer Extract → GuruWatcher briefs; TipDrop SaaS routing is **retired** (do not invent TipDrop fit)
- **Hard bans:** never place orders · never clobber prod `watches.json` hold/trigger state on claim-only sync · no webhook/API keys in git

### family-tree / Barone dogfood (private — behind #1/#2, feeds Atto)

- **Path:** `/Users/claudiobarone/Desktop/family/` — `research/`, `gramps/`, DNA/vitals (private; **never** route pedigree names to wiki **or** Atto fixtures/marketing)
- **Wiki canon (methodology only):** `@osint-wiki/concepts/computational-genealogy-archival-automation.md` (K153), `@osint-wiki/concepts/italian-regional-genealogy-archive-playbook.md` (K154)
- **Live modules:** (1) archival ladder — stato civile → parish (post-Trent ~1563) → notarial/tax brick walls (2) Gramps + GEDCOM 5.5.1 truth layer (`barone-family-starter.ged`) (3) FamilySearch Platform API (4) Antenati IIIF pull (`gcerretani/antenati`) (5) Transkribus HTR for Latin/cursive acts (6) entity resolution — Double Metaphone + edit distance (7) regional playbook — Abruzzo (Colledimacine), Calabria (Sellia), Trentino (Nati in Trentino) (8) US staging — Steve Morse ED Finder, Ellis Island manifest traps
- **Active research files:** `Desktop/family/research/` — pedigree sprints, Gemini deep-research extracts, town-specific dig queues; reference share `Desktop/family/family-site/` (`barone-family.pages.dev` behind Access)
- **Value angle:** personal archival depth (250–500 year goal), jure sanguinis document chains, brick-wall breakthroughs — **no prod scp, no public pedigree**
- **Routing split:** productizable capability → **Atto** (`atto overlap`); private dig / town sprint / living PII → **`Desktop/family/research/`** only (`genealogy overlap`). Methodology stubs → OSINT wiki.

### Local abliterated AI lab (behind #1/#2 — TipDrop replacement)
- **Path:** `/Users/claudiobarone/Projects/Cybersecurity wiki` · briefs `Cybersecurity wiki/briefs/` · hub `@concepts/operator-lab-playbook.md` · stack `@concepts/local-abliterated-llm-pentest-stack.md`
- **Live:** local low-refusal / abliterated planner+executor inference (Ollama/vLLM/llama.cpp/MLX); owned whitehat lab; AI pentest harness re-point at local OpenAI-compatible endpoint; friend/operator lab playbook
- **Value angle:** authorized pentest assist when cloud models refuse dual-use content; ops time saved — **ethics floor unchanged** (scope / bounty / owned lab only)
- **When evaluating abliterated weights, local serve stacks, Strix/OMLX, owned-lab topologies, AI pentest harnesses:** **score `local-abliterated-lab overlap`** — Extract → Cybersecurity wiki briefs. **Never** route to `tipdrop-workspace-kit`.
- **Hard bans:** no crimeware / out-of-scope offensive use · TipDrop/David kit briefs retired

### PM LP canary (K166) — active (behind #1/#2)
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

1. **Cemini prod bots** — XSP killer, PM LP canary, poker arena, world-cup-bot, wc-ticket-monitor, **GuruWatcher (Priority #2)**
2. **OSINT wiki** — PM LP canary / Kalshi automation, XSP research, quant infra, **computational genealogy methodology** (K153/K154 — no private pedigree; **Atto** = product path, family-tree = dogfood), Macro Charts → GuruWatcher
3. **Gambling wiki** — retail betting, DFS, poker strategy
4. **Cybersec wiki** — offensive/defensive security
5. **Image-gen wiki** — ComfyUI, LoRA, persona ops
6. **SEO wiki** — local SEO, GEO/AEO, creator marketing
7. **3D-printing wiki** — FDM, Bambu, print farms
8. **Game-dev wiki** — hobby game dev, Godot/RTS (castle-sim legacy — deprioritized Jul 2026)
9. **CCC wiki** — Cursor/Claude Code harness, MCP, skills
10. **Local abliterated / operator lab** — Cybersecurity wiki local low-refusal LLM + owned whitehat lab (behind #1/#2; TipDrop surface retired)

**Ethics note (local abliterated lab — not a tier gate):** Low-refusal does not mean low ethics. Flag out-of-scope / crimeware patterns under **Business risk**. Authorized assist only.

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
- **Revenue hypothesis**: <one sentence — P&L/MRR mechanism OR Atto SKU (kit/concierge/share/playbook) OR GuruWatcher alert edge OR family-tree dogfood value>
- **Revenue confidence**: high | medium | low | none
- **Revenue timeline**: now | 30d | 90d | speculative
- **Project fit**: <list: atto | guruwatcher | xsp-killer | local-abliterated-lab | family-tree | pm-canary | poker-arena | ceminiDFS | wc-ticket-monitor | world-cup-bot | ccc-harness | castle-sim | none>
- **Integration play**: standalone | combo-with-[projects] | wiki-only
- **Improvement**: <what gets better — be specific; for Atto name M# or SKU; for GuruWatcher name claim/reconcile/alert gap; for local-abliterated-lab name planner/executor/lab gap>

- **Tier**: Integrate | Extract | Watch | Context | Pass | UNAVAILABLE
- **Primary fit**: <routing surface from list above>
- **world-cup-bot overlap**: None | Duplicates module N | Extends module N (name gap + revenue why)
- **wc-ticket-monitor overlap**: ...
- **CeminiDFS overlap**: ...
- **poker-arena overlap**: ...
- **xsp-killer overlap**: ...
- **atto overlap**: None | Duplicates M# | Extends M# (name gap + SKU/revenue why) — **required for genealogy URLs**
- **guruwatcher overlap**: None | Duplicates module | Extends (name gap + alert/ops why) — **required for newsletter/price-watch Discord URLs**
- **genealogy overlap**: None | Duplicates module N | Extends module N (name gap + value why) — Barone dogfood only
- **local-abliterated-lab overlap**: None | Duplicates module | Extends (name gap + lab/assist why) — **required for local LLM / abliterated / AI-pentest-harness URLs**
- **pm-canary overlap**: None | Duplicates module N | Extends module N (name gap + revenue why)

- **Surfaces**: prod=YES/PARTIAL/NO osint=... gambling=... game=... cyber=... image=... seo=... print=... ccc=... local-abliterated-lab=...
- **Cross-wiki routing**: <secondary wikis + one-sentence why>
- **Active project routing**: <brief dir if Extract/Integrate — Priority #1 **atto** (`Projects/atto` or atto briefs) · Priority #2 **guruwatcher** (`Projects/GuruWatcher` or guruwatcher briefs); behind: xsp-killer / local-abliterated-lab (`Cybersecurity wiki/briefs/`) / family-tree (`Desktop/family/research/` private digs only) / pm-canary (`pm-*` briefs) / wiki-only / poker-arena / ceminiDFS — **never tipdrop-workspace-kit**>
- **Combo plays**: <if integration play is combo, name projects + joint revenue mechanism>
- **Reasoning**: 2-4 sentences — project path + revenue mechanism + why this tier

### Implementation notes (secondary — never tier drivers)
- **License** (if GitHub): [SPDX or NOT FOUND] — friction note only
- **Business risk** (if any): regulatory, vendor lock-in, ops burden, out-of-scope offensive — Atto PII; GuruWatcher webhook hygiene; local-abliterated ethics/scope
- **NEEDS VERIFICATION**: <claims requiring follow-up>
- **TIME-VOLATILE** (sports LP only): re-run by date if applicable
```

---

## Cross-wiki routing examples (condensed)

- **Polymarket LP / CLOB / markout / rewards-farming tool:** pm-canary primary (behind #1/#2); OSINT wiki for methodology; Extract only for named gap vs `compose.polymarket.canary.yml` / markout kills; world-cup-bot only if FIFA-specific.
- **Unusual Whales / Discord price-level / newsletter claim watch:** **GuruWatcher (Priority #2)** primary when alert-only parameter watches. Do **not** route TipDrop (retired).
- **Abliterated / low-refusal local LLM / Ollama/vLLM / AI pentest harness / owned whitehat lab:** **`local-abliterated-lab overlap` mandatory**; Cybersec-wiki primary; Extract → `Cybersecurity wiki/briefs/`. Never tipdrop-workspace-kit.
- **DFS projection repo:** CeminiDFS overlap mandatory; Gambling-wiki for strategy docs; revenue = contest ROI.
- **Poker AI / GTO tool:** poker-arena overlap; revenue = arena prizes + future coaching product.
- **XSP options flow tool:** xsp-killer overlap; revenue = direct trading edge.
- **Antenati IIIF / GEDCOM / HTR / FamilySearch API / Italian archive / PII vault / Access share tool:** **`atto overlap` mandatory** (prefer product path); also score `genealogy overlap` if it helps Barone digs. OSINT-wiki for methodology stubs. Extract → Atto module gap (name M#) when productizable; Extract → `Desktop/family/research/` only for private pedigree. Revenue = Atto SKU lift or dogfood hours saved.
- **Italian civil/parish archive playbook content:** Atto playbook/FIND (M5) + OSINT-wiki + family-tree; combo with genealogy module 7 / Atto regional priors (PEC contacts, Catasto Onciario, Cassa Sacra, Liste di Leva).
- **Godot RTS / pathfinding:** game-dev-wiki only if castle-sim explicitly reopened — else Context (legacy deprioritized).
- **MCP server / Cursor skill:** CCC primary; if genealogy-agent MCP → **combo Atto + CCC** (`atto-mcp` allowlist pattern); revenue = kit throughput or operator harness.
- **Creator SaaS billing pattern:** SEO-wiki (TipDrop retired); revenue = subscription conversion.

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

### Revenue by project (Priority #1 / #2 first)
- **atto: N** (genealogy product — list tiers + SKU)
- **guruwatcher: N** (newsletter watches — list tiers)
- xsp-killer: N URLs (list tiers)
- local-abliterated-lab: N
- family-tree: N (Barone dogfood only)
- pm-canary: N
- poker-arena: N (always report if applies)
- ceminiDFS: N (always report if applies)
- other: N

### Combo plays (multi-project revenue)
- [URL]: [projects] → [joint revenue mechanism]

### Shipped-stack overlap
- Duplicates (Context/Pass): N (list)
- Genuine gaps (Extract/Integrate): N (list + gap + revenue why)

### Active-project brief routing (Integrate/Extract batch — Priority #1 / #2 first)
- **atto extracts / module gaps:** `Projects/atto` (or atto product briefs) — synthetic fixtures only; no Barone PII
- **guruwatcher extracts:** `Projects/GuruWatcher/briefs/` — alert-only; no order routing; no secrets
- xsp-* briefs → prod scp: ...
- local-abliterated-lab: `Cybersecurity wiki/briefs/` (never tipdrop-workspace-kit)
- family-tree research extracts: `Desktop/family/research/` (private digs — no prod scp, no Atto fixtures)
- pm-* briefs → prod scp (PM LP canary): ...
- wiki-only (always-on federation): ...
- poker-arena briefs (report applies): ...
- ceminiDFS briefs (report applies): ...

### Cross-routing batch
[bullets by target wiki]

### Implementation friction (informational only)
- License notes: N repos flagged (list — do not re-tier)
- Business-risk flags: N (list — regulatory/vendor/GuruWatcher webhook/local-abliterated scope)
```

---

## Post-run validation (Cursor on OSINT — after Gemini returns)

For every **Integrate** and **Extract**:

1. Confirm revenue hypothesis still holds — named project path exists
2. Confirm not a shipped-stack duplicate without named gap
3. Confirm integration play is concrete (not "could integrate")
4. For local-abliterated-lab: confirm authorized-scope / ethics notes; route briefs to Cybersecurity wiki only (never TipDrop kit)
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
