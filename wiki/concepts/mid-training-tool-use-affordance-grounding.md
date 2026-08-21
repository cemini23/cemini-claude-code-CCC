---
title: "Mid-training for agentic tool use — affordance, grounding, recovery (MidTool)"
type: concept
tags: [concept, mid-training, tool-use, mcp, model-choice, k299]
keywords: [2608.20314, MidTool, MidTool-Mix, affordances, argument grounding, incomplete-info recovery]
related:
  - sources/arxiv-midtool-mid-training-data-synthesis-2608.20314.md
  - entities/tools/midtool.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: wont_wire
wire_target: "model-choice awareness only — no HF download, no runtime wire"
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-midtool-mid-training-data-synthesis-2608.20314.md`
- `@entities/tools/midtool.md`

## Raw Concept

Should general tool-use ability be shaped during mid-training rather than left entirely to post-training?

## Narrative

**MidTool** (UW / Snowflake / UNC): first open **mid-training** pipeline + corpus for *general tool use*. **MidTool-Mix = 20.3B tokens** from web (FineWeb), PDFs (FinePDFs), code, and structured tool artifacts (real APIs + MCP skills), synthesized into supervision by two branches:

- **Context-grounded trajectory augmentation** → *grounding*: recognize tool boundaries, infer parameters from docs/code, recover workflow structure from messy artifacts.
- **Native agentic trajectory synthesis** → *execution*: executable trajectories from real APIs / MCP skills / rollout traces with validation of schema grounding, turn order, required arguments, tool-response consistency.

Teaches four atomic capabilities: **recognize tool affordances · ground arguments from context · compose tool workflows · recover from incomplete information**. Mid-training Qwen3-4B/8B-Base on MidTool-Mix then applying the *same* downstream SFT (+RL) **consistently improves** BFCL, τ²-Bench, MCP Universe vs SFT-only baselines; RL compounds; biggest gains on harder multi-turn/interactive settings. Capability boundary: strong for broad tool-use transfer; specialized exploration (deep search) needs its own mid-training data.

**Cemini steal — model-choice awareness only:**

1. **Dedicated tool-use mid-training beats leaving it to post-training.** When selecting a model for MCP-heavy lanes, prefer families with agentic mid-training (K299 evidence), not only post-training RL.
2. **Evaluate the four atomic capabilities** (affordance recognition, argument grounding, workflow composition, incomplete-info recovery) rather than raw function-call accuracy (pairs K259 parameter-grounding / K296 terminal-state eval).
3. **Do not download HF `MidTool/midtool-release`** weights/datasets (volume + no runtime need); WATCH posture only.

| Verdict | **WATCH** — `wont_wire` runtime. Pairs K259 (CASCADE claim validation + NL→tool parameter grounding). |

## Snippets

> "General tool use, like other important LLM capabilities, benefits from dedicated mid-training rather than being left entirely to post-training." [Source: arxiv 2608.20314 (retrieved 2026-08-21)]
