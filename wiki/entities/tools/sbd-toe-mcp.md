---
title: "sbd-toe-mcp — governed security-by-design requirements over MCP (PoC, no install)"
type: entity
tags: [entity, tool, mcp, security, codegen, k441]
keywords: [2610.10659, SbD-ToE, sbd-toe-mcp, security-by-design, requirements, Apache-2.0]
related:
  - sources/arxiv-security-by-design-point-of-execution-2610.10659.md
  - concepts/specification-versus-capability-failure-attribution.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - briefs/2026-10-09_ccc-k441-k444-sip-ready.md
maturity: draft
wire_status: wont_wire
wire_target: "PoC MCP server (0★) — REFERENCE only; no CCC security-by-design workstream"
created: 2026-10-09
updated: 2026-10-09
---

## Relations

- `@sources/arxiv-security-by-design-point-of-execution-2610.10659.md`
- `@concepts/specification-versus-capability-failure-attribution.md`
- `@concepts/mcp-context-optimization.md`

## Raw Concept

Phase-0 entity for K441 — `@shiftleftpt/sbd-toe-mcp`, an MCP server that serves governed
security-by-design requirements (SbD-ToE) to a coding agent at the point of execution.

## Narrative

| Artifact | Availability | Verdict |
|----------|--------------|---------|
| `SbD-ToE/sbd-toe-mcp` | **Apache-2.0**, 0★, pushed 2026-09-28 | **REFERENCE** (PoC) |
| `SbD-ToE/sbd-toe-manual` | **CC-BY-SA-4.0**, 0★, pushed 2026-09-30 | Doc source |
| npm `@shiftleftpt/sbd-toe-mcp` 0.10.1 | Published 2026-06-25 | Pinned release |

**What it is:** the selector tool `prepare_sbd_toe_codegen_context(task, mode, risk_level)` returns
the activated security requirements (control objectives, base requirements, controls, evidence
expectations) for a task. The paper's own runs used `claude -p --permission-mode bypassPermissions
--strict-mcp-config --setting-sources project`.

**Why `wont_wire`:** it is a single-author PoC with 0★. CCC has no security-by-design workstream, and
the transferable content is the *pattern* (deliver governed requirements at the point of execution so
failures become attributable), captured in the K441 concept. The one runtime datapoint CCC cares
about is the payload size: the tool returns **45,000–76,000 characters**, which Claude Code saved to
a file in 41 of 59 sessions.

## Snippets

> "Given a task, a mode and a risk level, it returns the requirements that it activates for that task."
> [Source: arXiv 2610.10659 (retrieved 2026-10-09)]

## Phase-1

Runtime `wont_wire`. Concept `policy_wired` (see `concepts/specification-versus-capability-failure-attribution.md`).
