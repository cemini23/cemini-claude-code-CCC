---
title: SafeClawBench — staged agent security endpoints (arXiv 2606.18356)
type: source
tags: [source, arxiv, safeclawbench, agent-security, k121]
keywords: [2606.18356, semantic-core, sandbox-harm, openclaw]
related:
  - concepts/safeclawbench-staged-security-endpoints.md
  - concepts/seclaw-agent-security-evaluation.md
  - cybersecurity-wiki/concepts/safeclawbench-staged-agent-security.md
  - entities/tools/defenseclaw.md
maturity: draft
read_status: read
created: 2026-06-21
updated: 2026-06-21
---

## Relations

- `@concepts/safeclawbench-staged-security-endpoints.md` — CCC pointer synthesis
- `@concepts/seclaw-agent-security-evaluation.md` — trajectory eval peer (SeClaw)
- `@cybersecurity-wiki/concepts/safeclawbench-staged-agent-security.md` — canonical security eval track

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | SafeClawBench: Separating Semantic, Audit-Evidence, and Sandbox Harm in Tool-Using LLM Agents |
| **Authors** | Tian et al. (PKU, Huawei, Tsinghua) |
| **arXiv** | 2606.18356v1 [cs.CR] |
| **Dataset** | `huggingface.co/datasets/sairights/safeclawbench` |
| **Location** | `raw-sources/arxiv-2606.18356-safeclawbench-separating-semantic-audit-evidence.pdf` |
| **Retrieved** | 2026-06-21 |
| **Read status** | read |

## Narrative

**600 adversarial tasks** across six families: DPI, IPI, TRI, MPI, MEX, ADI (direct/indirect injection, tool-return injection, memory poison/extract, ambiguity-driven unsafe inference).

**Three separate endpoints** (do not collapse):

1. **Semantic Core** — model agrees with attacker text
2. **Harm evidence** — audit-visible artifact (narrower than semantic)
3. **Sandbox harm** — executable state/tool effects (291/347 sandbox harms passed semantic check in matched analysis)

Five agent endpoints × four prompt policies. Semantic failure 9–44.2% without extra protection.

**CCC routing:** evaluation methodology + dataset → **cybersecurity-wiki**; CCC keeps pointer + skill-vetting / defenseclaw links.

## Snippets

> "291 of 347 observed sandbox harms occur in rows that pass the semantic check."

> "Collapsing these endpoints into one attack success number hides semantic-only failures."
