#!/usr/bin/env python3
"""Generate K376–K384 wiki ingest artifacts."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-23"
BRIEF = "2026-09-23_ccc-k376-k384-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

ENTRIES = [{'arxiv': '2609.24161',
  'concept': 'mcp-tool-interface-granularity-eval',
  'k': 376,
  'narrative': 'MCP tool **interface granularity** — how many tools, how fine-grained schemas — is a controlled '
               'variable for agent eval, not an afterthought. **MCP-GRANITE** sweeps granularity and reports a '
               '**~4-tool sweet spot** on their benchmark suite: too few tools overload single-call semantics; too '
               'many inflate selection error and context cost. Treat granularity as a harness axis when comparing MCP '
               'stacks or ablating tool design (pairs K272 agent4binary packaging / K351 edge SLM JSON reliability). '
               'No public SPDX product requirement for CCC — eval vocabulary only. No clone. Runtime **`wont_wire`**.',
  'pdf': 'arxiv-2609.24161-mcp-granite-benchmark-granularity-interface-test.pdf',
  'slug': 'arxiv-mcp-granite-tool-interface-granularity-2609.24161',
  'title': 'MCP-GRANITE: Benchmarking Granularity of the MCP Tool Interface for LLM Agents',
  'verdict': 'ADOPT eval-first',
  'wired': True},
 {'arxiv': '2609.24620',
  'concept': None,
  'k': 377,
  'narrative': 'Bayer **Ascent** — clinical MCP agent stack over real hospital workflows. **OOD** for CCC product '
               'runtime; CCC steal is **MCP tool surface design** only: how clinical tasks map to typed tools, audit '
               'boundaries, and human oversight — not clinical deployment. No clone. **`wont_wire`**.',
  'pdf': 'arxiv-2609.24620-ascent-an-agentic-system-over-the-model-context.pdf',
  'slug': 'arxiv-ascent-clinical-mcp-agents-2609.24620',
  'title': 'Ascent: An Agentic System over the Model Context Protocol for Clinical Workflows',
  'verdict': 'OOD clinical MCP stub',
  'wired': True},
 {'arxiv': '2609.24972',
  'concept': 'regularized-recursive-harness-improvement',
  'k': 378,
  'narrative': '**Regularized recursive harness improvement**: proposer operates under a **budget**; **critic** scores '
               'candidate harness edits; **pruner** drops regressions before commit — RSI on harness artifacts without '
               'unbounded self-rewrite of pass criteria (pairs K281 AutoDesign / K313 StarHarness stratification / '
               'K292 continual harness learning). `google-research/rrsi` **Apache-2.0** → optional **GO REFERENCE** at '
               'Phase-0, not required for policy wire. Trainer runtime **`wont_wire`**. **Never auto-evolve** '
               '`.cursor/skills`.',
  'pdf': 'arxiv-2609.24972-rrsi-regularized-recursive-self-improvement-of-a.pdf',
  'slug': 'arxiv-rrsi-regularized-recursive-self-improvement-2609.24972',
  'title': 'RRSI: Regularized Recursive Self-Improvement of Agent Harnesses',
  'verdict': 'ADOPT pattern',
  'wired': True},
 {'arxiv': '2609.24974',
  'concept': None,
  'k': 379,
  'narrative': '**Harness distillation** — compress a heavy agent harness into a lighter one using an '
               '**agent-as-harness** meta loop. Awareness for eval and architecture discussions; '
               '`metaevo-ai/harness-zero` is **SIZE-SKIP** per federation jev rule — **NO clone**, no weight/shelf '
               'pull. Policy awareness wired in source + ccc-k376-k384 rule only. Runtime **`wont_wire`**.',
  'pdf': 'arxiv-2609.24974-harness-zero-harness-distillation-via-agent-as-h.pdf',
  'slug': 'arxiv-harness-zero-harness-distillation-2609.24974',
  'title': 'Harness-Zero: Harness Distillation via Agent-as-Harness',
  'verdict': 'ADOPT awareness',
  'wired': True},
 {'arxiv': '2609.24983',
  'concept': 'on-policy-token-alignment-annotation',
  'k': 380,
  'narrative': '**On-policy token alignment annotation** — correct SFT/preference data at **token granularity** from '
               'on-policy rollouts rather than coarse sequence labels. Eval/training-data axis for tool-use and agent '
               'trajectories where step boundaries matter; not a CCC runtime middleware. Runtime **`wont_wire`**.',
  'pdf': 'arxiv-2609.24983-onpanda-efficient-annotation-of-on-policy-alignm.pdf',
  'slug': 'arxiv-onpanda-on-policy-token-alignment-2609.24983',
  'title': 'onPanda: Efficient Annotation of On-Policy Alignment Data at Token Level',
  'verdict': 'ADOPT eval axis',
  'wired': True},
 {'arxiv': '2609.26760',
  'concept': 'grow-harness-not-context',
  'k': 381,
  'narrative': '**Failure-guided harness code growth** vs stuffing context: when agents fail for missing capability, '
               'add **executable harness code** (tools, checks, control flow) instead of expanding prompts/history. '
               'Pairs K334 harness-as-eval-artifact / K281 meta-harness optimization. HITL before persisting harness '
               'self-writes. No clone. Runtime **`wont_wire`**.',
  'pdf': 'arxiv-2609.26760-grow-the-harness-not-the-context-from-strategy-f.pdf',
  'slug': 'arxiv-growing-harness-not-context-2609.26760',
  'title': 'Grow the Harness, Not the Context: From Strategy Failure to Capability Gain',
  'verdict': 'ADOPT pattern',
  'wired': True},
 {'arxiv': '2609.26761',
  'concept': 'mcp-tool-metadata-supply-chain-risk',
  'k': 382,
  'narrative': '**Semantic MCP hijacking** via **tool metadata + trajectory traces** — descriptions and prior tool '
               'results shape selection without touching server binaries. **Cybersec-primary** supply-chain surface '
               'for MCP catalogs (pairs K274 CDH / K368 implicit trust / K350 harness supply-chain scan). '
               '`Lilaizhen/A2M` **null license** → **NO clone**. **No PoCs / no attack templates anywhere.** Runtime '
               '**`wont_wire`**; concept **`policy_wired`**.',
  'pdf': 'arxiv-2609.26761-a2m-trace-optimized-agent-hijacking-in-the-mcp-e.pdf',
  'slug': 'arxiv-a2m-mcp-metadata-hijacking-2609.26761',
  'title': 'A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem',
  'verdict': 'Cybersec-primary ADOPT policy',
  'wired': True},
 {'arxiv': '2609.26779',
  'concept': 'truncate-only-long-horizon-compaction',
  'k': 383,
  'narrative': '**Truncate-only long-horizon compaction** — evict context by **drop/truncate** only; **never '
               'rephrase** or LLM-summarize retained history into synthetic prose (pairs K265 blast-radius eviction / '
               'K124 compaction ≠ memory owner). `nguyenvuthientrang/cliffcompaction` **MIT** — REFERENCE note in '
               'narrative only; no clone required at Phase-0. Runtime **`wont_wire`**.',
  'pdf': 'arxiv-2609.26779-cliffcompaction-cost-efficient-compaction-for-lo.pdf',
  'slug': 'arxiv-cliffcompaction-long-horizon-compaction-2609.26779',
  'title': 'CliffCompaction: Cost-Efficient Compaction for Long-Horizon LLM Agents',
  'verdict': 'ADOPT pattern',
  'wired': True},
 {'arxiv': '2609.26781',
  'concept': 'decentralized-multi-agent-harness-scaling',
  'k': 384,
  'narrative': '**Orchestrator-free** decentralized multi-agent org scaling to **1024 agents** — harness pattern for '
               'organizational intelligence without a central conductor. `microsoft/Agensh` cited — **404 at Phase-0** '
               '→ **WATCH** SPDX/repo; no clone until public. Runtime **`wont_wire`** — do not replace '
               'Cursor/`/route`.',
  'pdf': 'arxiv-2609.26781-agensh-scaling-organizational-intelligence-to-1.pdf',
  'slug': 'arxiv-agensh-decentralized-multi-agent-scaling-2609.26781',
  'title': 'Agensh: Scaling Organizational Intelligence to 1024 Agents',
  'verdict': 'ADOPT pattern',
  'wired': True}]

def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k = e["k"]
    related, relations = [f"briefs/{BRIEF}"], [f"@briefs/{BRIEF}"]
    if e["concept"]:
        related.insert(0, f"concepts/{e['concept']}.md")
        relations.insert(0, f"@concepts/{e['concept']}.md")
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: source
tags: [source, arxiv, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yaml_list(related)}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
---

## Relations

{chr(10).join(f'- `{r}`' for r in relations)}

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | {e['title']} |
| **arXiv** | {e['arxiv']} (2026-09) |
| **Retrieved** | {DATE} |

## Narrative

**Verdict: {e['verdict']}.**

{e['narrative']}

## Snippets

> "{e['title']} — CCC K{k} synthesis." [Source: arXiv {e['arxiv']} — paraphrase]

| **Location** | `{EGRESS}/{e['pdf']}` |
"""
    (REPO / "wiki/sources" / f"{e['slug']}.md").write_text(body, encoding="utf-8")


