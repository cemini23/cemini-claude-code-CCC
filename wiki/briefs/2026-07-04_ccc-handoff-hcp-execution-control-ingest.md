---
title: CCC handoff — HCP MCP execution-control ingest
type: brief
tags: [brief, ccc-handoff, mcp, execution-control]
created: 2026-07-04
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/mcp-execution-control-invariants.md
updated: 2026-07-04
---

## Target

Claude Desktop / lazy-tool | prod-mcp dispatch + MCP skill design

## Summary

Cybersec-wiki ingest 2026-07-04: arXiv **2606.29073** — HCP eight execution-control invariants for MCP-style agents; B1 connection mitigations permit **6/10** attacks; HCP blocks **10/10** with audit. Phase-0 **CONDITIONAL-GO** (`SymbolicLight-AGI/handle-capability-protocol`, MIT, 0★).

## Body

### Why CCC cares

Cursor/Claude Desktop MCP stacks already implement **connection** (OAuth, transport, tool registry). This paper formalizes the missing **execution-control** layer: grants, principals, data-pipe auth, deny-path audit. Directly relevant to lazy-tool dispatch and prod-mcp Tier-2 promotion gates.

### Hardening for agent MCP flows

- Never treat tool `description` / `inputSchema` as authorization (I1)
- Bind user approvals to scoped grants, not session-wide blanket (I2)
- Log deny events with principal + capability + reason (I7)
- Run HCP 10-case regression when changing dispatch policy

Wiki: `@cybersecurity-wiki/concepts/mcp-execution-control-invariants.md`

### Eval stack

| Lane | Wiki |
|------|------|
| Admission / DCI / SPI | `@cybersecurity-wiki/concepts/mcp-security-posture.md` |
| Execution invariants | **NEW** `@cybersecurity-wiki/concepts/mcp-execution-control-invariants.md` |
| Intent narrowing | `@cybersecurity-wiki/concepts/intent-governed-tool-authorization.md` |
| Trajectory security | `@cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md` |

### Staged briefs

- `2026-07-04_hcp-mcp-execution-control-handoff.md`
- `2026-07-04_prod-mcp-eight-invariants-checklist.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2606-29073-hcp-mcp-execution-control-invariants.md
- @cybersecurity-wiki/concepts/mcp-execution-control-invariants.md
- @cybersecurity-wiki/entities/tools/handle-capability-protocol.md
