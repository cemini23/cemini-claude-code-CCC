---
title: SeClaw — trajectory-aware agent security eval (K98)
type: concept
tags: [concept, agent-security, evaluation, seclaw, k98]
keywords: [2606.02302, seclaw, trajectory, docker-testbed, mcp-security]
related:
  - sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md
  - concepts/skill-vetting.md
  - entities/tools/defenseclaw.md
  - entities/tools/lazy-tool.md
  - entities/tools/conductor-mcp.md
  - concepts/mcp-server-catalog-curation.md
  - "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md"
  - "@cybersecurity-wiki/entities/tools/seclaw-eval.md"
  - "@cybersecurity-wiki/briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md"
  - sources/trading-posts-compilation-18-2026-06-04.md
  - concepts/cross-wiki-tool-adoption-routing.md
  - concepts/failed-trajectory-harness-repair.md
  - concepts/etclovg-harness-layers.md
  - concepts/mcp-server-runtime-fault-taxonomy.md
  - sources/arxiv-mcp-runtime-fault-taxonomy-2606.05339.md
  - concepts/enterprise-mcp-adoption-practice.md
  - sources/arxiv-enterprise-mcp-adoption-2606.09182.md
  - concepts/safeclawbench-staged-security-endpoints.md
  - sources/arxiv-safeclawbench-staged-agent-security-2606.18356.md
  - meta/ccc-cross-wiki-handoff-briefs.md
  - concepts/substrate-constraints-coding-agent-oversight.md
  - sources/arxiv-steerability-via-constraints-coding-agent-oversight-2607.02389.md
  - entities/tools/openshell.md
  - concepts/cage-1-enterprise-agent-governance-eval.md
  - concepts/trustx-agent-risk-classification.md
  - concepts/verifiable-search-agent-environment.md
  - sources/arxiv-flowguard-mcp-security-evidence-2607.14754.md
  - concepts/mcp-security-signals-vs-runtime-evidence.md
maturity: draft
created: 2026-06-04
updated: 2026-07-18
cross-wiki-source: "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
---

## Relations

- `@sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md` — arXiv provenance
- `@concepts/skill-vetting.md` — manual Phase-0 checklist SeClaw automates
- `@entities/tools/defenseclaw.md` — Cisco admission-control parallel
- `@entities/tools/lazy-tool.md` — harness surface to regression-test
- `@entities/tools/conductor-mcp.md` — write-tool policy target
- `@osint-wiki/concepts/seclaw-agent-security-evaluation.md` — OSINT canon
- `@cybersecurity-wiki/concepts/seclaw-agent-security-evaluation.md` — **canonical** eval methodology (this page = CCC pointer)
- `@cybersecurity-wiki/entities/tools/defenseclaw.md` — runtime gate (cybersec canon)
- `@cybersecurity-wiki/entities/tools/seclaw-eval.md` — benchmark repo entity

## Raw Concept

arXiv 2606.02302 (K98 inbox): **spec-driven security task synthesis** + docker testbed for **trajectory-aware** scoring of tool-using agents — unsafe intermediate steps, not just final-answer politeness.

## Narrative

| Design choice | CCC implication |
|---------------|-----------------|
| Risk specs → tasks | Map to `@concepts/skill-vetting.md` rows before MCP GO |
| Trajectory scoring | Stop hooks + tool audit logs matter; final message "looks fine" is insufficient |
| Docker testbed | Laptop-only regression — not prod dependency |

### Adoption posture

| Check | Status |
|-------|--------|
| Repo | `github.com/seclaw-eval/seclaw-eval` |
| License | **NO LICENSE FILE** — GitHub API `license: null`; root `LICENSE` 404 [CONFIRMED 2026-06-04] |
| Code | README + `docs/` only — README states **"Code: Coming soon"**; 0★ |
| Verdict | **NO-GO (install)** — **REFERENCE (methodology)** until LICENSE + runnable code ship |
| vs defenseclaw | SeClaw = benchmark; defenseclaw = runtime gate — complementary |
| vs HarnessFix (2606.06324) | SeClaw scores **security** trajectories; HarnessFix repairs **reliability** harness flaws — both reject final-answer-only eval |
| vs MCP fault taxonomy (2606.05339) | Taxonomy's **Security** category (54 threads) + 27 subcategories define fault-injection fixtures; SeClaw scores agent trajectories against injected faults — complementary test design |
| vs substrate constraints (2607.02389) | SeClaw = trajectory security scoring; K138 = **code-shape** substrate making weak reviewers effective — use both in Tier-2 promotion |

**Do not** conflate with EMS/trading RBAC audits (OSINT `@concepts/ems-execution-security-gaps.md` scope).

## Phase-0 Audit (2026-06-04)

**Method:** GitHub API + README decode. No clone/run (no executable benchmark yet).

| Check | Result |
|-------|--------|
| License | **NONE** — no `LICENSE` file; API returns null SPDX |
| Maturity | **0★**; org `seclaw-eval`; last push **2026-06-02**; tree = `README.md` + `docs/` |
| Paper | arXiv 2606.02302 — trajectory-aware docker testbed (methodology valid for CCC wiki) |
| Failure mode | **License blocker** + **vapor code** — cannot run eval harness |

**Decision — NO-GO for install.** Keep arXiv source page + this concept as **REFERENCE** for trajectory scoring discipline (feeds skill-vetting + Stop-hook testing). Re-run Phase-0 when repo ships LICENSE + SeClaw-Bench code. Until then, use `@entities/tools/defenseclaw.md` scanner patterns for practical gates.

## Adoption trial (2026-06-04) — full run

| Step | Result |
|------|--------|
| GitHub API license | **NONE** (unchanged) |
| Repo tree | `README.md` + `docs/` only |
| Runnable benchmark | **NO** |
| Primary wiki | **cybersecurity-wiki** when code ships |

**Handoff:** `briefs/2026-06-04_cybersecurity-handoff-defenseclaw-seclaw.md`

## Snippets

> "trajectory-aware assessment of unsafe actions beyond final responses"
> — [Source: @osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md]
