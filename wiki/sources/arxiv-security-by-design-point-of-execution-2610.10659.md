---
title: "Applying Security by Design at the Point of Execution: How Governed Se (CCC K441)"
type: source
tags: [source, arxiv, k441]
keywords: [2610.10659, k441]
related:
  - concepts/specification-versus-capability-failure-attribution.md
  - entities/tools/sbd-toe-mcp.md
  - concepts/mcp-context-optimization.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - briefs/2026-10-09_ccc-k441-k444-sip-ready.md
maturity: draft
read_status: deep-read
created: 2026-10-09
updated: 2026-10-09
---

## Relations

- `@concepts/specification-versus-capability-failure-attribution.md`
- `@entities/tools/sbd-toe-mcp.md`
- `@concepts/mcp-context-optimization.md`
- `@concepts/mcp-contract-grounded-synthesis-and-validation-gate.md`
- `@briefs/2026-10-09_ccc-k441-k444-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Applying Security by Design at the Point of Execution: How Governed Security Requirements Affect the Security of AI-Generated Code |
| **arXiv** | 2610.10659 (2026-10) |
| **Repo** | `SbD-ToE/sbd-toe-mcp` |
| **Retrieved** | 2026-10-09 |

## Narrative

**Verdict: ADOPT pattern (MCP-delivered governed requirements).**

**The gap is often specification, not capability — deliver the requirements at the point of execution.** A coding agent is given a governed, versioned security-by-design knowledge base (SbD-ToE) through an **MCP server** whose selector returns the requirements that apply to a task; the agent calls it at the moment it writes code. Two benchmarks, two evaluators (a GPT-4o judge and executed exploits in containers). **DualGauge (59 Python tasks):** tasks passing all security tests **44.1% → 78.0%**; security tests passed **77.4% → 93.0%** (both p<0.001). **BaxBench (28 backend scenarios):** among functionally correct solutions the share with **no successful exploit rose 65% → 86%** — comparable to the authors' own **Oracle Security Reminder (85%)**, which they call an *unrealistic upper bound* because it names the weaknesses the tests check. The delivery reached that level **without knowing the tests**. **The cost:** the stricter code failed functional tests that assume values the task never states (short passwords, non-Luhn card numbers, undeclared fields), so the *joint* secure-and-functional metric did **not** improve significantly. **CCC reading:** a clean statement of a pattern CCC keeps meeting — *a benchmark score conflates three failure causes*: the model could not implement a property (**capability**), the knowledge base had no requirement for the weakness (**coverage**), or the test rejects a conforming implementation (**oracle**). Delivering the requirements makes the causes separable, the same move as K437's score-formulation-separately and K436's read/write split. Two harness observations to keep: (1) the MCP tool returned **45,000–76,000 characters** and Claude Code **saved it to a file in 41 of 59 sessions**, the agent reading part of it — a concrete tool-output-too-large datapoint (pairs `mcp-context-optimization`); (2) the runs are a **headless Claude Code lane** (`claude -p --permission-mode bypassPermissions --strict-mcp-config --setting-sources project`). **Phase-0: `SbD-ToE/sbd-toe-mcp` Apache-2.0** (0★, 2026-09-28); manual `SbD-ToE/sbd-toe-manual` **CC-BY-SA-4.0**. A PoC MCP server; no CCC workstream needs it → no clone. Runtime `wont_wire`; concept `policy_wired`.

## Snippets

> "the share of tasks passing all security tests rose from 44.1% to 78.0% and the share of security tests passed from 77.4% to 93.0%" [Source: arXiv 2610.10659 (retrieved 2026-10-09)]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2610.10659-applying-security-by-design-at-the-point-of-exec.pdf` |
