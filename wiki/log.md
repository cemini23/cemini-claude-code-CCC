## [2026-08-12] ingest | MCP auth gateway + ACM + agent-callable tools (K270–K273)

- **Note:** K266–K269 IDs already used by cybersec agent-security wave — this batch uses **K270–K273**.
- **K270** LLM-assisted writing in PMC (2608.10715) — hygiene awareness; **NO-GO** null SPDX.
- **K271** Enterprise MCP auth gateway (2608.10760) — persona×credential + central gateway — **ADOPT**; no public code.
- **K272** Agent-callable spectroscopic tools (2608.10866) — MCP+Skill packaging — **ADOPT**; **GO** MIT `.local/adopts/agent4binary` (~185MB); astronomy **wont_wire**.
- **K273** Agentic Configuration Management ACM (2608.11166) — baselines/provenance governance — **ADOPT**; no SPDX product.
- Phase-0: `adopt_k270`…`k273`; Phase-1: policy §K270–K273 + `ccc-k270-k273-phase1-wires.mdc`
- Route: mid+SkipGrokPlan attempted with wrong K266 IDs → killed; Cursor parent completed as K270–K273 (Grok CLI out).
- Briefs: prod / Atto / Poker / GuruWatcher / Cybersec

## [2026-08-11] ingest | Scaffold/Macaron/Verify/SHE/VectraYX harness wave (K261–K265)

- **K261 VectraYX** (2608.08477): Spanish cyber VLM + MCP tools — cybersec-primary; CCC stub; **NO-GO** weights.
- **K262 Scaffolding > interface** (2608.08654): scaffolding dominates MCP vs CLI — **ADOPT**; **NO-GO** code.
- **K263 Macaron-V1** (2608.09819): versioned model–harness + MoL — **ADOPT** vocab; **NO-GO** weights / null SPDX hcp-sdk.
- **K264 Agentic verification layers** (2608.09857): accept/reject/escalate — **ADOPT**; repo **404 NO-GO**.
- **K265 SHE** (2608.09885): four-artifact safety harness evolution — **ADOPT**; **GO** Apache `.local/adopts/SHE` (~5MB); HITL only.
- Phase-0: `adopt_k261`…`k265_phase0.sh`; Phase-1: policy wires §K261–K265 + `ccc-k261-k265-phase1-wires.mdc`
- Briefs: prod / Atto / Poker / GuruWatcher / Cybersec; route mid→claude-ds hung off-task → Cursor parent takeover (Grok CLI out)
- Also: route skill v2.2 Grok-out docs; `wiki/sweeps/2026-08-11-daily.md`; `docs/briefs/2026-08-10_cursor-route-orchestrator-viral.md`

## [2026-08-10] ingest | ResidencyRL adversarial curriculum + doc fidelity (K260)

- **K260 ResidencyRL** (2608.07418): Google multi-turn clinical RL (GRPO) — steal **adversarial curriculum packs**, hierarchical rubrics + safety penalties, **premature-closure** resistance, **documentation anti-hallucination** — **ADOPT** policy; **NO-GO** code (explicitly closed); **wont_wire** runtime (clinical OOD).
- Pages: 2 sources + 1 concept + 1 entity + handoff `@briefs/2026-08-10_ccc-handoff-k260-residencyrl-ingest.md`
- Phase-0: `scripts/adopt_k260_phase0.sh`
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` §K260; `ccc-k260-phase1-wires.mdc`; concept `policy_wired`
- **Briefs:** prod → cemini-prod; Poker → poker-arena; Atto → atto/briefs; GuruWatcher → GuruWatcher/briefs; Cybersec → `Cybersecurity wiki/briefs/` (no TipDrop)
- **Local adopts:** none (closed code)
- Also tracked: `docs/k220-meat-black-cat.md`, `wiki/sweeps/2026-08-09-daily.md`

## [2026-08-08] ingest | CASCADE MCP claim validation + parameter grounding (K259)

## [2026-08-08] route | agent-toolkit canon host + SIP/verify gates

- Migrated `/route` scripts from tipdrop-workspace-kit → private `cemini23/agent-toolkit`
- Skill v2.1: SIP SDR, verify gate, lane escalate, `_route_runs/`
- Prod `/opt/cemini/agent-toolkit`; egress rsync same path (no pwsh)
- Pages: `entities/tools/agent-toolkit.md`, `entities/skills/route.md`


- **K259 CASCADE** (2608.05359): LangGraph MCP gene-perturbation server — steal **claim-level** validation of MCP tool reports (not membership) + NL→MCP parameter-grounding failure taxonomy (schema / alias / confident-wrong-default) — **ADOPT** policy; **GO** MIT REFERENCE `.local/adopts/CASCADE` (~352MB shallow, no DepMap/model); **wont_wire** runtime (cancer genomics OOD).
- Pages: 2 sources + 1 concept + 1 entity + handoff `@briefs/2026-08-08_ccc-handoff-k259-cascade-ingest.md`
- Phase-0: `scripts/adopt_k259_phase0.sh`
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` §K259; concept `policy_wired`
- **Briefs:** prod → cemini-prod; Poker / Atto / GuruWatcher / Cybersec local-abliterated-lab (no TipDrop)
- **Archive:** PDF → egress-fi (or raw-sources fallback)
- Also commits pending K254–K258 phase1 wire_status closeout brief if present

## [2026-08-07] phase1 | K254–K258 wire_status closeout

- Concepts → `policy_wired` (`cemini-phase1-policy-wires.mdc`): hardware-confined signing, READ doc ops, TrajDebug, AV-AIVAT, PTC. Entity hardware-keystore already `policy_wired`. No SoftHSM/AV-AIVAT/PTC runtime install; no secrets; no LIVE Discord.

## [2026-08-07] ingest | Hardware keystore + READ + TrajDebug + AV-AIVAT + PTC (K254–K258)

- **K254 Hardware Keystores** (2608.06130): PKCS#11 hardware-confined signing + Zero-Trust MCP stack — **ADOPT** pattern; **NO-GO** clone (anonymous.4open only). Entity `@entities/tools/hardware-keystore-mcp-signing.md` `policy_wired`. Cybersec-primary.
- **K255 Beyond Top-K / READ** (2608.06305): MCP grep/outline/bounded-read over long docs; BM25≈READ — **ADOPT** interface; **GO** MIT `.local/adopts/READ` (~8.4MB). Entity `policy_wired` / runtime `wont_wire`.
- **K256 TrajDebug** (2608.06346): error-lifecycle attribution (trigger→state→cause) — **ADOPT** method; **GO** thin MIT shelf `.local/adopts/TrajDebug` (~4.2MB, **0 `.py`** under review). Entity `wont_wire`.
- **K257 AV-AIVAT** (2608.06362): anytime-valid AIVAT stopping; median **74×** fewer HUNL hands — **ADOPT** poker eval discipline; **NO-GO** code. Entity `wont_wire`. Poker-primary.
- **K258 Bitter Lesson PTC** (2608.06370): programmatic tool calling matches/beats JSON 11/14 models — **ADOPT** policy; **NO-GO** install. Entity `policy_wired`.
- Pages: 6 sources, 5 concepts, 5 entities, brief stub, handoff `@briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md`
- Phase-0: `scripts/adopt_k254_phase0.sh` … `adopt_k258_phase0.sh`
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` extended K254–K258; federation sync
- **Briefs:** prod → cemini-prod; Poker → poker-arena; Atto → atto; GuruWatcher → GuruWatcher; Cybersec → local-abliterated-lab (no TipDrop)
- **Archive:** 5 PDFs → cemini-egress-fi
- **Local adopts:** READ + TrajDebug (<500MB)
- **CI note:** GHA Actions budget empty — local `wiki_lint.py` only

## [2026-08-06] ingest | Scale-CDA + Canary Tools + RAC + ArtAnno + Argus (K249–K253)

- **K249 Scale-CDA** (2608.04235): edge MCP bridge + meta-action executors into planner hooks without mutating safety core — **ADOPT** pattern; **NO-GO** automotive install. Entity `@entities/tools/scale-cda.md` `wont_wire`.
- **K250 Canary Tools** (2608.04719): six-type canary taxonomy for MCP tool-selection diagnosis; CSR ~36×; tier≠safety — **ADOPT** policy; **NO-GO** install (no artifact). Entity `@entities/tools/canary-tools-mcp.md` `policy_wired`.
- **K251 RAC** (2608.04991): split-inference activation compression awareness — **ADOPT** concept; **NO-GO** install. Entity `@entities/tools/rac-split-inference.md` `wont_wire`.
- **K252 ArtAnno / BiHAA** (2608.05026): bidirectional HAI skill-evolution loop — **ADOPT** pattern; **NO-GO** product. Entity `@entities/tools/artanno.md` `wont_wire`. Skip Image-gen local wire.
- **K253 Argus** (2608.05144): four-role verification-gated persist/pivot runtime — **ADOPT** pattern; **NO-GO** clone (no LICENSE on `lbx154/Argus`). Entity `@entities/tools/argus-agentic-runtime.md` `wont_wire`.
- Pages: 6 sources, 5 concepts, 5 entities, brief stub, handoff `@briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md`
- Phase-0: `scripts/adopt_k249_phase0.sh` … `adopt_k253_phase0.sh` — all pass
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` extended K249–K253; federation sync
- **Briefs:** prod → `cemini-prod:/opt/cemini/briefs/`; Poker → poker-arena; Atto → atto/briefs; GuruWatcher → GuruWatcher/briefs; Cybersec → `Cybersecurity wiki/briefs/` (local-abliterated-lab) — no TipDrop
- **Archive:** 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`
- **Local adopts:** none (all code NO-GO / no artifact / no SPDX)

## [2026-08-05] routing | TipDrop retired — links eval v10.5 + local abliterated lab

- Deep-research prompts → **v10.5**: TipDrop.io / David kit removed from active project map; surface 10 = local abliterated / operator lab
- Overlap field `local-abliterated-lab`; briefs → `Cybersecurity wiki/briefs/` only (never tipdrop-workspace-kit)
- Canon: `prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md` + gemini-runtime; `@concepts/deep-research-evaluation-prompt.md`; `hot.md`

## [2026-08-05] ingest | UrbanAgent + GUI–MCP adoption gap + MultiGlobeQA + HIVE + TurnSight (K244–K248)

- **K244 UrbanAgent** (2608.03018): clarify-before-act + evidence-aligned close + execution-quality eval — **ADOPT** pattern; **NO-GO** install (no public repo, urban OOD). Entity `@entities/tools/urbanagent.md` `wont_wire`.
- **K245 Screenshots or Tools?** (2608.03327): MCP sign-flip by model class; adoption gap 23.9%; observation-rule screenshot trim — **ADOPT** policy; **NO-GO** install. Entity `@entities/tools/hybrid-gui-mcp-osworld.md` `policy_wired`.
- **K246 MultiGlobeQA** (2608.03882): geospatial computation not knowledge; MIT REFERENCE `.local/adopts/MultiGlobeQA` — **GO** eval bench; **wont_wire** CCC runtime.
- **K247 HIVE** (2608.03970): voice hurts constructive tasks; keyboard resilient; thinking budget ≠ voice fix — **ADOPT** input policy; concept-only.
- **K248 TurnSight** (2608.04007): turn-level hindsight for tool RL — **ADOPT** pattern; **NO-GO** clone (no SPDX). Entity `@entities/tools/turnsight.md` `wont_wire`.
- Pages: 6 sources, 5 concepts, 4 entities, brief stub, handoff `@briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md`
- Local adopts: `.local/adopts/MultiGlobeQA` (~53MB MIT)
- Phase-0: `scripts/adopt_k244_phase0.sh` … `adopt_k248_phase0.sh` — all pass
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` extended K244–K248; federation sync
- **Briefs:** prod → `cemini-prod:/opt/cemini/briefs/`; Poker → poker-arena; Atto → atto/briefs; GuruWatcher → GuruWatcher/briefs *(David/TipDrop kit retired same day — see routing entry above)*
- **Archive:** 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`

---

## [2026-08-04] ingest | Execution fidelity + MCP.jl + tabular LLM fail + Trajectory Sentinel + ACEM (K239–K243)

- **K239 Safety Invariants** (2608.00783): execution fidelity I1–I7 for irreversible transitions — **ADOPT** checklist; **NO-GO** install (no public repo). Entity `@entities/tools/datumpont-execution-fidelity.md` `wont_wire`.
- **K240 MixedComplementarityProblems.jl** (2608.00959): batched Julia MCP solver — **GO** BSD-3 REFERENCE `.local/adopts/MixedComplementarityProblems.jl`; **wont_wire** CCC runtime (robotics OOD).
- **K241 Tabular LLM failure** (2608.02412): dimensionality decisive — **ADOPT** no raw LLM single-pass for tabular analytics; concept-only.
- **K242 Agent Trajectory Sentinel** (2608.02464): ESN+CUSUM telemetry + deterministic verify + rollback repair — **ADOPT** + **GO** MIT `.local/adopts/agent-trajectory-sentinel`. Entity `policy_wired`.
- **K243 ACEM** (2608.02582): RF/CF/HIS cost vocabulary — **ADOPT** planning; **NO-GO** install (conceptual).
- Pages: 5 sources, 5 concepts, 3 entities, brief stub, handoff `@briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md`
- Local adopts: `.local/adopts/agent-trajectory-sentinel` (~108MB MIT), `.local/adopts/MixedComplementarityProblems.jl` (~2.6MB BSD-3)
- Phase-0: `scripts/adopt_k239_phase0.sh` … `adopt_k243_phase0.sh` — all pass
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` extended K239–K243; federation sync
- **Briefs:** prod → `cemini-prod:/opt/cemini/briefs/`; David → tipdrop-workspace-kit; Poker → poker-arena; Atto → atto/briefs; GuruWatcher → GuruWatcher/briefs
- **Archive:** 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`

---

## [2026-08-03] ingest | CyberNeuro + MCP-Tester + HAM-VLN + ACCEL + TokTier (K234–K238)

- **K234 CyberNeuro** (2607.28841): local-first MCP multi-agent + SKILL.md skill-DAG + HITL QC panel — **ADOPT** patterns; **NO-GO** product (gated site, no public repo). Entity `@entities/tools/cyberneuro.md` `wont_wire`.
- **K235 MCP-Tester** (2607.29247): mutation-consistency metamorphic testing for transpilers (NOT MCP protocol) — **ADOPT** + **GO** Zenodo REFERENCE `.local/adopts/mcp-tester-transpiler`. Entity `policy_wired`.
- **K236 HAM-VLN** (2607.29600): decision-coupled hierarchical memory write on same turn as action — **ADOPT** pattern (pairs K154/K230); **NO-GO** code. Entity `ham-vln` policy pattern only.
- **K237 ACCEL** (2607.29610): five-pillar agentic engineer competency rubric — **ADOPT** operator-education framing; **NO-GO** install (paper only).
- **K238 TokTier** (2607.29678): tokenization up to 64% TTFT at high cache hits — **ADOPT** awareness; **NO-GO** deploy (no public artifact).
- Pages: 5 sources, 5 concepts, 4 entities, brief stub, handoff `@briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md`
- Local adopt: `.local/adopts/mcp-tester-transpiler` (~3.3MB, Zenodo CC-BY-4.0)
- Phase-0: `scripts/adopt_k234_phase0.sh` … `adopt_k238_phase0.sh` — all pass
- Phase-1: `.cursor/rules/cemini-phase1-policy-wires.mdc` extended K234–K238; federation sync
- **Briefs:** prod → `cemini-prod:/opt/cemini/briefs/`; David → tipdrop-workspace-kit; Poker → poker-arena; Atto → atto/briefs
- **Archive:** 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`

---

## [2026-08-01] skill | free-audit — Grok-orchestrated low-cost council

- New `.cursor/skills/free-audit/` (`federation: true`) — Cursor packs → Grok audits+orchestrates → claude-ds/DeepSeek V4 Flash + ≥2 dynamic free OpenRouter models (exclude DeepSeek/Grok)
- Scripts: `build_audit_pack.py`, `select_free_or_models.py`, `prepare_free_audit.py`, `run_non_grok_legs.py`
- Wiki: `entities/skills/free-audit.md`; backlinks on cursor-audit + super-audit
- Parent Cursor delivers only `SYNTHESIS.md` path (minimal Cursor spend)

---

## [2026-07-31] phase1 | CCC backlog clear

- **MCP:** no new servers from this backlog (nuance=TEM OOD; euclid needs SWI-Prolog + niche; SearchOS/askchem need keys/domain). Keep exa/fetch/codebase-memory + global github/brave. Revisit euclid only if operator wants deterministic proof MCP.

- New alwaysApply rule `.cursor/rules/cemini-phase1-ccc-harness.mdc` (schema-bound MCP, policy-as-code, DAG validate, LightMem2 compaction, Bayesian≠Phase-0, skill packaging, ToM, flowforge/canvas, FARA verifier, AIH citation)
- CCC clones: **0 unwired** — policy_wired (patterns) + runtime_wired (mattpocock) + wont_wire (REFERENCE/trainers/OOD)
- Stubs: `asm-adopt-orphan`, `biosecbench-surveillance`
- Inventory aliases expanded in `scripts/phase1_adopt_inventory.py`
- OSINT rows left for OSINT wiki `/phase1` paste (out of CCC surface)

---

## [2026-07-31] harness | federation skill autosync

- `sync_federation_cursor_skills.sh` auto-discovers CCC skills with `federation: true` (no hard-coded CANON list)
- Tagged: goal, to-issues, grill-with-docs, cursor-audit, super-audit, route, phase1-wire
- CCC `post-commit.sh` runs sync when skills / shared federation rules change
- Rule `.cursor/rules/cemini-federation-skill-sync.mdc` (agent reminder); `~/bin/sync-federation-cursor-skills`
- Also syncs `cemini-phase1-policy-wires.mdc` federation-wide

---

## [2026-07-31] skill | Phase-1 adopt-wire federation skill + inventory

- New `.cursor/skills/phase1-wire/SKILL.md` — `/phase1` / wire adopts; policy vs runtime vs `wont_wire`
- Concept `@concepts/phase1-adopt-wire.md` + entity `@entities/skills/phase1-wire.md`
- Inventory `scripts/phase1_adopt_inventory.py` → `briefs/2026-07-31_phase1-adopt-inventory.md` (CCC+OSINT)
- Policy rule `.cursor/rules/cemini-phase1-policy-wires.mdc` (K230–K233 steals)
- Ingest contract: CLAUDE.md step 12 + `ccc-wiki-workflow.mdc` Phase-1 after ADOPT/GO
- Sync: `phase1-wire` via `federation: true` auto-discover + post-commit
- Pilot: MemHarness/Tycho/AgentRadio/AskChem → `policy_wired`; SHarD → `wont_wire`; TipDrop CLAUDE bullets
- Skip Image-gen / 3D local wire backlog

---

## [2026-07-31] ingest | MemHarness + Tycho + AgentRadio + AskChem (K230–K233)

