---
title: K253 CCC — S3Gym, Aspire, AutoSciRub, Addy skill decay
type: brief
tags: [brief, ccc, k253, harness]
target: claude.ai
created: 2026-09-01
updated: 2026-09-01
---

## Target

CCC meta-wiki harness policy. **No runtime install except AutoSciRub REFERENCE shelf.**

## Summary

Verdict: **policy + one REFERENCE clone.** K253 adds self-test/judge/improve (S3Gym), vague-goal self-evolution (Aspire — no repo), rubric-induction-before-improve (AutoSciRub MIT), and Addy **agentic skill decay** (verification floor, deliberate reps). Pairs K162 external eval, K237 misevolution, K324 validation ratchet. **HITL** before skill/harness mutation.

## Body

1. **Evaluate before improve** — AutoSciRub pattern: induce rubrics before self-improvement loops; do not rewrite pass criteria in-loop.
2. **S3Gym / Aspire** — document as WATCH; no SPDX clones; no unattended self-evolve of `.cursor/skills`.
3. **Skill decay** — agent throughput scales faster than attention; completed task ≠ rep; ask for explanations when learning.
4. Phase-0 clone: `.local/adopts/AutoSciRub` MIT only.

## Sources

- @concepts/k253-harness-self-improvement-wave.md
- @sources/arxiv-2608.31076-autoscirub-rubric-induction-2026-09-01.md
- @sources/substack-rss-addy-osmani-2026-08-31-agentic-skill-decay.md
