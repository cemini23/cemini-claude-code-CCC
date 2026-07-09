---
title: CCC handoff — ADI + SpellSmith MCP ingest
type: brief
tags: [brief, ccc-handoff, mcp, adi, spellsmith]
created: 2026-07-09
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/agent-data-injection-attacks.md
updated: 2026-07-09
---

## Target

Claude Desktop / lazy-tool | prod-mcp dispatch + coding-agent harness

## Summary

Cybersec-wiki ingest 2026-07-09: **2607.05120** ADI (trusted/untrusted data isolation) + **2607.07461** SpellSmith (MCP taint via security-aware descriptions). David K139 → tipdrop-workspace-kit.

## Body

### Why CCC cares

- **ADI** — Claude Code / lazy-tool tool-response parsing must not treat forged metadata as trusted
- **SpellSmith** — augment allowlisted MCP `description` + pre-invoke reflection before shell/network tools

Wiki: `@cybersecurity-wiki/concepts/agent-data-injection-attacks.md`, `@cybersecurity-wiki/concepts/mcp-taint-style-vulnerabilities.md`

### Staged briefs

- `2026-07-09_adi-trusted-untrusted-data-handoff.md`
- `2026-07-09_prod-mcp-trusted-untrusted-data-isolation-checklist.md`
- `2026-07-09_spellsmith-mcp-taint-mitigation-handoff.md`
- TipDrop: `2026-07-09_k139-agent-data-injection-harness-adopt.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2607-05120-agent-data-injection-attacks.md
- @cybersecurity-wiki/sources/arxiv-2607-07461-spellsmith-mcp-taint-style-vulnerabilities.md
