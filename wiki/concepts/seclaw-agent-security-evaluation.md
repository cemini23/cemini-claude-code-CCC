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
  - "@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md"
  - sources/trading-posts-compilation-18-2026-06-04.md
maturity: draft
created: 2026-06-04
updated: 2026-06-04
cross-wiki-source: "@osint-wiki/concepts/seclaw-agent-security-evaluation.md"
---

## Relations

- `@sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md` — arXiv provenance
- `@concepts/skill-vetting.md` — manual Phase-0 checklist SeClaw automates
- `@entities/tools/defenseclaw.md` — Cisco admission-control parallel
- `@entities/tools/lazy-tool.md` — harness surface to regression-test
- `@entities/tools/conductor-mcp.md` — write-tool policy target
- `@osint-wiki/concepts/seclaw-agent-security-evaluation.md` — OSINT canon
- `@cybersecurity-wiki/briefs/2026-06-04_k98-seclaw-agent-eval-from-osint.md` — eval methodology depth

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

## Snippets

> "trajectory-aware assessment of unsafe actions beyond final responses"
> — [Source: @osint-wiki/sources/arxiv-seclaw-spec-driven-agent-security-2606-02302-2026-06-04.md]
