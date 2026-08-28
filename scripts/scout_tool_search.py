#!/usr/bin/env python3
"""SCOUT tool-search (CCC K311 leftover, shipped 2026-08-28).

Operator-invoked federation helper: index LOCAL .cursor/skills/*/SKILL.md
frontmatter (name + description, plus one line from the body's first heading)
and return keyword / term-overlap top-k (k~=5). 'execute' means READ that
SKILL.md -- never a live MCP invoke, never a catalog dump.

Usage:
  python3 scripts/scout_tool_search.py query <terms...> [-k 5]
  python3 scripts/scout_tool_search.py read <skill-name>   # prints the SKILL.md path
  python3 scripts/scout_tool_search.py selftest
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = REPO_ROOT / ".cursor" / "skills"

STOP = {
    "the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with",
    "use", "using", "when", "how", "what", "that", "this", "is", "are", "it",
}


def _tokens(text: str) -> Counter:
    return Counter(
        w for w in re.findall(r"[a-z0-9][a-z0-9\-_]{1,}", text.lower()) if w not in STOP
    )


def _parse_frontmatter(text: str) -> dict:
    fm: dict[str, str] = {}
    m = re.match(r"^---\n(.*?)\n---", text, re.S)
    if not m:
        return fm
    lines = m.group(1).splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if ":" in line and not line.lstrip().startswith("-"):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val in (">", ">-", "|", "|-"):
                # YAML block scalar: fold following indented lines
                block = []
                i += 1
                while i < len(lines) and (lines[i].startswith(" ") or lines[i].strip() == ""):
                    block.append(lines[i].strip())
                    i += 1
                fm[key] = " ".join(x for x in block if x)
                continue
            fm[key] = val.strip('"').strip("'")
        i += 1
    return fm


def _first_heading_line(text: str) -> str:
    m = re.search(r"^#+\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def index_skills(skills_dir: Path | None = None) -> list[dict]:
    base = skills_dir or SKILLS_DIR
    out = []
    if not base.is_dir():
        return out
    for sk in sorted(base.iterdir()):
        f = sk / "SKILL.md"
        if not f.is_file():
            continue
        raw = f.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(raw)
        name = fm.get("name") or sk.name
        desc = fm.get("description") or ""
        # description may be a YAML block scalar (>-) -- keep first line if long
        desc_one = " ".join(desc.split())[:300]
        out.append(
            {
                "name": name,
                "path": str(f.relative_to(REPO_ROOT)),
                "desc": desc_one,
                "heading": _first_heading_line(raw)[:120],
                "text": f"{name} {desc_one} {_first_heading_line(raw)}",
            }
        )
    return out


def score(sk: dict, query: Counter, q_total: int) -> tuple[float, str]:
    text_l = sk["text"].lower()
    sk_tok = _tokens(sk["text"])
    overlap = sum(min(query[w], sk_tok[w]) for w in query)
    # substring fallback: query token contained in a description word (e.g. "git" in "GitHub")
    sub = sum(1 for w in query if w in text_l)
    if q_total == 0:
        return 0.0, "empty query"
    cov = max(overlap, sub * 0.5) / q_total
    if overlap:
        return cov, "term-overlap with query"
    if sub:
        return cov, "substring match in description"
    return 0.0, "no shared terms"


def search(terms: list[str], k: int = 5) -> list[dict]:
    query = _tokens(" ".join(terms))
    q_total = sum(query.values())
    ranked = []
    for sk in index_skills():
        s, why = score(sk, query, q_total)
        if s > 0:
            ranked.append({"name": sk["name"], "path": sk["path"], "score": round(s, 3), "why": why, "desc": sk["desc"]})
    ranked.sort(key=lambda r: (-r["score"], r["name"]))
    return ranked[:k]


def cmd_search(args: argparse.Namespace) -> int:
    if not args.terms:
        print("query terms required", file=sys.stderr)
        return 2
    for r in search(args.terms, args.k):
        print(f"{r['score']:.3f}  {r['name']:<28} {r['path']}")
        print(f"        why: {r['why']} | {r['desc'][:110]}")
    return 0


def cmd_read(args: argparse.Namespace) -> int:
    for sk in index_skills():
        if sk["name"].lower() == args.name.lower():
            print(sk["path"])
            return 0
    print(f"no skill named '{args.name}'", file=sys.stderr)
    return 1


def selftest() -> int:
    skills = index_skills()
    fed = 0
    for s in skills:
        raw = (REPO_ROOT / s["path"]).read_text(encoding="utf-8", errors="replace")
        if re.search(r"^federation:\s*true", raw, re.M):
            fed += 1
    if fed < 3:
        raise SystemExit(f"selftest FAIL: expected >=3 federation skills, found {fed}")
    res = search(["route"])
    if not any(r["name"].lower() == "route" for r in res):
        names = [r["name"] for r in res]
        raise SystemExit(f"selftest FAIL: query 'route' did not return the route skill ({names})")
    # query must prefer a match over nothing
    empty = search(["zzzzzzzz"])
    if empty:
        raise SystemExit(f"selftest FAIL: non-empty result for nonsense query ({empty})")
    print(f"selftest PASS: {len(skills)} skills indexed; {fed} federation; 'route' in top-k")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    q = sub.add_parser("query", help="top-k skill search")
    q.add_argument("terms", nargs="+")
    q.add_argument("-k", type=int, default=5)
    q.set_defaults(fn=cmd_search)
    r = sub.add_parser("read", help="print path of a SKILL.md to read")
    r.add_argument("name")
    r.set_defaults(fn=cmd_read)
    s = sub.add_parser("selftest", help="run selftest")
    s.set_defaults(fn=lambda _a: selftest())
    args = ap.parse_args()
    try:
        return int(args.fn(args))
    except SystemExit as e:
        code = e.code
        if isinstance(code, int):
            return code
        print(code, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
