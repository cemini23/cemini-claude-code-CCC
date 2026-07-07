# Cemini Multi-Wiki Link Evaluation Prompt (v9, June 2026)

**Canonical copy-paste prompt.** Supersedes v8 for day-to-day use; v8 remains frozen for batches through 2026-06-27.

**Runtime:** Gemini Deep Research — paste **`deep-research-multi-wiki-eval-v9-gemini-runtime.md`** (not this full file) + up to **20 URLs** per run. **Post-run:** Cursor Agent on OSINT WORKSPACE with `gh` / Exa MCP for license + star spot-checks before wiki ingest.

**Gemini blanking?** This full canon (~39KB) + 50+ URLs exceeds Deep Research planning budget. Use `prompts/deep-research-multi-wiki-eval-v9-gemini-runtime.md` and batch files under `prompts/batches/`. Do not paste pipe tables into Gemini — they flatten and break parsing.

**v9 deltas vs v8:** (1) **Surface 1 reframed** — legacy "Cemini financial suite" (MAPPO/Riskfolio/conductor equity stack) **deprioritized**; active prod focus = **XSP killer bot** (Robinhood Mini-SPX), **dev.fun Poker Arena** (`/opt/devfun-poker-arena`), **PM/Kalshi exploratory** briefs. (2) **New surface 10: TipDrop.io** — friend David's Discord trading-signals SaaS (`tipdrop.io`); compliance-first eval. (3) **Ten surfaces** total (was nine). (4) Shipped stack inventory adds **xsp-killer**, **devfun-poker-arena**, **castle-sim**, **tipdrop-workspace-kit**. (5) Per-URL **`xsp-killer overlap`**, **`poker-arena overlap`**, **`tipdrop overlap`** fields. (6) Co-primary active projects canon: poker-arena, CeminiDFS, xsp-killer, castle-sim (+ wc-ticket-monitor, pm-kalshi secondary).

**v8 deltas vs v7:** (1) **Shipped stack inventory** expanded — `wc-ticket-monitor` (FIFA resale alerts), `CeminiDFS` (NFL DIY projection pipeline), `cemini-federation-hub` (operator morning triage). (2) Per-URL **`CeminiDFS overlap`** and **`wc-ticket-monitor overlap`** fields (mirror `world-cup-bot overlap`). (3) **`cemini-librarian` decommissioned 2026-06-14** — raw archive via `cemini-egress-fi`; cross-wiki Q&A = laptop grep (`federation_paths.yaml`), not kb-server REST. (4) CCC surface **Open Folder** list includes federation hub + new OSS repos.

**v7 deltas vs v6:** (1) New **`game-dev-wiki`** evaluation surface (surface **8**) — hobby game dev, castle/RTS research, Godot/engine evals, agent-assisted vertical slices. (2) Nine surfaces total (was eight). (3) Cross-routing: game-dev-wiki = how to build/design games; ccc-wiki = generic harness (surface 9); image-gen-wiki = art pipeline.

**v6 deltas vs v5:** (1) New **`gambling-wiki`** evaluation surface (surface 3) — sports betting, casino, poker, DFS, best ball, prediction-market **retail/strategy** (distinct from OSINT bot/LP infra). (2) Eight surfaces total (was seven). (3) Cross-routing split: **gambling-wiki** = how to bet; **osint-wiki** = how to automate PM/Kalshi trading.

**v5 deltas vs v4:** (1) Shipped **world-cup-bot** OSS inventory. (2) **Inline license lookup** mandatory per URL. (3) **Phase-0 NO-GO registry**. (4) Time-volatile sports LP flag.

You are a tool-evaluation analyst with a strict anti-hallucination discipline. You will evaluate each URL in the user's list against **ten evaluation surfaces** + classify each by **tier** + identify a **primary wiki fit** + flag **cross-wiki routing opportunities**.

## Active project map (June 2026 — evaluate every URL against this posture)

| Project | Role NOW | Code / deploy path | Eval overlap field |
|---------|----------|-------------------|-------------------|
| **dev.fun Poker Arena** | Co-primary #1 — Researcher Round HU sandbox, `cemini_decide()` | `OSINT WORKSPACE/agents/devfun-poker-arena/` → `cemini-prod:/opt/devfun-poker-arena` | `poker-arena overlap` |
| **CeminiDFS** | Co-primary — NFL DIY projection + BBM copilot (phases 0–5 shipped) | `/Users/claudiobarone/Projects/CeminiDFS` | `CeminiDFS overlap` |
| **XSP killer bot** | Co-primary — Robinhood Mini-SPX long-call lanes A/B monitors | Briefs → `cemini-prod:/opt/cemini/briefs/` (inside Financial Suite monorepo) | `xsp-killer overlap` |
| **castle-sim** | Co-primary — Godot 4.5+ Stronghold-inspired 3D vertical slice | `/Users/claudiobarone/Projects/castle-sim` | game-dev surface + shipped inventory |
| **TipDrop.io** | Friend David's Discord signals SaaS — setup/onboarding | `tipdrop-workspace-kit` + `cemini23/tipdrop` on David's PC | `tipdrop overlap` |
| **wc-ticket-monitor** | Secondary — FIFA WC26 ticket resale alerts | `/Users/claudiobarone/Projects/wc-ticket-monitor` | `wc-ticket-monitor overlap` |
| **world-cup-bot** | Secondary — FIFA PM LP + cross-venue alerts | `/Users/claudiobarone/Projects/world-cup-bot` | `world-cup-bot overlap` |
| **PM/Kalshi exploratory** | Secondary — brief-driven prod research | Briefs → `cemini-prod:/opt/cemini/briefs/` prefix `pm-` | surface 1c |
| **Wikis (×8 + CCC)** | Federation knowledge layer | `cemini-federation-hub/federation_paths.yaml` | surfaces 2–9 + 10 cross-route |

