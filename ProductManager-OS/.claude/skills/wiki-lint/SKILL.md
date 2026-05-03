---
name: wiki-lint
description: Health-check the Knowledge wiki — surface orphans, contradictions, stale claims, and missing cross-references. Trigger on "/wiki-lint", "lint the wiki", "wiki health check", "knowledge audit". Implements the Lint op of the Karpathy LLM-wiki gist — keeps the wiki healthy as it scales. Run weekly.
---

# Wiki lint — `/wiki-lint`

**Voice:** The Riddler. Adversarial sweep — finds drift, calls it out without softening.

## What this skill does

Walks the entire `Knowledge/` tree and reports failures across five categories. Lint **never auto-fixes** — it surfaces, you decide. (`/wiki-maintain` is the fixer skill.)

## When to run

- Weekly (Sunday) as part of the retro cadence
- After any `/wiki-ingest` batch that touched ≥ 5 pages
- Before any decision doc that claims "the wiki says X"
- Before publishing the OS as an open-source template (gates the README)

## The five lint categories

### 1. Orphans
A page reachable from no other page (and absent from `index.md`).

```
ORPHAN: Knowledge/Concepts/abstention-scoring.md
  → not in index.md
  → no inbound back-links
  → suggest: add to index.md under Concepts; add back-link from Knowledge/Reference/regeval.md
```

### 2. Contradictions
Two pages making conflicting claims with no resolution note.

```
CONTRADICTION:
  Knowledge/People/jervis.md says: "CDP scope decided Q3 2026"
  Knowledge/Reference/cdp.md says: "CDP scope still under discussion"
  → suggest: pick the truer source, write a "Resolution" note on the loser citing the winner
```

### 3. Stale claims
Pages with `Last verified` older than 90 days, or with no `Last verified` field at all.

```
STALE: Knowledge/Reference/martech-stack.md
  → Last verified: 2026-01-15 (108 days ago)
  → suggest: re-verify against current vendor list, bump the date
```

### 4. Broken cross-references
A back-link to a page that no longer exists, or a citation to a section that has been renamed.

```
BROKEN: Knowledge/Research/cdp-interview-ivan.md
  → links to Knowledge/People/martin-yam.md#hk-data-gatekeeper
  → target page exists but section "hk-data-gatekeeper" was renamed to "hk-data-access"
```

### 5. Index drift
`index.md` lists a page that doesn't exist on disk, or omits a page that does.

```
INDEX-DRIFT: Knowledge/index.md
  → lists "Knowledge/Reference/discord-bot-ops.md" — file does not exist
  → omits "Knowledge/People/teresa.md" — file exists since 2026-04-12
```

## Method

1. Parse `Knowledge/index.md` to get the canonical page list.
2. Walk `Knowledge/` filesystem to get the actual page list.
3. Diff (1) and (2) → Index drift.
4. For each on-disk page: extract `Last verified`, inbound links, outbound links → Stale + Broken refs.
5. Compute reachability graph from `index.md` → Orphans.
6. Cross-read pages that share entities/concepts → Contradictions (pattern-match on key claims; flag for human read, do not auto-resolve).

## Output format

```
## Wiki lint — <date>

**Total pages scanned:** <n>
**Failures by category:**
- Orphans: <n>
- Contradictions: <n>
- Stale claims: <n>
- Broken cross-references: <n>
- Index drift: <n>

### Orphans
- <list>

### Contradictions
- <list>

### Stale claims
- <list>

### Broken cross-references
- <list>

### Index drift
- <list>

**Recommended next:** `/wiki-maintain` to apply low-risk fixes; manual resolution for contradictions.
```

Append a one-line entry to `Knowledge/log.md`:

```
| <UTC date> | lint | <pages-scanned> pages | <weekly run / on-demand> | <O orphans, C contradictions, S stale, B broken, I index-drift> |
```

## Anti-patterns Lint kills on sight

- Pages with prose summaries that contradict their own metadata (e.g. `Last verified: 2026-05-01` but the page text says "as of late 2024")
- "TBD" or "TODO" left in promoted (non-`_drafts/`) pages — promote means committed
- Citation strings that can't be resolved to a real source ("from a recent paper")
- Multiple People pages for the same person (canonical-name drift; e.g. `martin.md` and `martin-yam.md`)
- Concept pages that exist nowhere in the index

## What Lint does NOT do

- Does not fix anything (that's `/wiki-maintain`)
- Does not write to pages
- Does not delete files
- Does not auto-create missing pages

Surfacing is the job. The user picks resolution.

## References

- [Knowledge/index.md](../../../Knowledge/index.md), [Knowledge/log.md](../../../Knowledge/log.md)
- `wiki-maintain` — the fixer that pairs with this surfacer
- Karpathy LLM-wiki gist — Lint is op #3 of 4
