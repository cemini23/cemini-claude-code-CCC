#!/usr/bin/env python3
"""Generate K395 wiki ingest (Agent Approval Laundering)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-25"
BRIEF = "2026-09-25_ccc-k395-agent-approval-laundering-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"
RULE = "ccc-k395-phase1-wires.mdc"

ENTRY = {
    "arxiv": "2609.28586",
    "concept": "agent-approval-laundering-transitive-effects",
    "k": 395,
    "narrative": "**Agent approval laundering** — a user- or policy-**approved** tool invocation can still cause **transitive** "
    "effects outside the approved action envelope (follow-on tools, side channels, delegated sub-agents). "
    "Authorization at the **first hop** is not **effect closure** (pairs K310 pre-auth intent / K302 AID-Guard / K333 "
    "untrusted-model delegation). **Cybersec-primary**; **No PoCs / no exploit recipes.** No clone. Runtime **`wont_wire`**; "
    "concept **`policy_wired`**.",
    "pdf": "arxiv-2609.28586-agent-approval-laundering-transitive-effects.pdf",
    "slug": "arxiv-agent-approval-laundering-2609.28586",
    "title": "Agent Approval Laundering: Transitive Effects Beyond the Approved Invocation",
    "verdict": "Cybersec-primary ADOPT policy",
    "wired": True,
}


def write_source(e: dict) -> None:
    k = e["k"]
    body = f"""---
title: "{e['title']} (CCC K{k})"
type: source
tags: [source, k{k}, cybersec]
keywords: [{e['arxiv']}, k{k}, approval-laundering]
related:
  - concepts/{e['concept']}.md
  - concepts/phase1-adopt-wire.md
  - briefs/{BRIEF}
maturity: draft
read_status: skimmed
created: {DATE}
updated: {DATE}
---

## Relations

- `@concepts/{e['concept']}.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/{BRIEF}`

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
tags: [concept, k{k}, cybersec]
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
    checks = [
        f'check "source" test -f "${{REPO_ROOT}}/wiki/sources/{e["slug"]}.md"',
        f'check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{e["concept"]}.md"',
        f'check "policy K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"',
        f'check "ccc-rule K{k}" grep -q "K{k}" "${{REPO_ROOT}}/.cursor/rules/{RULE}"',
        f'check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/{e["concept"]}"',
    ]
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
    write_source(ENTRY)
    write_concept(ENTRY)
    write_phase0(ENTRY)
    print("done K395")


if __name__ == "__main__":
    main()
