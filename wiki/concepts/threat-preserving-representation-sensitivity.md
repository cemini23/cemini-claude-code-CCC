---
title: "Threat-Preserving Representation Sensitivity in Agent-Security Benchmarks (CCC K423)"
type: concept
tags: [concept, k423]
keywords: [2610.03585, k423]
related:
  - sources/arxiv-threat-preserving-representation-sensitivity-2610.03585.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-05_ccc-k421-k425-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-05
updated: 2026-10-05
---

## Relations

- `@sources/arxiv-threat-preserving-representation-sensitivity-2610.03585.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-05_ccc-k421-k425-sip-ready.md`

## Raw Concept

K423: ADOPT eval-methodology — arXiv 2610.03585.

## Narrative

**Benchmark validity — the security score depends on how you phrase the threat.** The paper asks a measurement question with a surprising answer. Take an agent-security benchmark, change **only the agent-visible representation** — a tool's *name*, its description — while holding the task, the harmful action, the security policy, the ground truth, the environment, and the evaluation criteria **fixed**. How stable is the reported attack success rate? Across **28,904 agent runs** on three independent benchmarks it is **not stable, and not uniformly**: renaming `DNSPoisoning` to `DNSConfiguration` **raises** committed ASR by **11.67 points** on GPT-5-mini and **13.21** on Claude Haiku 4.5; on MCPTox, adding threat wording **lowers** ASR by 11.00 and 4.11 points. The two are directionally aligned — more threat-explicit naming means less measured attack success — and the effect is **larger, not smaller, when the threat is hidden.** A control arm is sharper still: a **threat-neutral** name matched on token count, length, and casing reproduced **8.54 of the 11.00 points**, so explicit threat vocabulary is **not** the driver. On AgentDojo the ASR effect was small (0.50 points) but benign utility fell 5.36 points — **changing the label changed capability too.** **CCC relevance is direct and it is the K407 lesson generalised:** a score measured under one representation may not survive a threat-preserving rewrite of the same problem, so **robustness claims need a controlled set of variants, not a single number**. Pairs `@concepts/verifiable-deterministic-agent-benchmarking.md` / K407 (judge variance on byte-identical answers) / K392 (behavior assays) / `@concepts/low-cost-cross-vendor-behavior-assays.md`. **Cybersec-relevant too** — noted in their brief. No repo. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.03585 locators." [Source: CCC K423 synthesis]
