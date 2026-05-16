# CCC — Cemini Claude Code Wiki

Local-only knowledge hub on **how Cemini operates Claude Code** — agent orchestration, context/token economics, MCP servers, hooks, skills, slash commands, and the `/goal` · Ralph · OpenSpec prompting patterns.

Fifth sibling of the Cemini wiki federation alongside `osint-wiki`, `cybersecurity-wiki`, `image-gen-wiki`, `seo-wiki`, `3d-printing-wiki`.

## Quickstart

```bash
# Lint the wiki
python3 scripts/wiki_lint.py

# Check inbox for duplicates before ingesting
python3 scripts/preingest_check.py
```

Read `CLAUDE.md` for the full schema (LLM-facing). Active workstreams live in `ROADMAP.md`. Meta-lessons live in `LESSONS.md`. Session state lives in `hot.md` (gitignored).

## Structure

- `wiki/` — canonical wiki (markdown + YAML frontmatter)
- `scripts/` — `wiki_lint.py`, `preingest_check.py`
- `briefs/` — staged deliverables (gitignored)
- `raw-sources/` — archived source corpus (gitignored)
- `research to be indexed/` — transient drop zone (gitignored)
- `prompts/` — reusable prompt templates

## Adding content

1. Drop new source into `research to be indexed/`
2. `python3 scripts/preingest_check.py`
3. Read, discuss, then create `wiki/sources/<slug>.md` + touch related entity/concept pages
4. Update `wiki/index.md` + append to `wiki/log.md`
5. Move file to `raw-sources/`
6. `python3 scripts/wiki_lint.py` — fix any errors

Full ingest workflow in `CLAUDE.md` § Operations.

## Cross-wiki

This is one of **six** interconnected Cemini wikis. Use `@<wiki-alias>/path/to/page.md` to link into a sibling wiki; the lint script resolves cross-wiki paths against the `Related Wikis` table in `CLAUDE.md`. Bidirectional — every outbound cross-wiki link needs a backlink on the target side.

- `osint-wiki` — financial / quant / prediction-market research · **private (not publicly available)**
- `image-gen-wiki` — uncensored image / video / voice generation
- `seo-wiki` — local SEO, GBP, GEO/AEO, creator marketing
- `3d-printing-wiki` — FDM/FFF printing, Bambu, slicers, print farms
- `cybersecurity-wiki` — offensive / defensive security research
- `ccc-wiki` — this wiki (Cemini Claude Code meta-wiki) · **private (not publicly available)**

The OSINT and CCC wikis are private repositories — not publicly available.

## License

Personal workspace. No license — not for distribution.
