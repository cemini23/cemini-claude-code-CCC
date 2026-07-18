---
title: SafeClawBench — three-endpoint agent security eval
type: concept
tags: [concept, agent-security, safeclawbench, cross-wiki-route, k121]
keywords: [2606.18356, semantic-core, sandbox-harm, harm-evidence]
related:
  - sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md
  - concepts/seclaw-agent-security-evaluation.md
  - entities/tools/defenseclaw.md
  - concepts/skill-vetting.md
  - concepts/etclovg-harness-layers.md
  - cybersecurity-wiki/concepts/safeclawbench-staged-agent-security.md
  - sources/brief-k121-tokenpilot-safeclaw-gatekeepers-prod-2026-06-21.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/verifiable-search-agent-environment.md
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
maturity: draft
created: 2026-06-21
updated: 2026-07-18
---

## Relations

- `@sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md` — arXiv provenance
- `@concepts/seclaw-agent-security-evaluation.md` — SeClaw trajectory eval peer
- `@entities/tools/defenseclaw.md` — runtime scanner/admission parallel
- `@concepts/skill-vetting.md` — Phase-0 manual checklist
- `@concepts/etclovg-harness-layers.md` — Governance / Verification layers
- `@cybersecurity-wiki/concepts/safeclawbench-staged-agent-security.md` — **canonical** security benchmark track

## Raw Concept

Should agent security be one attack-success rate, or staged endpoints?

## Narrative

**SafeClawBench** [TENTATIVE — 2606.18356]: **600** tool-using agent adversarial tasks; report **three endpoints separately**:

| Endpoint | Measures | CCC use |
|----------|----------|---------|
| Semantic Core | Textual compliance with attack | Insufficient alone for "safe" |
| Harm evidence | Audit-visible artifacts | Log/hook evidence gates |
| Sandbox harm | Executable state changes | Tier-2 sandbox tests |

Key finding: sandbox harm can occur **after** semantic pass — motivates defense-in-depth beyond prompt policies.

**Cross-wiki:** full eval playbook → `@cybersecurity-wiki`. CCC uses endpoint separation in skill-vetting + Stop-hook testing discipline.

**Verdict:** Dataset on HuggingFace — **REFERENCE** for cybersec eval; NO-GO blind install without policy review.

## Snippets

> "Semantic failure rates vary widely across models, from 9.0% to 44.2%."

> — [Source: arxiv-2606.18356-safeclawbench-separating-semantic-audit-evidence.pdf]