- **K230 — MemHarness (2607.28272):** reconstruct retrieved memory for current state; GRPO; negative-transfer fix. **ADOPT**; **GO** Apache `.local/adopts/MemHarness` (~39MB).
- **K231 — Tycho (2607.28287):** active abstraction; sim fidelity ≠ RHAE; build/use/bypass. **ADOPT**; **GO** Apache `.local/adopts/Tycho` (~2.5MB); game-dev ARC stub.
- **K232 — AgentRadio (2607.28430):** async threads/messages/wait-for-mentions; 62.1% vs 32.3% SWE-Atlas. **ADOPT**; **GO** Apache `.local/adopts/AgentRadio` (~13MB).
- **K233 — AskChem (2607.28618):** claim-centered DOI+quote retrieval + MCP; chemistry OOD. **ADOPT** pattern; **GO** MIT `.local/adopts/askchem` (~9.3MB).
- **Pages:** 4 sources + 4 concepts + 4 entities + brief stub + handoff; Phase-0 k230–k233; prod + David + poker.
- **Archive:** 4 PDFs → egress-fi `ccc/`.

---

## [2026-07-30] ingest | MTGuard + HANDBOOK + MCPApps HITL + CHILL + SHarD + VetClaw + AgentSnare + MemSecBench + CAM-DF (K221–K229)

- **K221 — MTGuard (2607.25297):** lifecycle static–dynamic MCP co-analysis; FPR 3.7%. **ADOPT**; **NO-GO** code.
- **K222 — HANDBOOK.md (2607.25398):** standing SOP following; best strict 36.2%. **ADOPT** eval posture; **NO-GO** install.
- **K223 — MCPApps empirical (2607.25635):** blocking approval **37.2%**. **ADOPT** HITL gate; study only.
- **K224 — CHILL-Harness (2607.25825):** advantage-margin orchestration. **ADOPT**; chill-dev **404 NO-GO**.
- **K225 — SHarD (2607.25890):** harness-distributed sandbox/skill-scan/tool-restrict; OWASP 23-test 100%. **ADOPT**; **GO** MIT `.local/adopts/agent-security-lab` + `shard-demo` (~24MB).
- **K226 — VetClaw (2607.26042):** veterinary OOD — **REFERENCE** only.
- **K227 — AgentSnare (2607.26998):** decoy Delay/Divert/Defuse; cybersec-primary. **ADOPT** awareness; **NO-GO** install.
- **K228 — MemSecBench (2607.27080):** WEF; persist 84.2% / W–E 50.3% / repair 56.1%. **ADOPT** checklist; **NO-GO** code.
- **K229 — CAM-DF (2607.27083):** scores≠decisions; 37% fewer tools live. **ADOPT**; **NO-GO** code.
- **Pages:** 9 sources + 8 concepts + 1 entity + brief stub + handoff; Phase-0 k221–k229; prod + David + poker; cybersec AgentSnare stubs.
- **Archive:** 9 PDFs → egress-fi `ccc/`.

---

# CCC Wiki — Operations Log

Append-only chronological record of wiki operations: bootstraps, ingests, sweeps, retractions. Newest entries on top.

---

## [2026-07-29] ops | Codex CLI adopt 0.145.0 + ChatGPT auth smoke PASS

- Entity `@entities/tools/openai-codex-cli.md`; script `scripts/adopt_codex_cli.sh` (synced from OSINT)
- Vendor path fixed (`…/bin/codex`); ChatGPT login; default model gpt-5.6-terra smoke OK

## [2026-07-27] prompt | v10.4 Priority #1 Atto · Priority #2 GuruWatcher

- **Priority stack:** Atto #1 · GuruWatcher #2 · everything else behind (XSP / TipDrop / family-tree / PM canary / poker / CeminiDFS still scored).
- **Updated:** `prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md` + gemini-runtime · `@concepts/deep-research-evaluation-prompt.md` · `@concepts/cross-wiki-routing.md`
- **Overlap field:** `guruwatcher overlap` (newsletter claim extract / price-level Discord / UW pollers / watch reconcile)
- **Sync:** OSINT `active_project_brief_targets.yaml` + `daily_research_config.yaml` + federation hub `federation_paths.yaml`

## [2026-07-24] ingest | Traceable Scholarship + Euclid-MCP + local agents + ACM + OpenForgeRL (K210–K214)

- **K210 — Traceable Scholarship (2607.20916):** citation-first, NO_EVIDENCE, page anchors, Scope Contract. **ADOPT**; **GO** MIT `.local/adopts/AIH-Infra` (~276KB).
- **K211 — Euclid-MCP (2607.21412):** Prolog via MCP; semantic RAG unfit for rules. **ADOPT**; **GO** Apache `.local/adopts/euclid-mcp` (~1.2MB).
- **K212 — Agentic coding without cloud (2607.21482):** local open-weight data-prep agents. **ADOPT**; **GO** MIT RRBench (~21MB); ns_core **NO-GO**.
- **K213 — Agentic Context Management (2607.21503):** five-primitive lifecycle. **ADOPT** checklist; no code.
- **K214 — OpenForgeRL (2607.21557):** harness-native RL via proxy+K8s. **ADOPT** checklist; official artifact **NO-GO**.
- **Archive:** 5 PDFs → egress-fi `ccc/`.

## [2026-07-23] ingest | ChainWatch + SLM ensemble + offensive ethics + IteraSim RAG (K206–K209)

- **K206 — ChainWatch (2607.19432):** session kill-chain MCP detection vs per-call gap. **ADOPT** checklist; **NO-GO** code; cybersec stubs.
- **K207 — SLM ensemble malware analysis (2607.20216):** hybrid evidence+debate; 35.30% vs ungrounded frontier. **ADOPT** orchestration; `slms_mal` **404 NO-GO**; cybersec domain stub.
- **K208 — Ethics offensive agents (2607.20255):** indeterminacy + HITL humility. **ADOPT** oversight posture; cybersec primary.
- **K209 — IteraSim RAG (2607.20346):** multi-stage retrieval + Architect/Writer/Reviewer. **ADOPT**; **GO** MIT `.local/adopts/iterasim-rag-public` (~5.4MB).
- **Archive:** 4 PDFs → egress-fi `ccc/`.

## [2026-07-22] ingest | Agents4GEOS + BioSecBench + LangGraph pathways + Agents in the Wild (K202–K205)

- **K202 — Agents4GEOS (2607.18557):** 52 MCP tools; curated skills + fresh-context subagents; solver-grounded quantities. **ADOPT**; **GO** BSD-3 `.local/adopts/agents4geos` (~2.3MB); GEOS **NO-GO** (>500MB).
- **K203 — BioSecBench-Surveillance (2607.19262):** deterministic structured grading; 16 model×harness; best ~50.2%. **ADOPT** eval methodology; biosec → cybersec stubs; Apache REFERENCE clone (~208KB).
- **K204 — LangGraph workflows (2607.19297):** repair loops, evidence gating, HITL interrupt/checkpoint. **ADOPT** recipes; full LangGraph clone **NO-GO** (>500MB).
- **K205 — Agents in the Wild (2607.19336):** verification + fallback + HITL deploy checklist. **ADOPT**; tutorial only.
- **Pages:** 4 sources + 4 concepts + 1 entity + brief stub + handoff; Phase-0 k202–k205; prod + David + poker; cybersec BioSec stubs.
- **Archive:** 4 PDFs → egress-fi `ccc/`.

## [2026-07-21] prompt | deep-research v10.3 — Atto emphasize

- **Did not already include Atto** — only Barone family-tree / `genealogy overlap` (v10.1–v10.2).
- **v10.3:** Atto = Priority #1 genealogy **product** (`Projects/atto`, `~/AttoVault/`, `atto-mcp`); family-tree = private dogfood.
- Updated: `prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md`, `prompts/deep-research-multi-wiki-eval-v10-gemini-runtime.md`, `@concepts/deep-research-evaluation-prompt.md`.
- New field: `atto overlap` (required on genealogy URLs); routing split productizable → Atto vs private digs → `Desktop/family/research/`.

---

## [2026-07-21] ingest | DataFlow NL2Pipeline + schema-MCP + solver-grounded + FlashRT + SWE-Pruner (K197–K201)

- **K197 — DataFlow-Harness (2607.16617):** NL2Pipeline gap; typed mutations + MCP registry + Skills; 93.3% pass; −72.5% cost vs vanilla CC. **ADOPT** checklist; WebUI **NO-GO**; **CONDITIONAL** `.local/adopts/DataFlow` (Apache, ~11MB).
- **K198 — Schema-bound MCP skills (2607.17012):** bounds before dispatch; MCP-prompt skills; live jobs. **ADOPT**; **GO** MIT `.local/adopts/nuance-mcp` (~1.2MB).
- **K199 — Smart-grid tutorial (2607.18147):** solver-grounded numerics. **ADOPT** rule; energy OOD; case code **NO-GO** (no SPDX).
- **K200 — FlashRT (2607.18171):** IR + measurement-gated optimize loop. **ADOPT** checklist; repo **404 NO-GO**.
- **K201 — SWE-Pruner Pro (2607.18213):** prune from backbone internals; ≤39% tokens. **ADOPT** principle; closed models keep K115; repo **NO-GO** (no SPDX).
- **Pages:** 5 sources + 5 concepts + 2 entities + brief stub + handoff; Phase-0 k197–k201; prod + David + poker; scp list extended.
- **Archive:** 5 PDFs → egress-fi `ccc/`; inbox cleared on success.

## [2026-07-20] ingest | MCP gateway + ToolVerse + TARS + BusinessCaseBench + 5G/6G survey (K190–K194)

- **K190 — Scalable MCP cloud gateway (2607.15593, Alibaba):** hybrid lexical+semantic Top-15 (98% recall); 8.9× selection time / 23.8× tokens; session affinity. **ADOPT** checklist; **NO-GO** Alibaba code; **CONDITIONAL-GO** `.local/adopts/agentgateway` (Apache-2.0, ~42MB).
- **K191 — ToolVerse (2607.15660, Meituan):** ~422 MCP envs / ~4438 tools; GUST dependency-graph tasks; Turn-Aware Relative Advantage. **ADOPT** graph + turn scoring; **NO-GO** install (no official artifact).
- **K192 — TARS (2607.15948):** ToM profiler + RAG in-IDE explanations; n=18 → 26% faster. **ADOPT** pattern; **GO** MIT `.local/adopts/tars` (~15MB); **NO-GO** Cursor VSIX drop-in.
- **K193 — BusinessCaseBench (2607.16057):** expert-solution → checklist rubrics; Standard vs Complete Answer. **ADOPT** methodology; **NO-GO** install.
- **K194 — 5G/6G agentic survey (2607.16066):** telecom OOD — **REFERENCE** source stub only (prefer brief over deepen).
- **Pages:** 5 sources + 4 concepts + 2 entities + brief stub + handoff; Phase-0 `scripts/adopt_k190_phase0.sh`…`k194`; prod briefs + David + poker steals; `scp_harness_briefs_to_prod.sh` extended.
- **Archive:** 5 PDFs → `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`; inbox cleared on success.

## [2026-07-18] cursor | federate adopted-geo-tools domain skill

- Extended `scripts/sync_federation_cursor_skills.sh` with `DOMAIN_SKILL_DIRS` — syncs SEO canon `adopted-geo-tools` → user-global + all workspaces (alongside CCC CANON_SKILLS).
- New entity `@entities/skills/adopted-geo-tools.md`. Skill uses absolute `SEO_ROOT` so helpers work from OSINT/tipdrop/Home/etc.
- Updated `@entities/skills/goal.md` deploy note + user-global `cemini-projects.mdc` skill table.

---

## [2026-07-18] ingest | FlowGuard MCP evidence-grounded detection (K189)

- **K189 — FlowGuard (2607.14754, Fudan):** signals ≠ runtime evidence for MCP security; TRIAGE→RECON→STRIKE→ANALYSIS→REFINEMENT; F1 0.879/0.942 on cmd injection / FS; 523 findings / 326 servers. **ADOPT** evidence bar; **NO-GO** install (no public artifact; name-collision repos rejected).
- Concept `mcp-security-signals-vs-runtime-evidence`; source; prod + hands-on briefs; `scripts/adopt_k189_phase0.sh`.
- **Cross-route:** cybersec stubs `mcp-security-evidence-grounded-detection` + source; handoff `wiki/briefs/2026-07-18_ccc-handoff-flowguard-mcp-security.md`.
- **David:** TipDrop `ccc-k189-mcp-evidence-not-signals`; **Poker:** `k189-mcp-evidence-bar-steal`.
- **Note:** K188 reserved for cybersec ARMOR++ (2607.15246) deepen — do not reuse for FlowGuard.
- PDF → egress-fi `ccc/`.

---

## [2026-07-17] ingest | preinstall gate + SearchOS + policy-as-code + ACP (K179–K182)

- **K179 — Setup weaponization (2607.15143):** install-gap; harness×model; deterministic pre-install gate. **ADOPT**; cybersec deepen. No code.
- **K180 — SearchOS (2607.15257):** SOCM explicit search state. **ADOPT** checklist; **GO** MIT clone `.local/adopts/SearchOS` (~106MB).
- **K181 — Satellite mission compiler (2607.14798):** OPA/Rego layered validation + MCP tools. **ADOPT** pattern; **GO** EUPL clone `.local/adopts/satellite-mission-compiler`.
- **K182 — ACP+MCP three-layer (2607.14919):** UI auth/interrupt via ACP; MCP at execution. **ADOPT**; **CONDITIONAL** Apache `sancho-acp-clients`; core Sancho 404.
- **Cross-route:** ARMOR++ 2607.15246 → cybersec (PDF egress `cybersec/`).
- **David:** TipDrop `ccc-k179`…`ccc-k182`; **Poker:** k179/k180/k182 steals.
- **Local adopts:** SearchOS + satellite-mission-compiler + sancho-acp-clients under `.local/adopts/` (gitignored).

---

## [2026-07-16] ingest | optimizer compounding + MCP contract + graceful degradation (K171–K173)

- **K171 — Do Agent Optimizers Compound? (2607.14004, RELAI):** continual two-phase Terminal-Bench eval; GEPA transfers below baseline; only regression-in-loop compounds. **ADOPT** compounding questions; **NO-GO** `relai-ai/Continual-Learning-Terminal-Bench` (no LICENSE).
  - Concept `agent-optimizer-compounding-and-regression-control`, entity, prod brief, `scripts/adopt_k171_phase0.sh`
  - **David:** `tipdrop-workspace-kit/briefs/2026-07-16_ccc-k171-regression-in-loop-david.md`
  - **Poker:** `agents/devfun-poker-arena/briefs/2026-07-16_k171-optimizer-compounding-steal.md`
- **K172 — Contract-grounded BT via coding agent MCP (2607.12220):** MCP skill contract + validation gate before execute. Robotics empirics; **ADOPT** pattern; **NO-GO** unlicensed webviewer/tb3-mcp; ros-mcp-server Apache CONDITIONAL not cloned.
  - Concept `mcp-contract-grounded-synthesis-and-validation-gate`, entity, briefs, Phase-0
  - **David / Poker:** ccc-k172 + poker contract-style tool surface
- **K173 — JW-ASTClaw (2607.13549):** MCP multi-agent + cloud→local→rules fallback. **ADOPT** checklist; no public code.
  - Concept `mcp-multi-agent-graceful-degradation-stack`, briefs, Phase-0
- **Cross-route:** AgentHOI 2607.13881 → image-gen (WATCH, no LICENSE); ExpressionCueLens 2607.13924 → TipDrop companion-tone David brief (`ccc-k174-…`)
- **Local adopt:** none (all paper-primary repos unlicensed or absent; ros-mcp skipped)
- **Archive:** CCC PDFs → egress `ccc/`; AgentHOI → egress `image-gen/`
- **Note:** K170 already used today (grok-build / git-secrets OSINT brief)

---

## [2026-07-16] brief | K171 AgentsCAD MCP geometry grounding

- Brief: `briefs/2026-07-16_k171-agentscad-mcp-geometry-grounding-prod.md` → scp `cemini-prod:/opt/cemini/briefs/`
- Steal: MCP tool-grounding required for spatial transforms (from @3d-printing-wiki AgentsCAD ingest)
- No local code adopt

---

## [2026-07-15] ingest | SLM harness adaptation + harness-evolution eval (K168–K169)

- **K168 — Better Harnesses, Smaller Models (2607.08938, CMU):** failure-mode→adaptation map; SLM cost recovery via tailored harness. **ADOPT** taxonomy + diagnostic loop; **NO-GO** `malusamayo/migration-analysis` (no LICENSE; replication package). Magnitude claims `[NEEDS VERIFICATION]` pending K169 gate.
  - Created/finalized `concepts/failure-mode-harness-adaptation-mapping.md`, source, entity, prod brief, `scripts/adopt_k168_phase0.sh`
  - **David:** `tipdrop-workspace-kit/briefs/2026-07-15_ccc-k168-slm-harness-adaptation-david.md` (distinct from TipDrop OSINT K168 Middy brief)
  - **Poker:** `agents/devfun-poker-arena/briefs/2026-07-15_k168-slm-harness-for-repetitive-decides.md`
- **K169 — Rethinking Harness Evolution Eval (2607.12227, AI2/UW):** matched-budget protocol; harness evolution ≤ test-time scaling on Terminal-Bench 2.1; weak held-out generalization. **ADOPT** five-row checklist; **NO-GO** `rethinking-harness-evolution/code` (no LICENSE file; paid E2B).
  - Created/finalized `concepts/harness-evolution-vs-test-time-scaling-baseline.md`, source, entity, prod brief, `scripts/adopt_k169_phase0.sh`
  - **Poker:** `agents/devfun-poker-arena/briefs/2026-07-15_k169-eval-discipline-for-harness-tweaks.md`
- **Wired:** HarnessX/RHO/SEAGym/K164 caveat links, index, scp script, handoff brief, policy hands-on
- **Archive:** both PDFs → egress-fi `ccc/`
- **Local adopt:** none (both repos NO-GO on license; <500MB but unlicensed)
- **ID note:** TipDrop OSINT occupied bare `k167`/`k168` filenames today (12-factor / Middy) — CCC uses K168/K169 with `ccc-k168-` David prefix

## [2026-07-15] prompt | v10.2 Priority #1 + PM LP canary

- Priority #1: **XSP killer**, **TipDrop.io**, **family-tree**, **PM LP canary (K166)** (+ **wikis always-on**)
- Poker + CeminiDFS: still active — always report applies; #1 only wins ties
- Revenue lens unchanged
- PM paths: `compose.polymarket.canary.yml`, `docs/pm-lp-k166-phase1-canary.md`, overlap `pm-canary`
- Concept + cross-wiki-routing notes: `@concepts/deep-research-evaluation-prompt.md` v10.2

## [2026-07-14] hands-on | K155/K162/K164 harness policy patches

- Encoded ADOPT steals as operational policy (K124-style): `/goal` SC tags, `ccc-wiki-workflow.mdc`, completion-gates K162 ladder
- Hands-on brief: `briefs/2026-07-14_k162-k164-k155-harness-policy-hands-on.md`
- TipDrop: `hierarchical-skill-tree-routing.md` stub (David K164)
- Poker arena: `config/hu_capability_tree.json` + `examples/capability_tree.py` + tests
- Prior ingest (same day): K162 RSI survey + K164 hierarchical skill stack wiki pages / phase-0 scripts

## [2026-07-14] ingest | RSI survey + hierarchical skill stack (K162–K164)

