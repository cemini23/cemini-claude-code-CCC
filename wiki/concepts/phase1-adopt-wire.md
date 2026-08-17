---
title: Phase-1 adopt-wire — policy vs runtime vs WONT_WIRE
type: concept
tags: [concept, phase-1, adopt, wire, harness, federation]
keywords: [phase1-wire, policy wire, runtime wire, unwired adopts, wire_status]
related:
  - entities/skills/phase1-wire.md
  - concepts/skill-vetting.md
  - concepts/k73-phase0-audit-decisions.md
  - concepts/cross-wiki-tool-adoption-routing.md
  - concepts/reconstructive-agent-memory-vs-verbatim-replay.md
  - concepts/active-abstraction-programmatic-world-models.md
  - concepts/passive-awareness-async-multi-agent-coordination.md
  - concepts/claim-centered-retrieval-with-provenance.md
  - entities/tools/asm-adopt-orphan.md
  - entities/tools/biosecbench-surveillance.md
  - sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md
  - briefs/2026-08-03_ccc-handoff-k234-k238-ingest.md
  - sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md
  - briefs/2026-08-04_ccc-handoff-k239-k243-ingest.md
  - entities/tools/agent-trajectory-sentinel.md
  - sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md
  - briefs/2026-08-05_ccc-handoff-k244-k248-ingest.md
  - entities/tools/hybrid-gui-mcp-osworld.md
  - entities/tools/urbanagent.md
  - entities/tools/multiglobeqa.md
  - entities/tools/turnsight.md
  - sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md
  - briefs/2026-08-06_ccc-handoff-k249-k253-ingest.md
  - entities/tools/scale-cda.md
  - entities/tools/canary-tools-mcp.md
  - entities/tools/rac-split-inference.md
  - entities/tools/artanno.md
  - entities/tools/argus-agentic-runtime.md
  - briefs/2026-08-07_ccc-handoff-k254-k258-ingest.md
  - briefs/2026-08-07_phase1-wire-status-closeout-k254-k258.md
  - entities/tools/av-aivat.md
  - entities/tools/hardware-keystore-mcp-signing.md
  - entities/tools/programmatic-tool-calling-ptc.md
  - entities/tools/read-agentic-document-search.md
  - entities/tools/trajdebug.md
  - briefs/2026-08-08_ccc-handoff-k259-cascade-ingest.md
  - entities/tools/cascade-mcp.md
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
  - briefs/2026-08-10_ccc-handoff-k260-residencyrl-ingest.md
  - entities/tools/residencyrl.md
  - briefs/2026-08-11_ccc-handoff-k261-k265-ingest.md
  - concepts/llm-verification-layer-accept-escalate-reject.md
  - concepts/scaffold-over-tool-interface.md
  - concepts/trajectory-driven-safety-harness-evolution.md
  - concepts/versioned-model-harness-continual-adaptation.md
  - entities/tools/macaron-v1.md
  - entities/tools/scaffolding-mcp-cli-study.md
  - entities/tools/she-safety-harness.md
  - entities/tools/vectrayx-vision-1b.md
  - entities/tools/verification-layers-robot.md
  - briefs/2026-08-12_ccc-handoff-k270-k273-ingest.md
  - concepts/agentic-configuration-management-acm.md
  - concepts/domain-solvers-as-agent-callable-mcp-skills.md
  - concepts/enterprise-mcp-auth-gateway.md
  - concepts/llm-assisted-writing-detection-hygiene.md
  - entities/tools/agent4binary.md
  - entities/tools/agentic-configuration-management-acm.md
  - entities/tools/enterprise-mcp-auth-gateway.md
  - entities/tools/llm-usage-in-pmc.md
  - sources/arxiv-agentic-configuration-management-acm-2608.11166.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - concepts/role-specialization-model-multi-tool-coordination.md
  - entities/patterns/convergent-detour-hijacking.md
  - entities/patterns/role-specialization-model.md
  - entities/tools/vakra.md
  - briefs/2026-08-14_ccc-handoff-k277-k281-ingest.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - concepts/marc-clinical-multi-agent-coordination.md
  - concepts/repo-level-verified-code-proof-eval.md
  - concepts/meta-harness-optimization-hitl-eval-contract.md
  - entities/patterns/treatment-blind-endpoint-integrity.md
  - entities/tools/intersage.md
  - entities/tools/marc-v1.md
  - entities/tools/vero.md
  - entities/tools/autodesign.md
  - concepts/skill-misevolution.md
  - briefs/2026-08-17_ccc-handoff-k282-k284-ingest.md
  - concepts/differential-fault-injection-llm-modernization.md
  - concepts/recoverable-agent-execution-checkpoints.md
  - concepts/test-time-world-model-validate-before-act.md
  - entities/patterns/differential-fault-injection-validation.md
  - entities/tools/agentrewind.md
  - entities/tools/mettlebench.md
  - entities/tools/twin-arc-agi-3.md
