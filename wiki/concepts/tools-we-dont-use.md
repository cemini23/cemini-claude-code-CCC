---
title: Tools we don't use — institutional reject register
type: concept
tags: [concept, policy, license, tos, phase-0, ridark-eth]
keywords: [reject, do-not-adopt, tos-bypass, archived-repo, gpt4free, ridark-eth, ip-sale-liability]
related:
  - concepts/skill-vetting.md
  - concepts/cross-wiki-routing.md
  - concepts/cross-wiki-tool-eval-inventory.md
  - entities/tools/claude-code-ultimate-guide.md
  - concepts/token-economics-and-prompt-caching.md
  - entities/tools/claude-code-tips.md
  - entities/tools/claude-code.md
  - entities/tools/centaur.md
  - entities/tools/andrej-karpathy-skills-multica.md
  - concepts/tool-eval-license-skepticism-patterns.md
  - concepts/deep-research-evaluation-prompt.md
  - entities/tools/slot-casino-game-developer-skills.md
  - entities/tools/application-skills.md
  - sources/multi-wiki-tool-eval-v8-k103-2026-06-07.md
  - entities/tools/aarri-bench.md
  - sources/arxiv-aarri-research-intern-bench-2606-07462-2026-06-09.md
maturity: draft
created: 2026-05-22
updated: 2026-06-09
cross-wiki-source: "@osint-wiki/sources/trading-posts-oil-polymarket-html-dex-sniping-2026-05-21.md"
---

## Relations

- `@concepts/skill-vetting.md` — Phase-0 gate before any tool enters the stack
- `@concepts/cross-wiki-routing.md` — reject lists arrive via cross-wiki briefs, not auto-stubs
- `@concepts/cross-wiki-tool-eval-inventory.md` — per-tool verdicts; this page is the *policy* layer
- `@entities/tools/claude-code-ultimate-guide.md` — malicious-skill patterns complement ToS-bypass rejects

Cross-wiki: `@osint-wiki/entities/people/ridark-eth.md` — creator-marketing lists are **candidate filters**, not endorsements (K52 misrepresentation precedent).

## Raw Concept

Routed from `briefs/2026-05-21_k55-2-ridark-eth-ccc-relevant-repos.md`. Question: **why does Cemini document tools it will never adopt?** So future sessions don't re-audit ToS-toxic or archived repos because a viral list resurfaced.

## Narrative

### Reject criteria (any one triggers permanent skip)

1. **ToS / license bypass** — tools that exist to route around paid APIs without authorization.
2. **Archived + abandoned** — no maintainer response; security rot.
3. **"Educational purposes only" automation** — mass outreach / content-farm bots with legal disclaimers instead of licenses.
4. **Unverified creator lists** — @ridark_eth-style compilations without per-repo Phase-0 (see K52 fabricated L2/HFT claims on a real MIT repo).

### Registered rejects (CCC brief K55-2)

| Repo | Ridark # | Why permanent skip |
|------|----------|-------------------|
| `feder-cr/Jobs_Applier_AI_Agent_AIHawk` | 1 | Archived 2026-05-17; mass job-application automation; ToS risk |
| `FujiwaraChoki/MoneyPrinterV2` | 5 | Content-farm / cold-email automation; "educational" disclaimer; IP/legal landmine |
| `xtekky/gpt4free` | 18 | ToS-bypass API aggregation |
| `cheahjs/free-llm-api-resources` | 18 | Same class as gpt4free |
| `cmliu/CF-Workers-docker.io` | 30 | Archived; regional-blockage bypass; marginal CCC value |

### Awareness-only (do not install; may inform instrumentation design)

| Repo | Ridark # | Note |
|------|----------|------|
| `wusimpl/AntigravityQuotaWatcher` | 19 | Quota UI patterns — compare to `@entities/tools/codexbar.md` / `@entities/tools/ai-token-monitor.md` |
| `hamed-elfayome/Claude-Usage-Tracker` | 19 | Same |

### Skepticism register (audit before any use)

| Repo | Ridark # | Note |
|------|----------|------|
| `rtk-ai/rtk` | 16 | Claims 60–90% token reduction — require Phase-0 + benchmark; likely quality tradeoff |
| `BlockRunAI/ClawRouter` | 17 | Routing pattern sound; implementation unverified |

### K63 cursor abuse / piracy cluster (2026-05-24)

Reject **even when MIT** — ToS circumvention and operational risk per `@osint-wiki/sources/multi-wiki-tool-eval-36url-wiki-ingestion-2026-05-24.md`.

| Repo | Why permanent skip |
|------|-------------------|
| `kingparks/cursor-vip` | Piracy / VIP bypass |
| `yuaotian/go-cursor-help` | ToS circumvention |
| `chengazhen/cursor-auto-free` | NC license / abuse |
| `7836246/cursor2api` | Proxy abuse (eval wrongly claimed NO LICENSE) |

### K68 license overturn (2026-05-26)

Eval claimed MIT; **`gh api` verification** returned no LICENSE file — permanent skip per `@osint-wiki/entities/tools/claudish.md`.

| Repo | Why permanent skip |
|------|-------------------|
| `MadAppGang/claudish` | Eval Adopt **overturned** — `license: null`, no LICENSE file |

### K71 license demote (2026-05-27)

| Repo | Why not install |
|------|-----------------|
| `multica-ai/andrej-karpathy-skills` | Eval Adopt → **`license: null`** — reference markdown only → `@entities/tools/andrej-karpathy-skills-multica.md` |

### K103 license overturn + lock-in (2026-06-07)

| Repo | Why not install |
|------|-----------------|
| `membranedev/application-skills` | Eval Adopt overturned — **`license: null`** + Membrane platform lock-in → `@entities/tools/application-skills.md` |

### K107 AARRI-bench (2026-06-09)

| Repo | Why not install |
|------|-----------------|
| `AARR-bench/AARRI-bench` | **NO-GO** — `license: null` (`gh api` 2026-06-09); rubric steal-only → `@entities/tools/aarri-bench.md` |

### Process

When a new viral list appears: **license-verify via `gh api` → Phase-0 → promote or catalog** per `@concepts/cross-wiki-tool-eval-inventory.md`. Never create entity stubs for Reject-tier entries.

## Snippets

> Entries include ToS-violating tools, archived repos, and "educational purposes only" disclaimers. Treat as candidate-list filter.
> — [Source: briefs/2026-05-21_k55-2-ridark-eth-ccc-relevant-repos.md]
