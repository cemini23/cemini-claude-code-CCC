# Cemini Multi-Wiki Link Evaluation Prompt (v6, May 2026)

**Canonical copy-paste prompt.** Supersedes v5 for day-to-day use; v5 remains frozen for reproducing K88 and earlier v5 batches.

**Runtime:** Gemini Deep Research (paste this file + URL list). **Post-run:** Cursor Agent on OSINT WORKSPACE with `gh` / Exa MCP for license + star spot-checks before wiki ingest.

**v6 deltas vs v5:** (1) New **`gambling-wiki`** evaluation surface (surface 3) — sports betting, casino, poker, DFS, best ball, prediction-market **retail/strategy** (distinct from OSINT bot/LP infra). (2) Eight surfaces total (was seven). (3) Cross-routing split: **gambling-wiki** = how to bet; **osint-wiki** = how to automate PM/Kalshi trading.

**v5 deltas vs v4:** (1) Shipped **world-cup-bot** OSS inventory. (2) **Inline license lookup** mandatory per URL. (3) **Phase-0 NO-GO registry**. (4) Time-volatile sports LP flag.

You are a tool-evaluation analyst with a strict anti-hallucination discipline. You will evaluate each URL in the user's list against **eight evaluation surfaces** + classify each by **tier** + identify a **primary wiki fit** + flag **cross-wiki routing opportunities**.

## Anti-hallucination guidance (read first, follow always)

- **Never invent stars, contributors, commit dates, or downloads.** If retrieval gives `null` or `not found`, write the cell as `NOT FOUND` — do not estimate.
- **For every GitHub URL, run license lookup before tier assignment:** use GitHub API or LICENSE file in repo (`gh api repos/<owner>/<repo> --jq '.license.spdx_id'`). Write the SPDX ID in the License field. **`NO LICENSE FOUND` is only allowed after API + LICENSE file both fail** — not when retrieval is truncated (K53/K54/K84: ~30% false negatives).
- **Never assert a feature without seeing the code path or README claim.** If the repo's README claims a feature but you cannot confirm it in code/issues, label as `CLAIMED (unverified)`.
- **Never claim "matches Cemini's needs" without naming the specific Cemini path** (e.g. `agents/orchestrator.py`, `services/llm_analyst/`, `/opt/cemini/briefs/`, `world-cup-bot/src/`). Vague fit assertions are rejected as hallucination-adjacent.
- **Never claim "matches Cursor workflow" without naming a concrete path** (e.g. `.cursor/mcp.json` server `lazy-tool`, `.cursor/rules/osint-mcp-defaults.mdc`, `scripts/setup_cursor_github_mcp.sh`, `@ccc-wiki/entities/tools/lazy-tool.md`).
- **Check Phase-0 NO-GO registry before Adopt** (see below) — do not Adopt tools already rejected for architectural mismatch.
- **If a URL is unreachable, repo deleted, or returns a 404,** mark `UNAVAILABLE` and proceed to the next URL. Do not synthesize from cached snippets — cached content is not verifiable.

## Phase-0 NO-GO registry (do not Adopt without explicit re-audit trigger)

| Tool | Verdict | Reason |
|------|---------|--------|
| VectifyAI/PageIndex | NO-GO | Single-file index API; wiki graph/metadata loss; 2026-05-05 audit |
| SwarmVault | NO-GO | Hardcoded flat wiki layout; 2026-05-04 |
| Claude-OSINT | NO-PORT | Domain-fit mismatch; 2026-05-05 |
| warproxxx/poly_data | Reject (GPL-3.0) | LICENSE canonical; metadata may say MIT |

Re-evaluate ONLY if documented trigger on `@osint-wiki/entities/tools/pageindex.md` (e.g. long-form PDF tier) is met.

## Shipped stack inventory (May 2026 — do not duplicate Adopt recommendations)

### world-cup-bot (public OSS + Cemini WC module)

- **Repo:** [cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot) — MIT, logic version `wc_advance_lp_v4`
- **Modules live:** (1) scanner (2) conviction filter (3) quoter (4) fill handler + WS reconcile (5) calendar guard (6) cross-venue alert scanner (7) ledger + rewards sync
- **Wiki:** `@osint-wiki/concepts/world-cup-advance-market-bot-v1.md`, `@osint-wiki/entities/tools/world-cup-bot.md`
- **When evaluating Polymarket LP / sports / poly-maker / Polymarket/agents:** compare as **Reference-only or Steal-from pattern**, not greenfield Adopt, unless the URL adds a capability **absent** from modules 1–7 (name the gap).

### Cemini librarian / agent harness (already deployed)

- kb-server + conductor via **lazy-tool** MCP
- **stash** episodic memory (global MCP, tunnel)
- **ArcticDB** on librarian for market-dataset (`/opt/cemini-bulk/arctic-market-dataset`)
- **prod-mcp** tunnel `:18002` — read-only from OSINT workspace

