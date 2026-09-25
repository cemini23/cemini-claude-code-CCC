---
title: "Coding agents for generalized TAMP (cross-wiki from Cybersec OOD)"
type: source
tags: [source, ood, robotics, tamp, coding-agents]
keywords: [2609.30233, generalized-tamp, coding-agents]
related:
  - "@cybersecurity-wiki/sources/arxiv-2609-30233-coding-agents-generalized-tamp-ood.md"
maturity: validated
read_status: deep-read
created: 2026-09-25
updated: 2026-09-25
cross-wiki-routed: cybersecurity-wiki
---

## Relations

- @cybersecurity-wiki/sources/arxiv-2609-30233-coding-agents-generalized-tamp-ood.md — cyber ingest OOD stub + PDF on cybersec egress

## Raw Concept

| Field | Value |
|-------|-------|
| Title | Coding Agents for Generalized Task and Motion Planning Problems |
| arXiv | 2609.30233 |
| Location | cemini-egress-fi:/opt/cemini-bulk/research/cybersec/arxiv-2609-30233-coding-agents-for-generalized-task-and-motion-pl.pdf |
| Retrieved | 2026-09-25 |

## Narrative

Princeton-led **large-scale generalized TAMP** study: **Claude Code (Opus 5)**, **Codex (GPT-5.6 Sol, GPT-6 Astra)** synthesize policies in a **Docker sandbox** (no network; NumPy/SciPy only) with simulator API outside the container. **28** environments, **980** frozen programs × **100** held-out starts (**98k** eval episodes). Mean success **56–95%** vs **~47%** classical planners on 16 planner-available envs; agent programs scale better as object counts grow.

Steal for **CCC embodied agent harness** eval: treat coding agents + sandbox isolation as the generalized-planning baseline; red-team sandbox escape separately from cyber TAMP OOD stub.

## Snippets

> "980 generated programs on 100 held-out instances each, 98,000 evaluation episodes in total." [Source: arXiv 2609.30233]

> "We test this isolation through red-teaming, including attempts to read environment source code, import forbidden libraries, or reach the host or network." [Source: arXiv 2609.30233]