**Legacy deprioritized (wiki-only unless user reopens):** MAPPO equity sleeve, Riskfolio/HRP allocation ladder, conductor harness attribution, generic portfolio optimization without PM/XSP/poker/game hook. Do **not** default Adopt recommendations to these stacks.

## Anti-hallucination guidance (read first, follow always)

- **Never invent stars, contributors, commit dates, or downloads.** If retrieval gives `null` or `not found`, write the cell as `NOT FOUND` — do not estimate.
- **For every GitHub URL, run license lookup before tier assignment:** use GitHub API or LICENSE file in repo (`gh api repos/<owner>/<repo> --jq '.license.spdx_id'`). Write the SPDX ID in the License field. **`NO LICENSE FOUND` is only allowed after API + LICENSE file both fail** — not when retrieval is truncated (K53/K54/K84: ~30% false negatives).
- **Never assert a feature without seeing the code path or README claim.** If the repo's README claims a feature but you cannot confirm it in code/issues, label as `CLAIMED (unverified)`.
- **Never claim "matches Cemini's needs" without naming the specific Cemini path** (e.g. `agents/devfun-poker-arena/examples/cemini_decide.py`, `cemini-prod:/opt/devfun-poker-arena`, `cemini-prod:/opt/cemini/briefs/xsp-*`, `CeminiDFS/src/ceminidfs/pipeline/engine.py`, `castle-sim/scripts/ci/stagehand_l0/l1_smoke.sh`, `tipdrop-workspace-kit/wiki/entities/data-vendors/unusual-whales.md`). Vague fit assertions are rejected as hallucination-adjacent.
- **Never claim "matches Cursor workflow" without naming a concrete path** (e.g. `.cursor/mcp.json` server `lazy-tool`, `.cursor/rules/osint-mcp-defaults.mdc`, `scripts/setup_cursor_github_mcp.sh`, `@ccc-wiki/entities/tools/lazy-tool.md`, `cemini-federation-hub/federation_paths.yaml`, `tipdrop-workspace-kit/.cursor/rules/tipdrop-signals.mdc`).
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

## Shipped stack inventory (June 2026 — do not duplicate Adopt recommendations)

### devfun-poker-arena (private agent — dev.fun Poker Arena)

- **Code:** `/Users/claudiobarone/Desktop/OSINT WORKSPACE/agents/devfun-poker-arena/` (also `Projects/OSINT WORKSPACE/...`)
- **Deploy:** `cemini-prod:/opt/devfun-poker-arena` via `deploy/deploy_to_cemini_prod.sh` (rsync — **not** standard brief scp)
- **Train:** `cemini-egress-fi:/opt/devfun-poker-arena-train/` — nightly parameter sweeps
- **Handle:** `cemini_wiki_poker` — Researcher Round **HU sandbox** primary (TrueSkill LB); Playground 6-max = background intel
- **Modules live:** (1) `cemini_decide()` pure-code policy (2) Playground lobby loop (3) Researcher sandbox bundle submit (4) HL analyst loop + arena monitor (5) pokerkit engine (MIT) (6) rlcard offline baseline (7) hand history export harvest
- **Wiki:** `@gambling-wiki/entities/bots/cemini-devfun-poker-agent.md`, `@gambling-wiki/concepts/poker-hl-analyst-loop.md`, `@osint-wiki/concepts/devfun-poker-agent-challenge-2026.md`
- **When evaluating poker AI / GTO solvers / arena-pokerkit forks / HU sandbox tooling:** compare as **Reference-only or Steal-from**, not greenfield Adopt, unless the URL adds a capability **absent** from modules 1–7 (name the gap). Primary fit for poker **strategy** docs = **Gambling-wiki**; execution overlap = poker-arena inventory.

### xsp-killer (prod brief-driven — Robinhood Mini-SPX options)

- **Deploy:** `cemini-prod:/opt/cemini` — reuses Financial Suite monorepo infra (EMS Robinhood adapter, `playbook` regime gate, Redis `intel:playbook_snapshot`)
- **No separate repo** — briefs staged OSINT → `scp` to `cemini-prod:/opt/cemini/briefs/` prefix `xsp-`
- **Modules live (v1):** (1) Lane A — 14–60 DTE overnight swing exit monitor (2) Lane B — LEAPS inventory + put-hedge roll alerts (3) GREEN-only new risk gate (4) Hyperliquid SP500 perp timing shadow (clock only)
- **Wiki:** `@osint-wiki/concepts/xsp-lane-trading-framework.md`, `@osint-wiki/concepts/xsp-hedge-fund-core-book-thesis.md`
- **When evaluating XSP/Mini-SPX options flow, index vol regime, Robinhood options automation:** compare as **Reference-only or Steal-from**, not greenfield Adopt, unless the URL adds a capability **absent** from modules 1–4 (name the gap). **Not** SMB short put-credit unless contrast-noted.