- **K162 — RSI survey (2607.07663):** two-axis taxonomy + verification hierarchy. REFERENCE — cited GitHub 404 at Phase-0.
  - Created `concepts/bounded-self-refinement-vs-rsi-taxonomy.md`, source, brief, `scripts/adopt_k162_phase0.sh`
  - No David adopt; no local clone
- **K164 — Hierarchical skill architecture (2607.11138):** capability tree + LIFO stack + lazy manifests + fencing. REFERENCE + ADOPT patterns.
  - Created `concepts/hierarchical-skill-stack-lazy-orchestration.md`, source, brief, `scripts/adopt_k164_phase0.sh`
  - **David:** `tipdrop-workspace-kit/briefs/2026-07-14_k164-hierarchical-skill-tree-adopt.md`
  - **Poker:** `agents/devfun-poker-arena/briefs/2026-07-14_k164-hierarchical-tool-routing-steal.md`
- **Wired:** continual-harness, completion-gates, lazy-tool, mcp-context-optimization, subagent-orchestration, index, scp script, handoff brief
- **Archive:** both PDFs → egress-fi `ccc/`
- **Local adopt:** none installable <500MB (no public repos)

## [2026-07-13] ingest | MILES + QSP memory + DeepSearch + TrustX (K153–K157)

- **K153 — MILES (2607.06974, UNSW):** modular instruction memory + learnable coarse-to-fine selection for sequential reasoning. REFERENCE — no repo.
  - Created `concepts/modular-instruction-memory-learnable-selection.md`, source, brief, `scripts/adopt_k153_phase0.sh`
- **K154 — Ensemble QSP (2607.07666, AstraZeneca):** three-layer bounded memory + eviction; QSP domain off prod. REFERENCE.
  - Created `concepts/hierarchical-bounded-agent-memory.md`, source, brief, `scripts/adopt_k154_phase0.sh`
- **K156 — DeepSearch-World (2607.07820):** verifiable offline search env + self-distillation. WATCH — code promised not public.
  - Created `concepts/verifiable-search-agent-environment.md`, source, brief, `scripts/adopt_k156_phase0.sh`
- **K157 — TrustX ARC (2607.09586, RAI Institute):** 12-dimension agent risk tiering + coding-assistant extension. REFERENCE.
  - Created `concepts/trustx-agent-risk-classification.md`, source, brief, `scripts/adopt_k157_phase0.sh`
  - **David:** `tipdrop-workspace-kit/briefs/2026-07-13_k157-trustx-agent-risk-tier-adopt.md`
- **Wired:** metamemory, dual-representation, channel-fracture, cage-1, index, scp script, handoff brief
- **Archive:** all 4 PDFs → egress-fi `ccc/`
- **Note:** K155 = prior PolyWorkBench rubrics cross-wiki commit

## [2026-07-10] ingest | CAGE-1 + PolyWorkBench (K151–K152)

- **K151 — CAGE-1 (2607.03510, Roopam W. Sure):** enterprise agent governance eval; **Prebind Assurance** before binding actions; 12 dimensions. CCC-primary. **NOT** lahlfors cybernetic-governance-engine.
  - Created `concepts/cage-1-enterprise-agent-governance-eval.md`, `sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md`, `sources/brief-k151-...`, `briefs/2026-07-10_k151-cage-1-prebind-assurance-prod.md`, `scripts/adopt_k151_phase0.sh`, `wiki/briefs/2026-07-10_ccc-handoff-cage-polyworkbench-ingest.md`
  - **David:** `tipdrop-workspace-kit/briefs/2026-07-10_k151-prebind-assurance-adopt.md`
  - Verdict **REFERENCE** — no product repo; adopt Prebind checklist
- **K152 — PolyWorkBench (2607.06008, Tencent/BJTU):** 67 multilingual long-horizon tasks; hybrid structural+executable+semantic eval; client sensitivity (Claude Code, OpenClaw).
  - Created `concepts/multilingual-long-horizon-agent-eval.md`, `sources/arxiv-polyworkbench-multilingual-long-horizon-2607.06008.md`, `sources/brief-k152-...`, `briefs/2026-07-10_k152-polyworkbench-multilingual-eval-prod.md`, `scripts/adopt_k152_phase0.sh`
  - Verdict **REFERENCE** — no public repo at Phase-0; no David adoption
- **Wired:** agent-completion-verification-gates, gatekeeper-layered, client-as-first-order, agent-five-gate, etclovg, skill-vetting, orchestration-option-quantitative-metrics, recoverable-tool-reliability, algorithmic-impermeability, index, scp script
- **Archive:** both PDFs → egress-fi `ccc/`

## [2026-07-09] ingest | LCA algorithmic impermeability (K150)

- **Source:** arXiv 2607.06531 — Large Cancer Assistant; model-agnostic orchestration via algorithmic impermeability, SIP, SDR. **Clinical off-domain**; harness patterns only.
- **Created:** `concepts/algorithmic-impermeability-model-agnostic-orchestration.md`, `sources/arxiv-large-cancer-assistant-lca-2607.06531.md`, `sources/brief-k150-...`, `briefs/2026-07-09_k150-algorithmic-impermeability-orchestration-prod.md`, `scripts/adopt_k150_phase0.sh`
- **Updated:** handoff-validity, multi-agent-evidence-artifact-layers, model-native-vs-tool-mediated, agentic-online-rl, code-as-agent-harness, subagent-orchestration, bioinsight source, index
- **Verdict:** REFERENCE — no public repo; no David/TipDrop adoption
- **Archive:** `cemini-egress-fi:.../arxiv-2607.06531-...pdf`

## [2026-07-07] ingest | Agentic online-RL + HexStrike + ShopX (K139–K141)

- **K139 — AReaL / next-gen agentic RL (2607.01120, Ant Group):** self-evolving agents bottlenecked by online-RL systems (ATDP / data proxy / evolution control plane), not RL algos. CCC-primary.
  - Created `concepts/agentic-online-rl-self-evolving-systems.md`, `entities/tools/areal.md`, `sources/arxiv-next-gen-agentic-rl-self-evolving-2607.01120.md`, `sources/brief-k139-...`, `briefs/2026-07-07_k139-agentic-online-rl-self-evolving-prod.md`, `scripts/adopt_k139_phase0.sh`. Verdict **REFERENCE/WATCH** (Apache-2.0, no local RL).
- **K140 — HexStrike-AI orchestration (2607.02873, USTC):** driving client is first-order (2.1× gap, same model); solve 55.4%→72.0% via harness fixes. **Cybersec-primary**, CCC harness stub.
  - Created `concepts/client-as-first-order-harness-factor.md`, `briefs/2026-07-07_ccc-handoff-hexstrike-client-orchestration-ingest.md`, `sources/brief-k140-...`. Cybersec: source + `concepts/security-tool-orchestration-determinants.md` + lab checklist brief.
- **K141 — ShopX (2606.31693, Taobao):** model-native vs tool-mediated fulfillment harness lesson. Off-domain e-commerce; **REFERENCE** only.
  - Created `concepts/model-native-vs-tool-mediated-fulfillment.md`, `sources/arxiv-shopx-intent-to-item-fulfillment-2606.31693.md`.
- **Wired:** continual-harness cluster, harness-layer-competition, code-as-agent-harness, mcp-context-optimization, subagent-orchestration, etclovg, meta handoff briefs, index.
- **Archive:** AReaL + ShopX → egress-fi `ccc/`; HexStrike → egress-fi `cybersec/`.
- **Cross-wiki:** cybersec `@cybersecurity-wiki/concepts/security-tool-orchestration-determinants.md` (bidirectional).

## [2026-07-07] ingest | Steerability via constraints — coding-agent oversight (K138)

