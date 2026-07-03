---
title: Cognitive heuristics in LLM vulnerability detection (cross-wiki stub)
type: concept
tags: [concept, llm-security, code-review, cross-wiki-stub, k137-handoff]
keywords: [2606.30587, halo-effect, framing, anchoring, code-review]
related:
  - "@cybersecurity-wiki/concepts/cognitive-heuristics-llm-vuln-detection.md"
  - "@cybersecurity-wiki/sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md"
  - concepts/agent-completion-verification-gates.md
  - concepts/skill-vetting.md
  - briefs/2026-07-03_ccc-handoff-cognitive-heuristics-vuln-detection-ingest.md
  - meta/ccc-cross-wiki-handoff-briefs.md
maturity: draft
created: 2026-07-03
updated: 2026-07-03
cross-wiki-primary: "@cybersecurity-wiki/concepts/cognitive-heuristics-llm-vuln-detection.md"
---

## Relations

- `@cybersecurity-wiki/concepts/cognitive-heuristics-llm-vuln-detection.md` — primary synthesis (2606.30587)
- `@briefs/2026-07-03_ccc-handoff-cognitive-heuristics-vuln-detection-ingest.md` — CCC harness handoff

## Raw Concept

CCC routing stub for cybersec-wiki ingest 2026-07-03 — non-code context (author, framing, prior comments) biases LLM vulnerability scanners on identical code.

## Narrative

**CCC steal:** strip reputation/anchoring from agent PR-review prompts; fixed security system instruction; never auto-approve merge MCP without human gate. Complements SEVRA adversarial-diff attacks.

**Verdict:** **REFERENCE** — security eval lane on cybersec-wiki; apply hardening to Cursor `to-issues` / super-audit review flows.

## Snippets

> "Identical vulnerable code receives different verdicts when non-code context changes."
> — [Source: @cybersecurity-wiki/sources/arxiv-2606-30587-cognitive-heuristics-llm-vuln-detection.md, retrieved 2026-07-03]
