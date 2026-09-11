#!/usr/bin/env python3
"""Generate K346–K357 wiki ingest artifacts (sources, concepts, phase0 scripts)."""
from __future__ import annotations

import textwrap
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
WIKI = REPO / "wiki"
SCRIPTS = REPO / "scripts"
BRIEF = "2026-09-11_ccc-k346-k357-sip-ready.md"
DATE = "2026-09-11"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

ENTRIES = [
    {
        "k": 346,
        "arxiv": "2609.04894",
        "slug": "arxiv-world-acting-systems-taxonomy-2609.04894",
        "concept": "world-acting-systems-taxonomy",
        "title": "From Language Models to World-Acting Systems",
        "pdf": "arxiv-2609.04894-from-language-models-to-world-acting-systems-pro.pdf",
        "verdict": "ADOPT awareness",
        "narrative": (
            "Survey separates **model competence** from **system integration**, persistence, and safe authority "
            "across digital, social, virtual, and physical environments. CCC steal: do not conflate fluent outputs "
            "with governed world-acting — harness + broker + verification remain external (pairs K309/K325)."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 347,
        "arxiv": "2609.05314",
        "slug": "arxiv-hvac-llm-building-energy-2609.05314",
        "concept": None,
        "title": "LLMs for HVAC Operations in Building Energy Systems",
        "pdf": "arxiv-2609.05314-large-language-models-for-hvac-operations-in-bui.pdf",
        "verdict": "OOD stub",
        "narrative": (
            "Systematic review of 66 studies on LLMs for HVAC/building automation (2023–Mar 2026). "
            "Domain-specific building-energy OOD for CCC — short source stub only; `wont_wire`."
        ),
        "wired": False,
        "ood": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 348,
        "arxiv": "2609.05374",
        "slug": "arxiv-cua-universe-hybrid-gui-cli-2609.05374",
        "concept": "hybrid-gui-cli-agent-environment",
        "title": "CUA-Universe: Hybrid GUI+CLI Agent Environment",
        "pdf": "arxiv-2609.05374-cua-universe-a-scalable-and-dynamic-environment.pdf",
        "verdict": "ADOPT eval-first",
        "narrative": (
            "Real computer work is **hybrid GUI+CLI** over shared application state — GUI-only trajectories are inefficient. "
            "Scalable dynamic environment for hybrid agents. No public SPDX at Phase-0 → no clone. Eval runtime `wont_wire`. "
            "Pairs K321 ASIL structured actions / K286 multimodal harness awareness."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 349,
        "arxiv": "2609.05395",
        "slug": "arxiv-kopa-bench-korean-public-api-2609.05395",
        "concept": None,
        "title": "KOPA-Bench — Multi-Step Tool-Calling over Korean Open Public APIs",
        "pdf": "arxiv-2609.05395-multi-step-tool-calling-over-korean-open-public.pdf",
        "verdict": "OOD stub",
        "narrative": (
            "145-task benchmark for on-prem open-source agents chaining Korean government APIs. "
            "Locale/sovereignty-specific eval OOD for CCC — source stub; `wont_wire`."
        ),
        "wired": False,
        "ood": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 350,
        "arxiv": "2609.07360",
        "slug": "arxiv-scanning-harness-supply-chain-defects-2609.07360",
        "concept": "harness-supply-chain-defects",
        "title": "Scanning the Harness: Supply-Chain Defects in AI Coding-Agent Configurations",
        "pdf": "arxiv-2609.07360-scanning-the-harness-an-empirical-study-of-suppl.pdf",
        "verdict": "Cybersec-primary + ADOPT policy",
        "narrative": (
            "Coding-agent **harness artifacts** (CLAUDE.md, skills, hooks, MCP declarations, subagents) form an "
            "unvetted dependency layer from marketplaces/repos — no lockfile, no install-time check, developer privileges. "
            "Empirical supply-chain defect study. CCC: run cursor-security-preflight before third-party harness adoption; "
            "pairs K274 CDH trajectory audit + skill-vetting. **No PoCs.**"
        ),
        "wired": True,
        "ood": False,
        "cybersec": True,
        "no_clone": True,
    },
    {
        "k": 351,
        "arxiv": "2609.07370",
        "slug": "arxiv-edge-slm-mcp-tool-reliability-2609.07370",
        "concept": "edge-slm-mcp-tool-reliability",
        "title": "CPU Reliability Benchmark for MCP-Style Tool Calling in Sub-2B SLMs",
        "pdf": "arxiv-2609.07370-beyond-fluent-generation-a-cpu-reliability-bench.pdf",
        "verdict": "ADOPT eval axis",
        "narrative": (
            "Edge SLM agents on SBCs need **machine-readable JSON tool calls**, not fluent text alone. "
            "Reliability benchmark for MCP-style invocation on sub-2B models. Eval axis `policy_wired`; runtime `wont_wire`. "
            "Pairs K259 tool affordances / K296 terminal-state eval."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 352,
        "arxiv": "2609.07916",
        "slug": "arxiv-poisson-image-denoising-2609.07916",
        "concept": None,
        "title": "Poisson Image Denoising Using Minimax Concave Penalties",
        "pdf": "arxiv-2609.07916-poisson-image-denoising-using-minimax-concave-an.pdf",
        "verdict": "OOD stub",
        "narrative": (
            "Medical/astronomical Poisson noise image restoration — classical signal processing, not agent harness. "
            "OOD stub; optional `@image-gen-wiki` pointer only. `wont_wire`."
        ),
        "wired": False,
        "ood": True,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 353,
        "arxiv": "2609.10962",
        "slug": "arxiv-mcp-registry-random-sample-2609.10962",
        "concept": "mcp-registry-unbiased-sampling",
        "title": "What a Random Draw from the MCP Registry Contains",
        "pdf": "arxiv-2609.10962-what-a-random-draw-from-the-mcp-registry-contain.pdf",
        "verdict": "ADOPT eval/measurement",
        "narrative": (
            "Prior MCP ecosystem studies use repaired/curated samples. Unrepaired draw of 400/24,135 registry servers "
            "reveals coverage gap vs tool-use benchmarks. CCC: lazy-load + SCOUT top-k (K311) — never assume registry ≡ benchmark. "
            "Pairs K274 progressive disclosure."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 354,
        "arxiv": "2609.11117",
        "slug": "arxiv-agent-experiment-reproduction-nlpcc-2609.11117",
        "concept": "agent-experiment-reproduction-eval",
        "title": "NLPCC 2026 Shared Task 11: Agent-Based Experiment Reproduction",
        "pdf": "arxiv-2609.11117-overview-of-the-nlpcc-2026-shared-task-11-agent.pdf",
        "verdict": "ADOPT eval-first",
        "narrative": (
            "Agent task: reproduce scientific experiments from papers — eval beyond final repo snapshot, not ML-only. "
            "Pairs K280 Vero joint impl+proof eval / K281 meta-harness external eval contract. Runtime `wont_wire`."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 355,
        "arxiv": "2609.11677",
        "slug": "arxiv-ecdysis-runtime-harness-training-2609.11677",
        "concept": "runtime-harness-evolution-ecdysis",
        "title": "Ecdysis: Training Runtime Harnesses for LLM Agents",
        "pdf": "arxiv-2609.11677-ecdysis-efficient-and-effective-training-of-runt.pdf",
        "verdict": "ADOPT pattern",
        "narrative": (
            "Self-evolving **runtime harnesses** via iterative search + execution feedback on task instances. "
            "`cuiyu-ai/Ecdysis` null SPDX → no clone. Trainer `wont_wire`. **Never auto-evolve `.cursor/skills`.** "
            "Pairs K313 StarHarness stratified evolution / K162 external eval."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
        "repo": "cuiyu-ai/Ecdysis",
    },
    {
        "k": 356,
        "arxiv": "2609.11682",
        "slug": "arxiv-cobra-skills-bandit-evolution-2609.11682",
        "concept": "bandit-guided-skill-evolution",
        "title": "COBRA-Skills: Contextual Bandit-Guided Skill Optimization",
        "pdf": "arxiv-2609.11682-cobra-skills-contextual-bandit-guided-evolution.pdf",
        "verdict": "ADOPT policy",
        "narrative": (
            "Budgeted sequential optimization over evolving skill candidates — contextual bandit reduces costly "
            "execution-based eval. No public SPDX repo → policy only. **Never auto-evolve `.cursor/skills`.** "
            "Pairs K237 misevolution / K314 validation-gated skill memory."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
    {
        "k": 357,
        "arxiv": "2609.11911",
        "slug": "arxiv-artificial-id-persistent-alignment-2609.11911",
        "concept": "artificial-id-persistent-agent-drive",
        "title": "Artificial Id: Drive and Persistent Alignment in Agentic AI",
        "pdf": "arxiv-2609.11911-artificial-id-drive-and-persistent-alignment-in.pdf",
        "verdict": "ADOPT policy",
        "narrative": (
            "Persistent agents crossing task boundaries need an adaptive **internal drive** for objectives, retries, "
            "verification, and stopping — hand-specified harness transitions do not scale. Policy awareness only; "
            "runtime `wont_wire`. Pairs K327 Logos transcript boundaries / K309 Prime Agent continual harness."
        ),
        "wired": True,
        "ood": False,
        "cybersec": False,
        "no_clone": True,
    },
]


def yaml_list(items: list[str]) -> str:
    return "\n".join(f"  - {x}" for x in items)


def write_source(e: dict) -> None:
    k = e["k"]
    related = [f"briefs/{BRIEF}"]
    relations = [f"@briefs/{BRIEF}"]
    if e["concept"]:
        related.insert(0, f"concepts/{e['concept']}.md")
        relations.insert(0, f"@concepts/{e['concept']}.md")
    code_line = ""
    if e.get("repo"):
        code_line = f"| **Code** | `{e['repo']}` cited — **null SPDX** → no clone |\n"
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
{code_line}| **Retrieved** | {DATE} |

## Narrative

**Verdict: {e['verdict']}.**

{e['narrative']}

## Snippets

> "{e['title']} — CCC K{k} synthesis." [Source: arXiv {e['arxiv']} — paraphrase]

| **Location** | `{EGRESS}/{e['pdf']}` |
"""
    path = WIKI / "sources" / f"{e['slug']}.md"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {path.relative_to(REPO)}")


def write_concept(e: dict) -> None:
    c = e["concept"]
    k = e["k"]
    related = [
        f"sources/{e['slug']}.md",
        "concepts/phase1-adopt-wire.md",
        f"briefs/{BRIEF}",
    ]
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: concept
tags: [concept, k{k}]
keywords: [{e['arxiv']}, k{k}]
related:
{yaml_list(related)}
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

K{k}: {e['verdict']} — synthesized from arXiv {e['arxiv']}.

## Narrative

{e['narrative']}

## Snippets

> "See source page for arXiv {e['arxiv']} locators." [Source: CCC K{k} synthesis]
"""
    path = WIKI / "concepts" / f"{c}.md"
    path.write_text(body, encoding="utf-8")
    print(f"wrote {path.relative_to(REPO)}")


def write_phase0(e: dict) -> None:
    k = e["k"]
    checks = [
        f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"',
    ]
    if e["concept"]:
        checks.append(
            f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"'
        )
        checks.append(
            f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"'
        )
    else:
        stub = e["slug"].replace("arxiv-", "").rsplit("-2609", 1)[0]
        checks.append(
            f'check "no concept" test ! -f "${{REPO_ROOT}}/wiki/concepts/{stub}.md"'
        )
    if e["wired"]:
        checks.append(
            f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"'
        )
        checks.append(
            f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/ccc-k346-k357-phase1-wires.mdc"'
        )
    if e["no_clone"]:
        slug = e["concept"] or e["slug"].split("-")[1]
        checks.append(
            f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{slug}"'
        )
    if e["cybersec"]:
        src = f"${{REPO_ROOT}}/wiki/sources/{e['slug']}.md"
        con = f"${{REPO_ROOT}}/wiki/concepts/{e['concept']}.md"
        checks.append(
            f'check "no attack text" bash -c "! grep -rEi jailbreak|attack\\\\ prompt|exploit\\\\ template {src} {con}"'
        )
    warn = e["verdict"]
    script = f"""#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K{k} Phase-0 — ${{REPO_ROOT}}"
pass=0; fail=0; warn=0
check(){{ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }}
warn_note(){{ echo "  WARN  $1"; warn=$((warn+1)); }}
{chr(10).join(checks)}
warn_note "K{k} {warn}"
echo "Summary: ${{pass}} pass, ${{fail}} fail, ${{warn}} warn"
[[ "${{fail}}" -eq 0 ]]
"""
    path = SCRIPTS / f"adopt_k{k}_phase0.sh"
    path.write_text(script, encoding="utf-8")
    path.chmod(0o755)
    print(f"wrote {path.relative_to(REPO)}")


def main() -> None:
    for e in ENTRIES:
        write_source(e)
        if e["concept"]:
            write_concept(e)
        write_phase0(e)
    print("done — run phase1 rule + index updates separately")


if __name__ == "__main__":
    main()