- **Source:** arXiv 2607.02389 — substrate constraints + ~200 LoC docs CLI; backdoor recall 54.5% → 90.9%
- **Created:** `sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md`, `sources/brief-k138-substrate-constraints-agent-oversight-2026-07-07.md`, `entities/tools/openshell.md`, `briefs/2026-07-07_k138-substrate-constraints-agent-oversight-prod.md`
- **Expanded:** `concepts/substrate-constraints-coding-agent-oversight.md`, `briefs/2026-07-07_ccc-handoff-steerability-substrate-ingest.md`
- **Updated:** `agent-completion-verification-gates`, `skill-vetting`, `subagent-orchestration`, `mcp-context-optimization`, `etclovg-harness-layers`, `code-as-agent-harness`, `super-audit`, `seclaw-agent-security-evaluation`, `lazy-tool`, `index.md`
- **Phase-0:** `scripts/adopt_k138_phase0.sh` — REFERENCE; OpenShell Apache-2.0; David checklist on cybersec
- **Archive:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.02389-2607-02389v1-steerability-via-constraints-a-subs.pdf`
- **Cross-wiki:** cybersec primary `@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md`

## [2026-07-10] prompt | v10.1 family-tree replaces castle-sim

- **Updated:** `prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md` + gemini-runtime — co-primary #4 = **family-tree / computational genealogy** (`Desktop/family/`, OSINT K153/K154)
- **Demoted:** castle-sim → legacy deprioritized
- **Added:** `genealogy overlap` field (8 modules); value hypothesis for personal projects
- **Context:** OSINT session 2026-07-09 — K153/K154 ingest; private Barone pedigree sprint
- **Updated:** `deep-research-evaluation-prompt`, `cross-wiki-routing`

## [2026-07-06] prompt | v10 revenue-first link evaluation lens

- **Created:** `prompts/deep-research-multi-wiki-eval-v10-2026-07-06.md` + `v10-gemini-runtime.md` — supersedes v9 for day-to-day use
- **Lens shift:** primary question = "how does this make us money?" — project fit + revenue path + combo plays; license/ToS demoted to implementation notes
- **Tiers:** Integrate / Extract / Watch / Context / Pass (maps to v9 Adopt/Steal-from/Defer/Reference-only/Reject)
- **Updated:** `deep-research-evaluation-prompt`, `cross-wiki-routing`, `index.md`, `README.md`, `CLAUDE.md`

## [2026-07-03] brief audit | K109 stub + cross-wiki handoffs tracked

- **Gitignore fix:** `/briefs/` only — `wiki/briefs/` cross-wiki handoffs now versioned
- **Brief stub (1):** K109 Bayesian-Agent harness cluster prod
- **Concept stub (1):** `cognitive-heuristics-llm-vuln-detection` — cybersec routing (2606.30587)
- **Handoffs tracked (13):** full `wiki/briefs/` catalog incl. Jul 1–3 cybersec ingests
- **Updated:** `ccc-cross-wiki-handoff-briefs`, `confidence-aware-tool-orchestration`, `index.md`

## [2026-07-02] ingest | K137 AutoMem metamemory cognitive skill

- **Preingest:** 1 NEW (`2607.01224`)
- **Source:** Stanford AutoMem — scaffold + proficiency meta-LLM loops
- **Concept:** `metamemory-scaffold-proficiency-training`
- **Entity:** `automem-stanford-cognitive-skill` (no LICENSE — REFERENCE; not verygoodplugins/automem)
- **Brief:** `briefs/2026-07-02_k137-automem-metamemory-cognitive-skill-prod.md` → scp prod
- **Phase-0:** `scripts/adopt_k137_phase0.sh`
- **Pages updated:** `agent-memory-stack-comparison`, `agentic-memory-cross-scenario-generality`, `failed-trajectory-harness-repair`, `long-thread-context-decay`, `claude-mem`, `index.md`, `sweeps/2026-07-02-daily.md`
- **Archive:** PDF → egress-fi

## [2026-07-01] ingest | K136 Agentic orchestration options ABPM

- **Preingest:** 1 NEW (`2606.31518`)
- **Source:** TUM ABPM OO1–OO4 classification + light-sensing eval
- **Concepts (2):** `agentic-orchestration-options-abpm`, `orchestration-option-quantitative-metrics`
- **Entity (1):** `simple-agentic-scenario` (no LICENSE — REFERENCE)
- **Brief:** `briefs/2026-07-01_k136-agentic-orchestration-options-abpm-prod.md` → scp prod
- **Phase-0:** `scripts/adopt_k136_phase0.sh`
- **Pages updated:** `subagent-orchestration`, `etclovg-harness-layers`, `model-harness-six-responsibilities`, `handoff-validity`, `plan-then-execute`, `scatter-gather`, `gatekeeper-layered-agent-evaluation`, `index.md`, `sweeps/2026-07-01-daily.md`
- **Archive:** PDF → egress-fi

## [2026-06-30] brief audit | K115–K127 prod brief discoverability stubs

- **Gap:** 11 local `briefs/` on prod (scp batch K115–K127) lacked wiki discoverability stubs; K125 ESAA Windows handoff also missing
- **Brief stubs (11):** K115–K121 prod; K122 claim-drift; K126 skills; K127 AOHP; K125 ESAA Windows handoff
- **Backlinks:** `--fix-bidirectional --apply` on 35 target pages (concepts, entities, arXiv sources)
- **Index:** 11 new rows in `sources/` table
- **Lint:** exit 0 (pre-existing cross-wiki dangling links unchanged)

## [2026-06-30] ingest | K135 Clarus research collaboration infrastructure

- **Preingest:** 1 NEW (`2606.30246`)
- **Source:** Clarus web-scale scientific collaboration
- **Concept:** `web-scale-scientific-collaboration-infrastructure`
- **Entity:** `clarus` (SaaS REFERENCE — no public repo)
- **Brief:** `briefs/2026-06-30_k135-clarus-research-collaboration-prod.md` → scp prod
- **Phase-0:** `scripts/adopt_k135_phase0.sh`
- **Pages updated:** `paperclaw`, `xcientist`, `deep-scientist`, `externalized-research-synthesis-validation`, `multi-agent-evidence-artifact-layers`, `internet-of-agentic-ai-ioai`, `index.md`, `sweeps/2026-06-30-daily.md`
- **Archive:** PDF → egress-fi

## [2026-06-29] brief audit | K134 + K132 + federation batch wiki stubs

- **Gap:** K134 brief referenced `@wiki/entities/tools/codebase-memory-mcp.md` — page missing on CCC wiki (existed on OSINT only)
- **Entity (1):** `codebase-memory-mcp` — federation MCP adoption canon (CONDITIONAL-GO)
- **Brief stubs (3):** K134 prod; K132 local adoptions; K122–K126 federation batch
- **Source stub (1):** `eval-github-repos-plan-multi-wiki-2026-06-29` — cross-wiki pointer to OSINT K134 eval
- **Updated:** `index.md`, `cursor-ide-workspace.md`; OSINT entity backlink

---

## [2026-06-28] prompt | deep-research eval v9 — active projects + TipDrop

- **Created:** `prompts/deep-research-multi-wiki-eval-v9-2026-06-28.md` — supersedes v8 for day-to-day use
- **Surface 1 reframed:** legacy Cemini Financial Suite equity stack deprioritized → **Cemini active prod bots** (XSP killer, dev.fun poker arena, PM/Kalshi exploratory)
- **Surface 10 added:** **TipDrop.io** (David's Discord signals SaaS) with compliance-first eval
- **Shipped inventories:** xsp-killer, devfun-poker-arena, castle-sim, tipdrop-workspace-kit
- **Overlap fields:** poker-arena, xsp-killer, tipdrop (+ existing world-cup-bot, wc-ticket-monitor, CeminiDFS)
- **Updated:** `wiki/concepts/deep-research-evaluation-prompt.md`, `cross-wiki-routing.md`, `index.md`, `README.md`, `CLAUDE.md`

---

---

---

---

---

---

---

---

---

---

---

## [2026-06-27] ingest | K129 tool reliability + confidence orchestration (2 arXiv)

- **Preingest:** 2 NEW (`2606.25819`, `2606.26904`)
- **Sources (2):** ToolBench-X hazards; Robust-TO confidence orchestration
- **Concepts (2):** `recoverable-tool-reliability-hazards`, `confidence-aware-tool-orchestration`
- **Entity (1):** `toolbench-x` (LICENSE unverified — REFERENCE)
- **Briefs:** `briefs/2026-06-27_k129-tool-reliability-orchestration-prod.md`; `@image-gen-wiki/briefs/2026-06-27_k129-robust-to-confidence-tool-orchestration-handoff.md`
- **Phase-0:** `scripts/adopt_k129_phase0.sh`
- **Pages updated:** `gatekeeper-layered-agent-evaluation`, `etclovg-harness-layers`, `lazy-tool`, `index.md`, `sweeps/2026-06-27-daily.md`
- **Archive:** 2 PDFs → egress-fi

## [2026-06-26] ingest | K128 MemProbe memory recovery audit

- **Preingest:** 1 NEW (`2606.24595`)
- **Source:** MemProbe hidden user-state recovery benchmark
- **Concept:** `hidden-user-state-recovery-audit`
- **Entity:** `memprobe` (CC-BY-4.0, REFERENCE)
- **Brief:** `briefs/2026-06-26_k128-memprobe-memory-recovery-prod.md` → scp prod
- **Phase-0:** `scripts/adopt_k128_phase0.sh`
- **Pages updated:** `agent-memory-stack-comparison`, `worldmemarena`, `channel-fracture`, `multi-factor-agentic-memory`, `claude-mem`, `index.md`, `sweeps/2026-06-26-daily.md`
- **Archive:** PDF → egress-fi

## [2026-06-25] adopt | Federation Cursor skills + prod brief batch scp

- **Sync:** `scripts/sync_federation_cursor_skills.sh` — goal + to-issues + grill-with-docs → 18 workspaces + user-global
- **Legacy:** `sync_goal_skill_to_workspaces.sh` delegates to federation sync
- **Prod brief:** `briefs/2026-06-25_k122-k126-federation-cursor-harness-adoptions-cemini-prod.md`
- **Prod scp:** `scripts/scp_harness_briefs_to_prod.sh` → `cemini-prod:/opt/cemini/briefs/` (K115–K127 harness batch)
- **Global rule:** `~/.cursor/rules/cemini-projects.mdc` — federation skills table

## [2026-06-25] ingest | K125 memory orchestration cluster (4 arXiv)

- **Preingest:** 4 NEW (`2604.07065`, `2606.22485`, `2606.23752`, `2606.24535`)
- **Sources (4):** TaaS MCP trust; VADAOrchestra; ESAA-Conversational; governed fleet memory (MemClaw)
- **Concepts (4):** `mcp-trust-orchestration-collaboration`, `neurosymbolic-adaptive-reasoning-workflows`, `event-sourced-poly-agent-handoff`, `governed-fleet-shared-memory`
- **Entities (3):** `esaa-conversational` (CONDITIONAL-GO Windows), `memclaw`, `argusfleet` (REFERENCE — repo 404)
- **Brief stubs (6):** K125 prod + cross-wiki; K124×2 + K123 brief audit stubs
- **Cross-wiki briefs:** `@osint-wiki/briefs/2026-06-25_k125-vadaorchestra-osint-handoff.md`; `@cybersecurity-wiki/briefs/2026-06-25_k125-memclaw-fleet-memory-governance-handoff.md`
- **Local briefs:** `briefs/2026-06-25_k125-memory-orchestration-cluster-prod.md`, `briefs/2026-06-25_k125-esaa-windows-handoff.md`
- **Phase-0:** `scripts/adopt_k125_phase0.sh`
- **Pages updated:** `channel-fracture`, `handoff-validity`, `agent-memory-stack-comparison`, `subagent-orchestration`, `cross-wiki-routing`, `index.md`, `sweeps/2026-06-25-daily.md`
- **Archive:** 4 PDFs → egress-fi

## [2026-06-24] adopt | Cursor /goal skill — federation-wide deploy

- **Skill:** `.cursor/skills/goal/SKILL.md` + `cemini-goal-skill.mdc` rule
- **Sync:** `scripts/sync_goal_skill_to_workspaces.sh` → 18 workspaces + `~/.cursor/skills/goal/`
- **Wiki:** `entities/skills/goal.md`; `full-prompt-goal-template` Cursor note
- **Global:** `~/.cursor/rules/cemini-goal-skill.mdc`, `cemini-projects.mdc` /goal section

## [2026-06-24] adopt | K124 harness policy — pattern steals (no tool install)

- **Target:** hands-on — rules + schema + `/goal` + vetting + CPR + flaw template
- **Brief:** `briefs/2026-06-24_k124-harness-policy-hands-on.md`
- **Patches:** `.cursor/rules/ccc-wiki-workflow.mdc`, `CLAUDE.md`, `full-prompt-goal-template`, `skill-vetting` (steps 12–13), `cpr-context-compression`, `prompts/harness-flaw-record-template.md`
- **Steals:** evidence artifact layers, six-responsibility audit, diverse-trace skill promotion, rubric-gated compact, selective crystallization
- **NO-GO:** PaperClaw/Fara prod install (unchanged)

## [2026-06-24] ingest | K124 harness survey + memory cluster + PaperClaw

- **Preingest:** 7 NEW (`2606.20683`, `2606.20785`, `2606.20997`, `2606.22610`, `2606.23127`, `2606.23525`, `2606.24151`)
- **Sources (7):** harness survey; Fara CUA; BioInsight; PaperClaw; AFTER procedural memory; SelfCompact; Metis
- **Concepts (6):** `model-harness-six-responsibilities`, `scalable-cua-training-pipeline`, `multi-agent-evidence-artifact-layers`, `procedural-memory-transfer-after`, `self-compacting-adaptive-context`, `dual-representation-agent-memory`
- **Entities (3):** `paperclaw`, `fara`, `awesome-agent-engineering` (all MIT)
- **Pages updated (14):** `etclovg-harness-layers`, `code-as-agent-harness`, `externalized-research-synthesis-validation`, `xcientist`, `cpr-context-compression`, `long-thread-context-decay`, `agent-memory-stack-comparison`, `specification-driven-scientific-workflow-management`, `subagent-orchestration`, `cross-wiki-routing`, `skill-vetting`, `deep-scientist`, `index.md`, `sweeps/2026-06-24-daily.md`
- **Phase-0:** `scripts/adopt_k124_phase0.sh` — PaperClaw/Fara/Awesome MIT; others REFERENCE
- **Brief:** `briefs/2026-06-24_k124-harness-memory-research-cluster-prod.md`
- **Raw:** 7 PDFs → egress-fi `cemini-egress-fi:/opt/cemini-bulk/research/ccc/`; inbox cleared

## [2026-06-23] ingest | K123 DIA + agentic web gaps + cross-model verify + AOHP

- **Preingest:** 4 NEW (`2606.19319`, `2606.20120`, `2606.20570`, `2606.23449`)
- **Sources (4):** DIA enterprise data; dual-agent protocol translation; Agentverse gap taxonomy; AOHP OS harness
- **Concepts (4):** `autonomous-coding-agents-enterprise-data`, `cross-model-verified-agent-translation`, `agentic-web-infrastructure-gap-taxonomy`, `os-level-agent-harness-android`
- **Entity (1):** `aohp` (Apache-2.0)
- **Pages updated (14):** `agent-first-web-framework`, `internet-of-agentic-ai-ioai`, `gatekeeper-layered-agent-evaluation`, `handoff-validity-agent-harness`, `llm-as-code-agentic-programming`, `system-scaling-harness-agentic-ai`, `runtime-harness-interface-adaptation`, `code-as-agent-harness`, `specification-driven-scientific-workflow-management`, `index.md`, `sweeps/2026-06-23-daily.md`
- **Phase-0:** `scripts/adopt_k123_phase0.sh` — AOHP Apache-2.0; others REFERENCE
- **Brief:** `briefs/2026-06-23_k123-dia-agentic-web-aohp-prod.md`
- **Raw:** 4 PDFs → `raw-sources/`; inbox cleared

## [2026-06-22] adopt | K126 mattpocock skills + K122 claim-drift goal hygiene

- **Skills installed:** `.cursor/skills/to-issues`, `.cursor/skills/grill-with-docs` (MIT, mattpocock/skills)
- **Wiki catalog (2):** `entities/skills/to-issues.md`, `entities/skills/grill-with-docs.md`
- **Updated:** `entities/tools/mattpocock-skills.md`, `entities/patterns/full-prompt-goal-template.md` (claim-drift SC), `index.md`
- **Phase-0:** `scripts/adopt_k126_phase0.sh` — MIT pass; nvidia/skills REFERENCE only
- **Briefs (local):** `briefs/2026-06-22_k126-nvidia-mattpocock-skills-adopt.md`, `briefs/2026-06-22_k122-xcientist-claim-drift-prod.md`

## [2026-06-22] cross-wiki | K126 OSINT — agent skill Adopt stubs

- **New (2):** `entities/tools/nvidia-skills.md`, `entities/tools/mattpocock-skills.md` — routing stubs from OSINT links.docx eval
- **Updated:** `concepts/claude-code-skills-md-institutional-memory.md`, `wiki/index.md`
- **Brief (local):** `briefs/2026-06-22_k126-nvidia-mattpocock-skills-adopt.md` (gitignored)

## [2026-06-22] ingest | K122 XCIENTIST claim drift + research harness

- **Preingest:** 1 NEW (`2606.18874`)
- **Source (1):** XCIENTIST externalized research synthesis and validation
- **Concepts (2):** `claim-drift-automated-research`, `externalized-research-synthesis-validation`
- **Entity (1):** `xcientist` (OpenDFM/Xcientist, MIT)
- **Pages updated (12):** `agent-completion-verification-gates`, `failed-trajectory-harness-repair`, `system-scaling-harness-agentic-ai`, `handoff-validity-agent-harness`, `gatekeeper-layered-agent-evaluation`, `specification-driven-scientific-workflow-management`, `agent-rubrics-self-correction`, `code-as-agent-harness`, `deep-scientist`, `index.md`, `sweeps/2026-06-22-daily.md`
- **Phase-0:** `scripts/adopt_k122_phase0.sh` — Xcientist MIT
- **Brief:** `briefs/2026-06-22_k122-xcientist-claim-drift-prod.md`
- **Raw:** 1 PDF → `raw-sources/`; inbox cleared

## [2026-06-21] ingest | K121 TokenPilot + SafeClawBench + gatekeeper eval

- **Preingest:** 3 NEW (`2606.17016`, `2606.18356`, `2606.18422`)
- **Sources (3):** TokenPilot cache context; SafeClawBench staged security; Gatekeepers layered VQE eval
- **Concepts (3):** `prompt-cache-aligned-context-management`, `safeclawbench-staged-security-endpoints`, `gatekeeper-layered-agent-evaluation`
- **Entity (1):** `lightmem2` (MIT, TokenPilot integrated)
- **Pages updated (14):** `token-economics-and-prompt-caching`, `tool-response-context-pruning-summarization`, `mcp-context-optimization`, `three-cache-architecture`, `seclaw-agent-security-evaluation`, `defenseclaw`, `agent-completion-verification-gates`, `failed-trajectory-harness-repair`, `agent-rubrics-self-correction`, `index.md`, `sweeps/2026-06-21-daily.md`
- **Cross-wiki:** `@cybersecurity-wiki/concepts/safeclawbench-staged-agent-security.md`
- **Phase-0:** `scripts/adopt_k121_phase0.sh` — LightMem2 MIT; SafeClawBench HF dataset
- **Brief:** `briefs/2026-06-21_k121-tokenpilot-safeclaw-gatekeepers-prod.md`
- **Raw:** 3 PDFs → `raw-sources/`; inbox cleared

## [2026-06-21] prompt | v8 deep-research multi-wiki eval — shipped OSS projects

- **Created:** `prompts/deep-research-multi-wiki-eval-v8-2026-06-21.md` — supersedes v7 for day-to-day use
- **Shipped stack added:** `wc-ticket-monitor`, `CeminiDFS`, `cemini-federation-hub` (inventory + overlap fields)
- **Infra fix:** `cemini-librarian` offline 2026-06-14 → egress-fi archive + `federation_paths.yaml` laptop grep
- **Updated:** `concepts/deep-research-evaluation-prompt.md`, `concepts/cross-wiki-routing.md`, `index.md`, `README.md`, `CLAUDE.md`

## [2026-06-20] ingest | K120 User as Code + DynAMO orchestration

- **Preingest:** 2 NEW (`2606.16707`, `2606.19382`)
- **Sources (2):** User as Code executable memory; DynAMO topological scheduling
- **Concepts (2):** `executable-user-memory-user-as-code`, `plan-then-execute-topological-orchestration`
- **Entities (2):** `user-as-code` (Apache-2.0 CONDITIONAL-GO); `dynamo-orchestration` (REFERENCE)
- **Pages updated (12):** `agent-memory-stack-comparison`, `claude-mem`, `llm-as-code-agentic-programming`, `dynamic-workflow-orchestrator-off-model`, `tool-response-context-pruning-summarization`, `scatter-gather`, `handoff-validity-agent-harness`, `graphflow-verifiable-agent-workflows`, `subagent-orchestration`, `index.md`, `sweeps/2026-06-20-daily.md`
- **Phase-0:** `scripts/adopt_k120_phase0.sh` — both Apache-2.0; UaC laptop-only; DynAMO REFERENCE
- **Brief:** `briefs/2026-06-20_k120-user-as-code-dynamo-prod.md`
- **Raw:** 2 PDFs → `raw-sources/`; inbox cleared

## [2026-06-19] ingest | K119 Agent-first web + EDA handoff validity

- **Preingest:** 2 NEW (`2606.19116`, `2606.19795`)
- **Sources (2):** Agent-first web redesign; Agentic EDA handoff survey
- **Concepts (2):** `agent-first-web-framework`, `handoff-validity-agent-harness`
- **Pages updated (14):** `geo-seo-claude`, `channel-fracture`, `internet-of-agentic-ai-ioai`, `webwright`, `subagent-orchestration`, `specification-driven-scientific-workflow-management`, `agentic-pm-review-artifacts`, `agent-completion-verification-gates`, `mcp-context-optimization`, `index.md`, `sweeps/2026-06-19-daily.md`
- **Cross-wiki:** `@seo-wiki/concepts/agent-first-web-atml-framework.md`
- **Phase-0:** `scripts/adopt_k119_phase0.sh` — both **REFERENCE**; GEO routing to seo-wiki
- **Brief:** `briefs/2026-06-19_k119-agent-first-web-eda-handoff-prod.md`
- **Raw:** 2 PDFs → `raw-sources/`; inbox cleared

## [2026-06-18] ingest | K118 Pegasus specification-driven scientific workflow

- **Preingest:** 1 NEW (`2606.18425`)
- **Source (1):** From Specification to Execution — Pegasus AI-assisted WMS pipeline
- **Concept (1):** `specification-driven-scientific-workflow-management`
- **Entity (1):** `pegasus-ai-plugin-marketplace` — Apache-2.0, CONDITIONAL-GO reference (HPC)
- **Pages updated (12):** `openspec`, `llm-as-code-agentic-programming`, `failed-trajectory-harness-repair`, `agent-completion-verification-gates`, `claude-plugins-catalog-patterns`, `skill-vetting`, `dynamic-workflow-orchestrator-off-model`, `mcp-context-optimization`, `mcp-adaptive-systems-context-survey`, `index.md`, `sweeps/2026-06-18-daily.md`
- **Phase-0:** `scripts/adopt_k118_phase0.sh` — marketplace **Apache-2.0**; **NO-GO** Cemini prod (HPC-only)
- **Brief:** `briefs/2026-06-18_k118-spec-driven-pegasus-workflow-prod.md`
- **Raw:** 1 PDF → `raw-sources/`; inbox cleared

## [2026-06-17] ingest | K117 MemRefine + SEAGym + FinAcumen routing

- **Preingest:** 3 NEW (`2606.13177`, `2606.17546`, `2606.17642`)
- **Sources (3):** MemRefine storage-budgeted memory; SEAGym harness eval; FinAcumen experience memory (finance)
- **Concepts (3):** `storage-budgeted-agent-memory-compression`, `seagym-self-evolving-harness-evaluation`, `selective-experience-memory-harness`
- **Pages updated (11):** `multi-factor-agentic-memory-value-model`, `tool-response-context-pruning-summarization`, `agent-memory-stack-comparison`, `claude-mem`, `continual-harness-online-self-improvement`, `harnessx-composable-evolution-foundry`, `self-harness-model-specific-improvement-loop`, `harness-updating-vs-benefit-nonmonotonic`, `skillhone-continual-skill-decision-history`, `agent-completion-verification-gates`, `index.md`, `sweeps/2026-06-17-daily.md`
- **Cross-wiki:** `@osint-wiki/concepts/finacumen-financial-experience-memory.md`
- **Phase-0:** `scripts/adopt_k117_phase0.sh` — MemRefine/SEAGym **REFERENCE**; FinAcumen **NO-GO** install (osint only)
- **Brief:** `briefs/2026-06-17_k117-memory-seagym-finacumen-prod.md` → scp `cemini-prod:/opt/cemini/briefs/`
- **Raw:** 3 PDFs → `raw-sources/`; inbox cleared

## [2026-06-16] sync | cursor-audit + super-audit v1.3.0 role delegation

- **Skills (CCC mirror):** `.cursor/skills/cursor-audit/`, `.cursor/skills/super-audit/` — premium role-based model delegation (no hardcoded triples)
- **Wiki:** `entities/skills/cursor-audit.md`, `entities/skills/super-audit.md` — mode → role matrices, premium tier policy, API role catalog
- **Source:** OSINT WORKSPACE skill v1.3.0 (2026-06-16)

## [2026-06-16] ingest | K116 Orch-RM + HarnessX + LLM-as-Code

- **Preingest:** 3 NEW (`2606.13598`, `2606.14249`, `2606.15874`)
- **Sources (3):** Orch-RM orchestration reward; HarnessX foundry; LLM-as-Code agentic programming
- **Concepts (4):** `orchestration-reward-modeling-orch-rm`, `harnessx-composable-evolution-foundry`, `llm-as-code-agentic-programming`, `llm-as-orchestrator-failure-modes`
- **Pages updated (10):** `subagent-orchestration`, `conductor-mcp`, `code-as-agent-harness`, `continual-harness-online-self-improvement`, `etclovg-harness-layers`, `dynamic-workflow-orchestrator-off-model`, `agentic-programming-full-stack-thesis`, `agent-rubrics-self-correction`, `index.md`, `sweeps/2026-06-16-daily.md`
- **Phase-0:** `scripts/adopt_k116_phase0.sh` — OrchRM **404**; HarnessX **future release**; LLM-as-Code **REFERENCE**
- **Brief:** `briefs/2026-06-16_k116-orchrm-harnessx-llm-as-code-prod.md` → scp `cemini-prod:/opt/cemini/briefs/`
- **Raw:** 3 PDFs → `raw-sources/`; inbox cleared

## [2026-06-15] ingest | K115 context pruning + memory value + RAH + custom-agent methodology

- **Preingest:** 4 NEW (`2606.10209`, `2606.11869`, `2606.12945`, `2606.13643`)
- **Sources (4):** Less Context Better Agents; Agents All the Way Down; multi-factor agentic memory; Recursive Agent Harnesses
- **Concepts (4):** `tool-response-context-pruning-summarization`, `agents-all-the-way-down-custom-methodology`, `multi-factor-agentic-memory-value-model`, `recursive-agent-harness-harness-recursion`
- **Pages updated (10):** `context-engineering`, `mcp-context-optimization`, `subagent-orchestration`, `code-as-agent-harness`, `agent-memory-stack-comparison`, `claude-mem`, `dynamic-workflow-orchestrator-off-model`, `claude-harness-dynamic-workflows-k88`, `index.md`, `sweeps/2026-06-15-daily.md`
- **Phase-0:** `scripts/adopt_k115_phase0.sh` — all **REFERENCE**; BorgeAgent 404; RAH npm **NO-GO** (no license)
- **Brief:** `briefs/2026-06-15_k115-context-memory-recursion-prod.md` → scp `cemini-prod:/opt/cemini/briefs/`
- **Raw:** 4 PDFs → `raw-sources/`; inbox cleared

## [2026-06-13] ingest | K114 federation — 4 arXiv harness/KG papers

- **Preingest:** 4 NEW (`2606.04602`, `2606.08878`, `2606.12835`, `2606.13669`)
- **Sources (4):** Parthenon Law (six-layer legal harness); PerspectiveGap (orchestration prompting benchmark); IoAI vision survey; Agents-K1 (agent-native KG)
- **Concepts (3):** `perspectivegap-orchestration-prompting`, `internet-of-agentic-ai-ioai`, `agents-k1-agent-native-knowledge-orchestration`
- **Pages updated (9):** `subagent-orchestration`, `conductor-mcp`, `interaction-native-knowledge-harness`, `cross-wiki-routing`, `openagenet-trusted-agent-discovery`, `ship-subagent-writer-reviewer-tester`, `continual-harness-online-self-improvement`, `librarian-kb-server`, `index.md`
- **Cross-wiki:** `@osint-wiki/concepts/librarian-server-architecture.md` (Agents-K1 serving implications)
- **Phase-0:** Parthenon **REFERENCE** (`parthenon-skills` on GitHub); Agents-K1 **REFERENCE** (Scholar-KG scale; no Cemini fork); PerspectiveGap **Adopt** benchmark repo for prompt regression; IoAI **REFERENCE** vision only
- **Raw:** 4 PDFs → `raw-sources/`; inbox cleared

## [2026-06-13] ops | Hermes operator adoption — pre federation ingest

- **Status** — Hermes GO on librarian (gateway + crons) + laptop (SkillClaw + workspace); prod NO-GO unchanged
- **Pages (6)** — `hermes-agent`, `remote-hermes-access-pattern`, `five-layer-operator-stack`, `agent-memory-stack-comparison`, `agent-personality-file-hermes-openclaw`, `claude-honesty-critic-agent`; stubs `skillclaw`, `hermes-workspace`
- **Cross-wiki** — `@osint-wiki/concepts/hermes-laptop-operator-playbook.md` canon

## [2026-06-12] ingest | K113 Hermes tool eval + K112 honesty critic

- **K113** — `sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md`; entities hermes-workspace, skillclaw, wondelai-skills
- **K112** — `concepts/claude-honesty-critic-agent.md` + `sources/brief-k112-ccc-claude-honesty-critic-2026-06-12.md` from OSINT Posts Post 7
- **Cross-wiki** — `@osint-wiki/sources/multi-wiki-tool-eval-v5-k113-2026-06-12.md`

## [2026-06-12] ingest | K111 channel fracture + SkillHone

- **Preingest:** 2 NEW (`2606.04896`, `2606.08671`)
- **Sources (2):** Channel Fracture (Hermes cron memory injection); SkillHone (continual skill decision history)
- **Concepts (2):** `channel-fracture-cross-agent-memory-delivery`, `skillhone-continual-skill-decision-history`
- **Pages updated (11):** `hermes-agent`, `muse-autoskill-skill-lifecycle`, `bayesian-posterior-guided-skill-evolution`, `self-harness-model-specific-improvement-loop`, `agent-completion-verification-gates`, `subagent-orchestration`, `continual-harness-online-self-improvement`, `skill-vetting`, `ship-subagent-writer-reviewer-tester`, `hooks-for-automation`, `agent-memory-stack-comparison`, `index.md`, `sweeps/2026-06-12-daily.md`
- **Phase-0:** SkillHone **REFERENCE** (no public repo 2026-06-12); Channel Fracture **pattern-only** (Hermes study, steal receiver-verify)
- **Raw:** 2 PDFs → `raw-sources/`; inbox cleared

## [2026-06-11] ingest | K110 Self-Harness + enterprise MCP interviews

- **Preingest:** 2 NEW (`2606.09498`, `2606.09182`)
- **Sources (2):** Self-Harness; enterprise MCP adoption (n=20 interviews)
- **Concepts (2):** `self-harness-model-specific-improvement-loop`, `enterprise-mcp-adoption-practice`
- **Pages updated (10):** `continual-harness-online-self-improvement`, `retrospective-harness-optimization-rho`, `failed-trajectory-harness-repair`, `agent-completion-verification-gates`, `mcp-server-catalog-curation`, `mcp-server-runtime-fault-taxonomy`, `mcp-context-optimization`, `seclaw-agent-security-evaluation`, `index.md`, `sweeps/2026-06-11-daily.md`
- **Cross-wiki:** `@cybersecurity-wiki/concepts/enterprise-mcp-adoption-interviews.md`
- **Phase-0:** Self-Harness **REFERENCE** (no public repo 2026-06-11)
- **Raw:** 2 PDFs → `raw-sources/`; inbox cleared

## [2026-06-10] ingest | K109 arXiv harness cluster (6 papers)

- **Preingest:** 6 NEW (`2508.19239`, `2606.03161`, `2606.06545`, `2606.08348`, `2606.09122`, `2606.10106`)
- **Sources (6):** harness operational definition; MCP adaptive-systems survey; OpenAgenet OAN; Queen-Bee BeeSpec; Bayesian-Agent; hyperscale incident resolution
- **Concepts (6):** `agent-harness-operational-definition`, `openagenet-trusted-agent-discovery`, `queen-bee-beespec-enterprise-orchestration`, `bayesian-posterior-guided-skill-evolution`, `progressive-autonomy-incident-resolution`, `mcp-adaptive-systems-context-survey`
- **Entity:** `bayesian-agent` — CONDITIONAL-GO (MIT, ~27★); `scripts/adopt_k109_phase0.sh`
- **Pages updated (12):** `etclovg-harness-layers`, `code-as-agent-harness`, `agent-completion-verification-gates`, `continual-harness-online-self-improvement`, `mcp-context-optimization`, `subagent-orchestration`, `skill-vetting`, `claude-code`, `retrospective-harness-optimization-rho`, `muse-autoskill-skill-lifecycle`, `mcp-server-catalog-curation`, `index.md`
- **Cross-wiki:** `@cybersecurity-wiki/concepts/agentic-aiops-autonomous-incident-resolution.md` (SRE stub)
- **Phase-0:** OpenAgenet **REFERENCE** (GitHub org not verified); Queen-Bee **pattern-only** (no public repo)
- **Raw:** 6 PDFs → `raw-sources/`; inbox cleared

## [2026-06-10] phase-0 | K109 + K108 laptop trials

- **K109** (`scripts/adopt_k109_phase0.sh`): clone PASS; MIT license API PASS; `pip install -e` + `import bayesian_agent` + `bayesian-agent --help` PASS (`/tmp/k109-phase0-ccc`)
- **K108** (`scripts/adopt_k108_phase0.sh`): omnifs Apache-2.0 + clone PASS; **WARN** docker not on PATH (FUSE path blocked)
- **OpenAgenet:** `OpenAgenet/oan-public-docs` found — license **NOASSERTION**, 0★ — stays REFERENCE
- **Queen-Bee:** no public repo on GitHub search — pattern-only confirmed
- **Benchmarks:** skipped (API keys)

## [2026-06-10] trial | Bayesian-Agent live DeepSeek smoke

- **API:** `deepseek-v4-flash` + `deepseek-chat` OK via `api.deepseek.com` (env `DEEPSEEK_API_KEY`)
- **Native harness:** 1 task — `file_write` + verify loop; 3 API calls, 2833 tokens; `answer.txt` = `forty-two`
- **Registry CLI:** `evolve` + `summarize` on bundled `artifacts/ga_deepseek_baseline/sop_results.json` — posterior `benchmark/sop_bench` success 0.773, baseline accuracy 0.8 (20 tasks)
- **Datasets:** cloned `JinyiHan99/GA-Technical-Report` → `/tmp/k109-phase0-ccc/GA-Technical-Report/datasets` (~40MB)
- **SOP-Bench `--limit 1`:** baseline **PASS** (sop_01, 59,734 tokens, ~41s); `bayesian-full` **FAIL** on same task (empty-registry first run — expected noise at n=1)
- **SOP-Bench full 20 (2026-06-10):** baseline **20/20** (961,725 tokens, ~9m); `bayesian-full` **20/20** (see results dir); incremental on limit-5 failures **3/5→5/5** (2 repairs, +84k tokens)

## [2026-06-10] brief | K109 prod handoff — Bayesian-Agent harness cluster

- **Brief:** `briefs/2026-06-10_k109-bayesian-agent-harness-cluster-prod.md` — CONDITIONAL-GO laptop; **NO-GO** prod install; GA-Technical-Report dataset note; steal-from BeeSpec + T1–T4 + incremental repair
- **Prod scp:** `cemini-prod:/opt/cemini/briefs/` (awareness only)

## [2026-06-09] brief ingest | K108 THE HIVE + /ship + omnifs from OSINT

Ingested `briefs/2026-06-09_k108-ccc-hive-ship-omnifs-from-osint.md` — Posts 1, 2, 4 harness cluster (sha `b7956893…`).

**Pages created (5):** `the-hive-loop-routines-pattern`, `ship-subagent-writer-reviewer-tester`, `omnifs`, `sources/trading-posts-compilation-8-2026-06-09`, `scripts/adopt_k108_phase0.sh`.

**Pages updated (8):** `dynamic-workflow-orchestrator-off-model`, `claude-harness-dynamic-workflows-k88`, `hooks-for-automation`, `subagent-orchestration`, `skill-vetting`, `mcp-context-optimization`, `lazy-tool`, `cross-wiki-tool-eval-inventory`, `index.md`.

**Phase-0:** omnifs **CONDITIONAL-GO** (Apache-2.0, ~57★); THE HIVE + `/ship` pattern-only.

**Cross-wiki:** `@osint-wiki/sources/trading-posts-compilation-8-2026-06-09.md`, `@osint-wiki/entities/tools/omnifs.md`.

## [2026-06-08] ingest | TimeClaw — contextualized time series (2606.05404)

- **Preingest:** 1 NEW (`arxiv-2606.05404`)
- **Source:** Harnessing Generalist Agents for Contextualized Time Series — UIUC iSAIL; Apache-2.0 `TimeClaw` repo (0★)
- **Concept:** `time-series-native-agent-harness` — workspace + runtime tools + capability evolution + episodic memory
- **Entity:** `timeclaw` — CONDITIONAL-GO laptop trial; disambiguate from 2605.10038 homonym
- **Pages updated (8):** `code-as-agent-harness`, `mcp-context-optimization`, `muse-autoskill-skill-lifecycle`, `etclovg-harness-layers`, `continual-harness-online-self-improvement`, `runtime-context-mcp-file-refs`, `claude-mem`, `stash`, `index.md`
- **Cross-wiki:** `@osint-wiki/concepts/contextualized-time-series-agent-harness.md` (TSAIA/CiK finance stub)
- **Raw:** PDF → `raw-sources/`; inbox cleared
- **Phase-0 (2026-06-08):** clone + venv import PASS; `scripts/adopt_timeclaw_phase0.sh`; benchmarks skipped (no API key)

## [2026-06-07] brief ingest | K103 agent-harness cluster from OSINT

Ingested `briefs/2026-06-07_k103-ccc-agent-harness-from-osint.md` — K103 63-URL eval CCC slice + Posts harness cluster (sha `6ebbacb8…` eval, `78fad654…` posts).

**Pages created (11):** `agent-skill-manager` (expanded), `pydantic-ai`, `deep-scientist`, `autoresearch-claw`, `application-skills` (NO-GO), `agent-backpressure-loop`, `rl-agent-labs-system-prompt-learning`, `long-thread-context-decay`, `sources/multi-wiki-tool-eval-v8-k103-2026-06-07`, `sources/trading-posts-compilation-19-2026-06-07`, `scripts/adopt_k103_phase0.sh`.

**Pages updated (10):** `cross-wiki-tool-eval-inventory`, `skill-vetting`, `context-engineering`, `subagent-orchestration`, `federated-daily-research-digest`, `claude-code-large-codebase-workflow`, `rag-binary-quantization`, `full-stack-ai-engineer-agent-path`, `agent-skills-progressive-disclosure`, `tools-we-dont-use`, `index.md`.

**Phase-0:** pydantic-ai **GO**; asm **CONDITIONAL-GO**; application-skills **NO-GO** (null license + Membrane lock-in).

**Cross-wiki:** `@osint-wiki/sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md`, `@osint-wiki/sources/trading-posts-compilation-19-2026-06-07.md` (canon).

## [2026-06-07] ingest | RHO — Retrospective Harness Optimization (2606.05922)

- **Preingest:** 1 NEW (`arxiv-2606.05922`)
- **Source:** Retrospective Harness Optimization — MSRA/CityU; MIT `retro-harness` repo
- **Concept:** `retrospective-harness-optimization-rho` — DPP coreset → group rollout → best-of-N self-preference
- **Entity:** `retro-harness` — CONDITIONAL-GO laptop trial
- **Pages updated (9):** `failed-trajectory-harness-repair`, `continual-harness-online-self-improvement`, `harness-updating-vs-benefit-nonmonotonic`, `code-as-agent-harness`, `self-healing-agent-sessions`, `agent-rubrics-self-correction`, `skilladaptor-step-level-skill-adaptation`, `openevolve`, `index.md`
- **Raw:** PDF → `raw-sources/`; inbox cleared

## [2026-06-06] briefs | K102 ingest + backlog processed markers

- **K102** (`briefs/2026-06-06_k102-…`) — wiki: `typst`, `flowforge-skill`, K102 source stub; `scripts/adopt_k102_phase0.sh` (harness plugin PASS; typst not installed)
- **Processed markers** — 9 briefs tagged (k94, k95, k97, k98, inkh/automem handoffs, phase0 trials/scope/trial-plan)
- **Handoffs confirmed** — automem + inkh already in `OSINT WORKSPACE/briefs/`; cybersecurity handoff already in cybersec wiki

## [2026-06-06] phase-0 | SkillAdaptor + MCP fault taxonomy

- **SkillAdaptor** (`zjunlp/SkillAdaptor`): MIT, 6★, README stub only → **NO-GO install**, **REFERENCE** methodology
- **MCP fault taxonomy** (2606.05339): **ADOPT checklist**; figshare replication cited; no tool install
- **Lint:** bidirectional gap fixed (`agentic-memory-cross-scenario-generality` ↔ `failed-trajectory-harness-repair`)

## [2026-06-06] ingest | Daily digest batch — SkillAdaptor + MCP fault taxonomy

- **Preingest:** 2 NEW, 0 DUPLICATE (`arxiv-2606.01311`, `arxiv-2606.05339`)
- **Sources (2):** SkillAdaptor (2606.01311); MCP runtime fault taxonomy (2606.05339)
- **Concepts (2):** `skilladaptor-step-level-skill-adaptation`, `mcp-server-runtime-fault-taxonomy`
- **Pages updated (10):** `muse-autoskill-skill-lifecycle`, `skill-vetting`, `failed-trajectory-harness-repair`, `self-healing-agent-sessions`, `mcp-context-optimization`, `mcp-server-catalog-curation`, `continual-harness-online-self-improvement`, `agent-skills-progressive-disclosure`, `thin-harness-fat-skills-garrytan`, `seclaw-agent-security-evaluation`, `index.md`
- **Cross-wiki:** MCP Security category → `@cybersecurity-wiki/concepts/mcp-security-posture.md` (pointer only)
- **Raw:** PDFs → `raw-sources/`; inbox cleared

## [2026-06-05] deep-read | K100 HarnessFix + memory routing cleanup

- **Deep-read:** arXiv 2606.06324 (HarnessFix) — HTIR, ETCLOVG, repair operators, regression acceptance
- **Read:** arXiv 2606.04315 (AutoMEM / agentic memory); arXiv 2605.30738 MAVEN canonical source bumped to `read`
- **Concepts created/expanded:** `failed-trajectory-harness-repair`, `etclovg-harness-layers`, `agentic-memory-cross-scenario-generality`
- **Dedupe removed:** `agentic-tool-calling-generalization`, duplicate `arxiv-maven-...-2026-06-05` source stub
- **Routing fix:** 2606.04315 is **memory** (OSINT-primary), not tool-calling; dangling link → `@osint-wiki/concepts/exploration-graph-dead-ends.md`
- **Pages updated (10):** `code-as-agent-harness`, `skill-vetting`, `subagent-orchestration`, `seclaw-agent-security-evaluation`, `self-healing-agent-sessions`, `lazy-tool`, `maven-agentic-tool-calling-generalization`, three source pages, `index.md`
- **Brief:** `briefs/2026-06-05_automem-memory-cross-scenario-osint-handoff.md` — OSINT eval handoff for AutoMEM

## [2026-06-05] ingest | K100 federation morning — MAVEN + harness repair batch

- **Sources (3)** — 2605.30738 MAVEN; 2606.04315 cross-scenario generality; 2606.06324 failed-trajectory harness repair
- **Concepts (2)** — `failed-trajectory-harness-repair` (stub → deep-read in follow-up); MAVEN deduped to canonical page
- **Raw** — PDFs → librarian; inbox cleared

## [2026-06-04] adopt | LLM routing DeepSeek → OpenRouter failover

Cross-project routing shipped in OSINT WORKSPACE (`scripts/llm_routing.py`, `config/llm-routing.env.example`, `source_llm_routing_env.sh`, `install_llm_routing_env.sh`). CeminiSuite `deepseek_client.py` wired; poker `cemini_hl_loop.sh` auto-sources env.

- **CCC page:** `concepts/llm-routing-deepseek-openrouter-failover.md`
- **One-time:** `~/.cemini/llm-routing.env` created; `DEEPSEEK_API_KEY` merged from OSINT `.env` — operator still adds `OPENROUTER_API_KEY`

## [2026-06-04] brief → prod | Phase-0 adoption deployment scope

Answer: laptop adoptions **do not** apply across all projects or prod automatically.

**Updated:** `concepts/cross-wiki-tool-adoption-routing.md` — deployment scope table (Mac user vs project vs prod vs librarian).

**Prod brief scp'd:** `briefs/2026-06-04_phase0-adoption-scope-cemini-prod.md` → `cemini-prod:/opt/cemini/briefs/` (7268 bytes). Prod: Phase 1 governance doc + optional skill-scanner trial vs `vet_skill.py`; NO-GO harness/openevolve/Skill_Seekers.

## [2026-06-04] adopt | Full Phase-0 trial run + cross-wiki routing

Nine-tool trial batch in `/tmp/ccc-trials-full-20260604/`; CCC-local adoptions applied.

**Created:** `concepts/cross-wiki-tool-adoption-routing.md`

**Updated:** `skill-vetting` (step 3b skill-scanner), `skillnet`, `scienceaix-agentskills`, `seclaw-agent-security-evaluation`, `revfactory-harness`, `agents-best-practices`, `index.md`

**CCC hands-on:** expanded `.claude/skills/agents-best-practices/references/` (4 files); skill-scanner on all project skills.

**Handoff:** `briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md` → cybersecurity-wiki.

**Blocked:** harness generation (org API); Webwright plugin (SSH clone); defenseclaw sidecar (LLM key).

## [2026-06-04] adopt | Phase-0 GO trials — hands-on installs

Trials run in `/tmp/ccc-adopt-trials-20260604/` + project `.claude/skills/` (gitignored). Verdicts in each entity `## Adoption trial (2026-06-04)`.