def write_concept(e: dict) -> None:
    k, c = e["k"], e["concept"]
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: concept
tags: [concept, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
  - sources/{e['slug']}.md
  - concepts/phase1-adopt-wire.md
  - briefs/{BRIEF}
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: {DATE}
updated: {DATE}
---

## Relations

- `@sources/{e['slug']}.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/{BRIEF}`

## Raw Concept

K{k}: {e['verdict']} — arXiv {e['arxiv']}.

## Narrative

{e['narrative']}

## Snippets

> "See source page for arXiv {e['arxiv']} locators." [Source: CCC K{k} synthesis]
"""
    (REPO / "wiki/concepts" / f"{c}.md").write_text(body, encoding="utf-8")


def write_phase0(e: dict) -> None:
    k = e["k"]
    rule = "ccc-k376-k384-phase1-wires.mdc"
    checks = [f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"']
    if e["concept"]:
        checks += [
            f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
            f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        ]
    if e["wired"]:
        checks += [
            f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
            f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/{rule}"',
        ]
    slug = e["concept"] or e["slug"].split("-")[1]
    checks.append(f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{slug}"')
    script = f"""#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K{k} Phase-0 — ${{REPO_ROOT}}"
pass=0; fail=0; warn=0
check(){{ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }}
warn_note(){{ echo "  WARN  $1"; warn=$((warn+1)); }}
{chr(10).join(checks)}
warn_note "K{k} {e['verdict']}"
echo "Summary: ${{pass}} pass, ${{fail}} fail, ${{warn}} warn"
[[ "${{fail}}" -eq 0 ]]
"""
    p = REPO / "scripts" / f"adopt_k{k}_phase0.sh"
    p.write_text(script, encoding="utf-8")
    p.chmod(0o755)


def main() -> None:
    for e in ENTRIES:
        write_source(e)
        if e["concept"]:
            write_concept(e)
        write_phase0(e)
    print("done K376–K384")


if __name__ == "__main__":
    main()
