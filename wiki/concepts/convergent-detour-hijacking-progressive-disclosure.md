---
title: "Convergent Detour Hijacking — progressive-disclosure skill supply-chain attack (K274)"
type: concept
tags: [concept, skill-security, progressive-disclosure, cost-trajectory, k274]
keywords: [2608.12273, CDH, skill-selection, planner-integrity, attract-detour-converge, trajectory-necessity]
related:
  - sources/arxiv-convergent-detour-hijacking-cdh-2608.12273.md
  - entities/patterns/convergent-detour-hijacking.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/skill-vetting.md
  - entities/tools/agent-skill-manager.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
  - concepts/phase1-adopt-wire.md
  - entities/tools/vakra.md
  - sources/arxiv-vakra-multi-hop-api-retrieval-2608.12282.md
  - concepts/measurement-integrity-mcp-security-eval.md
  - concepts/intersage-trust-native-ioa-protocol.md
  - entities/patterns/treatment-blind-endpoint-integrity.md
  - entities/tools/intersage.md
  - sources/arxiv-labels-not-endpoints-treatment-leakage-2608.12880.md
  - sources/arxiv-intersage-trust-native-ioa-protocol-2608.13030.md
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- `@sources/arxiv-convergent-detour-hijacking-cdh-2608.12273.md`
- `@entities/patterns/convergent-detour-hijacking.md`
- `@concepts/agent-skills-progressive-disclosure.md`

## Raw Concept

How can a publisher who controls only one static skill steer a progressive-disclosure agent onto a costlier trajectory while the task still completes?

## Narrative

K274 formalizes the **skill-selection + planning-integrity / cost-trajectory** threat model for progressive-disclosure skill platforms (SKILL.md, MCP catalogs, skill registries). CDH is a text-only, runtime-independent attack: description wins selection (attract), body fabricates plausible dependencies (detour), then re-enters the original route (converge).

### Steal (ADOPT)

1. **Trajectory necessity is a security requirement** — final-answer correctness does not imply cost safety. Audit trajectories, not just outputs.
2. Treat skill **selection metadata and instruction body as two coupled control points** — a static skill can bridge the progressive-disclosure boundary.
3. **Pre-installation review**: routing claims must match the skill's declared role; body dependencies unrelated to that role are a red flag.
4. **Runtime monitoring**: flag unexplained cross-skill transitions; enforce token/invocation budgets. Budgets do not assume harmful behavior changes the output.
5. Defense evals must jointly measure attack suppression, task completion, and defense overhead — avoid suppressing legitimate multi-skill workflows.

| Verdict | **ADOPT** threat model + defense posture. No code to adopt — pattern only. |

## Snippets

> "Thus, correct outcomes do not guarantee trajectory integrity or cost safety."

> "These findings make trajectory necessity — not final-answer correctness alone — a security requirement for extensible agents."

[Source: arXiv 2608.12273 p.1, p.14]