| Tool | Trial outcome | Posture |
|------|---------------|---------|
| openevolve | smoke PASS (venv) | ADOPTED smoke tier |
| Webwright | pip + project skill; plugin SSH fail | ADOPTED project skill |
| Skill_Seekers | wiki/concepts export + package zip | ADOPTED CLI workflow |
| revfactory/harness | `harness@harness-marketplace` user plugin | ADOPTED Claude Code plugin |
| agents-best-practices | project skill + wiki steal | ADOPTED cherry-pick |
| defenseclaw | `make all` + skill-scanner | ADOPTED CLI scanners |
| SkillNet / scienceaix / SeClaw | no install (REFERENCE / NO-GO) | unchanged |

**Wiki:** `@concepts/subagent-orchestration.md` — harness control plane steal.

**Artifacts (local):** `/tmp/ccc-adopt-trials-20260604/skill-seekers-out-markdown.zip`; `.claude/skills/{webwright,agents-best-practices}/`.

## [2026-06-04] phase-0 | K88/K93/K98 backlog batch (9 tools)

GitHub API + README skim audits; openevolve smoke via `scripts/openevolve-phase0-smoke.sh`. Verdicts in each page `## Phase-0 Audit (2026-06-04)` section.

| Tool | Verdict | Notes |
|------|---------|-------|
| openevolve | **CONDITIONAL-GO** | Smoke PASS (isolated venv); Docker eval still gated |
| Webwright | **CONDITIONAL-GO** | MIT; Claude Code plugin path only — not Cursor browser replacement |
| Skill_Seekers | **CONDITIONAL-GO** | MIT; one wiki-chapter export trial + vet output before prod skills |
| SkillNet | **CONDITIONAL-GO (REFERENCE)** | MIT; no routing layer until gap vs lazy-tool proven |
| revfactory/harness | **CONDITIONAL-GO** | Apache-2.0; isolated worktree trial; pick one meta-harness |
| agents-best-practices | **CONDITIONAL-GO (cherry-pick)** | MIT; no global install until dedup vs wiki |
| defenseclaw | **CONDITIONAL-GO** | Apache-2.0; pattern theft > full sidecar for laptop workflow |
| SeClaw | **NO-GO (install) / REFERENCE** | No LICENSE file; code "coming soon" |
| scienceaix/agentskills | **REFERENCE** | MIT confirmed; stale catalog — discovery queue only |

## [2026-06-04] ingest | Daily digest — 2 arXiv papers (agent skills + InKH)

Ingested from `research to be indexed/` (daily digest 2026-06-04 sweep).

