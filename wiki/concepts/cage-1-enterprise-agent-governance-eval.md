---
title: CAGE-1 — enterprise agent governance evaluation (Prebind Assurance)
type: concept
tags: [concept, enterprise, governance, evaluation, prebind, harness, k151]
keywords: [cage-1, prebind assurance, standing, twelve dimensions, 2607.03510, enterprise agent, fail closed]
related:
  - sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md
  - concepts/agent-completion-verification-gates.md
  - concepts/gatekeeper-layered-agent-evaluation.md
  - concepts/agent-five-gate-org-chart.md
  - entities/patterns/tier1-tier2-agent-model.md
  - concepts/safeclawbench-staged-security-endpoints.md
  - concepts/seclaw-agent-security-evaluation.md
  - concepts/etclovg-harness-layers.md
  - concepts/skill-vetting.md
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - sources/brief-k151-cage-1-enterprise-agent-governance-2026-07-10.md
  - briefs/2026-07-10_ccc-handoff-cage-polyworkbench-ingest.md
  - concepts/multilingual-long-horizon-agent-eval.md
  - "@cybersecurity-wiki/concepts/cage-1-enterprise-agent-governance-eval.md"
  - "@cybersecurity-wiki/sources/arxiv-2607-03510-cage-1-enterprise-agent-governance.md"
  - concepts/trustx-agent-risk-classification.md
  - sources/arxiv-trustx-agent-risk-classification-2607.09586.md
  - concepts/hierarchical-skill-stack-lazy-orchestration.md
  - concepts/mcp-contract-grounded-synthesis-and-validation-gate.md
  - sources/arxiv-contract-grounded-bt-coding-agent-mcp-2607.12220.md
maturity: draft
created: 2026-07-10
updated: 2026-07-16
---

## Relations

- `@sources/arxiv-cage-1-enterprise-agentic-governance-2607.03510.md` — K151 provenance (Roopam W. Sure)
- `@concepts/agent-completion-verification-gates.md` — completion proof at session end; Prebind at **action bind** time
- `@concepts/gatekeeper-layered-agent-evaluation.md` — layered rubric eval complement

## Raw Concept

K151 arXiv **2607.03510** — **CAGE-1** evaluates whether enterprise agents are deployment-ready on **governed action**, not task fluency alone. Central term: **Prebind Assurance**.

## Narrative

### Prebind Assurance vs completion gates

| Gate type | When | CCC surface |
|-----------|------|-------------|
| **Prebind Assurance** (CAGE-1) | Before action becomes **binding/consequential** | Tier-2 approval, defenseclaw, prod write hooks, OpenSpec AC before merge |
| **Completion proof** (K72) | Before session claims **done** | `wiki_lint.py`, pytest, artifact checks |

Prebind asks: was the action **admitted, held, narrowed, refused, escalated, quarantined, or made non-effective** before protected consequence formed?

### Twelve dimensions → Cemini mapping [TENTATIVE]

| Dimension | Cemini analogue |
|-----------|-----------------|
| Identity and Authority | Tier 1/2 model; SSH/prod RBAC; `@entities/patterns/tier1-tier2-agent-model.md` |
| Policy Enforcement | `.cursor/rules/`, hooks, permission allowlists |
| Retrieval Trust | Wiki provenance, preingest, egress-fi archive |
| Memory Integrity | claude-mem policy, SPI vetting (K100), hot.md schema |
| Tool Safety | MCP Phase-0, lazy-tool allowlist, SeClaw trajectory eval |
| Planning Control | `/goal` AC, OpenSpec before implementation |
| Human Oversight | Glasswing review, super-audit before prod ship |
| Audit and Replayability | `wiki/log.md`, git, claude-mem traces |
| Conflict and Boundary Handling | Prebind + `@concepts/algorithmic-impermeability-model-agnostic-orchestration.md` SIP |
| Failure Behavior | Fail closed; HarnessFix; `@concepts/failed-trajectory-harness-repair.md` |
| Operational Readiness | Phase-0 scripts, wiki_lint, CI |
| Business Fitness | v10 revenue-first eval lens |

### Capability ≠ trust

> An agent may complete a task and still be unsuitable for production — e.g. correct answer from unauthorized context, right tool under wrong authority.

### Name collision

**NOT** `lahlfors/cybernetic-governance-engine` (gateway product also called CAGE). Sure CAGE-1 = **evaluation framework** only.

| Verdict | **REFERENCE** — adopt Prebind checklist for prod-touching agents; no product install |

## Snippets

> "Capability and trust are different properties."
> — [Source: arxiv-2607.03510 §5, retrieved 2026-07-10]
