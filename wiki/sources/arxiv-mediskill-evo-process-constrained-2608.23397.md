---
title: "MediSkill-Evo — process-constrained self-evolution for evidence-grounded clinical interaction"
type: source
tags: [source, arxiv, clinical, self-evolution, typed banks, process critic, safety, k307]
keywords: [2608.23397, mediskill-evo, agentclinic, frozen test-time snapshot, casia, misevolution]
related:
  - concepts/process-constrained-self-evolution.md
  - concepts/skill-misevolution.md
  - briefs/2026-08-25_ccc-k300-k309-sip-ready.md
maturity: draft
read_status: read
created: 2026-08-25
updated: 2026-08-25
---

## Relations

- `@concepts/process-constrained-self-evolution.md`
- `@concepts/skill-misevolution.md`
- `@briefs/2026-08-25_ccc-k300-k309-sip-ready.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | MediSkill-Evo: Process-Constrained Self-Evolution for Evidence-Grounded Clinical Interaction |
| **arXiv** | 2608.23397 |
| **Authors** | Ruoyu Wu, Shenfu Xie, Yinqian Sun, Haibo Tong, Feifei Zhao et al. (CASIA; Beijing Key Lab of Safe AI and Superalignment) |
| **Code** | none public → pattern only |
| **Retrieved** | 2026-08-25 |

## Narrative

Clinical agents must convert partial observations into grounded actions; a correct final label does not certify the process respected evidence and care-process contracts. MediSkill-Evo evolves governed process knowledge **without backbone fine-tuning**:

- **Four typed banks** — Clinical Skills, Process Rules, Symbolic Schemas, Measurement procedures — kept separate because they demand different scopes and safeguards.
- Publication into a **frozen test-time snapshot** governed by provenance, support, replay, and controller-defined safety checks.
- **Process-Constrained Preference Harness** binds evidence to source, rejects controller-invalid candidates, ranks actions via a safety-prioritized Clinical Process Critic.

Frozen-suite eval (2 backbone endpoints × 6 stress dimensions): on 300 held-out Qwen encounters, diagnosis accuracy **61.33% → 69.00%**, treatment-intent coverage **33.62% → 66.44%**, auto-scored critical failures **31.00% → 16.33%** vs AgentClinic. Hard-isolation recovery: 93.61% under patient-behavior pressure, 100% temporal evidence, 92.22% triage red flags.

Transferable shape for any skill/harness self-evolution: **type your memory banks, freeze the eval snapshot before evolution, gate candidates through a process critic with veto power**. Pairs K237 misevolution gates and K162 external-eval contract.

| Verdict | **ADOPT pattern** — typed banks + frozen test-time snapshot + process critic. Clinical domain **`wont_wire`**; no unattended skill evolve on CCC. |
|---------|---------|

## Snippets

> "Four typed banks separately maintain Clinical Skills, Process Rules, Symbolic Schemas, and Measurement procedures, while provenance, support, replay, and controller-defined safety checks govern publication into a frozen test-time snapshot." [Source: arXiv 2608.23397 abstract]

| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.23397-mediskill-evo-process-constrained-self-evolution.pdf` |
|--------------|-------------------------------------------------------------------------------------------------------------------|