**Pages created (5):** `agent-skills-progressive-disclosure`, `interaction-native-knowledge-harness`, `scienceaix-agentskills`, `sources/arxiv-agent-skills-architecture-security-2602.12430`, `sources/arxiv-interaction-native-knowledge-harness-2606.01886`.

**Pages updated (10):** `agent-skills-taxonomy`, `skill-vetting`, `anthropic-skills`, `mcp-context-optimization`, `thin-harness-fat-skills-garrytan`, `muse-autoskill-skill-lifecycle`, `context-engineering`, `llm-wiki-compiler`, `index.md`.

**Cross-wiki:** InKH financial deployment → OSINT ingested K99 (`@osint-wiki/concepts/interaction-native-knowledge-harness.md`). 2602.12430 CCC-primary.

**Raw:** 2 PDFs → `raw-sources/`; inbox cleared.

## [2026-06-04] brief ingest | K98 agent org chart + MCP from OSINT

Ingested `briefs/2026-06-04_k98-ccc-agent-org-chart-mcp-from-osint.md` — Posts.docx K98 (13 posts, sha `32400c1f…`) harness cluster + SeClaw arXiv.

**Pages created (5):** `agent-five-gate-org-chart`, `mcp-server-catalog-curation`, `seclaw-agent-security-evaluation`, `sources/trading-posts-compilation-18-2026-06-04`, `sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04`.

**Pages updated (9):** `claude-code-subagent-templates`, `subagent-orchestration`, `code-as-agent-harness`, `conductor-mcp`, `lazy-tool`, `skill-vetting`, `k67-explorax-100-repos-reference`, `index.md`.

**Cross-wiki:** `@osint-wiki/sources/trading-posts-compilation-18-2026-06-04.md`, `@osint-wiki/concepts/seclaw-agent-security-evaluation.md`, `@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md`.

**Explicit non-actions:** Bloome / MiroFish / TradingAgents install without Phase-0; NEMO laptop REFERENCE only.

## [2026-06-03] brief ingest | K97 agent-harness cluster from OSINT

Ingested `briefs/2026-06-03_k97-ccc-agent-harness-from-osint.md` — Posts.docx K97 (17 posts, sha `bf5682b3…`), 10 harness posts routed to CCC.

**Pages created (4):** `claude-code-cheat-sheet-shortcuts`, `runtime-context-mcp-file-refs`, `agent-rubrics-self-correction`, `claude-cowork-automation-vs-hooks`.

**Pages updated (11):** `sources/trading-posts-compilation-17-2026-06-03`, `claude-harness-dynamic-workflows-k88`, `agent-token-discipline-openclaw-hermes`, `hermes-agent`, `codex-side-fork-workflow`, `claude-obsidian-notebooklm-bridge`, `monokern-compounding-research-pipeline`, `damidefi`, `kimi-agent-swarm`, `subagent-orchestration`, `claude-code`, `context-engineering`, `index.md`.

**Cross-wiki:** `@osint-wiki/sources/trading-posts-compilation-17-2026-06-03.md` (canon).

## [2026-06-03] ingest | K95

Daily digest fetch (`wiki/sweeps/2026-06-03-daily.md`). Five NEW arXiv harness/agent papers from `research to be indexed/` (+ CLI-Anything brief from OSINT per prior stub).

**Pages created (11):** `runtime-harness-interface-adaptation`, `adaptive-auto-harness-open-ended-streams`, `embedded-agent-modular-edge-architecture`, `slm-agent-orchestration-gateway`, `life-harness`, `adaptive-auto-harness`, `sources/arxiv-runtime-harness-adaptation-2605.22166`, `sources/arxiv-adaptive-auto-harness-2606.01770`, `sources/arxiv-agentxgcore-mobile-core-2606.00417`, `sources/arxiv-embedded-agent-modular-edge-2606.02862`, `sources/arxiv-slm-orchestration-gateway-2606.03557`.

**Pages updated (11):** `code-as-agent-harness`, `continual-harness-online-self-improvement`, `harness-updating-vs-benefit-nonmonotonic`, `system-scaling-harness-agentic-ai`, `subagent-orchestration`, `agent-sandbox-unikraft`, `lazy-tool`, `conductor-mcp`, `openevolve`, `index.md`.

**Cross-wiki (log only):** Five arXiv papers not yet on `@osint-wiki`. OSINT daily sweep flagged same PDFs — CCC owns harness-interface + lazy-tool/conductor routing synthesis; OSINT may own prediction-market stream eval (2606.01770) and telecom AgentxGCore (2606.00417) if routed. CLI-Anything (2606.03854) brief ingested separately — no duplicate full OSINT pages.

**Raw:** 5 PDFs → `raw-sources/` + `cemini-librarian:/opt/cemini-bulk/research/`; inbox cleared.

## [2026-06-02] brief ingest | K94 agent skills + Tool Forge from OSINT

Ingested `briefs/2026-06-02_2026-06-02_k94-ccc-agent-skills-agyn-toolforge-from-osint.md`.

**Pages created (4):** `agent-skills-taxonomy`, `tool-forge`, `sources/arxiv-agent-skills-survey-2605.07358-2026-06-02`, `sources/arxiv-tool-forge-governed-agentic-2605.28000-2026-06-02`.

**Pages updated (8):** `agyn`, `maven-agentic-tool-calling-generalization`, `worldmemarena-multimodal-agent-memory-eval`, `muse-autoskill-skill-lifecycle`, `autosci-memory-centric-research-agents`, `system-scaling-harness-agentic-ai`, `skill-vetting`, `thin-harness-fat-skills-garrytan`, `lazy-tool`, `index.md`.

**Cross-wiki:** `@osint-wiki` steal-from stubs on harness papers (MAVEN, WorldMemArena, MUSE, AutoSci, system-scaling); Agyn → `@osint-wiki/entities/tools/agyn-platform.md`.

**Lint:** `--fix-bidirectional --apply` — 0 gaps post-fix.

## [2026-06-02] ingest | CCC inbox — 5 arXiv papers (digest 2026-06-02)

Daily digest fetch (`scripts/daily_research_digest_run.py`). Scheduled LaunchAgent failed (exit 512 — env); manual run succeeded.

**Pages created (9):** `maven-agentic-tool-calling-generalization`, `worldmemarena-multimodal-agent-memory-eval`, `decoupled-intelligence-multi-agent-reference`, `agyn`, `sources/arxiv-sia-harness-weight-updates-2605.27276` (OSINT stub only), `arxiv-maven-agentic-tool-calling-2605.30738`, `arxiv-worldmemarena-agent-memory-2605.29341`, `arxiv-agyn-agent-platform-2605.27575`, `arxiv-decoupled-intelligence-multi-agent-2605.27685`.

**Pages updated (2):** `harness-updating-vs-benefit-nonmonotonic`, `index.md`.

**Skipped duplicate narrative:** SIA 2605.27276 — canon `@osint-wiki` K84.

**Raw:** 5 PDFs → `raw-sources/`; inbox cleared. Sweep: `wiki/sweeps/2026-06-02-daily.md`.

## [2026-06-01] ingest | CCC inbox — 3 arXiv harness papers (digest fetch)

Ingested from `research to be indexed/` (daily digest 2026-06-01). **Skipped** arXiv 2605.27276 (SIA) — already on `@osint-wiki` K84.

**Pages created (6):** `system-scaling-harness-agentic-ai`, `muse-autoskill-skill-lifecycle`, `autosci-memory-centric-research-agents`, `sources/arxiv-system-scaling-harness-2605.26112`, `sources/arxiv-muse-autoskill-2605.27366`, `sources/arxiv-autosci-2605.31468`.

**Pages updated (8):** `code-as-agent-harness`, `harness-updating-vs-benefit-nonmonotonic`, `continual-harness-online-self-improvement`, `skillrae-retrieval-augmented-execution`, `skill-vetting`, `monokern-compounding-research-pipeline`, `federated-daily-research-digest`, `index.md`.

**Raw:** 3 PDFs → `raw-sources/`; inbox cleared.

## [2026-06-01] brief ingest | K93 digest + monokern + harness (structural + wiki)

Ingested `briefs/2026-06-01_k93-ccc-digest-monokern-harness-from-osint.md`.

**Structural:** federated daily digest install (`scripts/daily_research_digest_run.py`, `daily_research_fetch.py`, `daily_research_config.yaml`, `wiki/sweeps/`, LaunchAgent `com.cemini.daily-research-digest.ccc`).

**Pages created (10):** `revfactory-harness`, `thin-harness-fat-skills-garrytan`, `harness-updating-vs-benefit-nonmonotonic`, `monokern-compounding-research-pipeline`, `federated-daily-research-digest`, `meta/daily-research-digest-cadence`, `sources/multi-wiki-tool-eval-v5-k93-2026-06-01`, `sources/trading-posts-compilation-31-2026-06-01`, `sources/arxiv-harness-updating-not-benefit-2605.30621`, `sources/monokern-research-pipeline-claude-notebooklm-obsidian-2026-06-01`.

**Pages updated (3):** `agents-best-practices`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-v5-k93-2026-06-01.md`, `@osint-wiki/sources/trading-posts-compilation-31-2026-06-01.md`.

## [2026-06-01] adopt | K92 GO items on laptop

- claude-trading-skills (5 skills, trading-* prefix)
- obsidian-second-brain (vault wiki/, bg agent off)

## [2026-06-01] phase0 | K92 eval repos — license + clone audits

- **tradermonty/claude-trading-skills** — GO (MIT, active)
- **eugeniughelbur/obsidian-second-brain** — GO laptop-only (canon @osint-wiki/sources/)

## [2026-06-01] brief ingest | K92 v7 tool eval slice + Posts-12 agent harness

Ingested `briefs/2026-06-01_k92-ccc-agent-harness-from-osint.md`.

**Pages created (8):** `harness-layer-competition-cursor-claude-perplexity`, `deepseek-coding-cost-routing`, `agentic-pm-review-artifacts`, `obsidian-second-brain-eugeniughelbur`, `claude-trading-skills`, `slot-casino-game-developer-skills`, `sources/multi-wiki-tool-eval-v7-k92-2026-06-01`, `sources/trading-posts-compilation-12-2026-06-01` (filled).

**Pages updated (4):** `agent-personality-file-hermes-openclaw`, `obsidian-vellum-second-brain-stack`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-12-2026-06-01.md`, `@osint-wiki/sources/multi-wiki-tool-eval-v7-k92-2026-06-01.md`.

## [2026-05-31] brief ingest | K90 v6 tool eval + Posts-16 agent harness

Ingested `briefs/2026-05-31_k90-ccc-agent-harness-from-osint.md`.

**Pages created (12):** `agent-personality-file-hermes-openclaw`, `nine-stage-agent-team-production`, `remote-hermes-access-pattern`, `ai-agents-learning-roadmap-reference`, `claude-artifacts-app-building`, `npxskillui`, `hermes-desktop`, `librechat`, `skyhook-radar`, `sources/multi-wiki-tool-eval-v6-k90-2026-05-31`, `sources/trading-posts-compilation-16-2026-05-31`.

**Pages updated (8):** `cross-wiki-tool-eval-inventory`, `deep-research-evaluation-prompt`, `everything-claude-code`, `hermes-agent`, `agent-token-discipline-openclaw-hermes`, `claude-code-software-factory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`, `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`.

## [2026-05-31] brief ingest | K88 v5 tool eval + Posts-42 harness workflows

Ingested `briefs/2026-05-31_k88-ccc-workflows-and-tool-eval-from-osint.md`.

**Pages created (15):** `karpathy-agent-infrastructure-basics`, `claude-code-subagent-templates`, `claude-harness-dynamic-workflows-k88`, `webwright`, `skill-seekers`, `book-to-skill`, `skillnet`, `cc-thinking-skills`, `claude-skill-registry`, `alirezarezvani-claude-skills`, `jezweb-claude-skills`, `ruflo`, `sources/multi-wiki-tool-eval-v5-k88-2026-05-31`, `sources/trading-posts-compilation-42-2026-05-31`.

**Pages updated (7):** `cross-wiki-tool-eval-inventory`, `deep-research-evaluation-prompt`, `karpathy-token-efficiency-patterns`, `claude-plugins-catalog-patterns`, `obsidian-vellum-second-brain-stack`, `index.md`.

**Lint:** `scripts/wiki_lint.py` — cross-wiki alias resolution + citation-safe `@alias/path` boundary check.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-v5-k88-2026-05-31.md`, `@osint-wiki/sources/trading-posts-compilation-42-2026-05-31.md`.

## [2026-05-30] prompt | v5 deep-research multi-wiki eval

Added `prompts/deep-research-multi-wiki-eval-v5-2026-05-30.md` — current default (world-cup-bot inventory, inline `gh` license lookup, NO-GO registry, TIME-VOLATILE sports LP).

**Updated:** `concepts/deep-research-evaluation-prompt`, `index.md`.

## [2026-05-30] brief ingest | K84 Codex /side /fork /goal harness patterns

Ingested `briefs/2026-05-30_k84-codex-harness-from-osint-posts.md`.

**Pages created (2):** `codex-side-fork-workflow`, `sources/trading-posts-compilation-k84-2026-05-30`.

**Pages updated (8):** `2026-05-13_multi-codex-codex-home-isolation`, `full-prompt-goal-template`, `cursor-ide-workspace`, `lazy-tool`, `conductor-mcp`, `claude-code`, `claude-desktop-vs-claude-code`, `code-as-agent-harness`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-k84-2026-05-30.md`.

## [2026-05-30] brief ingest | K78 five-tool stack + Obsidian contribution-rate workflows

Ingested `briefs/2026-05-29_k78-five-tool-obsidian-workflows-from-osint.md`.

**Pages created (4):** `five-layer-operator-stack`, `obsidian-contribution-rate-workflow`, `sources/trading-posts-compilation-6-2026-05-29`, `entities/people/damidefi`.

**Pages updated (9):** `obsidian-vellum-second-brain-stack`, `claude-obsidian-notebooklm-bridge`, `obsidian-agent-maintenance-workflow`, `hermes-agent`, `kimi-agent-swarm`, `cursor-ide-workspace`, `claude-code`, `trading-posts-compilation-20-2026-05-27`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-6-2026-05-29.md`.

## [2026-05-28] brief ingest | K76 Skills.md + CLAUDE.md five-section workflows

Ingested `briefs/2026-05-28_k76-claude-skills-claude-md-workflows-from-osint.md`.

**Pages created (3):** `claude-code-skills-md-institutional-memory`, `claude-md-five-section-template`, `sources/trading-posts-macro-charts-skills-md-2026-05-28`.

Cross-wiki: `@osint-wiki/concepts/claude-code-skills-md-workflow.md`, `@osint-wiki/sources/trading-posts-macro-charts-skills-md-2026-05-28.md`.

## [2026-05-28] brief ingest | K73 Phase-0 audit decisions

Ingested `briefs/2026-05-28_k73-phase0-audit-ccc-decisions.md`.

**Pages created (3):** `k73-phase0-audit-decisions`, `entities/tools/mermaid-skill`, `entities/tools/tvscreener`.

**Page updated:** `entities/tools/metatrader-mcp-server` posture changed to NO-GO for current scope.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-25url-2026-05-28.md`.

## [2026-05-28] brief ingest | K73 license skepticism + workflow patterns

Ingested `briefs/2026-05-28_k73-ccc-tool-eval-license-skepticism.md` and `briefs/2026-05-28_k73-ccc-workflows-from-osint.md`.

**Pages created (6):** `tool-eval-license-skepticism-patterns`, `enterprise-auto-mode-telemetry-rollout`, `harness-de-bloat-4x4-pattern`, `sources/multi-wiki-tool-eval-25url-2026-05-28`, `sources/trading-posts-compilation-38-2026-05-28`, `sources/arxiv-continual-harness-self-improving-agents-2605.09998` (backlink refresh).

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-25url-2026-05-28.md`, `@osint-wiki/sources/trading-posts-compilation-38-2026-05-28.md`.

## [2026-05-27] brief ingest | K72 Posts-25 workflows + Continual Harness

Ingested `briefs/2026-05-27_k72-ccc-workflows-from-osint.md`.

**Pages created (12):** `agent-completion-verification-gates`, `agent-memory-stack-comparison`, `claude-plugins-catalog-patterns`, `claude-prompt-engineering-techniques`, `claude-code-finance-research-setup`, `obsidian-vellum-second-brain-stack`, `karpathy-token-efficiency-patterns`, `full-stack-ai-engineer-agent-path`, `train-llm-agents-2026-curriculum`, `agentic-programming-full-stack-thesis`, `continual-harness-online-self-improvement`, `sources/arxiv-continual-harness-self-improving-agents-2605.09998`, `sources/trading-posts-compilation-25-2026-05-27`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-25-2026-05-27.md`, `@osint-wiki/concepts/continual-harness-online-self-improvement.md`.

## [2026-05-27] brief ingest | K71 27-URL eval (CCC tooling slice)

Ingested `briefs/2026-05-27_k71-ccc-tooling-from-osint.md`.

**Pages created (11):** `metatrader-mcp-server`, `three-man-team`, `claude-subconscious`, `council-of-high-intelligence`, `open-claude-code`, `mercury-agent-skills`, `solo-founder-superpowers`, `build-your-own-openclaw`, `ai-infra-engineer-learning`, `andrej-karpathy-skills-multica`, `bmad-creative-intelligence-suite`.

**Policy:** `multica-ai/andrej-karpathy-skills` Adopt demoted (no LICENSE).

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-27url-2026-05-27.md`.

## [2026-05-27] wire | notebooklm-py laptop + agent skills

- **CLI:** `notebooklm-py` 0.5.0, Playwright chromium, `notebooklm login`, `auth check --test --json` ok
- **Skills:** `notebooklm skill install` (user + OSINT project) → `.claude/skills/notebooklm`, `.agents/skills/notebooklm`
- **OSINT:** `.cursor/skills/notebooklm-osint-bridge` (Cemini redaction + workflow)
- **Wiki:** `notebooklm-py` + `claude-obsidian-notebooklm-bridge` → validated

## [2026-05-27] brief ingest | K69 Claude/Obsidian/LLM workflows (Posts.docx CCC slice)

Ingested `briefs/2026-05-27_k69-claude-obsidian-llm-workflows-from-osint.md`.

**Pages created (8):** `llm-engineering-stack-curriculum`, `agent-sandbox-unikraft`, `rag-binary-quantization`, `claude-code-large-codebase-workflow`, `agent-token-discipline-openclaw-hermes`, `claude-obsidian-notebooklm-bridge`, `entities/tools/notebooklm-py`, `sources/trading-posts-compilation-20-2026-05-27.md`.

**Updated:** `local-llm-mechanics-primer`, `context-engineering`, `token-economics-and-prompt-caching`, `claude-code`, `hermes-agent`, `tier1-tier2-agent-model`, `obsidian-agent-maintenance-workflow`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-20-2026-05-27.md`.

## [2026-05-26] brief ingest | K68 22-URL eval (CCC tooling slice)

Ingested `briefs/2026-05-26_k68-ccc-tooling-from-osint.md`.

**Pages created (5):** `google-eng-practices`, `ml-intern`, `rowboat`, `centaur`, `purple-cli`.

