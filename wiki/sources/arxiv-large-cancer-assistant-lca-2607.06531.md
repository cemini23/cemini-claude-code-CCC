---
title: Large Cancer Assistant (LCA) — model-agnostic clinical orchestration (arXiv 2607.06531)
type: source
tags: [source, arxiv, orchestration, model-agnostic, clinical, k150]
keywords: [2607.06531, LCA, algorithmic impermeability, SIP, standardized intermediate payload, SDR, entry theory, oncology]
related:
  - concepts/algorithmic-impermeability-model-agnostic-orchestration.md
  - concepts/handoff-validity-agent-harness.md
  - concepts/multi-agent-evidence-artifact-layers.md
  - sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md
  - concepts/cross-wiki-routing.md
  - sources/brief-k150-algorithmic-impermeability-orchestration-2026-07-09.md
  - concepts/agentic-online-rl-self-evolving-systems.md
  - concepts/code-as-agent-harness.md
  - concepts/model-native-vs-tool-mediated-fulfillment.md
  - concepts/subagent-orchestration.md
maturity: draft
read_status: read
created: 2026-07-09
updated: 2026-07-09
phase_0_verdict: "REFERENCE 2026-07-09 — clinical oncology off-domain; no public code repo at Phase-0 (PDF cites repository placeholder); steal algorithmic impermeability + SIP + SDR patterns"
---

## Relations

- `@concepts/algorithmic-impermeability-model-agnostic-orchestration.md` — CCC harness synthesis
- `@sources/arxiv-bioinsight-multi-agent-biomedical-2606.20997.md` — prior biomedical orchestration steal (K124)

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | The Large Cancer Assistant (LCA): A Model-Agnostic Orchestration Framework for Scalable Clinical Decision Support in Oncology |
| **Authors** | Ghassen Marrakchi, Basarab Matei (LIPN, CNRS, Sorbonne Paris Nord) |
| **arXiv** | 2607.06531v1 [cs.AI] |
| **Code** | PoC artifacts cited in paper; **no public GitHub URL at Phase-0** (repository placeholder in PDF) |
| **Location** | `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2607.06531-2607-06531v1-the-large-cancer-assistant-lca-a-mo.pdf` |
| **Retrieved** | 2026-07-09 |
| **Read status** | read (7-tuple, impermeability, SIP, SDR, PoC scenarios) |

## Narrative

**LCA** is a **post-hoc, model-agnostic** orchestration framework for multimodal oncology CDS — decoupling data ingestion/routing from black-box AI inference via **Algorithmic Impermeability**.

### Architecture (7-tuple) [TENTATIVE]

| Component | Role |
|-----------|------|
| **Entry Theory** | GDL-based standardization of multimodal patient data (structural + medical axes) |
| **Cancer Switching Module** | Dynamic routing by cancer profile / modality availability |
| **AI execution** | Black-box models — strictly isolated from routing logic |
| **SIP** | Standardized Intermediate Payload — boundary before volatile hospital IT / EMR |
| **SDR** | Supplementary Data Requests — targeted asks when modalities missing (100% recall in PoC) |

### PoC results

- Negligible orchestration overhead vs inference
- **Invariant routing projection** when AI models swapped (impermeability validated)
- **100% recall** generating SDR under injected data anomalies
- Multi-protocol execution verified

### Cross-wiki routing

**Clinical oncology domain — off-topic for CCC prod, cybersec, gambling, OSINT finance.** Ingest for **harness patterns only** (impermeability, SIP, SDR). No David/TipDrop adoption. Pairs with `@concepts/multi-agent-evidence-artifact-layers.md` (typed intermediate artifacts) and `@concepts/handoff-validity-agent-harness.md` (SIP as handoff contract).

| Verdict | **REFERENCE** — harness design vocabulary; NO-GO clinical install |

## Snippets

> "Algorithmic Impermeability, ensuring the orchestration logic remains strictly independent of underlying black-box AI models."
> — [Source: arxiv-2607.06531 abstract, retrieved 2026-07-09]

> "The SIP establishes a clear architectural boundary, natively setting the stage for downstream EMR interoperability."
> — [Source: arxiv-2607.06531 abstract, retrieved 2026-07-09]

> "100% recall rate in generating targeted Supplementary Data Requests (SDR) under injected data anomalies."
> — [Source: arxiv-2607.06531 abstract, retrieved 2026-07-09]
