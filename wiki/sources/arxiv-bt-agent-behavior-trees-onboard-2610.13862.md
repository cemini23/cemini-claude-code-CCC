---
title: "BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi (CCC K447)"
type: source
tags: [source, arxiv, k447]
keywords: [2610.13862, k447]
related:
  - concepts/code-enforces-decisions-multi-fidelity-eval.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agent-harness-operational-definition.md
  - concepts/harness-security-axis-comparison.md
  - concepts/test-time-world-model-validate-before-act.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@concepts/code-enforces-decisions-multi-fidelity-eval.md`
- `@concepts/agent-completion-verification-gates.md`
- `@concepts/agent-harness-operational-definition.md`
- `@concepts/harness-security-axis-comparison.md`
- `@concepts/test-time-world-model-validate-before-act.md`
- `@briefs/2026-10-12_ccc-k445-k448-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | BT-Agent: Deploying Onboard Robot Agents with Behavior Trees and Multi-Fidelity Evaluation |
| **arXiv** | 2610.13862 (2026-10) |
| **Retrieved** | 2026-10-12 |

## Narrative

**Verdict: ADOPT pattern (harness split + multi-fidelity eval).**

**Let code enforce the conditions and let the model decide — then evaluate on more than one fidelity.** BT-Agent separates **task-level model reasoning** from **reactive execution** through predefined **behavior-tree (BT) skills**. An onboard **Actor** (ReAct loop) selects a skill and arguments; a **supervisor BT** runs one skill at a time; and each skill's **local guards recheck cancellation, time and preconditions on every tick and can interrupt a running action without another model call** — measured **19 ms** to commanded-zero velocity vs **3.2–3.9 s** for the next model decision. **The Actor cannot modify a skill's implementation or its guards**, so the logic is reviewable and testable independently of the policy. **Ablations name the two harness levers:** replacing **structured tool calls** with textual commands lowers success at every size (smallest models worst), and **removing informative failure feedback costs 2–6 points**. **Multi-fidelity evaluation:** a 161-task **text** benchmark vs 39 paired **Habitat** tasks — text runs **10.9× faster** (950 vs 87 episodes/hour), but **text success does not establish completion under sensing and motion** (only **57.3%** of text successes succeed in Habitat; Spearman ρ = 0.61), and **fault injection exposes failures that nominal success hides** (at 27B a nominal tie with ReAct becomes a BT-Agent lead under injected faults). A 9B model runs fully onboard on a Spot. **CCC reading:** the split is K436/K447's 'code enforces, model decides' shape — the same family as K444's L3 gate and K443's explicit-state policy — and the multi-fidelity lesson is the cheap-proxy caveat: **a fast text proxy ranks well but does not prove the deployable behavior** (pairs K438's cheap-proxy correlation finding). Reported under **Apache-2.0** (promised). Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "text supports 10.9 higher evaluation throughput, while simulation reveals how perception and motion failures change task outcomes." [Source: arXiv 2610.13862 (retrieved 2026-10-12)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.13862-bt-agent-deploying-onboard-robot-agents-with-beh.pdf` |
