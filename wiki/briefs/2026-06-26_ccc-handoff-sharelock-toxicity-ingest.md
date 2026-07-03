---
title: CCC handoff — ShareLock MCP + ToxSearch-S ingest
type: brief
tags: [brief, ccc-handoff, mcp, llm-red-team]
created: 2026-06-26
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
updated: 2026-06-29
---

## Target

Claude Desktop / lazy-tool MCP posture | authorized LLM eval pipelines

## Summary

Cybersec-wiki ingest 2026-06-26: two arXiv papers — **ShareLock** (multi-tool Shamir MCP poisoning, 2606.27027) and **ToxSearch-S** (parallel QD toxicity search, 2606.24166). Both Phase-0 **Reference** (no public artifacts).

## Body

### MCP / skill vetting (`@ccc-wiki/concepts/skill-vetting.md`)

- Extend catalog review beyond per-tool scans: correlate metadata patterns across tools from same publisher (ShareLock share set).
- Pair SkillSpector/DefenseClaw with **multi-tool orchestration red-team** — side effects on filesystem paths, not chat refusal alone.
- Wiki: `@cybersecurity-wiki/concepts/multi-tool-threshold-mcp-poisoning.md`

### LLM robustness eval

- ToxSearch-S speciation pattern for breadth-first jailbreak discovery under wall-clock pressure.
- Wiki: `@cybersecurity-wiki/concepts/llm-adversarial-fuzzing.md`

### Staged briefs (cybersec-wiki)

- `2026-06-26_sharelock-multi-tool-threshold-mcp-redteam-checklist.md`
- `2026-06-26_toxsearch-s-adversarial-fuzzing-handoff.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2606-27027-sharelock-multi-tool-threshold-mcp-poisoning.md
- @cybersecurity-wiki/sources/arxiv-2606-24166-toxsearch-s-distributed-toxicity-search.md