maturity: draft
created: 2026-07-31
updated: 2026-08-17
---

## Relations

- `@concepts/adversarial-curriculum-structured-reward-doc-fidelity.md`
- `@entities/skills/phase1-wire.md` — Cursor skill
- `@concepts/skill-vetting.md` — Phase-0 gate (audit ≠ wire)
- `@concepts/k73-phase0-audit-decisions.md` — eval ≠ adopt; Phase-1 adds ≠ wire
- `@concepts/cross-wiki-tool-adoption-routing.md` — which wiki owns the wire
- `@concepts/reconstructive-agent-memory-vs-verbatim-replay.md` — MemHarness policy
- `@concepts/active-abstraction-programmatic-world-models.md` — Tycho policy
- `@concepts/passive-awareness-async-multi-agent-coordination.md` — AgentRadio policy
- `@concepts/claim-centered-retrieval-with-provenance.md` — AskChem policy
- `@entities/tools/asm-adopt-orphan.md` — CCC orphan adopt wont_wire
- `@entities/tools/biosecbench-surveillance.md` — CCC orphan adopt wont_wire
- `@sources/brief-k234-k238-cyberneuro-mcp-tester-ham-accel-toktier-2026-08-03.md` — K234–K238 batch brief stub
- `@sources/brief-k239-k243-safety-sentinel-acem-2026-08-04.md` — K239–K243 batch brief stub
- `@entities/tools/agent-trajectory-sentinel.md` — K242 `policy_wired` entity
- `@sources/brief-k244-k248-urban-gui-mcp-hive-turnsight-2026-08-05.md` — K244–K248 batch brief stub
- `@entities/tools/hybrid-gui-mcp-osworld.md` — K245 `policy_wired` entity
- `@sources/brief-k249-k253-scale-cda-canary-rac-artanno-argus-2026-08-06.md` — K249–K253 batch brief stub
- `@entities/tools/canary-tools-mcp.md` — K250 `policy_wired` entity

## Raw Concept

Phase-0 decides whether a tool/pattern may enter the corpus. Phase-1 decides how it enters the **operator harness** (rules, CLAUDE.md, MCP) so agents actually follow it.

## Narrative

### Three gates

1. **Doc-level eval** — triage candidates (multi-wiki digest).
2. **Phase-0** — GO / CONDITIONAL / REFERENCE / NO-GO + optional `.local/adopts/` clone.
3. **Phase-1** — wire into daily agent behavior, or mark `wont_wire`.

Cloning without Phase-1 produces an endless REFERENCE shelf. Cemini default: **policy wire** for ADOPT patterns; **runtime wire** only for true drop-in clients; **wont_wire** for trainers, Modal/Harbor fleets, and OOD demos.

### Wire classes

| Class | `wire_status` | Artifact |
|-------|---------------|----------|
| Policy | `policy_wired` | Cursor `.mdc` rule and/or `CLAUDE.md` bullets |
| Runtime | `runtime_wired` | MCP / PATH / project skill install |
| Keep clone only | `wont_wire` | Entity notes “paper repro”; no harness edit |
| Later | `deferred` | Explicit next action |

### Surfaces

Wire on active ops: CCC, OSINT, TipDrop, Atto, poker, Cybersec, Game-dev, Gambling, SEO, CeminiSuite. **Do not** build local Image-gen / 3D-printing wire backlogs.

### Inventory

`python3 scripts/phase1_adopt_inventory.py --write-brief` scans CCC + OSINT `.local/adopts/` and joins wiki `wire_status`.

## Snippets

> Phase-0 audits; Phase-1 wires. [Source: `.cursor/skills/phase1-wire/SKILL.md`]