**Policy:** `MadAppGang/claudish` eval Adopt overturned → `@concepts/tools-we-dont-use.md` K68 section.

**Backlinks:** `cross-wiki-tool-eval-inventory`, `index.md`, orchestration/skill pages via lint.

Cross-wiki: `@osint-wiki/sources/multi-wiki-tool-eval-22url-2026-05-26.md`.

## [2026-05-26] brief ingest | K67 Claude/Obsidian workflows (Posts.docx CCC slice)

Ingested `briefs/2026-05-26_k67-claude-obsidian-workflows-from-osint.md`.

**Pages created (6):** `claude-premortem-skill`, `obsidian-agent-maintenance-workflow`, `obsidian-trading-journal-workflow`, `claude-code-software-factory`, `claude-code-personal-os-scope`, `sources/k67-explorax-100-repos-reference` (unread-stub).

**Updated:** `claude-obsidian` (K67 pattern-only note), `skill-vetting`, `subagent-orchestration`, `openspec`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: `@osint-wiki/sources/trading-posts-compilation-38-2026-05-26.md`.

## [2026-05-21] brief ingest | K65 Kimi Agent Swarm vs Claude Agent Teams

Ingested `briefs/2026-05-24_k65-kimi-agent-swarm-vs-claude-teams.md` (was in correct `briefs/` folder; missed on prior pass).

**Pages created (2):** `concepts/kimi-agent-swarm-vs-claude-agent-teams.md`, `entities/tools/kimi-agent-swarm.md`.

**Backlinks:** `subagent-orchestration`, `scatter-gather`, `cross-wiki-tool-eval-inventory`, `index.md`.

Cross-wiki: OSINT K65 canon (`@osint-wiki/concepts/kimi-agent-swarm-vs-claude-agent-teams.md`).

## [2026-05-21] query | Brief inbox check + K64 Hermes routing stub

**Briefs:** 22 files in `briefs/` — all have `processed:` markers; no new drops in `research to be indexed/`.

**Action:** K64 exists on OSINT only (CeminiSuite target); CCC slice = Hermes catalog → conductor reference. Created `entities/tools/hermes-agent.md`; backlinks on `conductor-mcp`, `cross-wiki-tool-eval-inventory`, `index.md`.

## [2026-05-21] hands-on | K63 Cursor adoption (CCC project)

Implemented K63 **Adopt** slice for this repo (not OSINT lazy-tool):

- `.cursor/mcp.json` — **exa** (`scripts/mcp_exa.sh`) + **fetch**
- `.cursor/rules/ccc-*.mdc` (4) — wiki workflow, page format, visual deliverables, rejected piracy tools
- `.cursor/curated-rules/README.md` — awesome-cursorrules mapping
- `scripts/openevolve-phase0-smoke.sh` — Phase-0 PASS (isolated venv)

**Wiki:** `cursor-ide-workspace`, `awesome-cursorrules` → validated; `openevolve` smoke noted.

## [2026-05-24] brief ingest | K63 Cursor/agent tooling (36-URL eval CCC slice)

Ingested `briefs/2026-05-24_k63-ccc-cursor-agent-tooling-from-osint.md`.

**Pages created (6):** `openevolve`, `awesome-cursorrules`, `claude-code-game-studios`, `agents-best-practices` (defer), `everything-claude-code` (ECC defer stub), `cursor-community-plugins` (CONDITIONAL-GO).

**Policy:** cursor piracy cluster added to `@concepts/tools-we-dont-use.md`.

**Backlinks:** `cursor-ide-workspace`, `subagent-orchestration`, `cross-wiki-tool-eval-inventory`, `tools-we-dont-use`.

## [2026-05-23] brief ingest | K60 Ai-Engineering-Roadmap (reference-only)

Ingested `briefs/2026-05-23_k60-ai-engineering-roadmap-from-osint.md`.

**Page created:** `entities/tools/ai-engineering-roadmap.md` — MIT CONFIRMED (~552★); curriculum gap-check vs existing conductor/skills/MCP docs; no install.

**Inventory:** upgraded K53 `ai-engineer-roadmap` catalog row; added K60 section.

**Also marked processed:** `briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md` (ingested prior commit; marker was missing).

## [2026-05-23] brief ingest | K59 SkillRAE + GraphFlow (OSINT Tier-B harness papers)

Ingested `briefs/2026-05-23_k59-skillrae-graphflow-from-osint.md`.

**Pages created (4):**
- `concepts/skillrae-retrieval-augmented-execution.md` + `sources/arxiv-skillrae-2605.10114.md`
- `concepts/graphflow-verifiable-agent-workflows.md` + `sources/arxiv-graphflow-2605.14968.md`

**Backlinks:** `code-as-agent-harness`, `lazy-tool`, `mcp-context-optimization`, `context-engineering`, `skill-vetting`, `openspec`, `conductor-mcp`, `cc-wf-studio`, `scatter-gather`, `glasswing`, `anthropic-skills`, `the-architect`, `cross-wiki-tool-eval-inventory`.

**Deferred:** SkillsVote (2605.18401) — not downloaded.

**OSINT backlink:** `@ccc-wiki/...` on both OSINT concept stubs.

## [2026-05-22] brief ingest | K57 local-LLM + agent infra + K55-2 ridark CCC subset

**K57** (`briefs/2026-05-22_k57-local-llm-and-agent-infra-from-osint.md`):
- `concepts/local-llm-mechanics-primer.md` — @TheAhmadOsman LLMs 101 stub
- `entities/tools/open-design.md`, `entities/tools/the-architect.md` — MIT/Apache-2.0 CONFIRMED via `gh api`
- AI OS essay (Post 5) — reference note on `conductor-mcp` only (no new page)
- `rag-from-scratch` — catalog row in `cross-wiki-tool-eval-inventory.md` only