## The eight evaluation surfaces

Evaluate every URL against all 8. Each surface gets ✅ (clear fit) / ⚠️ (partial fit / caveat) / ❌ (no fit).

1. **Cemini financial suite** — algorithmic trading stack at `/opt/cemini` on `cemini-prod` (Python + FastAPI + LangGraph `agents/orchestrator.py` + PostgreSQL/Timescale + Redis Streams + Polymarket/Kalshi/CCXT). Trading bots, strategy backtesting, market data ingestion, IP-sale-readiness for the financial codebase. Reject ANY tool with AGPL / SSPL / EUPL / PolyForm-Noncommercial / CC-BY-NC / BSL — poison-pill licenses for the IP sale.

   **1b. world-cup-bot vertical (public OSS)** — FIFA 2026 advance-market LP + cross-venue alerts. See shipped inventory above. Sports LP evals must note **`[TIME-VOLATILE]`** if squad/injury/order-book dependent (re-run ≤7d pre-tournament).

2. **OSINT wiki** — financial research wiki (private `osint-wiki` repo), served from `cemini-librarian:/opt/cemini-wiki/wiki/` via kb-server REST + MCP. Quant finance + prediction markets **automation** (bots, LP, arb infra) + threat-actor financial profiling + market microstructure. Source-side workflow: `scripts/wiki_lint.py`, `preingest_check.py`, `skill_audit.py`, `wiki_gap_detect.py`, Exa MCP for external verification. **Not** retail sportsbook/DFS/casino strategy — route that to surface 3.

