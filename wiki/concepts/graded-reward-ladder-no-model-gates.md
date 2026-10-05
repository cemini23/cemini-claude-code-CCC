---
title: "NeutronGym: Physics-Graded Neutron Instrument Design for LLM Agents (CCC K424)"
type: concept
tags: [concept, k424]
keywords: [2610.03631, k424]
related:
  - sources/arxiv-neutrongym-graded-reward-ladder-2610.03631.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-05_ccc-k421-k425-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- `@sources/arxiv-neutrongym-graded-reward-ladder-2610.03631.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-05_ccc-k421-k425-sip-ready.md`

## Raw Concept

K424: ADOPT eval methodology — arXiv 2610.03631.

## Narrative

**NeutronGym — make the grader a simulator, and gate the tasks before you trust them.** An executable environment for neutron instrument design where agents build instruments through 22 validating MCP tools, **McStas ray-traces what they actually built**, and a **level-resolved ladder** grades it with **no LLM judge**: L1 syntax, L2 runtime, L3 structure, L4 science. The score **cannot be argued with** — it is a physics measurement, not an opinion. Two design lessons stand out, and both are about **distrusting your own benchmark**. First, **no-model admission probes**: before any pass rate is read as capability, a family must survive the best fixed answer, the best rule that reads the prompt, and every instance's solution applied to every other — decided on a one-sided confidence bound. Nine reward failures motivated the protocol and **four of the authors' own designs failed it.** Second, **contamination probes**: published instruments ship as example files, and in a pilot audit **4 of 7 agent episodes retrieved the reference file through ordinary, permitted tools**. Trained results: RL on the ladder takes Qwen3-8B from **11.3% → 76.7%** on held-out instances, past an untrained 32B; **removing partial credit collapses it by 60 points**; and imitation of the model's own successes degraded it three times. **CCC relevance:** the ladder and the no-model gate are directly transferable eval machinery, and the `wont_wire` finding is the honest one — frontier models still solve 98–99%, so the trained model matches a classical optimizer only when handed the closed-form physics. Pairs K406 Assay (mechanical gate) / `@concepts/verifiable-deterministic-agent-benchmarking.md` / K416 YouRA / K423 TPRS. No repo surfaced. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.03631 locators." [Source: CCC K424 synthesis]
