---
title: Handoff validity — contracts for agent harness transfers
type: concept
tags: [concept, handoff, provenance, harness, k119]
keywords: [2606.19795, handoff-contract, handoff-object, eacp]
related:
  - sources/arxiv-agentic-eda-handoff-2606.19795.md
  - concepts/channel-fracture-cross-agent-memory-delivery.md
  - concepts/agent-completion-verification-gates.md
  - concepts/agentic-pm-review-artifacts.md
  - concepts/specification-driven-scientific-workflow-management.md
  - concepts/code-as-agent-harness.md
  - concepts/subagent-orchestration.md
  - concepts/etclovg-harness-layers.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/plan-then-execute-topological-orchestration.md
  - sources/arxiv-dynamo-topological-orchestration-2606.19382.md
  - concepts/claim-drift-automated-research.md
  - sources/arxiv-xcientist-research-harness-claim-drift-2606.18874.md
  - concepts/externalized-research-synthesis-validation.md
  - concepts/cross-model-verified-agent-translation.md
  - sources/arxiv-dual-agent-cross-model-protocol-translation-2606.20120.md
  - concepts/autonomous-coding-agents-enterprise-data.md
  - concepts/os-level-agent-harness-android.md
  - entities/tools/paperclaw.md
  - sources/arxiv-paperclaw-autonomous-research-2606.22610.md
  - concepts/event-sourced-poly-agent-handoff.md
  - sources/arxiv-esaa-conversational-event-sourced-2606.23752.md
  - entities/tools/esaa-conversational.md
  - concepts/hidden-user-state-recovery-audit.md
  - concepts/web-scale-scientific-collaboration-infrastructure.md
  - sources/arxiv-clarus-scientific-collaboration-infrastructure-2606.30246.md
maturity: draft
created: 2026-06-19
updated: 2026-06-30
---

## Relations

- `@sources/arxiv-agentic-eda-handoff-2606.19795.md` — EDA survey provenance (2606.19795)
- `@concepts/channel-fracture-cross-agent-memory-delivery.md` — handoff without validity proof
- `@concepts/agent-completion-verification-gates.md` — acceptance at receiver
- `@concepts/agentic-pm-review-artifacts.md` — review artifacts as handoff objects
- `@concepts/specification-driven-scientific-workflow-management.md` — spec as handoff contract
- `@concepts/code-as-agent-harness.md` — harness interface layer
- `@concepts/subagent-orchestration.md` — Task tool handoffs
- `@concepts/etclovg-harness-layers.md` — layer tagging on handoff failures
- `@concepts/failed-trajectory-harness-repair.md` — cross-session repair when contracts break

## Raw Concept

When an agent passes work to another agent, tool, or session — what makes the transfer **valid** for downstream use?

## Narrative

**Handoff validity** [TENTATIVE — EDA survey framing, 2606.19795]: artifact/state/knowledge satisfies **recipient acceptance conditions** and carries enough **context, evidence, provenance** that the consumer need not reconstruct hidden upstream assumptions.

### Core vocabulary (steal-for CCC)

| Term | Harness analogue |
|------|------------------|
| Handoff object | Subagent summary, ingest source page, OpenSpec spec, `briefs/` deliverable |
| Handoff contract | Acceptance criteria in `/goal`, OpenSpec AC, ingest "touch 3–15 pages" |
| Evidence | Test output, `wiki_lint.py` pass, Phase-0 script verdict |
| Coordination mechanism | Generate–repair (lint loop); recover–resume (`hot.md` + git); retrieve–answer (conductor) |

### Three validity scopes → Cemini mapping

| EDA class | CCC example |
|-----------|-------------|
| Stage-Bound | Single subagent task passes local check but breaks parent integration |
| Flow-Bound | Multi-step ingest: source → concepts → index → lint → commit |
| Organization-Bound | Cross-wiki stub with provenance; osint vs CCC routing admissibility |

**EACP five layers** — research agenda for EDA; CCC steals **discovery → message → tool → workflow → security** layering when designing conductor/MCP handoffs. No EACP prod install.

### Harness rules

1. Subagent prompts must state **consumer acceptance conditions** explicitly.
2. Prove handoff at **receiver** (inverse verification) — see channel fracture.
3. Repeat failures → `@concepts/failed-trajectory-harness-repair.md`, not more silent retries.
4. **Claim drift** (K122) — handoff summary must preserve mechanism structure, not just status "done"; see `@concepts/claim-drift-automated-research.md`.

## Snippets

> "Handoff validity extends beyond local correctness."

> — [Source: arxiv-2606.19795-agentic-electronic-design-automation-a-handoff-p.pdf]
