---
title: "MotorMind: Scaffolding General Vision Language Models for Zero-Shot Robot Manipulation (CCC K408)"
type: concept
tags: [concept, k408]
keywords: [2609.38078, k408]
related:
  - sources/arxiv-motormind-vlm-mid-level-action-harness-2609.38078.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-09-30_ccc-k406-k410-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-09-30
updated: 2026-09-30
---

## Relations

- `@sources/arxiv-motormind-vlm-mid-level-action-harness-2609.38078.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-09-30_ccc-k406-k410-sip-ready.md`

## Raw Concept

K408: REFERENCE (cross-domain) — arXiv 2609.38078.

## Narrative

**MotorMind — VLM as robot controller.** A general-purpose VLM is equipped with a compact **mid-level action representation** (parameterized translations, rotations, gripper ops) plus a **deterministic embodiment-specific control layer** that converts proposals into physical motion. **Asynchronous monitoring** checks updated observations during execution and can cancel pending commands **at the next action boundary** — monitoring never blocks execution. Memory summaries are written in the background for later planning. 66.7% on LIBERO-PRO base and 53.8% under perturbation vs 13.3%/19.2% for the strongest prior zero-shot method; 95% average on a real xArm6. Swapping the backbone (Qwen3.8-Flash-Next → GPT-6 Sol) lifts base from 66.7% to 83.3%, showing **harness and backbone decouple**. **Cross-domain:** robotics is outside the CCC scope, so this is REFERENCE. No public repo surfaced. CCC value is the *pattern instance*: async monitor + non-blocking verification + boundary-only cancellation. Pairs K404 harness learning / `test-time-world-model-validate-before-act` / `world-acting-systems-taxonomy` / `system-scaling-harness-agentic-ai`. Runtime **`wont_wire`**; concept **`policy_wired`** awareness only.

## Snippets

> "See source page for arXiv 2609.38078 locators." [Source: CCC K408 synthesis]
