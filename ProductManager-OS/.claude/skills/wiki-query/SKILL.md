---
name: wiki-query
description: Synthesize an answer from the Knowledge wiki across multiple pages, cite sources inline, file good answers back as new wiki pages. Trigger on "/wiki-query <question>", "what does the wiki say about", "synthesize from the wiki", "knowledge query". Implements the Query op of the Karpathy LLM-wiki gist — explorations compound like ingested sources.
---

# Wiki query — `/wiki-query <question>`

**Voice:** Oracle. Three signals beat twelve. Refuses to assert without a wiki citation.

## What this skill does

Answers a question by synthesizing across the wiki. Crucially, every good answer is **filed back as a new wiki page** — explorations compound like ingested sources. This is the difference between "asking an LLM" and "growing a knowledge base."

## Preconditions

- `Knowledge/index.md` exists (`/wiki-ingest` has run at least once, or bootstrap from index template).
- The question is specific enough to anchor on entities or concepts. If too broad, ask for narrowing before searching.

## Step-by-step

### 1. Decompose the question
Break the question into 2–5 sub-queries, each anchored on an entity or concept that should exist in the wiki. Print the decomposition before searching.

### 2. Search the wiki
For each sub-query:
- Identify the candidate page(s) in `Knowledge/` (use `index.md` first, then targeted `Grep` if needed).
- Read the relevant sections.
- Note: page path, the exact passage cited, and the "Last verified" date.

If a sub-query has no answer in the wiki, surface it as a **gap** — do not improvise from outside knowledge. Suggest `/wiki-ingest` for the missing source.

### 3. Synthesize
Compose the answer with:
- A 2–4 sentence headline answer.
- A bulleted reasoning chain, each bullet citing a wiki page (path) and a verbatim phrase or fact.
- An "Unknowns" section listing what the wiki cannot answer yet.
- A "Stale check" flag if any cited page has `Last verified` > 90 days old.

### 4. File the answer back
If the answer is non-trivial (≥ 3 sources, or surfaces a synthesis not previously written down), file it as a new page under `Knowledge/Concepts/<slug>.md` with:
- The headline answer
- The reasoning chain (citations preserved)
- Back-links to every page cited
- Date authored, "Last verified" = today

Add the row to `Knowledge/index.md` and append to `Knowledge/log.md`:

```
| <UTC date> | query-filed | Concepts/<slug>.md | <user question> | <one-line synthesis> |
```

If the answer is trivial (single citation, no synthesis), do NOT file — that's noise. Just answer.

## Output format

```
## Wiki query — <question>

**Headline:** <2–4 sentences>

**Reasoning:**
- <claim> — `Knowledge/<path>` "<verbatim phrase>" (verified <date>)
- ...

**Unknowns (gaps in the wiki):**
- <gap> — suggest `/wiki-ingest <source candidate>`

**Stale citations (verify before relying on these):**
- `Knowledge/<path>` — last verified <date>, > 90 days old

**Filed as:** `Knowledge/Concepts/<slug>.md` (or "not filed — trivial single-source answer")
```

## Anti-patterns

- Answering from outside knowledge without flagging "(not in wiki)" — Riddler will block downstream artifacts that lean on this
- Filing every answer as a new page (signal-to-noise collapse; only file the synthesis-grade ones)
- Citing a page without quoting from it (no provenance)
- Skipping the stale-check (wiki rot creeps in silently)

## References

- [Knowledge/index.md](../../../Knowledge/index.md)
- Karpathy LLM-wiki gist — Query is op #2 of 4; "explorations compound"
- `wiki-ingest`, `wiki-lint`, `wiki-maintain` — sister ops
