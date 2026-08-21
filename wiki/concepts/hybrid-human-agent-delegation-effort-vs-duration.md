---
title: "Hybrid human–agent delegation — effort vs duration, person not task"
type: concept
tags: [concept, hci, delegation, hybrid, mcp, k295]
keywords: [2608.19551, ICC, effort-vs-duration, delegation, risk-calibrated]
related:
  - sources/arxiv-delegating-or-doing-hybrid-human-agent-interfaces-2608.19551.md
  - entities/tools/delegating-or-doing-hybrid-hai.md
  - concepts/hybrid-gui-mcp-tool-adoption-gap.md
  - sources/brief-k295-k299-harness-wave-2026-08-21.md
  - briefs/2026-08-21_ccc-handoff-k295-k299-ingest.md
  - concepts/phase1-adopt-wire.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-21
updated: 2026-08-21
---

## Relations

- `@sources/arxiv-delegating-or-doing-hybrid-human-agent-interfaces-2608.19551.md`
- `@entities/tools/delegating-or-doing-hybrid-hai.md`

## Raw Concept

Does adding an MCP-connected agent to a GUI reduce work, and who delegates what?

## Narrative

**Delegating or Doing?** (N=73, HAI '26): MCP+GUI hybrid CMS where users complete CRUD tasks via GUI, chat agent, or both. Key findings:

- **AI-assisted interaction cut clicks / page navigations / scrolls** (NB-GLM significant; AI-First fewest, Traditional most, Hybrid between) — lower *interaction effort*.
- **…but not wall-clock**: task duration did not differ significantly across conditions (AI-First descriptively fastest, 46.6 s).
- **Delegation variance is person > task**: by-participant random intercept ≈ half the chat-interaction variance (**ICC = .50**); an explicit AI-First directive only nudged average delegation, leaving the spread intact — occasional high-leverage handoffs, not sustained conversation.
- **No systematic risk-avoidance**: CRUD operation type did not predict delegation (χ²(3)=6.60, p=.086); DELETE drew descriptively *more* chat interactions than UPDATE.

**Cemini steal:**

1. **Measure effort and duration separately.** A hybrid interface judged on speed alone "does nothing" — track clicks/navigations/steps eliminated per delegation as the real signal.
2. **Do not treat MCP presence as a speedup.** Availability reduces manipulation events; it does not reduce completion time — do not claim latency wins from tool presence.
3. **Hybrid availability ≠ high-risk auto-delegate.** Users will not self-restrict on consequential actions — put confirmation/preview/reversibility **on the agent path**, at least as strong as in the GUI (pairs K239 execution fidelity).
4. **Do not make delegation the default**; design for the single handoff (state intent → confirm result), not sustained dialogue.

| Verdict | **ADOPT** — `policy_wired` (no public repo). Pairs K245 (GUI–MCP adoption gap) / K247 (voice input). |

## Snippets

> "AI-assisted interaction significantly reduced clicks, page navigations, and scrolling … task duration did not differ significantly across conditions." — delegation varied far more between participants than between tasks (ICC = .50). [Source: arxiv 2608.19551 (retrieved 2026-08-21)]
