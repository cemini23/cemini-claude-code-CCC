---
title: CCC handoff — steerability substrate coding-agent ingest
type: brief
tags: [brief, ccc-handoff, harness, coding-agents, verification]
created: 2026-07-07
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md
  - sources/brief-k138-substrate-constraints-agent-oversight-2026-07-07.md
updated: 2026-07-07
---

## Target

Claude Desktop / Claude Code | harness repos + merge verification gates

## Summary

Cybersec-wiki ingest 2026-07-07: arXiv **2607.02389** — substrate constraints + docs CLI lift small-reviewer backdoor recall **54.5% → 90.9%**; argues against MCP context saturation for local code review. Phase-0 **Reference**.

## Body

### Why CCC cares

David's harness stack already uses objective completion gates (`agent-completion-verification-gates`). This paper adds **code-shape constraints** so those gates and small reviewer subagents can audit agent output without full-repo context.

### Hardening for Claude Code flows

- Enforce linter/type/contract stack on agent-edited paths before `/goal` claims done
- Put invariants in **module docstrings** next to violating code
- Add lightweight `docs symbol` projection for review subagents
- Multi-pass per-function review — single-pass fails on 8B-class models
- Prefer small CLI projection over dumping MCP payloads into review context

Wiki: `@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md`

### Eval stack

| Lane | Wiki |
|------|------|
| Completion proof | `@ccc-wiki/concepts/agent-completion-verification-gates.md` |
| Substrate oversight | **NEW** `@cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md` |
| PR framing attacks | `@cybersecurity-wiki/concepts/llm-code-review-agent-security.md` |
| VM isolation | `@cybersecurity-wiki/concepts/agent-vm-sandboxing.md` |

### Staged briefs

- `2026-07-07_steerability-substrate-coding-agent-oversight-handoff.md`
- `2026-07-07_harness-substrate-constraints-checklist.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2607-02389-steerability-constraints-coding-agent-oversight.md
- @cybersecurity-wiki/concepts/substrate-constraints-coding-agent-oversight.md
