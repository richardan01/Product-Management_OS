# Knowledge index

**Owner:** Oracle (canonical bookkeeping) · **Schema:** Karpathy LLM-wiki — Ingest / Query / Lint / Maintain.
**Rule:** every page in `Knowledge/` is reachable from this index in ≤ 2 hops. Orphans are a Lint failure.

## How this index works

The wiki compounds. New artifacts come in via Ingest, get filed under the right entity/concept, and gain back-links here. Queries pull from the wiki, not from raw sources. Lint runs weekly; Maintain keeps `log.md` chronologically truthful.

- Read [Knowledge/log.md](log.md) for the chronological record (what was added/edited, when, by whom).
- Run `/wiki-ingest <source>` to file new sources.
- Run `/wiki-query <question>` to synthesize across the wiki.
- Run `/wiki-lint` weekly to surface orphans, contradictions, stale claims.
- Run `/wiki-maintain` after major Ingest batches to refresh this index and re-cross-link.

---

## People

Stakeholders, manager chain, key colleagues. Profiles live in `Knowledge/People/`.

| Page | Role | Last verified |
|---|---|---|
| _populate via `/wiki-ingest` or by hand; promote from auto-memory when stable_ | — | — |

## Reference

Domain canon: KPay org, CDP brief, martech stack, frontier-lab JD pack, RegEval domain primers. Lives in `Knowledge/Reference/`.

| Page | Topic | Last verified |
|---|---|---|
| _populate via Ingest_ | — | — |

## Research

Synthesised research outputs (interview synthesis, market scans, paper digests). Lives in `Knowledge/Research/`.

| Page | Topic | Last verified |
|---|---|---|
| _populate via Ingest_ | — | — |

## Concepts

Cross-cutting notes that aren't a person, a domain artifact, or a research output — e.g. "abstention scoring", "judge alignment", "warm-intro path". File under `Knowledge/Concepts/` (create on first use).

| Page | One-liner | Last verified |
|---|---|---|
| _populate via Ingest_ | — | — |

---

## Cross-references that should always exist

These hard-links are tested by `/wiki-lint`:

- Every Person page links to at least one Reference or Research page they're cited in.
- Every Reference page lists the canonical decisions or PRDs that depend on it.
- Every Research page names its source transcripts and the Person pages of interviewees.
- Every Concept page links from at least one PRD, essay, or eval.

## Anti-patterns

- Filing a Reference page without a "Last verified" date (Lint failure)
- Two pages making contradictory claims with no resolution note (Lint failure)
- A Research page without back-links to its interviewees (Lint failure)
- Editing this index by hand instead of via `/wiki-maintain` (drift risk; not enforced but discouraged)
