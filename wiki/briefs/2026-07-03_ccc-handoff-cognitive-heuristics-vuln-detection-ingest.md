---
title: CCC handoff — cognitive heuristics vuln detection ingest
type: brief
tags: [brief, ccc-handoff, llm-security, code-review]
created: 2026-07-03
related:
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/cognitive-heuristics-llm-vuln-detection.md
updated: 2026-07-03
---

## Target

Claude Desktop / lazy-tool | agent code-review + MCP merge tools

## Summary

Cybersec-wiki ingest 2026-07-03: arXiv **2606.30587** — cognitive heuristics (halo/framing/anchoring) bias LLM vulnerability scanners; 97% suppression PoC. Phase-0 **Reference**.

## Body

### Why CCC cares

Claude Code / Desktop agents used for PR review ingest **non-code context** (author, task framing, prior comments). Paper shows identical vulnerable code gets different verdicts — complements SEVRA's adversarial-diff attacks.

### Hardening for agent review flows

- Strip reputation/anchoring from review prompts
- Fixed security system instruction — never "routine-only"
- Pair with SEVRA + heuristic perturbation regression
- **Never** auto-approve merge MCP without human gate

Wiki: `@cybersecurity-wiki/concepts/cognitive-heuristics-llm-vuln-detection.md`

### Eval stack

| Lane | Wiki |
|------|------|
| PR narrative attacks | `@cybersecurity-wiki/concepts/llm-code-review-agent-security.md` (SEVRA) |
| Context-only heuristics | **NEW** `@cybersecurity-wiki/concepts/cognitive-heuristics-llm-vuln-detection.md` |
| Trajectory security | `@cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md` |

### Staged briefs

- `2026-07-03_cognitive-heuristics-llm-scanner-redteam-checklist.md`
- `2026-07-03_ci-merge-gate-cognitive-context-hardening-handoff.md`

## Sources

- @cybersecurity-wiki/sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md
- @cybersecurity-wiki/concepts/cognitive-heuristics-llm-vuln-detection.md
