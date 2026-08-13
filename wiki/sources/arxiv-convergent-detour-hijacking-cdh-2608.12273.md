---
title: "Convergent Detour Hijacking — task-preserving resource amplification in skill-based agents"
type: source
tags: [source, arxiv, skill-security, progressive-disclosure, cost-trajectory, k274]
keywords: [2608.12273, CDH, skill-selection, planner-integrity, attract-detour-converge, trajectory-necessity]
related:
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - entities/patterns/convergent-detour-hijacking.md
  - concepts/agent-skills-progressive-disclosure.md
  - concepts/skill-vetting.md
  - entities/tools/agent-skill-manager.md
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- `@concepts/convergent-detour-hijacking-progressive-disclosure.md`
- `@entities/patterns/convergent-detour-hijacking.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | Convergent Detour Hijacking: Task-Preserving Resource Amplification in Skill-Based LLM Agents |
| **arXiv** | 2608.12273 |
| **Authors** | Junliang Liu, Ruoyu Li, Wenxin Tang, Jingyu Xiao, Zhenyu Liu, Jingheng Xu, Laizhong Cui (Shenzhen Univ / CUHK) |
| **Code** | No public artifact at Phase-0 — attack paper, pattern only |
| **Retrieved** | 2026-08-13 |

## Narrative

Text-only, runtime-independent **publisher-only** supply-chain attack on **progressive-disclosure** skill agents. A malicious skill's description wins selection (attract), its body recruits unnecessary benign skills into a bounded detour (detour), then an explicit return condition re-enters the original route so the task still completes (converge).

**Attack mechanics:**

- Two sequential control points: **routing metadata** (`d_s`) shapes selection, **instruction body** (`b_s`) shapes planning. Neither alone reproduces the effect — the coupling is the attack.
- Attacker-controlled **coordinator skill** is co-selected alongside legitimate skills without suppressing them.
- 53-skill OpenClaw registry, 9 functional groups, 536 multi-skill tasks, 491 held-out. Paired clean–injected eval across LLM backends, single-task + multi-turn.

**Key results (DeepSeek-V4-Pro):** coordinator selected in **80.02%** of tasks; among coordinator-hit runs that complete, token consumption **+66.91%** and end-to-end execution time **+92.45%**; aggregate task completion stays comparable.

| Verdict | **ADOPT** skill-selection + planning-integrity / cost-trajectory threat model. **NO-GO** code (none). Pattern only — no SPDX artifact expected. |

**Defense pointers (from paper discussion):** pre-installation review (routing claims vs declared role; body deps unrelated to role) + runtime monitors (flag unexplained cross-skill transitions; token/invocation budgets). Core claim: **correct outcomes do not guarantee trajectory integrity or cost safety** — trajectory necessity is the security requirement.

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.12273-convergent-detour-hijacking-task-preserving-reso.pdf`
