---
title: K260 CCC — ResidencyRL adversarial curriculum + doc fidelity
type: brief
tags: [brief, ccc, k260]
created: 2026-08-10
---

## Target

CCC — Cursor / Claude Code harness wiki

## Summary

Steal multi-turn adversarial curriculum, hierarchical rubrics + safety penalties, premature-closure resistance, and documentation anti-hallucination from Google ResidencyRL. No code clone.

## Body

1. **Curriculum packs** — routine / intake-asymmetric / adversarial mix for agent evals and red-team packs.
2. **Structured reward** — rubrics + hard fidelity/safety penalties; prefer execution verify over autorater-only (K162).
3. **Premature closure** — gate terminate on required-check coverage.
4. **Doc fidelity** — durable artifacts must not fabricate unelicited facts.
5. **NO-GO** ResidencyRL codebase (Google closed + medical-safety rationale).

## Sources

- `@ccc-wiki/concepts/adversarial-curriculum-structured-reward-doc-fidelity.md`
- arXiv 2608.07418
