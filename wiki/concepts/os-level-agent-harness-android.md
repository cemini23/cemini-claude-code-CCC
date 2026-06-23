---
title: OS-level agent harness — Android agent-native design (AOHP)
type: concept
tags: [concept, os-level, android, aohp, agent-native-os, k123]
keywords: [2606.23449, aosp, service-composition, information-flow]
related:
  - sources/arxiv-aohp-os-level-agent-harness-2606.23449.md
  - entities/tools/aohp.md
  - concepts/runtime-harness-interface-adaptation.md
  - concepts/code-as-agent-harness.md
  - concepts/system-scaling-harness-agentic-ai.md
  - concepts/handoff-validity-agent-harness.md
maturity: draft
created: 2026-06-23
updated: 2026-06-23
---

## Relations

- `@sources/arxiv-aohp-os-level-agent-harness-2606.23449.md` — AOHP technical report
- `@entities/tools/aohp.md` — github.com/aohp-os/aohp
- `@concepts/runtime-harness-interface-adaptation.md` — harness-interface evolution peer

## Raw Concept

What OS primitives does an **agent-native** personal OS need beyond app-centric Android/iOS?

## Narrative

**App-centric mismatch** [TENTATIVE — 2606.23449]: fixed GUIs, per-app permissions, single-active-app assumptions create token overhead and security gaps for cross-app agents.

**AOHP mechanisms → harness analogues:**

| AOHP | CCC laptop harness |
|------|-------------------|
| Personalized service composition | Task-level `/goal` envelopes vs per-tool micromanagement |
| Efficient agent interfaces (structured UI, events) | MCP tool schemas, browser snapshot vs raw HTML |
| Secure information flow tracking | Permission hooks, cybersecurity-wiki scoping |

**Eval:** OpenClaw agents on mobile cross-app tasks — +21% completion, -51% tokens vs stock Android.

**Verdict:** **REFERENCE** architecture; **CONDITIONAL-GO** clone repo (`scripts/adopt_k123_phase0.sh`); **NO-GO** AOSP prod build without dedicated hardware lab.

## Snippets

> "Treat agents as first-class OS actors, enabling adaptive user interfaces and agent-friendly runtime environments."
> — [Source: arxiv-2606.23449-2606-23449v1-aohp-an-open-source-os-level-agent.pdf, retrieved 2026-06-23]