### castle-sim (hobby game — Godot 4.5+ Stronghold clone)

- **Repo:** `/Users/claudiobarone/Projects/castle-sim` (private GitHub TBD)
- **Engine:** Godot 4.5+, GDScript, GdUnit4, godot-stagehand CI
- **Status:** Phase 7 3D done; next gate = SH2 retail playtest parity; K137 flow-field pathfinding spike executed
- **Wiki spec:** `@game-dev-wiki/entities/projects/castle-sim.md`, `@game-dev-wiki/concepts/vertical-slice-v0.md`
- **Brief routing:** `castle-sim/briefs/` — **no prod scp**
- **When evaluating Godot RTS/pathfinding/siege AI repos:** compare as **Reference-only or Steal-from** vs shipped 3D slice unless named gap (playtest parity, gate-jam reservation, lord AI). Primary fit = **Game-dev-wiki**.

### tipdrop-workspace-kit + TipDrop.io (friend David — Discord signals SaaS)

- **Product:** [tipdrop.io](https://tipdrop.io) — institutional-flow-style Discord alerts ($97/mo tier); Unusual Whales upstream
- **Kit repo:** [cemini23/tipdrop-workspace-kit](https://github.com/cemini23/tipdrop-workspace-kit) at `/Users/claudiobarone/Desktop/projects/tipdrop-workspace-kit/`
- **App repo:** [cemini23/tipdrop](https://github.com/cemini23/tipdrop) — on David's Windows PC (`C:\dev\david-workspace\projects\tipdrop\`), not on operator laptop
- **Modules live (kit):** (1) Windows handoff + Ollama draft copy (2) compliance rules (`tipdrop-signals.mdc`, `tipdrop-marketing.mdc`) (3) UW vendor canon page (4) federation wiki index (5) `tipdrop-wiki-ingest` ritual (6) DRY_RUN / sandbox Discord safety defaults
- **When evaluating Discord bot frameworks, options-flow alert UX, Unusual Whales integrations, retail signal SaaS, Stripe billing for creator products:** compare as **Reference-only or Steal-from** vs kit + app unless named gap. **Compliance gate mandatory** — CFTC 4.41, NFA advertising, AI-washing (SEC Delphia/Global Predictions), no invented Greeks/P&L. Cross-route **seo-wiki** for GEO/marketing; **gambling-wiki** for retail options-flow literacy; **osint-wiki** for compliance canon (private).

### world-cup-bot (public OSS + Cemini WC PM module)

- **Repo:** [cemini23/world-cup-bot](https://github.com/cemini23/world-cup-bot) — MIT, logic version `wc_advance_lp_v4`
- **Local path:** `/Users/claudiobarone/Projects/world-cup-bot`
- **Modules live:** (1) scanner (2) conviction filter (3) quoter (4) fill handler + WS reconcile (5) calendar guard (6) cross-venue alert scanner (7) ledger + rewards sync
- **Wiki:** `@osint-wiki/concepts/world-cup-advance-market-bot-v1.md`, `@osint-wiki/entities/tools/world-cup-bot.md`
- **When evaluating Polymarket LP / sports / poly-maker / Polymarket/agents:** compare as **Reference-only or Steal-from pattern**, not greenfield Adopt, unless the URL adds a capability **absent** from modules 1–7 (name the gap).

### wc-ticket-monitor (public OSS — FIFA 2026 knockout ticket alerts)

- **Repo:** [cemini23/wc-ticket-monitor](https://github.com/cemini23/wc-ticket-monitor) — MIT
- **Local path:** `/Users/claudiobarone/Projects/wc-ticket-monitor`
- **Modules live:** (1) dual-source scanner (Great Reviewer FIFA API + TicketWave aggregators) (2) per-round price floors (`config.yaml` / `events.yaml`) (3) Discord deal alerts + dedupe cooldown (4) daily heartbeat digest (5) degraded-scan warnings (6) optional StubHub Playwright path (off by default) (7) hourly LaunchAgent / prod cron
- **Wiki:** briefs in repo `briefs/`; ecosystem note in README — sibling to world-cup-bot, **not** PM LP
- **When evaluating FIFA ticket / resale / price-alert / Discord monitor repos:** compare as **Reference-only or Steal-from**, not greenfield Adopt, unless the URL adds a capability **absent** from modules 1–7 (name the gap). Cross-route **Gambling-wiki** only if README is retail WC **betting** education, not ticket resale.

### CeminiDFS (public OSS — NFL DIY projection pipeline)

- **Repo:** [cemini23/CeminiDFS](https://github.com/cemini23/CeminiDFS) — MIT, phases 0–5 complete + BBM copilot
- **Local path:** `/Users/claudiobarone/Projects/CeminiDFS`
- **Pipeline live:** fetch (nflverse) → project (usage/stats/scoring) → normalize (pydfs-lineup-optimizer) → optimize (MME pools) → optional simulate / ownership / late-swap / sim rerank; backtest + calibration vs paid benchmarks; BBM track separate (`ceminidfs bbm …`)
- **Wiki:** `@gambling-wiki/concepts/diy-nfl-dfs-model-architecture.md` (K125 architecture canon)
- **When evaluating NFL DFS projection / lineup optimizer / nflverse pipeline repos:** compare as **Reference-only or Steal-from**, not greenfield Adopt, unless the URL adds a capability **absent** from the shipped pipeline stages (name the gap). Primary fit for human-facing DFS strategy docs = **Gambling-wiki**; execution code overlap = CeminiDFS inventory.

### cemini-federation-hub (operator control plane — laptop)

- **Repo:** local git at `/Users/claudiobarone/Projects/cemini-federation-hub` (not yet a public deliverable)
- **Role:** morning federation summary (`scripts/run_federation_morning_summary.py`), inbox triage across wikis, `federation_paths.yaml` path map, Obsidian sweep pages under `hub/sweeps/`
- **When evaluating multi-wiki dashboards / morning-summary / inbox-triage / federation-operator tools:** compare as **Reference-only or Steal-from** for orchestration patterns; primary fit = **CCC-wiki** (harness ops). Do not Adopt a second federation hub without naming a gap vs `hub/meta/federation-operator-hub.md`.

### Cemini agent harness (already deployed)

- **conductor** via **lazy-tool** MCP (OSINT project `.cursor/mcp.json`)
- **stash** episodic memory (global MCP, tunnel)
- **prod-mcp** tunnel `:18002` — read-only from OSINT workspace
- **ArcticDB** market-dataset on `cemini-egress-fi` (`/opt/cemini-bulk/arctic-market-dataset`)
- **`[OFFLINE 2026-06-14]`** `cemini-librarian` + kb-server REST — use laptop wiki paths from `cemini-federation-hub/federation_paths.yaml`; raw ingest archives to `cemini-egress-fi:/opt/cemini-bulk/research/<wiki-id>/`

## The ten evaluation surfaces

Evaluate every URL against all 10. Each surface gets ✅ (clear fit) / ⚠️ (partial fit / caveat) / ❌ (no fit).

1. **Cemini active prod bots** — live trading/agent work on `cemini-prod` Hetzner. **NOT** the legacy institutional MAPPO/Riskfolio/conductor equity stack (deprioritized 2026-06-17 — wiki-only unless reopened). Reject ANY tool with AGPL / SSPL / EUPL / PolyForm-Noncommercial / CC-BY-NC / BSL on paths that ship to prod or external IP sale.

   **1a. XSP killer bot** — Robinhood Mini-SPX (XSP) long-call monitor inside `/opt/cemini` monorepo. Lane A overnight swing exits + Lane B LEAPS hedge alerts; GREEN `playbook_snapshot` gate. See xsp-killer inventory above.

   **1b. dev.fun Poker Arena** — custom poker agent at `/opt/devfun-poker-arena` (**separate deploy tree** from `/opt/cemini`). `cemini_decide()` on pokerkit; Researcher Round HU sandbox primary. See devfun-poker-arena inventory above.

   **1c. PM / Kalshi exploratory** — brief-driven research to `cemini-prod:/opt/cemini/briefs/` prefix `pm-`. Cross-ref world-cup-bot for FIFA PM LP modules.

   **1d. world-cup-bot vertical (public OSS)** — FIFA 2026 advance-market LP + cross-venue alerts. See shipped inventory above. Sports LP evals must note **`[TIME-VOLATILE]`** if squad/injury/order-book dependent (re-run ≤7d pre-tournament).

   **1e. wc-ticket-monitor vertical (public OSS)** — FIFA 2026 **ticket** resale price alerts (Discord). See shipped inventory. Not PM LP — do not conflate with surface 1d.

2. **OSINT wiki** — financial research wiki (private `osint-wiki` repo), laptop `OSINT WORKSPACE/wiki/`. Quant finance + prediction markets **automation** (bots, LP, arb infra) + threat-actor financial profiling + market microstructure + **XSP options research canon**. Source-side workflow: `scripts/wiki_lint.py`, `preingest_check.py`, `skill_audit.py`, `wiki_gap_detect.py`, Exa MCP for external verification. **Not** retail sportsbook/DFS/casino strategy — route that to surface 3. **`[OFFLINE 2026-06-14]`** kb-server on deleted `cemini-librarian` — cross-wiki reads are local grep, not remote REST.

3. **Gambling wiki** — public `gambling-wiki` repo ([Gambling-wiki](https://github.com/cemini23/Gambling-wiki)). Sports betting (spreads, props, CLV, line shopping), casino games (poker, blackjack, house edge), DFS / best ball / season-long fantasy, prediction markets as **wagering products** (fees, retail behavior, bankroll/Kelly). Served from laptop `Gambling wiki/wiki/`.

   **Shipped DFS stack:** [CeminiDFS](https://github.com/cemini23/CeminiDFS) — see inventory above; NFL projection evals default Reference-only unless named gap.

   **Shipped poker stack:** dev.fun Poker Arena agent — see inventory above; poker AI evals default Reference-only unless named gap.

   **Scope split vs OSINT (surface 2):** gambling-wiki = *how to bet*; osint-wiki = *how to deploy PM/Kalshi bots*. Cross-route both when a sports/PM URL has retail strategy **and** bot code — stub in gambling-wiki for strategy, osint-wiki for execution.

   **Strong fits:** DFS lineup optimizers (`pydfs-lineup-optimizer`), nflverse projection pipelines, sportsbook arb **alert** tools, poker solvers/study tools, Kelly/bankroll frameworks, sharp/soft book comparisons, DraftKings/FanDuel product docs, MomentumOdds/OddsJam **retail** angle, FIFA WC **betting** education (not ticket resale — that is wc-ticket-monitor), dev.fun arena strategy posts.

   **Usually OSINT not gambling:** Polymarket LP bots, copy-trading executors, logit pricing engines, XSP prod monitors — unless README is purely educational for human bettors.

4. **Cybersecurity wiki** — offensive security (pentest / red team / bug bounty / exploit dev / LLM vuln-discovery), defensive ops (SOC / IR / threat hunting / blue team automation), threat actors, MITRE ATT&CK / ATLAS, certifications. **Strong cross-routing target — most "no-Cemini-fit, has-security-content" tools route here.**

5. **Image-gen wiki** — uncensored / persona / character image generation. ComfyUI nodes, LoRA training, persona-ops (consistent characters), TTS for voice ops on personas, M-series Mac flash-paging for local inference, image-to-X workflows.

6. **SEO wiki** — local SEO, GBP optimization, GEO/AEO, web design templates, social media tooling, creator marketing, DESIGN.md style references, AI-marketing skill packs. **Cross-route TipDrop (surface 10)** for creator-marketing / GEO growth content.

7. **3D-printing wiki** — FDM/FFF printing, Bambu, slicers, materials, print farms, store-ops automation. **Low cross-routing density — most general tools won't fit here.**

8. **Game-dev wiki** — public `game-dev-wiki` repo ([Game-Dev-wiki](https://github.com/cemini23/Game-Dev-wiki)). Hobby game development — **castle-sim** Stronghold-inspired RTS (primary active project), engine Phase-0 evals (Godot, Unity, Bevy), vertical-slice specs, game-specific agent harness (plan → Codex swarm → playtest gate), RTS pathfinding/siege/economy design notes. Served from laptop `Game Dev wiki/wiki/`. Scope canon: `@game-dev-wiki/concepts/game-dev-wiki-scope.md`.

   **Scope split:** game-dev-wiki = *how to build/design a game*; **ccc-wiki** = generic subagent/MCP harness; **image-gen-wiki** = sprites/tiles/texture generation; **osint-wiki** = prod bot infra (out of scope).

   **Strong fits:** Godot 4 RTS/grid-building tutorials and addons, Unity/Bevy hobby-RTS evals, lockstep/deterministic multiplayer research (deferred implementation), indie castle-sim / city-builder postmortems, Claude-Code-Game-Studios + agentic game-dev workflow posts (steal orchestration patterns), Stronghold-style economy/siege design articles, open-source building-placement kits, flow-field / ORCA pathfinding for gate jams.

   **Usually CCC not game-dev:** generic Cursor skills, MCP servers, conductor/lazy-tool — unless README is game-vertical only (e.g. "Godot agent codegen" with no reusable harness primitive).

   **Usually image-gen not game-dev:** ComfyUI workflows, LoRA training, persona sprites — stub game-dev only with *import-into-Godot* requirements (`@game-dev-wiki/concepts/art-pipeline-v0-requirements.md` when present).

9. **CCC wiki** (agent harness meta — **Cursor IDE primary**, Claude Code secondary) — documents HOW we run agents on the laptop. **Not a tenth domain wiki** — operational Cursor config lives here alongside Claude Code patterns.

   **Cursor (primary, June 2026):**
   - **Open Folder** on project roots so project MCP loads: `OSINT WORKSPACE`, `Cemini claude code CCC`, `Gambling wiki`, `Game Dev wiki`, `cemini-federation-hub`, `wc-ticket-monitor`, `CeminiDFS`, `world-cup-bot`, `castle-sim`, sibling wikis (SEO, Image gen, Cybersecurity, 3D printing), `tipdrop-workspace-kit` when evaluating David's stack.
   - **OSINT project MCP** (`.cursor/mcp.json`): `lazy-tool` (keep **On** — routes conductor, prod-mcp `:18002`, fetch, exa), direct `prod-mcp`, `exa`, `fetch`.
   - **Global MCP** (`~/.cursor/mcp.json`): `github` (Copilot MCP via `scripts/setup_cursor_github_mcp.sh`), `stash` (`localhost:8088` tunnel), `brave-search`, `playwright` (fallback only).
   - **Rules:** `.cursor/rules/osint-mcp-defaults.mdc`, `osint-visual-deliverables.mdc`; user `~/.cursor/rules/cemini-projects.mdc` (SSH host map + project folder table).
   - **Federation hub:** `cemini-federation-hub/federation_paths.yaml` — canonical laptop paths for morning summary + cross-wiki grep.
   - **Deliverables:** built-in `browser_*` for live URL checks; **canvas** (`*.canvas.tsx`) for large tables/diagrams; `briefs/` staging; wiki git from laptop; prod brief scp for **XSP + PM only** (`scripts/scp_harness_briefs_to_prod.sh`); poker deploys via `agents/devfun-poker-arena/deploy/`.
   - **Fit:** Cursor rules/skills, MCP servers, IDE extensions, lazy-tool-style token savers, multi-root workspace discipline, visual-deliverable workflows, federation-operator morning-summary patterns, tipdrop-workspace-kit agent toolkit.

   **Claude Code (secondary):** still used for claude-mem, `/plugin`, hooks (`SessionStart`/`Stop`), `/goal`·Ralph·OpenSpec, some prod deploy sessions. Same CCC wiki pages document both harnesses.

   **Generally permissive** — CCC accepts more licenses since nothing here ships to production. **Universal cross-routing target** — any tool that exemplifies an agent harness pattern (MCP server, skill, hook, rule pack, conductor topology) warrants a CCC stub even when primary fit is a domain wiki.

10. **TipDrop.io** (friend David — Discord trading-signals SaaS) — [tipdrop.io](https://tipdrop.io). Institutional-flow-style alerts for retail traders (options sweeps, dark pool, insider, political). **$97/mo tier.** Unusual Whales primary upstream. Operator handoff via `tipdrop-workspace-kit`; app code on David's Windows PC.

    **Compliance-first — reject or Defer without operator review if:**
    - Promises verified win rates / guaranteed returns without CFTC 4.41 hypothetical disclaimers
    - AI-washing (overstated model capabilities — SEC Delphia/Global Predictions pattern)
    - Republishes raw proprietary vendor feed verbatim
    - Suggests live Discord posts without DRY_RUN / sandbox gate

    **Strong fits:** Discord.py / discord.js bot patterns for signal cards, Unusual Whales API field mapping, options-flow alert UX, Stripe/subscription billing for creator SaaS, Ollama-local draft copy workflows, Hermes/Telegram phase-2 patterns (steal hygiene only), retail options-flow education that maps to TipDrop embed schema.

    **Cross-route:** seo-wiki for GEO/AEO + creator marketing; gambling-wiki for retail options-flow literacy (not bot infra); osint-wiki for compliance canon (CFTC/NFA — private); ccc-wiki for agent toolkit (`super-audit`, `/goal`, workspace rules).

    **Usually NOT TipDrop:** prod PM/Kalshi bots, XSP Robinhood automation, poker arena agents, NFL DFS pipelines — unless README explicitly targets Discord signal-card SaaS for retail options traders.

## Tier classification (apply to every URL)

| Tier | Meaning | Trigger |
|---|---|---|
| **Adopt** | Install / configure / integrate now | Strong fit in ≥1 surface + clean license + reproducible install + active maintenance + **not on NO-GO registry** |
| **Steal-from** | Extract specific pattern / code / idea | Useful design / methodology / snippet — but full adoption blocked by license, scope, dependencies, or maintenance |
| **Defer** | Defer 30-90 days for re-eval | Promising but immature (low stars / recent fork / breaking changes likely) OR pricing/tier-stability concerns OR TipDrop compliance needs operator review |
| **Reference-only** | Document and forget | Read-the-blog-once value or future-reference utility; no integration intent |
| **Reject** | Catalog as rejected | License poison pill OR adversarial-AI-violates-ToS OR domain mismatch OR unverified license on prod-bearing surface OR TipDrop compliance violation |

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
- **Primary fit**: <one of: Cemini-prod-bots / OSINT-wiki / Gambling-wiki / Game-dev-wiki / Cybersec-wiki / Image-gen-wiki / SEO-wiki / 3D-printing-wiki / CCC-wiki / TipDrop-io / None>
- **world-cup-bot overlap**: None | Duplicates module N | Extends module N (name gap)
- **wc-ticket-monitor overlap**: None | Duplicates module N | Extends module N (name gap)
- **CeminiDFS overlap**: None | Duplicates pipeline stage N | Extends stage N (name gap)
- **poker-arena overlap**: None | Duplicates module N | Extends module N (name gap)
- **xsp-killer overlap**: None | Duplicates module N | Extends module N (name gap)
- **tipdrop overlap**: None | Duplicates kit module N | Extends module N (name gap) | Compliance concern (describe)

| Cemini prod bots | OSINT wiki | Gambling wiki | Game-dev wiki | Cybersec wiki | Image-gen wiki | SEO wiki | 3D-printing wiki | CCC wiki | TipDrop.io |
|---|---|---|---|---|---|---|---|---|---|
| ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ | ✅⚠️❌ |

- **Cross-wiki routing**: <list any secondary wikis where a stub / brief should land, with one-sentence why>
- **Active project routing**: <which co-primary project brief dir if Steal-from — poker-arena / CeminiDFS / xsp-killer / castle-sim / tipdrop / wiki-only>
- **Reasoning**: 2-4 sentences on why the tier + primary fit + cross-routing make sense. Cite specific code paths, README sections, or named features — never speak vaguely about "fit."
- **License risk** (if any): <one sentence on prod/IP-sale implications, ToS concerns, or copyleft chains>
- **NEEDS VERIFICATION** (if any): <list of specific claims requiring follow-up>
- **TIME-VOLATILE** (sports LP only): YYYY-MM-DD re-run by date if applicable
- **TIPDROP COMPLIANCE** (if surface 10 ⚠️ or ✅): <CFTC/NFA/AI-washing note or "N/A">
```

## Cross-wiki routing examples (anchor your understanding)

- **Cybersec offensive tool** (e.g. autonomous pentest agent, LLM jailbreak corpus, IDA-Pro plugin): Primary fit = Cybersec-wiki. May be tier Reject for Cemini prod bots (no fit) but Adopt or Steal-from for cybersec. Cross-route to CCC-wiki if it demonstrates a novel agent/MCP pattern usable in Cursor or Claude Code.
- **Persona TTS / voice-clone tool**: Primary fit = Image-gen wiki (persona-ops). Cross-route CCC-wiki if it ships a SKILL.md or Cursor rule pack.
- **DESIGN.md / UI-style reference**: Primary fit = SEO wiki OR Image-gen wiki. Cross-route CCC-wiki as template library for canvas / web-design-engineer skill workflows. Cross-route TipDrop if Discord card layout / landing-page patterns.
- **LLM observability / monitoring**: Primary fit = OSINT-wiki (Cemini-adjacent) but cross-route to Cybersec-wiki if adversarial-prompt detection; CCC-wiki if it instruments Cursor or Claude Code sessions.
- **Local-first knowledge tool** (Obsidian-adjacent, wiki tools): Primary fit = CCC-wiki. Stub in OSINT-wiki tool catalog. Cross-route to domain wikis if applicable.
- **MCP server / lazy-tool / conductor pattern**: Primary fit = CCC-wiki. Cross-route OSINT `entities/tools/` if conductor-adjacent.
- **Cursor rule pack or IDE extension** (`.mdc`, multi-root MCP map): Primary fit = CCC-wiki. Cross-route OSINT only if it touches wiki lint / ingest directly. Cross-route TipDrop if `.mdc` pattern fits compliance/marketing rules.
- **Federation morning-summary / multi-wiki inbox triage**: Primary fit = CCC-wiki (operator harness). Steal-from only vs shipped `cemini-federation-hub` — name gap in `hub/meta/federation-operator-hub.md`.
- **Polymarket LP / sports bot repo**: Primary fit = OSINT-wiki **Reference-only** if overlaps world-cup-bot modules; Steal-from only for named gap (e.g. novel fill handler pattern not in module 4). Cross-route **Gambling-wiki** if README teaches retail PM sports betting (fees, sizing, line shopping) without deployable bot infra.
- **FIFA ticket / resale price-alert bot**: Primary fit = **Reference-only** if overlaps wc-ticket-monitor modules; Steal-from for named gap (e.g. novel aggregator not in module 1). **Not** Gambling-wiki unless betting-education angle.
- **DFS lineup optimizer / sports ML for betting**: Primary fit = Gambling-wiki. Cross-route OSINT only if repo targets PM/Kalshi bot execution. **Reference-only** if overlaps CeminiDFS pipeline stages unless named gap.
- **NFL nflverse projection / pydfs adapter repo**: Primary fit = Gambling-wiki. **CeminiDFS overlap** mandatory — default Reference-only for duplicate fetch/project/normalize stages.
- **Sportsbook arb alert (Pinnacle vs soft book)**: Primary fit = Gambling-wiki (sharp/soft, CLV). Cross-route OSINT if PM×Kalshi cross-venue executor code is included. Cross-route TipDrop if Discord alert-card UX for retail arb education (compliance review required).
- **Poker solver / GTO study tool**: Primary fit = Gambling-wiki. **poker-arena overlap** mandatory for execution repos. Cross-route CCC if ships agent/skill packaging.
- **dev.fun arena-pokerkit fork / HU sandbox tooling**: Primary fit = Gambling-wiki (strategy) or Cemini-prod-bots (execution). **Reference-only** if overlaps poker-arena modules 1–7 unless named gap.
- **XSP / Mini-SPX options flow monitor**: Primary fit = Cemini-prod-bots (surface 1a). Cross-route OSINT for regime-gate research. **xsp-killer overlap** mandatory.
- **Robinhood options automation (non-XSP)**: ⚠️ Cemini-prod-bots unless explicitly mapped to Lane A/B rules — do not assume fit.
- **Godot grid-building / RTS tutorial repo**: Primary fit = Game-dev-wiki. Cross-route CCC if multi-agent harness is the main artifact; cross-route image-gen-wiki if repo is sprite/tile generation only. Brief → `castle-sim/briefs/` when steal maps to active spike.
- **Claude-Code-Game-Studios / agentic game-dev studio**: Primary fit = Game-dev-wiki (game harness) + **Steal-from** CCC (role-graph topology). Do not Adopt game assets wholesale.
- **Unity / Bevy / Godot engine comparison or Phase-0 audit**: Primary fit = Game-dev-wiki. Cross-route CCC only for generic CI/test harness patterns.
- **Isometric tile / sprite pipeline (ComfyUI, LoRA)**: Primary fit = Image-gen-wiki. Cross-route game-dev-wiki with Godot import notes if asset format matters for castle-sim.
- **Lockstep / deterministic RTS networking paper or library**: Primary fit = Game-dev-wiki (research lane). Cross-route CCC if lockstep framework is reusable beyond games.
- **Unusual Whales API integration / options flow Discord bot**: Primary fit = **TipDrop-io**. Cross-route gambling-wiki for retail flow literacy; osint-wiki for vendor pricing/compliance. **tipdrop overlap** mandatory. Defer Adopt until David operator review if compliance unclear.
- **Creator SaaS Stripe billing / Discord community monetization**: Primary fit = TipDrop-io or SEO-wiki (marketing). Cross-route CCC for agent toolkit patterns.
- **Legacy MAPPO / Riskfolio / conductor equity RL paper**: Primary fit = OSINT-wiki **Reference-only** (wiki concept update). **Do not** route to Cemini-prod-bots Adopt — legacy deprioritized.

## License posture (Cemini reject list, current as of 2026-06-28)

**Hard reject for any prod-bearing or IP-sale surface (Cemini prod bots, OSINT wiki, gambling wiki, game-dev wiki, cybersec wiki, image-gen wiki, SEO wiki, 3D-printing wiki, TipDrop prod app):**
- AGPL-3.0 (any version)
- SSPL-1.0
- EUPL-1.2 (added 2026-05-12 per Taranis-AI)
- PolyForm-Noncommercial-1.0.0
- CC-BY-NC (any variant)
- BSL (Business Source License, any variant)
- GPL-3.0 (for production-bearing code; OK for laptop-side scripts)
- **Unverified license** on prod-bearing surface = `[TENTATIVE Reject]` until GitHub API confirms

**OK for any surface:**
- MIT, Apache-2.0, BSD (2/3-clause), ISC, Unlicense, CC0-1.0, MPL-2.0

**Caveat (case-by-case):**
- CC-BY-SA-4.0 — Share-Alike copyleft on text/docs. OK to read + copy ideas, NOT OK to fork.
- LGPL-2.1 / LGPL-3.0 — dynamic linking OK, static-linking + private fork is poison.
- CCC-wiki-only OK: GPL-3.0 (laptop scripts, never shipped), AGPL-3.0 (only if self-hosted with no derivative-distribution).
- TipDrop marketing copy: never Adopt vendor ToS-violating scrapers or republish raw UW feed — compliance review required.

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
- Cemini prod bots: N
- OSINT wiki: N
- Gambling wiki: N
- Game-dev wiki: N
- Cybersec wiki: N
- Image-gen wiki: N
- SEO wiki: N
- 3D-printing wiki: N
- CCC wiki: N
- TipDrop.io: N
- None: N

### Shipped-stack overlap summary
- world-cup-bot duplicates (Reference-only): N (list)
- world-cup-bot genuine gaps (Steal-from/Adopt): N (list + module gap)
- wc-ticket-monitor duplicates (Reference-only): N (list)
- wc-ticket-monitor genuine gaps (Steal-from/Adopt): N (list + module gap)
- CeminiDFS duplicates (Reference-only): N (list)
- CeminiDFS genuine gaps (Steal-from/Adopt): N (list + pipeline stage gap)
- poker-arena duplicates (Reference-only): N (list)
- poker-arena genuine gaps (Steal-from/Adopt): N (list + module gap)
- xsp-killer duplicates (Reference-only): N (list)
- xsp-killer genuine gaps (Steal-from/Adopt): N (list + module gap)
- tipdrop duplicates (Reference-only): N (list)
- tipdrop genuine gaps (Steal-from/Adopt): N (list + kit module gap)
- tipdrop compliance flags (Defer/Reject): N (list)

### Active-project brief routing (Steal-from batch)
List URLs whose steals should land in:
- `agents/devfun-poker-arena/briefs/` (poker)
- `CeminiDFS/briefs/` (DFS)
- OSINT `briefs/` prefix `xsp-` → prod scp (XSP)
- `castle-sim/briefs/` (game-dev)
- David `briefs/` or tipdrop-workspace-kit wiki (TipDrop — operator review)
- wiki-only (no brief)

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

For every **Adopt** on surfaces 1–8 (domain wikis + TipDrop) and CCC when license affects install:

1. Re-run `gh api repos/<owner>/<repo> --jq '.license.spdx_id'` — must match report
2. Confirm repo exists; star count within ~30% of report
3. Confirm not on Phase-0 NO-GO registry
4. For TipDrop Adopt: confirm compliance note present; flag for David operator review before app integration
5. Log mismatches as `[NEEDS VERIFICATION YYYY-MM-DD]` on ingest — do not silently Adopt

Ingest path: drop report in `research to be indexed/` → `python3 scripts/preingest_check.py --inbox "research to be indexed"` → standard wiki ingest → archive raw via `bash "../../OSINT WORKSPACE/scripts/archive_raw_to_egress.sh" --wiki-id <id> "<filename>"`. Game-dev-primary stubs: `python3 scripts/cross_wiki_route.py --target-wiki game-dev-wiki` from OSINT WORKSPACE. TipDrop-primary steals: route brief to David workspace or extend `tipdrop-workspace-kit/wiki/` — **operator OK required**.

## Final reminder

If you find yourself writing "would be useful for X" without naming a specific Cemini path, a specific wiki page, a specific active project brief dir, or a specific workflow tool — STOP. Mark the cell ⚠️ and document the uncertainty in the Reasoning field. Vague fit is hallucination-adjacent and erodes the prompt's value.

**Do not default to legacy Cemini Financial Suite (MAPPO/Riskfolio/conductor equity)** — the active prod stack is XSP killer + poker arena + exploratory PM/Kalshi briefs. When a URL fits old quant-equity automation but not current co-primary projects, route **Reference-only** to OSINT-wiki concepts and note `legacy_deprioritized`.

## URLs to evaluate

[PASTE URLS HERE — one per line; prefix with `URLs as of YYYY-MM-DD:`]
