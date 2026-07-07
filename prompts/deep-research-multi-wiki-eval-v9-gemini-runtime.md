# Cemini Multi-Wiki Link Evaluation — Gemini Deep Research RUNTIME (v9)

**Use this file for Gemini Deep Research paste.** Full canon: `deep-research-multi-wiki-eval-v9-2026-06-28.md` (Cursor spot-check only).

**Hard limits (Gemini blanks if violated):**
- **Max 20 URLs per run.** If the user pasted more, STOP and output only a batch plan — do not evaluate yet.
- **First output MUST be `## Research plan`** (URL count, batch split, order) before any URL section.
- **No markdown pipe tables.** Use bullets and one-line field lists only.
- **Plain text only** — no emoji checkmarks in tables; write YES / PARTIAL / NO for surface fit.

---

## Task

Evaluate each URL against **10 surfaces**, assign a **tier**, name **primary fit**, flag **cross-wiki routing**, and score **shipped-stack overlaps**.

### Ten surfaces (score each YES / PARTIAL / NO)

1. **Cemini prod bots** — XSP killer (Robinhood Mini-SPX briefs), dev.fun poker arena (`/opt/devfun-poker-arena`), PM/Kalshi briefs. NOT legacy MAPPO/Riskfolio/conductor equity.
2. **OSINT wiki** — PM/Kalshi bots, LP, arb infra, XSP research. Not retail betting strategy.
3. **Gambling wiki** — retail betting, DFS, poker strategy, Kelly/CLV.
4. **Cybersec wiki** — offensive/defensive security, LLM vuln discovery.
5. **Image-gen wiki** — ComfyUI, LoRA, persona ops.
6. **SEO wiki** — local SEO, GEO/AEO, creator marketing.
7. **3D-printing wiki** — FDM, Bambu, print farms.
8. **Game-dev wiki** — Godot/castle-sim RTS, pathfinding, siege AI.
9. **CCC wiki** — Cursor/Claude Code harness, MCP, skills, rules.
10. **TipDrop.io** — David's Discord options-flow signals SaaS; Unusual Whales upstream; **compliance-first** (CFTC 4.41, NFA, no AI-washing, no raw UW republish, DRY_RUN Discord).

### Active co-primary projects (name path when claiming fit)

- **Poker arena:** `agents/devfun-poker-arena/examples/cemini_decide.py` → overlap field `poker-arena`
- **CeminiDFS:** `CeminiDFS/src/ceminidfs/pipeline/` → overlap field `CeminiDFS`
- **XSP killer:** briefs `xsp-*` → `cemini-prod:/opt/cemini/briefs/` → overlap field `xsp-killer`
- **castle-sim:** `castle-sim/briefs/` → game-dev surface
- **TipDrop:** `tipdrop-workspace-kit/` + `cemini23/tipdrop` → overlap field `tipdrop`

### Shipped stacks — default Reference-only unless named gap

- **TipDrop kit modules:** (1) Windows handoff (2) compliance rules (3) UW vendor page (4) wiki ingest (5) DRY_RUN Discord (6) Ollama draft copy
- **Poker arena modules:** cemini_decide, lobby, sandbox submit, HL loop, pokerkit, rlcard, export harvest
- **CeminiDFS stages:** fetch → project → normalize → optimize → simulate/ownership/late-swap
- **world-cup-bot / wc-ticket-monitor / xsp-killer:** see full v9 canon if relevant

### Tiers

Adopt | Steal-from | Defer | Reference-only | Reject | UNAVAILABLE

### License rules

- GitHub URL: report SPDX from LICENSE file or GitHub API metadata — never guess.
- Hard reject on prod/TipDrop surfaces: AGPL, SSPL, EUPL, PolyForm-NC, CC-BY-NC, BSL, GPL-3.0 in shipped code.
- OK: MIT, Apache-2.0, BSD, ISC, MPL-2.0.

### Anti-hallucination (mandatory)

- Stars / last commit / issues: NOT FOUND if unverified — never estimate.
- Unverified features: label CLAIMED (unverified).
- Every fit claim must name a **specific path** (see co-primary list) or wiki page — else PARTIAL + explain uncertainty.
- 404 / deleted repo: tier UNAVAILABLE, skip deep analysis.

### Phase-0 NO-GO (never Adopt without re-audit)

PageIndex, SwarmVault, Claude-OSINT, warproxxx/poly_data (GPL-3.0).

---

## Required output order

### Step 1 — Research plan (MANDATORY FIRST)

```
## Research plan
- URLs received: N
- URLs to evaluate this run: N (max 20)
- Deferred to next batch: [list or none]
- Batch theme: [e.g. Unusual Whales MCP + Discord alert bots + TipDrop]
- Evaluation order: [numbered URL list]
- Estimated depth: license + README + last commit per repo
```

### Step 2 — Per URL (repeat for each URL in this run only)

```
## URL N: [repo name]

- URL: ...
- License: [SPDX or NOT FOUND] (method: GitHub LICENSE | API | UNAVAILABLE)
- Stars / Last commit / Issues: ... / ... / ... (or NOT FOUND)
- Stack: ...
- Tier: ...
- Primary fit: [Cemini-prod-bots | OSINT-wiki | Gambling-wiki | Game-dev-wiki | Cybersec-wiki | Image-gen-wiki | SEO-wiki | 3D-printing-wiki | CCC-wiki | TipDrop-io | None]
- Surfaces: prod=NO osint=NO gambling=NO game=NO cyber=NO image=NO seo=NO print=NO ccc=PARTIAL tipdrop=YES
- Overlaps: tipdrop=[None|Duplicates M#|Extends M# (gap)] poker-arena=... CeminiDFS=... xsp-killer=... wc-bot=... wc-tickets=...
- Cross-wiki routing: ...
- Active project routing: [poker-arena | CeminiDFS | xsp-killer | castle-sim | tipdrop | wiki-only]
- Reasoning: 2-4 sentences with specific README/code references
- License risk: ... (or none)
- TIPDROP COMPLIANCE: ... (or N/A)
- NEEDS VERIFICATION: ... (or none)
```

### Step 3 — Aggregate summary (after all URLs in this run)

```
## Aggregate summary
- Adopt: N — [list]
- Steal-from: N — [list]
- Defer: N — [list]
- Reference-only: N — [list]
- Reject: N — [list]
- UNAVAILABLE: N — [list]
- Primary-fit counts: [one line each]
- tipdrop genuine gaps: [list + module gap]
- tipdrop compliance flags: [list]
- Cross-routing batch: [bullets by target wiki]
```

---

## URLs to evaluate (THIS RUN ONLY — delete lines beyond 20 before submit)

[PASTE UP TO 20 URLS HERE — prefix with `URLs as of YYYY-MM-DD:`]
