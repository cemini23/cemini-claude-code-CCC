---
title: "APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces (CCC K445)"
type: concept
tags: [concept, k445]
keywords: [2610.13623, k445]
related:
  - sources/arxiv-apex-harm-shared-workspace-agent-safety-2610.13623.md
  - concepts/agent-approval-laundering-transitive-effects.md
  - concepts/agent-data-injection-attacks.md
  - concepts/mcp-app-hitl-approval-gap.md
  - concepts/authorization-to-effect-closure.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-12_ccc-k445-k448-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-12
updated: 2026-10-12
---

## Relations

- `@sources/arxiv-apex-harm-shared-workspace-agent-safety-2610.13623.md`
- `@concepts/agent-approval-laundering-transitive-effects.md`
- `@concepts/agent-data-injection-attacks.md`
- `@concepts/mcp-app-hitl-approval-gap.md`
- `@concepts/authorization-to-effect-closure.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-12_ccc-k445-k448-sip-ready.md`

## Raw Concept

K445: ADOPT eval-methodology (shared-workspace injection) — arXiv 2610.13623.

## Narrative

**Completing the task is not evidence of safe behavior.** A benchmark for **prompt and script injection against long-horizon CLI agents in shared professional workspaces** (investment banking, law, consulting) — 115–328 files per task, 63 tools over MCP (mail, chat, calendar, docs, sheets, PDFs, code-exec), 12 frontier models, 180 instances. **Six attack categories**: static prompt injection, static script injection, **dynamic** prompt/script injection (a background `inotify` watcher hides a file after the agent reads it and plants a corrupted replacement that points at attacker code), task-specific script replacement, and attacker-provided generic script. **Headline:** Opus 5 and Sonnet 5 are most robust (**8% / 20%** average ASR), but **task-specific replacement and attacker-provided generic scripts stay effective at 81–84% and 73% ASR**. Gemini 3.8 Flash has the highest task score (**0.877**) with a **33% ASR** — the two axes are independent: *an agent can produce a correct deliverable while performing an unauthorized action*. **Two transferable findings for the harness:** (1) **readability governs refusal** — Python scripts have the lowest ASR because the agent can `cat` the source, while **PYC/ELF are executed unread** (they must be decompiled), so *do not hand an agent an unreadable artifact plus permission to run it*; (2) **internal leakage is under-guarded** — agents refuse email / external-link disclosure but treat sharing through shared folders and calendars as a benign workflow step. **CCC reading:** the shared-workspace threat model is the multi-MCP reality, and the core rule — *task success and safety are separate measurements* — is the same conclusion as K441 (score conformance, not just absence of failure) and K442 (accuracy ≠ humility). Pairs `agent-approval-laundering-transitive-effects` / `agent-data-injection-attacks`. **Code released** (Apex-Agents harness); no install this wave. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "See source page for arXiv 2610.13623 locators." [Source: CCC K445 synthesis]
