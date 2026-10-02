---
title: "VISTA: A Visual Harness for Reasoning in an Interactive World (CCC K419)"
type: concept
tags: [concept, k419]
keywords: [2610.02200, k419]
related:
  - sources/arxiv-vista-lossless-visual-memory-harness-2610.02200.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-02_ccc-k416-k420-sip-ready.md
  - concepts/agentic-meta-reasoning-control-plane.md
  - concepts/context-engineering.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-02
updated: 2026-10-02
---

## Relations

- `@sources/arxiv-vista-lossless-visual-memory-harness-2610.02200.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-02_ccc-k416-k420-sip-ready.md`

## Raw Concept

K419: ADOPT pattern (MIT) — arXiv 2610.02200.

## Narrative

**VISTA — lossless memory plus a way to look again.** A visual harness giving a general-purpose multimodal model long-horizon vision. The design rests on a diagnosis: existing VLMs **encode each observation once** and then discard the raw input, so the representation may omit **details that only turn out to matter later** — and the model cannot know at encoding time which they are. VISTA answers with three components: **visual observation** (perceive the environment directly), a **lossless visual memory** that keeps every frame *including intermediate animation frames* in original form, indexed by turn and frame, and **visual inspection tools** that let the model **revisit any frame or magnify any region** as its reasoning evolves. The framing is sharp: this is an **explicit attention mechanism over the interaction history**, letting the model choose what to look at instead of hoping the initial encoding kept it. Results are strong — **Claude Opus 5.0 goes from RHAE 40.68 to a perfect 100.00** on ARC-AGI-3 with xhigh effort, completing all 25 public games using **57.4% fewer actions than first-time humans**; GPT-5.6 Sol reaches 99.00. The harness transfers with minimal adaptation to three further benchmarks. **CCC relevance:** the general lesson is that **lossless retention plus cheap retrieval beats clever compression**, and that the agent should control what it re-reads rather than the harness pre-deciding. That contrasts productively with the compression-heavy line (K411 CLI truncation, K387 KV working-set, `@concepts/truncate-only-long-horizon-compaction.md`). Pairs K410 (compact controller state) / `@concepts/context-engineering.md` / `@concepts/test-time-world-model-validate-before-act.md`. **Phase-0: `joshhhhhan/VISTA` MIT**, 126★, 4 forks, 2.8 MB, pushed 2026-09-05 — healthy and **clone-eligible**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.02200 locators." [Source: CCC K419 synthesis]
