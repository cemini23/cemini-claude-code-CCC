---
title: CCC handoff — K295–K299 harness wave
type: brief
tags: [brief, handoff, k295, k296, k297, k298, k299]
related:
  - briefs/2026-08-21_ccc-k295-k299-sip-ready.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - sources/arxiv-delegating-or-doing-hybrid-human-agent-interfaces-2608.19551.md
  - sources/arxiv-thinkingbox-sandbox-benchmark-stateful-business-2608.19741.md
  - sources/arxiv-rl-trotter-long-time-quantum-simulation-2608.20139.md
  - sources/arxiv-task-coevolve-adaptive-validation-task-selection-2608.20169.md
  - sources/arxiv-midtool-mid-training-data-synthesis-2608.20314.md
  - concepts/hybrid-human-agent-delegation-effort-vs-duration.md
  - concepts/terminal-state-eval-discovery-reliability-gap.md
  - concepts/adaptive-validation-task-selection-harness-optimization.md
  - concepts/mid-training-tool-use-affordance-grounding.md
  - entities/tools/delegating-or-doing-hybrid-hai.md
  - entities/tools/midtool.md
  - entities/tools/task-coevolve.md
  - entities/tools/thinkingbox.md
  - concepts/phase1-adopt-wire.md
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@briefs/2026-08-21_ccc-k295-k299-sip-ready.md`

## Summary

K295 Delegating-or-Doing (effort ≠ duration, person > task delegation) + K296 Thinkingbox (terminal-state eval, MIT REFERENCE clone) + K298 Task-CoEvolve (variance-weighted val tasks, NO-GO clone) + K299 MidTool (WATCH, skip HF). K297 RL-Trotter = OOD quantum stub, `wont_wire`.

## Local

- `.local/adopts/thinkingbox` (MIT) — GO REFERENCE only; benchmark runtime **`wont_wire`**
- **No** `.local/adopts/Task-CoEvolve` (null SPDX); **no** MidTool HF download

## Routing

- Prod briefs + hands-on policy (scp'd via `scripts/scp_harness_briefs_to_prod.sh`)
- **Atto:** `../atto/briefs/2026-08-21_k296-thinkingbox-task-coevolve-from-ccc.md`
- **Cybersec:** `../Cybersecurity wiki/briefs/2026-08-21_k296-thinkingbox-from-ccc.md`
- **k244 fill:** 6 missing pages cited by `briefs/2026-08-21_k244-harness-skill-wayfinder.md` (Task-CoEvolve → K298)
- **Leftover (propose-only):** wayfinder skill, BPS router, EnvHarness wrap