**K55-2 ridark** (`briefs/2026-05-21_k55-2-ridark-eth-ccc-relevant-repos.md`):
- `concepts/tools-we-dont-use.md` — reject register (#1, #5, #18, #30 + skepticism tier)
- `entities/tools/repomix.md`, `n8n-mcp.md`, `anything-llm.md` — MIT verified 2026-05-22
- `entities/tools/claude-code-tips.md` — NOASSERTION license, defer
- OpenHands / ida-pro-mcp / rtk / ClawRouter — inventory catalog only (no stub farm)

**Backlinks:** `claude-code`, `context-engineering`, `token-economics`, `cross-wiki-routing`, `skill-vetting`, `twelve-rule-claude-md-template`, `cross-wiki-tool-eval-inventory`, `conductor-mcp` (+ lint `--fix-bidirectional --apply`).

## [2026-05-21] docs | Multi-wiki eval prompt v3 restore + v4 (Cursor-primary)

**Canonical prompts (repo root `prompts/`):**
- `deep-research-multi-wiki-eval-v3-2026-05-21.md` — frozen verbatim (7 surfaces, CCC = surface 7); reproduces K53/K54/K55
- `deep-research-multi-wiki-eval-v4-2026-05-21.md` — current default: same 7 surfaces, CCC surface expanded for **Cursor primary** + Claude Code secondary + post-run spot-check

**Wiki pages (2):**
- `concepts/deep-research-evaluation-prompt.md` — version lineage + ingest workflow
- `concepts/cursor-ide-workspace.md` — Open Folder / MCP / rules / vs Claude Code

**Note:** An earlier draft mistakenly split into 8 surfaces (Cursor #7 + Claude Code #8); discarded in favor of user's v3 structure.

## [2026-05-21] brief ingest | K48 code-as-harness + self-healing (OSINT arXiv)

Ingested `briefs/2026-05-21_k48-code-as-harness-and-self-healing-from-osint.md` (post-batch; arrived after 15-brief sweep).

**Pages created (2):**
- `concepts/code-as-agent-harness.md` — three-layer survey model → Claude Code / conductor / MCP / hooks mapping
- `concepts/self-healing-agent-sessions.md` — failure taxonomy + retry budget for long sessions

**Backlinks updated (12):** `claude-code`, `conductor-mcp`, `subagent-orchestration`, `hooks-for-automation`, `glasswing-deliberate-disagreement`, `openspec`, `skill-vetting`, `stash`, `lazy-tool`, `claude-mem`, `full-prompt-goal-template` (+ mutual link between the two new concepts).

**OSINT backlink:** `@ccc-wiki/concepts/code-as-agent-harness.md` added to `@osint-wiki/concepts/code-as-agent-harness.md`.

## [2026-05-21] batch ingest | 15 cross-wiki briefs triaged and ingested

Bulk triage of all unprocessed briefs in `briefs/` (15 total). Two were already-ingested (concept stubs existed); 13 were unprocessed.

**Pages created (8):**
- `entities/patterns/citadel-agent-orchestration.md` — apex agent-orchestration OS layer (K51)
- `entities/patterns/glasswing-deliberate-disagreement.md` — evilsocket/audit adversarial-verification pattern (K56)
- `entities/tools/defenseclaw.md` — Cisco security governance for agentic AI (K45)
- `entities/tools/cc-wf-studio.md` — VS Code visual workflow editor for CC pipelines (K53)
- `entities/tools/delive.md` — system-audio capture + MCP + agent skill bridge (K54/K55)
- `entities/tools/everos.md` — context-offload-to-disk memory OS (K54)
- `entities/skills/src-hunter-skill.md` — 305-payload SKILL.md design exemplar (K55)
- `concepts/cross-wiki-tool-eval-inventory.md` — consolidated catalog of all ~35 CCC-routed items from K45–K56

**Already-ingested (2, added processed marker):**
- `2026-05-13_multi-codex-codex-home-isolation.md` → concept stub existed at `concepts/2026-05-13_multi-codex-codex-home-isolation.md`
- `2026-05-13_tolaria-steal-from-patterns.md` → concept stub existed at `concepts/2026-05-13_tolaria-steal-from-patterns.md`

**Backlinks updated (5 existing pages):**
- `concepts/subagent-orchestration.md` — added citadel, glasswing, cc-wf-studio
- `concepts/agent-vm-sandboxing.md` — added defenseclaw
- `concepts/skill-vetting.md` — added defenseclaw, src-hunter-skill
- `concepts/twelve-rule-claude-md-template.md` — added Karpathy 82k★ reference
- `concepts/cross-wiki-routing.md` — added cross-wiki-tool-eval-inventory

**Remaining items cataloged** in `concepts/cross-wiki-tool-eval-inventory.md` (one-line per item, ~35 items across K45–K56).

All 15 briefs marked `processed: 2026-05-21`. Briefs retained for provenance trail.

## [2026-05-17] cross-wiki route | ai-token-monitor + CodexBar + SuperClaude_Framework + Roo-Code (OSINT 56-repo tool eval)

Four entity pages cross-routed into CCC from the OSINT-side 56-repo multi-wiki tool eval `@osint-wiki/sources/multi-wiki-tool-eval-ipsale-risk-2026-05-17.md`. All four are CCC-primary-fit, all tier **Adopt** in the eval.

**New pages (4, all `entities/tools/`)**:
- `entities/tools/ai-token-monitor.md` — cross-platform Tauri desktop app monitoring Claude Code + Codex token usage; offline-first except opt-in leaderboards. MIT. Token telemetry for the laptop-side fleet.
- `entities/tools/codexbar.md` — lightweight macOS menu-bar app; live API stats, daily/weekly limit tracking, desktop overrun notifications for Claude Code + Codex. MIT. The enforcement/alerting layer for token-economic policy.
- `entities/tools/superclaude-framework.md` — Claude Code configuration/automation framework (slash commands + cognitive personas + KNOWLEDGE.md integrations). ~22.8k★. MIT. Maps to CCC's document/extend/standardize mandate.
- `entities/tools/roo-code.md` — autonomous AI agent team embedded in the code editor; ~24.1k★. Apache-2.0. **Repo ARCHIVED by owner** — recorded as adoptable only as a fork-and-maintain blueprint, not a live dependency; Apache-2.0 permits the fork. Archived-repo caveat called out in Narrative + Dead Ends.

**Bidirectional backlinks added** to 4 existing CCC pages: `entities/openusage.md` (sibling token tool — linked from both monitors), `concepts/token-economics-and-prompt-caching.md` (concept link for both monitors), `concepts/subagent-orchestration.md` (concept link for SuperClaude_Framework persona model + Roo-Code agent team), `entities/tools/claude-code.md` (harness link for SuperClaude_Framework), `entities/claude-code-agent-farm.md` (sibling multi-agent tool — linked from Roo-Code). `updated:` bumped on all five.

**`index.md` updated**: 4 tool rows + 4 cross-wiki-link rows. No pre-existing near-equivalent pages — `openusage` is the closest sibling (token telemetry) but is a distinct tool (Go daemon vs Tauri app vs Swift menu-bar); linked, not merged. Do NOT git commit — left staged.

---

## [2026-05-17] parked-followup batch | 10 ROADMAP follow-ups stubbed from sibling-wiki primaries

Cleared 10 of the 11 parked follow-ups from `ROADMAP.md` § Follow-ups from the deep-dive. Each new page is a Claude-Code-side stub pointing at an existing OSINT or Cybersec primary; bodies focus on the CCC slice (Tier-2 gates, hook collisions, harness configuration, memory-stack composition).

**New pages (10)**:
- `concepts/agent-vm-sandboxing.md` — cross-wiki stub → `@cybersecurity-wiki/concepts/agent-vm-sandboxing.md`
- `concepts/skill-vetting.md` — internal extraction from `entities/mcp-servers/anthropic-skills.md` (5-step Phase-0 checklist; OSINT-side namesake is `[RETRACTED]`, intentionally different concept)
- `concepts/twelve-rule-claude-md-template.md` — cross-wiki stub → `@osint-wiki/concepts/claude-md-12-rule-template.md`
- `entities/tools/claude-obsidian.md` — cross-wiki stub → `@osint-wiki/entities/tools/claude-obsidian.md` (DO NOT ADOPT, recorded for the hook-collision case study)
- `entities/patterns/cpr-context-compression.md` — cross-wiki stub → `@osint-wiki/concepts/context-compression-resume-pattern.md`
- `entities/patterns/autoresearch-loop.md` — cross-wiki stub → `@osint-wiki/concepts/autoresearch-loop-pattern.md`
- `entities/patterns/scatter-gather.md` — cross-wiki stub → `@osint-wiki/concepts/scatter-gather-topology.md`
- `entities/mcp-servers/stash.md` — cross-wiki stub → `@osint-wiki/sources/alash3al-stash.md`
- `entities/mcp-servers/llm-wiki-compiler.md` — cross-wiki stub → `@osint-wiki/sources/atomicmemory-llm-wiki-compiler.md`
- `entities/mcp-servers/polymarket-mcp-server.md` — cross-wiki stub → `@osint-wiki/sources/caiovicentino-polymarket-mcp-server.md`

**Bidirectional backlinks added** to 17 existing CCC pages: cua, claude-mem, claude-code, claude-code-ultimate-guide, conductor-mcp, pmxt-mcp-pattern, plugin, full-prompt-goal-template, ralph-loop, tier1-tier2-agent-model, anthropic-skills, librarian-kb-server, context-engineering, token-economics-and-prompt-caching, subagent-orchestration, hooks-for-automation, cross-wiki-routing.

**`index.md` updated**: 1 tool row, 3 mcp-server rows, 3 pattern rows, 3 concept rows, 10 cross-wiki-link rows.

**Deferred from this batch**:
- `entities/patterns/structured-findings-schema.md` — no primary page found in OSINT/Cybersec; defer until either a primary surfaces or Cemini ships its own structured-findings shape.
- `entities/mcp-servers/kb-server.md` — covered by existing `entities/mcp-servers/librarian-kb-server.md`; would be duplicate. Closed from the parked list.

---

## [2026-05-16] cross-wiki ingest | Claude-Code/agent-orchestration tools from OSINT tool-eval (v3 iteration)

Five pages cross-routed into CCC from the OSINT-side tool-eval ingest `@osint-wiki/sources/tool-eval-wiki-fit-v3-iteration-2026-05-16.md`.

**2 primary tool pages** (CCC primary fit):
- `entities/tools/claude-for-legal.md` — Anthropic's official legal-vertical Claude Code/MCP plugin suite (Apache-2.0, 6,100★/6 issues). Verdict STEAL-FROM: extract managed-agent cookbooks (cadence jobs), cold-start interviews (skill bootstrapping), the Trust Layer injection guardrail (subagent orchestration), and the MCP-connector reference architecture. `[NEEDS VERIFICATION 2026-05-16]` on the Trust Layer "license gates" mechanism.
- `entities/tools/skillkit.md` — universal cross-agent skill translation/management bridge (Apache-2.0, 1,100★, last commit 2026-04-21). Verdict ADOPT: the `npx @skillkit/mcp` runtime-discovery server + SKILL.md↔.mdc translation. Marketplace (400k+ skills) treated as discovery-only. `[NEEDS VERIFICATION 2026-05-16]` on P2P-mesh security in zero-trust subnets.

**3 cross-wiki pattern stubs** (primary home is a sibling wiki; CCC-relevant patterns only):
- `entities/mcp-servers/pmxt-mcp-pattern.md` — MCP-exposes-trading-execution pattern (`@pmxt/mcp`); primary `@osint-wiki/entities/tools/pmxt.md`
- `entities/tools/polyterm-tui-pattern.md` — terminal-native UI-design reference; primary `@osint-wiki/entities/tools/polyterm.md`
- `entities/tools/osmedeus-acp-orchestration.md` — ACP subprocess-agent orchestration pattern for the conductor; primary `@cybersecurity-wiki/entities/tools/osmedeus.md`

**Bidirectional backlinks added** to 11 existing CCC pages: subagent-orchestration, full-prompt-goal-template, anthropic-skills, plugin, claude-mem, claude-desktop-vs-claude-code, context-engineering, conductor-mcp, tier1-tier2-agent-model, claude-code, exa. `index.md` updated (4 tool rows, 1 mcp-server row, 6 cross-wiki-link rows). No pre-existing near-equivalent pages found — all 5 are new.

---

## [2026-05-13] deep-dive sweep | mined OSINT/Cybersec/SEO/3D-printing/Image-gen for Claude Code material

Cross-wiki inventory pass dispatched two parallel Explore agents to scan the four sibling wikis (OSINT was the largest pool; SEO + Cybersec produced the densest finds). 48 OSINT entries + ~20 sibling entries surfaced. Decisions:

**16 NEW pages added**:
- `entities/tools/`: lazy-tool, claude-code-router, spec-kit, ttok, tech-debt-skill, cua, claude-code-ultimate-guide
- `entities/mcp-servers/`: (none new this round)
- `entities/skills/` (new subdir): tech-debt-audit, claude-seo-agrici, marketingskills, geo-seo-claude
- `entities/commands/` (new subdir): plugin
- `entities/patterns/`: tier1-tier2-agent-model
- `concepts/`: claude-desktop-vs-claude-code, three-cache-architecture, mcp-context-optimization

**8 existing pages deepened** (added Relations + new sections):
- claude-code (now hub-flagged), claude-mem, anthropic-skills, token-economics-and-prompt-caching, subagent-orchestration, hooks-for-automation, ralph-loop, context-engineering

**Cross-wiki backlinks added** (10 sibling pages):
- SEO: claude-code-tool-stack, claude-platforms, claude-seo-agrici, geo-seo-claude, marketingskills, github-repo-audit-2026-05-07
- Cybersec: llm-pentest-automation, pentest-ai-agents, cua, claude-code-ultimate-guide
- Plus `ccc-wiki` row added to SEO and Cybersec wikis' `Related Wikis` tables (the OSINT row was added at bootstrap)

**Lint**: clean. 32 pages indexed (up from 16), 179 outbound edges (up from 58), 36/36 cross-wiki refs resolve (up from 8/8). 0 orphans, 0 bidirectional gaps, 0 dangling refs, 0 frontmatter issues.

**Source-wiki page-count by category** (post-sweep):
- entities/tools: 13 (up from 6)
- entities/mcp-servers: 3
- entities/skills: 4 (new)
- entities/commands: 1 (new)
- entities/patterns: 3 (up from 2)
- concepts: 8 (up from 5)
- TOTAL seed pages: 32 (up from 16)

Backlogged in ROADMAP for follow-up depth: structured-findings-schema pattern, cpr-context-compression pattern, agent-vm-sandboxing concept, skill-vetting concept, twelve-rule-claude-md-template concept, plus per-skill audit pages for any future skill adoption.

---

## [2026-05-13] bootstrap | CCC meta-wiki seeded from sibling-wiki schemas

Fifth sibling wiki in the Cemini federation initialized. Topic: meta — how Cemini operates Claude Code.

- Mirrored Cybersecurity wiki's `CLAUDE.md` schema (laptop-only flavor); adapted folder layout (entity categories: tools / skills / mcp-servers / hooks / commands / patterns / people), Related-Wikis table, Phase-0 audit failure-mode bullets.
- Ported `scripts/wiki_lint.py` and `scripts/preingest_check.py` from OSINT WORKSPACE/scripts. No code changes — the scripts are env-driven (`WIKI_DIR`) and locate the wiki by `Path(__file__).parent.parent / "wiki"`.
- Authored root files: `README.md`, `ROADMAP.md`, `LESSONS.md`, `hot.md`, `.gitignore`.
- Wrote 16 seed pages:
  - `entities/tools/`: claude-code, claude-mem, exa-mcp, conductor-mcp, openspec, syncthing
  - `entities/mcp-servers/`: anthropic-skills, exa, librarian-kb-server
  - `entities/patterns/`: ralph-loop, full-prompt-goal-template
  - `concepts/`: context-engineering, token-economics-and-prompt-caching, subagent-orchestration, cross-wiki-routing, hooks-for-automation
- Wired 7 cross-wiki body @-links from CCC into OSINT (ralph-loop, full-prompt-goal-template, openspec, conductor, librarian, subagent-orchestration, cross-wiki-routing).
- Added `ccc-wiki` row to OSINT's CLAUDE.md Related Wikis table (path: `../projects/Cemini claude code CCC/wiki/`) and added `@ccc-wiki/...` backlinks to the OSINT target pages.
- Initialized git repo. No remote configured. Initial commit covers the schema, scripts, seed corpus, and index/log.
- Lint result: clean (exit code 0). All `@path` body mentions resolve; all `related:` paths resolve; no orphans; no bidirectional gaps; no missing frontmatter.

Pages created: 16 + index.md + log.md. Outbound cross-wiki links: 7. Inbound backlinks added to OSINT: matches outbound count.

## [2026-05-13] cross-wiki route | Nested Learning (Behrouz et al, NeurIPS 2025)

Cross-wiki stub routed from `@osint-wiki/sources/nl-nested-learning-behrouz-neurips2025.md`.
- Created wiki/concepts/nested-learning.md (stub)

## [2026-05-14] cross-wiki route | visual-explainer — Agent Skill for Rich HTML Diagram Generation

Cross-wiki stub routed from `@osint-wiki/entities/tools/visual-explainer.md`.
- Created wiki/entities/visual-explainer.md (stub)

## [2026-05-14] cross-wiki route | openusage — Local Token Economics Dashboard

Cross-wiki stub routed from `@osint-wiki/entities/tools/openusage.md`.
- Created wiki/entities/openusage.md (stub)

## [2026-05-14] cross-wiki route | claude_code_agent_farm — Parallel Claude Code Orchestration via tmux

Cross-wiki stub routed from `@osint-wiki/entities/tools/claude-code-agent-farm.md`.
- Created wiki/entities/claude-code-agent-farm.md (stub)

## [2026-05-14] cross-wiki route | Fusion — Multi-Node Agent Orchestrator with Worktree Isolation

Cross-wiki stub routed from `@osint-wiki/entities/tools/fusion.md`.
- Created wiki/entities/fusion.md (stub)

## [2026-05-15] cross-wiki route | multi-codex — CODEX_HOME env-var isolation pattern

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_multi-codex-codex-home-isolation.md (stub)

## [2026-05-15] cross-wiki route | tolaria — refactoring-workflow patterns (STEAL-FROM, AGPL-3.0)

Cross-wiki stub routed from `@osint-wiki/sources/eval-github-repos-2026-05-13.md`.
- Created wiki/concepts/2026-05-13_tolaria-steal-from-patterns.md (stub)

## [2026-05-16] phase-0 | K49 tool audits (SkillKit, claude-for-legal)

Phase-0 clone audits of the 2 CCC-wiki K49 tools. Verdicts in each entity page's `## Phase-0 Audit` section.

- **SkillKit → CONDITIONAL-GO** (downgraded from the eval's ADOPT). Apache-2.0 confirmed; deps clean. Domain-fit mismatch: SkillKit's headline value is cross-agent skill translation (Cursor/Devin) + a multi-machine P2P mesh — Cemini's CCC is Claude-Code-only with no multi-machine deployment, so those features solve problems Cemini doesn't have. The "400k-skill marketplace" claim is inflated ~26× (actual catalog: 15,120). Adopt only the `npx @skillkit/mcp` runtime-discovery server; skip the translation layer + mesh. Single-maintainer (personal account) — bus-factor risk.
- **claude-for-legal → STEAL-FROM-CONFIRMED.** Apache-2.0 confirmed; genuine `anthropics` org repo (Anthropic-staff commits). Pattern extraction into IP-sale surfaces is cleared. Extractable patterns confirmed present: managed-agent cookbooks (5 templates), cold-start interview SKILL.md, and the Trust Layer — actually a two-part guardrail (read-only-subagent injection check + admin allowlist), richer than the eval's "license gate" framing. Do not adopt the suite; extract the patterns for `subagent-orchestration`.

## [2026-05-31] cross-wiki route | Trading posts compilation 16 K90

Cross-wiki stub routed from `@osint-wiki/sources/trading-posts-compilation-16-2026-05-31.md`.
- Filled `wiki/sources/trading-posts-compilation-16-2026-05-31.md` + K90 concept pages (see ingest entry above)

## [2026-05-31] cross-wiki route | Multi-wiki tool eval v6 K90

Cross-wiki stub routed from `@osint-wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md`.
- Filled `wiki/sources/multi-wiki-tool-eval-v6-k90-2026-05-31.md` + K90 tool entity pages (see ingest entry above)

## [2026-06-01] cross-wiki route | Trading posts compilation K92 (12 posts)

Cross-wiki stub routed from `@osint-wiki/sources/trading-posts-compilation-12-2026-06-01.md`.
- Filled source + K92 harness pages (see ingest entry above)

## [2026-06-05] skill | cursor-audit — multi-model Cursor debug harness

Mirrored from OSINT WORKSPACE `.cursor/skills/cursor-audit/` (origin: codex + opus caught different errors on same bug).
- Created `.cursor/skills/cursor-audit/` (SKILL.md + reference.md + examples.md) in CCC + OSINT
- Created `wiki/entities/skills/cursor-audit.md`
- Backlinks: `@concepts/subagent-orchestration.md`, `@entities/patterns/glasswing-deliberate-disagreement.md`, `@entities/tools/council-of-high-intelligence.md`, `@entities/skills/tech-debt-audit.md`

## [2026-06-06] skill | cursor-audit — open-source distro in agent-toolkit-demo

Public ship of multi-model Cursor audit skill (v1.0.1).
- Added `skills/cursor-audit/` to [agent-toolkit-demo](https://github.com/cemini23/agent-toolkit-demo) (SKILL.md + reference.md + examples.md + README.md)
- CI: `vet-cursor-audit` job in agent-toolkit-demo workflow
- Scrubbed OSINT-private refs → [vet](https://github.com/cemini23/vet) for static brief gates
- Updated `wiki/entities/skills/cursor-audit.md` install path; CCC + OSINT mirrors bumped to 1.0.1
- Toolkit README links: agent-toolkit-demo, CCC, vet

## [2026-06-09] skill | super-audit — five-model pre-ship council (public distro)

Extends cursor-audit: 3 Cursor Task + 2 HTTP API auditors (OpenRouter/DeepSeek); tailored prompt packs per run.
- Public: [agent-toolkit-demo/skills/super-audit](https://github.com/cemini23/agent-toolkit-demo/tree/main/skills/super-audit) commit `40b97db`; `vet-super-audit` CI PASS 100/100
- Mirrored `.cursor/skills/super-audit/` in CCC + OSINT
- Created `wiki/entities/skills/super-audit.md`
- Backlinks: `@entities/skills/cursor-audit.md`, `@concepts/subagent-orchestration.md`, `@entities/patterns/glasswing-deliberate-disagreement.md`, `@osint-wiki/concepts/llm-routing-deepseek-openrouter-failover.md`
- Provenance: poker Tournament S1 + WC bot prod super audits

## [2026-06-13] skill | cursor-audit + super-audit — remove Fable 5 defaults

v1.2.0: Anthropic withdrew `claude-fable-5-thinking-high` from Cursor subagents. Opus is now the Anthropic default for all modes; fallback chain is opus → sonnet. Deleted `fable-5-prompting.md`. Mirrored in OSINT + agent-toolkit-demo.

## [2026-06-09] skill | cursor-audit + super-audit — Claude Fable 5 Anthropic default

v1.1.0: add `claude-fable-5-thinking-high` as default Anthropic leg for agentic/coding modes; opus retained for `brief-plan`.
- Updated `.cursor/skills/cursor-audit/` + `.cursor/skills/super-audit/` in OSINT + CCC
- Updated `wiki/entities/skills/cursor-audit.md` + `super-audit.md`
- Public distro: agent-toolkit-demo skills sync; vet PASS 100/100

## [2026-06-06] cross-wiki route | ADK Arena — agent framework benchmark (OSINT handoff)

Cross-wiki stub routed from `@osint-wiki/sources/arxiv-adk-arena-agent-dev-kits-2606.05548-2026-06-06.md`.
- Created wiki/concepts/adk-arena-agent-framework-benchmark.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — Ahmad Osman on why local AI is catching up

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-06-30-ahmad-osman-on-why-local-ai-is-catching-up.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-06-30-ahmad-osman-on-why-local-ai-is-catching-up.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — [AINews] not much happened today

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-06-30-ainews-not-much-happened-today.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-06-30-ainews-not-much-happened-today.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — AIEWF Daily Dispatch: Loops, Software Factories & Forward Deployed Engineers

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-aiewf-daily-dispatch-loops-software-factories-fo.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-aiewf-daily-dispatch-loops-software-factories-fo.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — [AINews] Sonnet 5 today, and Fable 5 tomorrow

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-ainews-sonnet-5-today-and-fable-5-tomorrow.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — Autoresearch: The feedback loop behind self-improving agents

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-autoresearch-the-feedback-loop-behind-self-impro.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-autoresearch-the-feedback-loop-behind-self-impro.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — Forward Deployed Engineers and the future of software engineering

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-forward-deployed-engineers-and-the-future-of-sof.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-forward-deployed-engineers-and-the-future-of-sof.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — How Cursor deploys AI inside the enterprise

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-how-cursor-deploys-ai-inside-the-enterprise.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-how-cursor-deploys-ai-inside-the-enterprise.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — 🔬 The Coolest Diffusion Research Isn't in LLMs — Evan Feinberg & Sergey Edunov, Genesis Molecular AI

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-the-coolest-diffusion-research-isnt-in-llms-evan.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-the-coolest-diffusion-research-isnt-in-llms-evan.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — Warp CEO Zach Lloyd on why software factories are the next phase of coding

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-01-warp-ceo-zach-lloyd-on-why-software-factories-ar.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-01-warp-ceo-zach-lloyd-on-why-software-factories-ar.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — AIEWF Daily Dispatch: Autoresearch and the tension between AI and human agency

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-02-aiewf-daily-dispatch-autoresearch-and-the-tensio.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-02-aiewf-daily-dispatch-autoresearch-and-the-tensio.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — [AINews] not much happened today

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-02-ainews-not-much-happened-today.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-02-ainews-not-much-happened-today.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — Skill engineering and the case against one-shot AI design

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-02-skill-engineering-and-the-case-against-one-shot.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-02-skill-engineering-and-the-case-against-one-shot.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — The website of the future may assemble itself for every visitor

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-02-the-website-of-the-future-may-assemble-itself-fo.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-02-the-website-of-the-future-may-assemble-itself-fo.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — AIEWF Daily Dispatch: The great loops debate and the state of AI engineering

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-03-aiewf-daily-dispatch-the-great-loops-debate-and.md (stub)

## [2026-07-05] cross-wiki route | Latent Space — Vercel's Andrew Qu on why agents are a new kind of software

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-03-vercels-andrew-qu-on-why-agents-are-a-new-kind-o.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-03-vercels-andrew-qu-on-why-agents-are-a-new-kind-o.md (stub)

## [2026-07-05] cross-wiki route | The Pragmatic Engineer — Impressions from visiting OpenAI, Anthropic, & Cursor

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-06-30-impressions-from-visiting-openai-anthropic-curso.md`.
- Created wiki/sources/newsletter-rss-pragmatic-engineer-2026-06-30-impressions-from-visiting-openai-anthropic-curso.md (stub)

## [2026-07-05] cross-wiki route | The Pragmatic Engineer — How Kent Beck shapes the software engineering industry

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md`.
- Created wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-01-how-kent-beck-shapes-the-software-engineering-in.md (stub)

## [2026-07-05] cross-wiki route | Addy Osmani's Blog — Agentic Autonomy Levels

Cross-wiki stub routed from `@osint-wiki/sources/substack-rss-addy-osmani-2026-07-03-agentic-autonomy-levels.md`.
- Created wiki/sources/substack-rss-addy-osmani-2026-07-03-agentic-autonomy-levels.md (stub)

## [2026-07-07] cross-wiki route | Latent Space — [AINews] The Field Guide to Fable

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-07-ainews-the-field-guide-to-fable.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-07-ainews-the-field-guide-to-fable.md (stub)

## [2026-07-08] cross-wiki | K149 ccc

- Lilian Weng harness + context-engineering integrate briefs

## [2026-07-15] ingest | K169 — Better Harnesses Smaller Models + Rethinking Harness Evolution Evaluation

- **Sources:** arXiv 2607.08938 (CMU — SLM harness adaptation, 90% cost recovery) + arXiv 2607.12227 (AI2/UW — harness-evolution evaluation rigor)
- **New pages:** `sources/arxiv-better-harnesses-smaller-models-2607.08938.md`, `sources/arxiv-rethinking-harness-evolution-evaluation-2607.12227.md`, `concepts/failure-mode-harness-adaptation-mapping.md`, `concepts/harness-evolution-vs-test-time-scaling-baseline.md`, `entities/tools/migration-analysis-replication-package.md` (NO-GO, no LICENSE), `entities/tools/rethinking-harness-evolution-eval-harness.md` (NO-GO, no LICENSE + paid infra)
- **Backlinks + `[NEEDS VERIFICATION 2026-07-15]` caveats added** on `concepts/harnessx-composable-evolution-foundry.md`, `concepts/seagym-self-evolving-harness-evaluation.md`, `concepts/retrospective-harness-optimization-rho.md`, `concepts/hierarchical-skill-stack-lazy-orchestration.md` — none of those source papers ran a test-time-scaling baseline or held-out generalization check, which the AI2/UW paper shows is necessary to trust magnitude claims
- **Phase-0:** both repos NO-GO adopt (no LICENSE on either GitHub API check; second repo also needs paid Claude/GPT/E2B/Serper API keys) — REFERENCE only
- **Briefs:** `briefs/2026-07-15_k169-harness-adaptation-evaluation-rigor-prod.md` → scp'd to `cemini-prod:/opt/cemini/briefs/` [CONFIRMED 6079 bytes on remote]; David adopt → `tipdrop-workspace-kit/briefs/2026-07-15_k169-slm-harness-adaptation-cost-recovery-adopt.md`; poker steal → `OSINT WORKSPACE/agents/devfun-poker-arena/briefs/2026-07-15_k169-slm-harness-cost-recovery-steal.md`
- **Archive:** both PDFs archived to `cemini-egress-fi:/opt/cemini-bulk/research/ccc/` (auto-archived by inbox pipeline before this session's explicit archive call ran; confirmed present + correct byte size via `ssh cemini-egress-fi`); local `research to be indexed/` copies removed
- Updated `wiki/index.md` (8 new rows); `ROADMAP.md` follow-up noted
- **Note:** a concurrent session in this workspace independently staged complementary K168/K169 artifacts for the same two papers around the same time — `briefs/2026-07-15_k168-slm-harness-adaptation-prod.md`, `briefs/2026-07-15_k169-harness-evolution-eval-discipline-prod.md`, `briefs/2026-07-15_k168-k169-harness-policy-hands-on.md`, source stubs `sources/brief-k168-slm-harness-adaptation-2026-07-15.md` / `sources/brief-k169-harness-evolution-eval-discipline-2026-07-15.md`, handoff `wiki/briefs/2026-07-15_ccc-handoff-slm-harness-eval-ingest.md`, Phase-0 scripts `scripts/adopt_k168_phase0.sh` / `scripts/adopt_k169_phase0.sh`, and backlinks on 9 further concept pages (`agent-harness-operational-definition`, `etclovg-harness-layers`, `failed-trajectory-harness-repair`, `harness-updating-vs-benefit-nonmonotonic`, `mcp-context-optimization`, `model-native-vs-tool-mediated-fulfillment`, `multi-agent-evidence-artifact-layers`, `operator-model-selection`, `meta/ccc-cross-wiki-handoff-briefs`). All of this was compatible with (referenced the same target filenames as) this session's core content — reconciled, not duplicated. All briefs from both sessions were sent to prod together in the single `scp_harness_briefs_to_prod.sh` run above.

## [2026-07-28] cross-wiki route | Latent Space — Codex / ChatGPT Work (2026-07-28)

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-latent-space-2026-07-28-codex-chatgpt-work.md`.
- Created wiki/sources/newsletter-rss-latent-space-2026-07-28-codex-chatgpt-work.md (stub)

## [2026-07-28] cross-wiki route | Pragmatic Engineer — Inside Anthropic (2026-07-28)

Cross-wiki stub routed from `@osint-wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-28-inside-anthropic.md`.
- Created wiki/sources/newsletter-rss-pragmatic-engineer-2026-07-28-inside-anthropic.md (stub)

## [2026-08-03] brief | K220 meat + Black-cat harness extract from OSINT

- Brief: `briefs/2026-08-03_k220-meat-black-cat-harness.md`
