---
title: "BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi (CCC K447)"
type: concept
tags: [concept, k447]
keywords: [2610.13862, k447]
related:
  - sources/arxiv-bt-agent-behavior-trees-onboard-2610.13862.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-harness-operational-definition.md
  - concepts/harness-security-axis-comparison.md
  - concepts/test-time-world-model-validate-before-act.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@sources/arxiv-bt-agent-behavior-trees-onboard-2610.13862.md`
- `@concepts/agent-completion-verification-gates.md`
- `@concepts/agent-harness-operational-definition.md`
- `@concepts/harness-security-axis-comparison.md`
- `@concepts/test-time-world-model-validate-before-act.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-12_ccc-k445-k448-sip-ready.md`

## Raw Concept

K447: ADOPT pattern (harness split + multi-fidelity eval) — arXiv 2610.13862.

## Narrative

**Let code enforce the conditions and let the model decide — then evaluate on more than one fidelity.** BT-Agent separates **task-level model reasoning** from **reactive execution** through predefined **behavior-tree (BT) skills**. An onboard **Actor** (ReAct loop) selects a skill and arguments; a **supervisor BT** runs one skill at a time; and each skill's **local guards recheck cancellation, time and preconditions on every tick and can interrupt a running action without another model call** — measured **19 ms** to commanded-zero velocity vs **3.2–3.9 s** for the next model decision. **The Actor cannot modify a skill's implementation or its guards**, so the logic is reviewable and testable independently of the policy. **Ablations name the two harness levers:** replacing **structured tool calls** with textual commands lowers success at every size (smallest models worst), and **removing informative failure feedback costs 2–6 points**. **Multi-fidelity evaluation:** a 161-task **text** benchmark vs 39 paired **Habitat** tasks — text runs **10.9× faster** (950 vs 87 episodes/hour), but **text success does not establish completion under sensing and motion** (only **57.3%** of text successes succeed in Habitat; Spearman ρ = 0.61), and **fault injection exposes failures that nominal success hides** (at 27B a nominal tie with ReAct becomes a BT-Agent lead under injected faults). A 9B model runs fully onboard on a Spot. **CCC reading:** the split is K436/K447's 'code enforces, model decides' shape — the same family as K444's L3 gate and K443's explicit-state policy — and the multi-fidelity lesson is the cheap-proxy caveat: **a fast text proxy ranks well but does not prove the deployable behavior** (pairs K438's cheap-proxy correlation finding). Reported under **Apache-2.0** (promised). Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "See source page for arXiv 2610.13862 locators." [Source: CCC K447 synthesis]