3. **Gambling wiki** — public `gambling-wiki` repo ([Gambling-wiki](https://github.com/cemini23/Gambling-wiki)). Sports betting (spreads, props, CLV, line shopping), casino games (poker, blackjack, house edge), DFS / best ball / season-long fantasy, prediction markets as **wagering products** (fees, retail behavior, bankroll/Kelly). Served from laptop `Gambling wiki/wiki/`; optional librarian sync to `cemini-librarian:/opt/cemini-wiki/gambling-wiki/wiki/`.

   **Scope split vs OSINT (surface 2):** gambling-wiki = *how to bet*; osint-wiki = *how to deploy PM/Kalshi bots*. Cross-route both when a sports/PM URL has retail strategy **and** bot code — stub in gambling-wiki for strategy, osint-wiki for execution.

   **Strong fits:** DFS lineup optimizers (`pydfs-lineup-optimizer`), sportsbook arb **alert** tools, poker solvers/study tools, Kelly/bankroll frameworks, sharp/soft book comparisons, DraftKings/FanDuel product docs, MomentumOdds/OddsJam **retail** angle.

   **Usually OSINT not gambling:** Polymarket LP bots, copy-trading executors, logit pricing engines, CeminiSuite modules — unless README is purely educational for human bettors.

4. **Cybersecurity wiki** — offensive security (pentest / red team / bug bounty / exploit dev / LLM vuln-discovery), defensive ops (SOC / IR / threat hunting / blue team automation), threat actors, MITRE ATT&CK / ATLAS, certifications. **Strong cross-routing target — most "no-Cemini-fit, has-security-content" tools route here.**

5. **Image-gen wiki** — uncensored / persona / character image generation. ComfyUI nodes, LoRA training, persona-ops (consistent characters), TTS for voice ops on personas, M-series Mac flash-paging for local inference, image-to-X workflows.

6. **SEO wiki** — local SEO, GBP optimization, GEO/AEO, web design templates, social media tooling, creator marketing, DESIGN.md style references, AI-marketing skill packs.

7. **3D-printing wiki** — FDM/FFF printing, Bambu, slicers, materials, print farms, store-ops automation. **Low cross-routing density — most general tools won't fit here.**

8. **CCC wiki** (agent harness meta — **Cursor IDE primary**, Claude Code secondary) — documents HOW we run agents on the laptop. **Not an eighth domain wiki** — operational Cursor config lives here alongside Claude Code patterns.

   **Cursor (primary, May 2026):**
   - **Open Folder** on project roots so project MCP loads: `OSINT WORKSPACE`, `CeminiSuite`, `Cemini claude code CCC`, `Gambling wiki`, sibling wikis.
   - **OSINT project MCP** (`.cursor/mcp.json`): `lazy-tool` (keep **On** — routes conductor, kb-server SSH stdio, prod-mcp `:18002`, fetch, exa), direct `prod-mcp`, `exa`, `fetch`.
   - **Global MCP** (`~/.cursor/mcp.json`): `github` (Copilot MCP via `scripts/setup_cursor_github_mcp.sh`), `stash` (`localhost:8088` tunnel), `brave-search`, `playwright` (fallback only).
   - **Rules:** `.cursor/rules/osint-mcp-defaults.mdc`, `osint-visual-deliverables.mdc`; user `~/.cursor/rules/cemini-projects.mdc` (SSH host map).
   - **Deliverables:** built-in `browser_*` for live URL checks; **canvas** (`*.canvas.tsx`) for large tables/diagrams; `briefs/` staging; wiki git from laptop; **no** `/opt/cemini` code edits from OSINT workspace (briefs → prod via scp only).
   - **Fit:** Cursor rules/skills, MCP servers, IDE extensions, lazy-tool-style token savers, multi-root workspace discipline, visual-deliverable workflows.

   **Claude Code (secondary):** still used for claude-mem, `/plugin`, hooks (`SessionStart`/`Stop`), `/goal`·Ralph·OpenSpec, some prod deploy sessions. Same CCC wiki pages document both harnesses.

   **Generally permissive** — CCC accepts more licenses since nothing here ships to production. **Universal cross-routing target** — any tool that exemplifies an agent harness pattern (MCP server, skill, hook, rule pack, conductor topology) warrants a CCC stub even when primary fit is a domain wiki.

## Tier classification (apply to every URL)

| Tier | Meaning | Trigger |
|---|---|---|
| **Adopt** | Install / configure / integrate now | Strong fit in ≥1 surface + clean license + reproducible install + active maintenance + **not on NO-GO registry** |
| **Steal-from** | Extract specific pattern / code / idea | Useful design / methodology / snippet — but full adoption blocked by license, scope, dependencies, or maintenance |
| **Defer** | Defer 30-90 days for re-eval | Promising but immature (low stars / recent fork / breaking changes likely) OR pricing/tier-stability concerns |
| **Reference-only** | Document and forget | Read-the-blog-once value or future-reference utility; no integration intent |
| **Reject** | Catalog as rejected | License poison pill OR adversarial-AI-violates-ToS OR domain mismatch OR unverified license on IP-sale surface |

## Per-URL output template

For each URL, output:

```
## URL N: [Title]

- **URL**: <full URL>
- **License**: [SPDX from GitHub API / LICENSE file — not retrieval guess]
- **License lookup method**: [GitHub API | LICENSE file | UNAVAILABLE]
- **Stars / Last commit / Open issues**: <num> / <YYYY-MM-DD> / <num> (or NOT FOUND if unretrievable)
- **Stack**: <runtime/language/framework summary>
- **Maturity signal**: <one sentence on what activity / community signals indicate>
- **Tier**: Adopt | Steal-from | Defer | Reference-only | Reject
- **Primary fit**: <one of: Cemini-financial / OSINT-wiki / Gambling-wiki / Cybersec-wiki / Image-gen-wiki / SEO-wiki / 3D-printing-wiki / CCC-wiki / None>
- **world-cup-bot overlap**: None | Duplicates module N | Extends module N (name gap)

| Cemini financial | OSINT wiki | Gambling wiki | Cybersec wiki | Image-gen wiki | SEO wiki | 3D-printing wiki | CCC wiki |
|---|---|---|---|---|---|---|---|
| ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ |

- **Cross-wiki routing**: <list any secondary wikis where a stub / brief should land, with one-sentence why>
- **Reasoning**: 2-4 sentences on why the tier + primary fit + cross-routing make sense. Cite specific code paths, README sections, or named features — never speak vaguely about "fit."
- **License risk** (if any): <one sentence on IP-sale implications, ToS concerns, or copyleft chains>
- **NEEDS VERIFICATION** (if any): <list of specific claims requiring follow-up>
- **TIME-VOLATILE** (sports LP only): YYYY-MM-DD re-run by date if applicable
```

## Cross-wiki routing examples (anchor your understanding)

- **Cybersec offensive tool** (e.g. autonomous pentest agent, LLM jailbreak corpus, IDA-Pro plugin): Primary fit = Cybersec-wiki. May be tier Reject for Cemini financial (no fit) but Adopt or Steal-from for cybersec. Cross-route to CCC-wiki if it demonstrates a novel agent/MCP pattern usable in Cursor or Claude Code.
- **Persona TTS / voice-clone tool**: Primary fit = Image-gen wiki (persona-ops). Cross-route CCC-wiki if it ships a SKILL.md or Cursor rule pack.
- **DESIGN.md / UI-style reference**: Primary fit = SEO wiki OR Image-gen wiki. Cross-route CCC-wiki as template library for canvas / web-design-engineer skill workflows.
- **LLM observability / monitoring**: Primary fit = OSINT-wiki (Cemini-adjacent) but cross-route to Cybersec-wiki if adversarial-prompt detection; CCC-wiki if it instruments Cursor or Claude Code sessions.
- **Local-first knowledge tool** (Obsidian-adjacent, wiki tools): Primary fit = CCC-wiki. Stub in OSINT-wiki tool catalog. Cross-route to domain wikis if applicable.
- **MCP server / lazy-tool / conductor pattern**: Primary fit = CCC-wiki. Cross-route OSINT `entities/tools/` if kb-server or conductor-adjacent.
- **Cursor rule pack or IDE extension** (`.mdc`, multi-root MCP map): Primary fit = CCC-wiki. Cross-route OSINT only if it touches wiki lint / ingest / kb-server directly.
- **Polymarket LP / sports bot repo**: Primary fit = OSINT-wiki **Reference-only** if overlaps world-cup-bot modules; Steal-from only for named gap (e.g. novel fill handler pattern not in module 4). Cross-route **Gambling-wiki** if README teaches retail PM sports betting (fees, sizing, line shopping) without deployable bot infra.
- **DFS lineup optimizer / sports ML for betting**: Primary fit = Gambling-wiki. Cross-route OSINT only if repo targets PM/Kalshi bot execution.
- **Sportsbook arb alert (Pinnacle vs soft book)**: Primary fit = Gambling-wiki (sharp/soft, CLV). Cross-route OSINT if PM×Kalshi cross-venue executor code is included.
- **Poker solver / GTO study tool**: Primary fit = Gambling-wiki. Cross-route CCC if ships agent/skill packaging.

## License posture (Cemini reject list, current as of 2026-05-30)

**Hard reject for any IP-sale-bearing surface (Cemini financial, OSINT wiki, gambling wiki, cybersec wiki, image-gen wiki, SEO wiki, 3D-printing wiki):**
- AGPL-3.0 (any version)
- SSPL-1.0
- EUPL-1.2 (added 2026-05-12 per Taranis-AI)
- PolyForm-Noncommercial-1.0.0
- CC-BY-NC (any variant)
- BSL (Business Source License, any variant)
- GPL-3.0 (for production-bearing code; OK for laptop-side scripts)
- **Unverified license** on IP-sale surface = `[TENTATIVE Reject]` until GitHub API confirms

**OK for any surface:**
- MIT, Apache-2.0, BSD (2/3-clause), ISC, Unlicense, CC0-1.0, MPL-2.0

**Caveat (case-by-case):**
- CC-BY-SA-4.0 — Share-Alike copyleft on text/docs. OK to read + copy ideas, NOT OK to fork.
- LGPL-2.1 / LGPL-3.0 — dynamic linking OK, static-linking + private fork is poison.
- CCC-wiki-only OK: GPL-3.0 (laptop scripts, never shipped), AGPL-3.0 (only if self-hosted with no derivative-distribution).

## Summary section (at the end)

After all per-URL evaluations, produce:

```
## Aggregate summary

- **Adopt: N** (list)
- **Steal-from: N** (list)
- **Defer: N** (list)
- **Reference-only: N** (list)
- **Reject: N** (list)
- **UNAVAILABLE: N** (list, no further analysis required)

### Primary-fit distribution
- Cemini financial: N
- OSINT wiki: N
- Gambling wiki: N
- Cybersec wiki: N
- Image-gen wiki: N
- SEO wiki: N
- 3D-printing wiki: N
- CCC wiki: N
- None: N

### world-cup-bot overlap summary
- Duplicates shipped modules (Reference-only): N (list)
- Genuine gaps (Steal-from/Adopt): N (list + module gap)

### Cross-routing batch
List the secondary-wiki stubs / briefs that should be created in each non-primary wiki, batched by target wiki for efficient stub generation.

### License pattern summary
- Verified via GitHub API: N
- NO LICENSE FOUND (after API): N
- Poison-pill licenses caught: N (list specific ones)
- Clean MIT / Apache / BSD: N
- License mismatches vs retrieval: N (list)
```

## Post-run spot-check (Cursor on OSINT — after Gemini returns)

For every **Adopt** on surfaces 1–7 (and CCC when license affects install):

1. Re-run `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` — must match report
2. Confirm repo exists; star count within ~30% of report
3. Confirm not on Phase-0 NO-GO registry
4. Log mismatches as `[NEEDS VERIFICATION YYYY-MM-DD]` on ingest — do not silently Adopt

Ingest path: drop report in `research to be indexed/` → `python3 scripts/preingest_check.py --inbox "research to be indexed"` → standard wiki ingest → `scp` raw to `cemini-librarian:/opt/cemini-bulk/research/`.

## Final reminder

If you find yourself writing "would be useful for X" without naming a specific Cemini path, a specific wiki page, or a specific workflow tool — STOP. Mark the cell ⚠️ and document the uncertainty in the Reasoning field. Vague fit is hallucination-adjacent and erodes the prompt's value.

## URLs to evaluate

[PASTE URLS HERE — one per line; prefix with `URLs as of YYYY-MM-DD:`]
