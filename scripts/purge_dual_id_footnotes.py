#!/usr/bin/env python3
"""Replace **Dual-ID:** blocks in CCC k* rules with one-line ID policy."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES = ROOT / ".cursor/rules"
REPL = "**IDs:** Resolve by arXiv id / slug / file path — K# is a log batch label only.\n"
PATTERNS = [
    re.compile(r"\n\*\*Dual-ID:\*\*[^\n]*\n(?:[^\n#][^\n]*\n?)*", re.M),
    re.compile(r"\n\*\*Dual-ID \(resolve[^\n]*\n(?:[^\n#][^\n]*\n?)*", re.M),
    re.compile(r"\n\*\*Dual-ID note:\*\*[^\n]*\n", re.M),
]


def main() -> int:
    changed = 0
    for path in sorted(RULES.glob("*.mdc")):
        text = path.read_text(encoding="utf-8")
        if "Dual-ID" not in text:
            continue
        new = text
        for pat in PATTERNS:
            new = pat.sub("\n" + REPL, new)
        # Inline trailing Dual-ID clauses on same line — shorten to arXiv ref only
        new = re.sub(
            r"\.\s+\*\*Dual-ID:\*\*[^.\n]+",
            ". Resolve by arXiv id / slug.",
            new,
        )
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
            print(path.name)
    print(f"changed {changed} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
