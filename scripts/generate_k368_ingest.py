#!/usr/bin/env python3
"""Generate K368 wiki ingest artifacts (single paper)."""
from __future__ import annotations

from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
DATE = "2026-09-17"
BRIEF = "2026-09-17_ccc-k368-sip-ready.md"
EGRESS = "cemini-egress-fi:/opt/cemini-bulk/research/ccc"

E = {
    "k": 368,
    "arxiv": "2609.18217",
    "slug": "arxiv-implicit-trust-mcp-tool-calling-2609.18217",
    "concept": "implicit-trust-mcp-input-channels",
    "title": "Measuring Implicit Trust in LLM Tool-Calling Pipelines",
    "pdf": "arxiv-2609.18217-measuring-exploiting-implicit-trust-tool-calling.pdf",
    "verdict": "Cybersec-primary + ADOPT policy",
    "narrative": (
        "MCP tool interactions expose models to attacker-controlled text via **multiple input channels** "
        "(tool descriptions, tool results, sampling messages) in one **shared context window without privilege "
        "separation**. Framework measures per-model **trust profiles** across channel/payload framings; "
        "cross-channel fragmentation can reassemble harmful intent from benign-looking pieces. CCC steal: "
        "**channel-aware trust measurement** + external enforcement — not model self-arbitration (pairs K310 "
        "pre-auth intent / K326 recognition≠enforcement / K365 session privacy / K274 CDH). "
        "**No PoCs, no attack templates, no fragmentation recipes anywhere.** Runtime **`wont_wire`**."
    ),
}


def main() -> None:
    related = [f"concepts/{E['concept']}.md", f"briefs/{BRIEF}"]
    source = f"""---
title: "{E['title']} (CCC K368)"
type: source
tags: [source, arxiv, k368, cybersec, mcp]
keywords: [{E['arxiv']}, implicit trust, mcp, tool-calling, k368]
related:
  - concepts/{E['concept']}.md
  - briefs/{BRIEF}
maturity: draft
read_status: read
created: {DATE}
updated: {DATE}
---

## Relations

- `@concepts/{E['concept']}.md`
- `@briefs/{BRIEF}`

## Raw Concept

| Field | Value |
|-------|-------|
| **Title** | {E['title']} |
| **arXiv** | {E['arxiv']} (2026-09) |
| **Retrieved** | {DATE} |

## Narrative

**Verdict: {E['verdict']}.**

{E['narrative']}

## Snippets

> "Shared MCP context lacks privilege separation across tool description, result, and sampling channels." [Source: arXiv {E['arxiv']} — paraphrase]

| **Location** | `{EGRESS}/{E['pdf']}` |
"""
    concept = f"""---
title: "{E['title']} (CCC K368)"
type: concept
tags: [concept, k368, cybersec, mcp, implicit-trust]
keywords: [{E['arxiv']}, implicit trust, mcp channels, k368]
related:
  - sources/{E['slug']}.md
  - concepts/phase1-adopt-wire.md
  - briefs/{BRIEF}
maturity: draft
wire_status: policy_wired
wire_target: ".cursor/rules/cemini-phase1-policy-wires.mdc"
created: {DATE}
updated: {DATE}
---

## Relations

- `@sources/{E['slug']}.md`
- `@concepts/phase1-adopt-wire.md`
- `@briefs/{BRIEF}`

## Raw Concept

K368: MCP tool-calling **implicit trust** across undifferentiated input channels.

## Narrative

{E['narrative']}

## Snippets

> "Measure trust per channel; enforce externally — do not rely on model refusal alone." [Source: CCC K368 synthesis]
"""
    phase0 = f"""#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
echo "K368 Phase-0 — ${{REPO_ROOT}}"
pass=0; fail=0; warn=0
check(){{ local l="$1"; shift; if "$@"; then echo "  PASS  $l"; pass=$((pass+1)); else echo "  FAIL  $l"; fail=$((fail+1)); fi; }}
warn_note(){{ echo "  WARN  $1"; warn=$((warn+1)); }}
check "source" test -f "${{REPO_ROOT}}/wiki/sources/{E['slug']}.md"
check "concept" test -f "${{REPO_ROOT}}/wiki/concepts/{E['concept']}.md"
check "concept wired" grep -q "wire_status: policy_wired" "${{REPO_ROOT}}/wiki/concepts/{E['concept']}.md"
check "policy K368" grep -q "K368" "${{REPO_ROOT}}/.cursor/rules/cemini-phase1-policy-wires.mdc"
check "ccc-rule K368" grep -q "K368" "${{REPO_ROOT}}/.cursor/rules/ccc-k368-phase1-wires.mdc"
check "no clone" test ! -d "${{REPO_ROOT}}/.local/adopts/implicit-trust-mcp"
check "no attack text" bash -c "! grep -rEi 'jailbreak|attack prompt|exploit template|fragmentation attack' '${{REPO_ROOT}}/wiki/sources/{E['slug']}.md' '${{REPO_ROOT}}/wiki/concepts/{E['concept']}.md'"
warn_note "K368 Cybersec-primary — implicit trust across MCP channels; policy only; no PoCs."
echo "Summary: ${{pass}} pass, ${{fail}} fail, ${{warn}} warn"
[[ "${{fail}}" -eq 0 ]]
"""
    (REPO / "wiki/sources" / f"{E['slug']}.md").write_text(source, encoding="utf-8")
    (REPO / "wiki/concepts" / f"{E['concept']}.md").write_text(concept, encoding="utf-8")
    p0 = REPO / "scripts/adopt_k368_phase0.sh"
    p0.write_text(phase0, encoding="utf-8")
    p0.chmod(0o755)
    print("wrote K368 artifacts")


if __name__ == "__main__":
    main()
