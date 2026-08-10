---
title: "ResidencyRL — multi-turn RL in simulated clinical environments"
type: source
tags: [source, arxiv, rl, multi-turn, clinical, harness, k260]
keywords: [2608.07418, ResidencyRL, GRPO, adversarial-curriculum, structured-reward, premature-closure, SOAP]
related:
  - concepts/adversarial-curriculum-structured-reward-doc-fidelity.md
  - entities/tools/residencyrl.md
  - concepts/harness-native-agent-rl-training.md
  - concepts/agent-rubrics-self-correction.md
  - concepts/bounded-self-refinement-vs-rsi-taxonomy.md
  - sources/brief-k260-residencyrl-2026-08-10.md
  - briefs/2026-08-10_ccc-handoff-k260-residencyrl-ingest.md
maturity: draft
created: 2026-08-10
updated: 2026-08-10
---

## Relations

- `@concepts/adversarial-curriculum-structured-reward-doc-fidelity.md`
- `@entities/tools/residencyrl.md`
- `@concepts/harness-native-agent-rl-training.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | ResidencyRL: Reinforcement Learning in Simulated Clinical Environments |
| **arXiv** | 2608.07418v1 (cs.AI, 2026-08-07) |
| **Authors** | Liévin, Schmidgall, Strother, Bijamov, et al. (Google DeepMind / Google Research + clinical collaborators) |
| **Code** | **Not open-sourced** — internal Google infra + medical-safety rationale ([CONFIRMED] Code Availability §) |
| **Domain** | Clinical multi-turn agent RL (telehealth sim) |
| **Retrieved** | 2026-08-10 |

## Narrative

Online multi-turn RL (GRPO) trains a Gemini-initialized clinician agent against LLM patient simulators across up to ~60 dialogue turns + 8 tool calls. Curriculum scenario packs: routine telehealth (~83%), targeted history/intake (~15%), adversarial (~2%). Hierarchical autorater reward: diagnosis / management / intake / communication / documentation / style + hard penalties (hallucinations, contraindications, missed red flags). Held-out: +7.0 pp diagnostic accuracy under adversarial conditions (88% vs 81%); −31% missed red-flag rate; clinicians prefer trained agent in 87.6% side-by-sides. Procedural gains transfer to AMIE multi-visit, AgentClinic, CRAFT-MD.

Clinical product **OOD** for Cemini runtime. Steal is harness methodology: adversarial curriculum mix, structured rubrics + safety penalties, resist premature closure, documentation fidelity (no fabricated chart facts).

| Verdict | **ADOPT** harness patterns. **NO-GO** code (closed). Entity `wont_wire`. |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.07418-residencyrl-reinforcement-learning-in-simulated.pdf` (archived 2026-08-10).

## Snippets

> "Due to this, and more importantly, the safety implications associated with the unmonitored use of AI systems in medical contexts, we are not open-sourcing the codebase employed in our work at this time." [Source: arXiv 2608.07418 Code Availability]

> Case study: base model terminated after ~5 turns and "hallucinates the medical history and medications taken which were never stated by the patient in the transcript." [Source: arXiv 2608.07418 §F.2]
