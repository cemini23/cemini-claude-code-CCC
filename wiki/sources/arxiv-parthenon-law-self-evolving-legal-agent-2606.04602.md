---
title: Parthenon Law — self-evolving legal-agent framework (arXiv 2606.04602)
type: source
tags: [source, arxiv, parthenon, legal-agent, harness, self-evolving, k114]
keywords: [2606.04602, parthenon, harvey-lab, solver-evaluator-learner, six-layer-harness]
related:
  - concepts/continual-harness-online-self-improvement.md
  - concepts/subagent-orchestration.md
  - concepts/agent-harness-operational-definition.md
  - concepts/ship-subagent-writer-reviewer-tester.md
  - entities/tools/claude-code.md
  - entities/tools/claude-for-legal.md
  - concepts/skillhone-continual-skill-decision-history.md
maturity: draft
read_status: read
created: 2026-06-13
updated: 2026-06-13
---

## Relations

- `@concepts/continual-harness-online-self-improvement.md` — non-parametric harness learning loop peer
- `@concepts/subagent-orchestration.md` — solver–evaluator–learner role split
- `@concepts/agent-harness-operational-definition.md` — harness-as-unit-of-evaluation framing
- `@concepts/ship-subagent-writer-reviewer-tester.md` — parallel writer/reviewer separation pattern
- `@entities/tools/claude-code.md` — Claude Code evaluated as baseline harness on Harvey LAB
- `@entities/tools/claude-for-legal.md` — vertical legal plugin patterns; Parthenon is academic vertical harness
- `@concepts/skillhone-continual-skill-decision-history.md` — redacted evaluator→learner boundary parallel

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Parthenon Law: A Self-Evolving Legal-Agent Framework |
| **Authors** | Hejia Geng, Leo Liu (TapNTell) |
| **arXiv** | 2606.04602v2 [cs.AI] |
| **Code** | github.com/HHHHHejia/parthenon-skills |
| **Location** | `raw-sources/arxiv-2606.04602-parthenon-law-a-self-evolving-legal-agent-framew.pdf` |
| **Retrieved** | 2026-06-13 |
| **Read status** | read — six-layer architecture, LAB empirical study, anti-leakage learning loop |

## Narrative

Large-scale empirical study on **Harvey Legal Agent Benchmark (LAB)**: **12,510** trajectories across Codex, Claude Code, and legal-native harnesses. Per-criterion accuracy rises with stronger models; **strict all-criteria matter completion** stays low (~1/8 matters for strongest baseline).

**Parthenon** — six auditable layers wrapping (not replacing) workspace harnesses:

| Layer | Role |
|-------|------|
| Model | Pluggable LLM capability |
| Harness | Codex / Claude Code / OpenCode / OpenHands runtime |
| Agent | Solver · evaluator · learner (information-isolated) |
| Knowledge | Statutes, windows, deliverable schemas, calendars, synonyms, dispatch rules (~2,300 entries) |
| Tools | 14 deterministic audit/release-gate capabilities |
| Skills | 1,251 task-routed procedural playbooks (rubric-blind) |

**Self-evolving loop:** solver drafts → rubric-isolated evaluator scores → learner proposes task-agnostic edits to Skills/Tools/Knowledge with **anti-leakage** (no rubric text, task ids, or answer keys to learner). With model+harness fixed, Parthenon adds **+13.8/+10.2/+7.4** pp pooled accuracy and roughly **triples** strict completion on weaker solvers.

Five recurring failure classes (~2/3 of errors): missing facts, numbers/dates, legal-rule use, deliverable form, coverage — stable across 24 practice areas.

**CCC verdict:** **REFERENCE** — steal six-layer separation, release gates, solver–evaluator–learner redaction, harness-only learning without weight updates. Legal Knowledge/Tools content is vertical-specific; federation wikis map Skills→`SKILL.md`, Tools→MCP/scripts, Knowledge→`wiki/`. `parthenon-skills` repo exists for Phase-0 if legal vertical expands.

## Snippets

> "Reliability comes from separating three functions that must not share information — drafting the work product, evaluating it, and proposing harness edits — not from adding agents to drafting."

> "Parthenon does not change the model; it changes the harness that each subsequent model call inhabits."

> — [Source: arxiv-2606.04602-parthenon-law-a-self-evolving-legal-agent-framew.pdf §3.1–3.2, retrieved 2026-06-13]
