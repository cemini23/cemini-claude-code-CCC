#!/usr/bin/env python3
"""Discover LLM API keys for super-audit API leg (masked output).

Usage:
  python3 discover_api_keys.py
  python3 discover_api_keys.py --json
  python3 discover_api_keys.py --workspace /path/to/project
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Env vars we care about for API auditors
KEY_VARS = (
    "OPENROUTER_API_KEY",
    "DEEPSEEK_API_KEY",
    "ADVISOR_API_KEY",
    "ANTHROPIC_API_KEY",
    "OPENAI_API_KEY",
)
URL_VARS = (
    "OPENROUTER_BASE_URL",
    "DEEPSEEK_BASE_URL",
    "ADVISOR_BASE_URL",
    "DEEPSEEK_MODEL",
    "ADVISOR_MODEL",
)


def _mask(value: str) -> str:
    v = value.strip()
    if len(v) <= 8:
        return "***"
    return f"{v[:6]}…{v[-4:]}"


def _load_env_file(path: Path) -> dict[str, str]:
    out: dict[str, str] = {}
    if not path.is_file():
        return out
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        k, v = k.strip(), v.strip().strip('"').strip("'")
        if k:
            out[k] = v
    return out


def _candidate_files(workspace: Path) -> list[Path]:
    custom = os.environ.get("CEMINI_LLM_ROUTING_ENV", "").strip()
    paths: list[Path] = []
    if custom:
        paths.append(Path(custom))
    paths.extend(
        [
            Path.home() / ".cemini" / "llm-routing.env",
            workspace / ".env",
            workspace / "config" / "llm-routing.env",
        ]
    )
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in paths:
        rp = p.resolve() if p.is_absolute() or str(p).startswith("~") else p
        if str(p).startswith("~"):
            rp = Path(str(p).replace("~", str(Path.home())))
        if rp in seen:
            continue
        seen.add(rp)
        unique.append(rp)
    return unique


def discover(workspace: Path) -> dict:
    merged: dict[str, str] = {}
    sources: list[str] = []
    for f in _candidate_files(workspace):
        if not f.is_file():
            continue
        chunk = _load_env_file(f)
        if not chunk:
            continue
        sources.append(str(f))
        for k, v in chunk.items():
            if k not in merged and v:
                merged[k] = v

    # OS env overrides file (already in process env)
    for k in KEY_VARS + URL_VARS:
        if os.environ.get(k, "").strip():
            merged[k] = os.environ[k].strip()

    keys: dict[str, dict] = {}
    for k in KEY_VARS:
        val = merged.get(k, "").strip()
        keys[k] = {"present": bool(val), "masked": _mask(val) if val else None}

    urls = {k: merged.get(k) for k in URL_VARS if merged.get(k)}

    # Suggest default API slots
    suggestions: list[dict] = []
    if keys["OPENROUTER_API_KEY"]["present"]:
        suggestions.append(
            {
                "label": "grok-4.3-openrouter",
                "model": "x-ai/grok-4.3",
                "api_key_env": "OPENROUTER_API_KEY",
                "base_url_env": "OPENROUTER_BASE_URL",
            }
        )
    if keys["ADVISOR_API_KEY"]["present"] or (
        keys["OPENROUTER_API_KEY"]["present"] and merged.get("ADVISOR_MODEL")
    ):
        suggestions.append(
            {
                "label": "advisor",
                "model": merged.get("ADVISOR_MODEL", "google/gemini-2.5-flash"),
                "api_key_env": "ADVISOR_API_KEY"
                if keys["ADVISOR_API_KEY"]["present"]
                else "OPENROUTER_API_KEY",
                "base_url_env": "ADVISOR_BASE_URL"
                if merged.get("ADVISOR_BASE_URL")
                else "OPENROUTER_BASE_URL",
            }
        )
    if keys["DEEPSEEK_API_KEY"]["present"]:
        suggestions.append(
            {
                "label": "deepseek-reasoner",
                "model": "deepseek-reasoner",
                "api_key_env": "DEEPSEEK_API_KEY",
                "base_url_env": "DEEPSEEK_BASE_URL",
            }
        )
        suggestions.append(
            {
                "label": "deepseek-v4-flash",
                "model": merged.get("DEEPSEEK_MODEL", "deepseek-v4-flash"),
                "api_key_env": "DEEPSEEK_API_KEY",
                "base_url_env": "DEEPSEEK_BASE_URL",
            }
        )

    ready = keys["OPENROUTER_API_KEY"]["present"] or keys["DEEPSEEK_API_KEY"]["present"]
    return {
        "workspace": str(workspace.resolve()),
        "sources_loaded": sources,
        "keys": keys,
        "urls": urls,
        "suggested_api_slots": suggestions[:2],
        "api_leg_ready": ready,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Workspace root for .env discovery",
    )
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    result = discover(args.workspace)
    if args.json:
        print(json.dumps(result, indent=2))
        return 0 if result["api_leg_ready"] else 1

    print(f"workspace: {result['workspace']}")
    if result["sources_loaded"]:
        print("sources:")
        for s in result["sources_loaded"]:
            print(f"  - {s}")
    else:
        print("sources: (none — copy config/llm-routing.env.example → ~/.cemini/llm-routing.env)")

    print("\nkeys:")
    for k, info in result["keys"].items():
        status = info["masked"] if info["present"] else "missing"
        print(f"  {k}: {status}")

    if result["urls"]:
        print("\nurls/models:")
        for k, v in result["urls"].items():
            print(f"  {k}: {v}")

    print("\nsuggested API slots (pick 2 in auditors.json):")
    for s in result["suggested_api_slots"]:
        print(f"  - {s['label']}: {s['model']} ({s['api_key_env']})")

    print(f"\napi_leg_ready: {result['api_leg_ready']}")
    return 0 if result["api_leg_ready"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
