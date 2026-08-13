---
title: "VAKRA — multi-hop reasoning across APIs and retrieval under tool-use policies"
type: source
tags: [source, arxiv, benchmark, tool-policy, multi-hop, k275]
keywords: [2608.12282, VAKRA, API-hops, multi-source, NL-policy-constraints, re-exec-verify, ReAct]
related:
  - concepts/multi-hop-api-retrieval-eval-tool-policies.md
  - entities/tools/vakra.md
  - concepts/verifiable-deterministic-agent-benchmarking.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/mcp-claim-validation-and-parameter-grounding.md
  - concepts/convergent-detour-hijacking-progressive-disclosure.md
  - sources/brief-k274-k276-skill-security-eval-2026-08-13.md
  - briefs/2026-08-13_ccc-handoff-k274-k276-ingest.md
maturity: draft
created: 2026-08-13
updated: 2026-08-13
---

## Relations

- `@concepts/multi-hop-api-retrieval-eval-tool-policies.md`
- `@entities/tools/vakra.md`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use Policies |
| **arXiv** | 2608.12282 |
| **Authors** | Ankita Rajaram Naik, Anupama Murthi, Benjamin Elder, et al. (IBM, Yorktown Heights) |
| **Code** | `github.com/IBM/VAKRA` — **CC BY-NC-SA 4.0** (LICENSE file verified; `gh api` NOASSERTION since CC is non-standard SPDX) → **NO-GO clone** |
| **Dataset** | `huggingface.co/datasets/ibm-research/VAKRA` — **WATCH only** |
| **Retrieved** | 2026-08-13 |

## Narrative

Enterprise-grade tool-use benchmark: **8,000+ executable APIs across 62 domains**, with three difficulty settings — (a) diverse API interaction styles, (b) multi-hop reasoning over structured APIs, (c) multi-source reasoning with **natural-language tool-use policy constraints**. Correctness verified by **re-executing predicted tool calls against live database-backed APIs**, accommodating multiple valid solution paths. Fixed ReAct harness isolates model capability from agent architecture.

**Key results:** best model (GPT-5.5) reaches only **70.4%** on single-hop endpoint-style tasks, drops to **50–51%** on compositional business-intelligence APIs; most models lose **>50%** accuracy as reasoning depth increases; policy-constrained questions expose severe failures — **2.4%** on unanswerable queries. Trace analysis: failures concentrate at **language-mediated reasoning** (entity disambiguation, cross-source grounding, schema alignment), not tool-invocation mechanics.

| Verdict | **ADOPT** eval axes (API hops, multi-source grounding, NL policy constraints, re-exec verify). **NO-GO** clone (`IBM/vakra`, CC-BY-NC-SA — non-commercial). HF dataset WATCH only. Dual interest: cybersec K235 benchflow brief + osint-wiki `entities/tools/vakra.md` (reference-only, same license verdict). |

**Location:** `cemini-egress-fi:/opt/cemini-bulk/research/ccc/arxiv-2608.12282-vakra-evaluating-multi-hop-reasoning-across-apis.pdf`
