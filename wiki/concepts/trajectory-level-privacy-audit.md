---
title: "AgentPrivArena: Evaluating and Auditing Real-world AI Agent Privacy (CCC K427)"
type: concept
tags: [concept, k427]
keywords: [2610.06454, k427]
related:
  - sources/arxiv-agentprivarena-trajectory-privacy-audit-2610.06454.md
  - concepts/phase1-adopt-wire.md
  - briefs/2026-10-06_ccc-k426-k430-sip-ready.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-10-06
updated: 2026-10-06
---

## Relations

- `@sources/arxiv-agentprivarena-trajectory-privacy-audit-2610.06454.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/2026-10-06_ccc-k426-k430-sip-ready.md`

## Raw Concept

K427: ADOPT pattern (repo is website only) — arXiv 2610.06454.

## Narrative

**AgentPrivArena — judge the trajectory, not the last message.** Privacy benchmarks score an agent's **final response**; this one argues that misses where violations *originate*. An agent can **read a sensitive file it never needed and never mention it** — outcome-level scoring sees nothing, while the record sits in context for the rest of the run. The framework runs agents against **six real self-hosted services** (BookStack, Mattermost, Rocket.Chat, Mailpit, GoToSocial, Radicale) exposed through **authentic MCP servers in a Docker sandbox**, so records exist as *service state* rather than as text in a prompt — the agent has to **find** them. Two contributions: **trajectory-level privacy metrics** (unnecessary access, not just leakage) and **AgentPrivAudit**, a runtime in-loop auditor with a **read boundary and a write boundary**. The design insight is that the two boundaries can legitimately disagree: in one worked case the read boundary cleared an appointment time for a *colleague*, and the write boundary removed it because the reply was going to a *public channel* — **the same fact, different audience, different verdict**. And the authors report their own failure mode honestly: repeated abstraction ratchets until a correct-by-safety reply scores **0 for helpfulness**, and **nothing in the loop distinguishes "withheld a sensitive detail" from "withheld the answer."** Static-vs-live is the other measured result: pre-authored traces average **1.9 read steps / 0.2% deep**, live execution **5.1 / 14.3%**, because real runs must *locate* records and recover from stale identifiers. Pairs K395 approval laundering / `@concepts/tool-argument-privacy-minimization.md` / K421 (untrusted input + sensitive access + egress) / `@concepts/measurement-integrity-mcp-security-eval.md`. **Phase-0: `voidreaming/agentprivarena` MIT, 3.8 MB — but it is the project *website*, not the framework** → **no clone**. Runtime **`wont_wire`**; concept **`policy_wired`**.

## Snippets

> "See source page for arXiv 2610.06454 locators." [Source: CCC K427 synthesis]
