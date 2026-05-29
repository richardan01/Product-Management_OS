---
name: wiki-ingest
description: Ingest a new source into the Knowledge wiki — read, summarize, file under the right entity/concept, update index and log. Trigger on "/wiki-ingest <path-or-url>", "ingest this", "file this in the wiki", "add this to knowledge". Implements the Ingest op of the Karpathy LLM-wiki gist.
---

# Wiki ingest — `/wiki-ingest <source>`

**Voice:** Citation-disciplined, "as of <date>", refuses to assert without source.

## What this skill does

Takes a single new source (file path or URL) and threads it into the Knowledge wiki. One source typically touches 5–15 pages: a primary summary page, plus updates to existing entity/concept pages where the source corroborates, contradicts, or extends them.

This is the only sanctioned way to add content to `Knowledge/`. Direct file creation outside this skill bypasses index + log discipline and will be flagged by `/wiki-lint`.

## Preconditions

1. `Knowledge/index.md` and `Knowledge/log.md` exist (bootstrap-on-first-run if not).
2. The source is readable: a local file path **or** a public URL.
3. If the source is a transcript, the interviewees are already entries in `Knowledge/People/` — if not, surface and confirm before ingesting.

## Two-stage model: staging vs. promotion

Ingestion is **not** promotion. The agent proposes; the PM decides what becomes durable knowledge.

- **Stage 1 (automatic):** Raw artifact → `Knowledge/Source/` (immutable copy) + staging note → `Knowledge/Ingestion/`
- **Stage 2 (PM judgment):** PM reviews the staging note and approves promotion to durable layers (Research, Hypotheses, Decisions, People)

This prevents the ingestion backlog from polluting the durable layer and keeps the brain's signal-to-noise ratio high.

## Step-by-step

### 1. Archive the source
- Copy (never move) the raw artifact to `Knowledge/Source/<YYYY-MM-DD>-<slug>.<ext>`. This file is **immutable** — never edit it.
- If the source is a URL, save a markdown snapshot.

### 2. Read and stage
- Read the full source. Do not skim.
- Extract: title, author/source name, capture date, type (transcript / paper / article / brief / spec / other).
- Create a staging note at `Knowledge/Ingestion/<YYYY-MM-DD>-<slug>.md` with:
  - Source reference (path to `Knowledge/Source/`)
  - Provenance tag for each extracted claim (see `Knowledge/Reference/provenance-tags.md`)
  - Top 3 takeaways with verbatim quote + source line/timestamp
  - Candidate hypotheses surfaced (link to `Knowledge/Hypotheses/candidate/` if relevant)
  - Open questions raised

### 3. Identify touch-points
List every durable page this source corroborates, contradicts, or extends:
- New page needed — file path under `People/`, `Reference/`, `Research/`, `Hypotheses/candidate/`, or `Concepts/`
- Existing page to update — file path + which section + proposed delta
- **Contradiction detected** — name both claims with their provenance tags; do NOT merge
- Index entry (always one new row)

### 4. Draft the primary summary page
Under `Knowledge/Research/` (for transcripts/paper digests) or `Knowledge/Reference/` (for canonical domain docs), draft a page with:
- One-paragraph TL;DR
- Top 3 takeaways with verbatim quote + provenance tag + source line/timestamp
- Minority signals: contradicting evidence from this source
- Open questions surfaced
- Back-links: `## Related` section listing the touched pages

### 5. Confirm with user
Print:
- Primary page draft path + 3 takeaways
- List of touched pages with the proposed delta on each
- Any contradictions detected (surface both sides)
- Any candidate hypotheses seeded
- One-line summary for `log.md`

Wait for explicit go-ahead before any write outside `Ingestion/` and `Source/`.

### 6. Apply
- Move the draft from `Ingestion/` staging to its final location.
- Apply each delta (insert sections, add citations with provenance tags, update "Last verified").
- Add the new row to `Knowledge/index.md` under the correct rubric with lifecycle state.
- Append a row to `Knowledge/log.md`.
- If candidate hypotheses were created, confirm they are filed in `Knowledge/Hypotheses/candidate/`.

## Output format

```
## Wiki ingest — <source>

**Primary page:** Knowledge/<path>
**Touch-points:** <n> pages
- [path] — <delta>

**Top 3 takeaways:**
1. <takeaway> — "<verbatim quote>" (source: <line/page>)
2. ...
3. ...

**Open questions raised:**
- <question>

**Log entry:** <one-line>

**Confirm to apply, or revise framing.**
```

## Anti-patterns

- Filing under `Knowledge/` without a back-link to the source (orphan; Lint failure)
- Summarizing without quoting (loses provenance)
- Skipping the user-confirm step
- Adding to existing pages without recording the delta in `log.md`
