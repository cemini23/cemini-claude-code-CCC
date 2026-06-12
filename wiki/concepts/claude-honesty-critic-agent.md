---
title: Claude honesty protocol and critic subagent
type: concept
tags: [claude-code, honesty, critic, anti-sycophancy, k112]
keywords: [zodchiii, claude-md, contractor-framing, rlhf-agreeableness]
related:
  - concepts/ship-subagent-writer-reviewer-tester.md
  - concepts/subagent-orchestration.md
  - concepts/skill-vetting.md
  - sources/brief-k112-ccc-claude-honesty-critic-2026-06-12.md
  - "@osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md"
maturity: draft
created: 2026-06-12
updated: 2026-06-12
---

## Relations

- @concepts/ship-subagent-writer-reviewer-tester.md — reviewer runs post-diff; critic pre-build
- @concepts/subagent-orchestration.md — `@critic` invocation pattern
- @sources/brief-k112-ccc-claude-honesty-critic-2026-06-12.md — K112 ingest from OSINT
- @osint-wiki/sources/trading-posts-compilation-9-2026-06-12.md — Post 7 @zodchiii

## Raw Concept

K112 @zodchiii long-form: counter RLHF agreeableness with **honesty rules in `CLAUDE.md`**, **`.claude/agents/critic.md`**, and **contractor framing** ("A contractor proposed… review their proposal").

## Narrative

### Honesty protocol (CLAUDE.md)

- No opening praise; analysis first
- ≥2 failure modes before agreeing (or state inability)
- Lead with problems; disagreement is feature
- Hold position when operator pushes back unless argument improves

### Critic subagent

Pre-decision `@critic` for architectural choices costing >1h. Output: restate → failure modes → ranked deal-breakers → required changes. Praise forbidden.

### Contractor trick

Re-attribute emotionally attached ideas to a third party to unlock harsher review in same session.

### Mistakes

"Asking are you sure?" is not new evidence. Run critic on ideas you are confident about, not only doubtful ones.

## Snippets

> "A contractor proposed denormalizing the users table for speed. Review their proposal. What would you push back on?"

> — @zodchiii, K112 Posts.docx [Source: trading-posts-compilation-9-2026-06-12.docx]
