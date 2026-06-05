---
title: "Glasswing pattern — deliberate disagreement adversarial verification (evilsocket/audit)"
type: entity
tags: [pattern, agent-orchestration, adversarial-verification, glasswing, evilsocket, subagent, cross-wiki-route]
keywords: [glasswing, deliberate-disagreement, evilsocket-audit, adversarial-verification, reachability-gating, feedback-loops, narrow-agents, agent-sdk]
related:
  - concepts/subagent-orchestration.md
  - entities/patterns/scatter-gather.md
  - entities/patterns/tier1-tier2-agent-model.md
  - entities/patterns/citadel-agent-orchestration.md
  - concepts/code-as-agent-harness.md
  - concepts/self-healing-agent-sessions.md
  - concepts/graphflow-verifiable-agent-workflows.md
  - entities/tools/council-of-high-intelligence.md
  - entities/skills/cursor-audit.md
maturity: draft
created: 2026-05-21
updated: 2026-06-05
cross-wiki-source: "@osint-wiki/sources/analyzing-github-projects-agentic-infra-2026-05-21.md"
---

## Relations

- @concepts/subagent-orchestration.md — the subagent dispatch model this pattern builds on
- @entities/patterns/scatter-gather.md — Glasswing's multi-agent fan-out is scatter-gather with adversarial gating
- @entities/patterns/tier1-tier2-agent-model.md — each narrow Glasswing agent is Tier 1 (advisory); the gating logic is Tier 2 (execution)
- @entities/patterns/citadel-agent-orchestration.md — Citadel's circuit breaker + Glasswing's disagreement gating are complementary safety primitives
- @concepts/code-as-agent-harness.md — adversarial verification lens paired with 2605.18747 taxonomy
- @concepts/self-healing-agent-sessions.md — preferred recovery path vs blind corrective re-prompt
- @entities/skills/cursor-audit.md — operational Glasswing #2 via three-model conflict table
- @osint-wiki/sources/analyzing-github-projects-agentic-infra-2026-05-21.md (cross-wiki source)

## Raw Concept

Cross-wiki brief routed from the OSINT K56 agentic-infrastructure ingest (May 2026). `evilsocket/audit` (MIT, 388★) implements an 8-stage vulnerability-discovery agent using Claude Code Agent SDK with a novel "deliberate disagreement" pattern — multiple narrow agents independently verify each other's findings, and disagreement gates progress. This pattern is directly applicable to Cemini's conductor / multi-agent reasoning architecture.

## Narrative

### What evilsocket/audit does

An 8-stage vulnerability-discovery agent driven entirely by Claude Code Agent SDK (Pro/Max subscription, no API key needed). Each stage is a narrow agent with a specific remit; stages are gated by explicit reachability checks and adversarial verification.

### The Glasswing pattern (4 primitives)

The "deliberate disagreement" architecture has four extractable primitives:

1. **Many narrow agents** — each agent has a single, well-defined task (not a generalist trying to do everything)
2. **Deliberate disagreement** — two agents independently assess the same surface; if their findings conflict, the disagreement gates forward progress until resolved. This is adversarial verification as infrastructure, not ad-hoc skepticism.
3. **Explicit reachability gating** — an agent cannot proceed to stage N+1 unless stage N's output satisfies explicit reachability criteria. No implicit handoffs.
4. **Feedback loops** — findings from later stages feed back as inputs to earlier stages on re-run. The pipeline learns.

### Why CCC cares

The "deliberate disagreement" primitive is the highest-value extractable pattern from the K56 batch:

- **Conductor multi-agent reasoning**: Cemini's conductor currently fans out and merges, but doesn't gate on disagreement. Two subagents giving conflicting answers to the same query should trigger a resolution step, not a silent merge.
- **Phase-0 skill audits**: two independent audit subagents running the same checklist against the same skill → disagreement gates the GO/NO-GO decision. This makes the skill-vetting pipeline self-verifying.
- **Scatter-gather upgrade path**: Glasswing is scatter-gather with adversarial gating and feedback loops — a natural evolution target for Cemini's current flat scatter-gather pattern.
- **cursor-audit skill** (`@entities/skills/cursor-audit.md`): ships Glasswing primitive #2 today — three readonly Task auditors, synthesis **Conflicts** table gates SHIP. Lighter than evilsocket/audit's 8-stage pipeline; Cursor-native.

### Constraint

MIT license (verified). Clean for pattern extraction. The repo is a Claude Code Agent SDK reference implementation — code is studyable directly.

[CONFIRMED] — MIT license verified via cross-wiki source.
