---
title: Failure-mode-indexed harness adaptation — SLM cost recovery framework
type: concept
tags: [concept, harness-adaptation, slm, cost-efficiency, failure-taxonomy, k168]
keywords: [2607.08938, tool-use failure, instruction-following failure, knowledge failure, long-context failure, planning failure, add contexts, create tools, instrument code, harness optimizer, gepa]
related:
  - sources/arxiv-better-harnesses-smaller-models-2607.08938.md
  - concepts/harness-evolution-vs-test-time-scaling-baseline.md
  - concepts/etclovg-harness-layers.md
  - concepts/harnessx-composable-evolution-foundry.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/operator-model-selection.md
  - concepts/mcp-context-optimization.md
  - entities/tools/migration-analysis-replication-package.md
  - sources/brief-k168-slm-harness-adaptation-2026-07-15.md
  - briefs/2026-07-15_ccc-handoff-slm-harness-eval-ingest.md
  - sources/brief-k169-harness-adaptation-evaluation-rigor-prod-2026-07-15.md
  - concepts/agent-optimizer-compounding-and-regression-control.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/arxiv-agent-optimizers-compound-continual-learning-2607.14004.md
  - concepts/hybrid-slm-ensemble-orchestration.md
  - sources/arxiv-slm-ensemble-malware-orchestration-2607.20216.md
maturity: draft
created: 2026-07-15
updated: 2026-07-23
---

## Relations

- `@sources/arxiv-better-harnesses-smaller-models-2607.08938.md` — CMU K168 provenance
- `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — companion caution: don't credit magnitude claims without a scaling baseline
- `@concepts/etclovg-harness-layers.md` — this framework's three categories map onto ETCLOVG's context/tools/control layers
- `@concepts/harnessx-composable-evolution-foundry.md` — sibling nine-dimension search space; this paper's search space is narrower (context/tools/hooks/context-mgmt/sub-agents) but empirically validated with real cost numbers
- `@concepts/operator-model-selection.md` — model-routing policy this framework directly informs (when is a cheap model viable with the right harness?)

## Raw Concept

What determines whether an agent failure can be fixed by editing the **harness** rather than requiring a **bigger model** — and which harness edit fixes which failure? Synthesized from `@sources/arxiv-better-harnesses-smaller-models-2607.08938.md` (CMU, 2607.08938).

## Narrative

### The capability-gap model

Agent failure = **task demand > model capability**, along five axes: **tool-use**, **instruction-following**, **knowledge**, **long-context**, **planning/reasoning**. A harness edit doesn't make the model smarter — it either (a) reduces the demand on that axis, or (b) offloads the responsibility to deterministic code. Both are viable; the paper's data says which strategy fits which axis:

| Failure axis | Best-fit strategies | Risk introduced |
|---------------|---------------------|------------------|
| tool-use | filter tools (T2), wrap sequences into new tools (T1) | more tools created → new tool-use failures if overdone |
| instruction-following | reinforce instructions (A1), enforce via hooks (L1) | longer prompt → new instruction-following/long-context load |
| knowledge | externalize implicit knowledge into prompt (A1), encode into tool implementation (T1) | context bloat |
| long-context | progressive reveal / compress (A2), compact tool outputs (T1) | management itself risks new planning/reasoning failures (more exploration work) |
| planning/reasoning | provide explicit plan skeleton (A1), encode planning into tool (T1) | — least offloadable; harness cannot substitute for missing core reasoning |

**Key asymmetry:** planning/reasoning is the axis hardest to fully offload — this is why weak-base-capability SLMs benefit least from harness adaptation (+15.5%) vs. strong-base SLMs (+48.8%). A harness can absorb *task difficulty*, not *missing model capability*.

### Diagnostic loop (practical checklist, generalized from the paper's optimizer)

1. Run the task with a generic/minimal harness; collect **raw** (not summarized) trajectories.
2. For each failure, tag it against the five axes above — most real failures are compound (e.g. tool-use failure caused by a knowledge gap about which tool applies).
3. Pick the adaptation strategy whose "risk introduced" column doesn't reintroduce a worse failure than the one being fixed.
4. Validate on a **held-out** batch before promoting — see `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` for why in-distribution-only validation overstates the fix.
5. Re-run per model migration — adaptations are model-specific and do not transfer cleanly (paper RQ4: ministral-3-8b needed new file-editing tools; qwen3-coder-30b-a3b needed JSON-vs-XML tool-call format fixes; gemma-4-26b-a4b needed prompt+hook combos).

### When adaptation is worth the $20-ish optimization cost

- **Task diversity is low** (instances share a workflow) — Spearman ρ = −0.96 between diversity and optimized-harness score.
- **Task recurs often enough** to amortize the one-time optimization cost (paper: ~13 runs to break even given per-run savings).
- **Base model capability is not the bottleneck** — check a general benchmark index (paper uses Artificial Analysis) before investing; a weak model with a great harness still underperforms a capable model with a mediocre one.

### Cemini mapping

| Cemini surface | Applicable adaptation |
|-----------------|------------------------|
| `@concepts/operator-model-selection.md` routing | Add "harness-adapted" as a third tier between "cheap model, generic prompt" and "always use frontier model" — repetitive, low-diversity subagent tasks (log triage, format conversion, routine classification) are the ROI sweet spot |
| Poker arena per-hand decisions | Highly repetitive, structured workflow → strong candidate for filtered-tool + fixed-plan harness on a cheap model instead of frontier LLM per hand (see K169 poker brief) |
| TipDrop message parsing/classification | Low-diversity, recurring workflow → candidate for the anti-loop-hook + tool-filter pattern from Fig. 4 |
| Subagent dispatch (`Task` tool) | Anti-loop hooks (deny repeated identical tool calls with an explanatory rejection) are a cheap, generally-applicable guardrail regardless of model tier |

### Verdict

**ADOPT** the five-axis failure taxonomy and the diagnostic checklist as a design discipline for any future SLM/cheap-model routing decision. **REFERENCE** (do not install) the optimizer implementation itself — it's a `software-agent-sdk`-specific research harness, not a portable tool; see `@entities/tools/migration-analysis-replication-package.md`. **[NEEDS VERIFICATION 2026-07-15]** on the specific magnitude claims (89.7% recovery at 4% cost) pending a test-time-scaling baseline comparison per `@concepts/harness-evolution-vs-test-time-scaling-baseline.md` — the failure-mode taxonomy is sound independent of whether the specific optimizer numbers replicate.

## Snippets

> "A knowledge failure may be mitigated by adding contexts of domain instructions, a tool-use failure by transforming the available tools, a long-context failure by hiding irrelevant observations, and an instruction-following failure by enforcing constraints outside of the model outputs." — §II-B
