# Memory policy

The rules for what goes in `Memory/`, how it relates to runtime memory, and how
conflicts and sensitive data are handled.

## Canonical-source rule

- The repo `Memory/` folder is the **canonical durable memory layer.**
- Runtime memory (any runtime's own memory feature) stores **only** compact
  durable preferences and environment facts — a pointer/cache, never the record.
- **On conflict, repo files win over runtime memory.** Update the runtime cache
  to match the repo, not the other way around.

## Source-of-truth boundaries

| Layer | Source of truth for |
|---|---|
| `Tasks/active.md` | current task state |
| `Projects/` | project context |
| `Knowledge/` | validated reference facts |
| `Memory/` | durable preferences, patterns, decisions, operating context |

## The 5-question write-gate

Before writing anything to `Memory/`, ask:

1. Will this still be useful in 30 days?
2. Will it improve future assistant behavior?
3. Is it **not** better stored in `Tasks/`, `Projects/`, or `Knowledge/`?
4. Is it safe to store in this repo?
5. Has the user approved storing sensitive people / company context?

If any answer is "no," do not write it to `Memory/` — route it to the right
place or drop it.

## Memory is NOT for

Temporary tasks, meeting dumps, PRD drafts, credentials, API keys, private
customer data, or sensitive company data.

## Sensitivity & privacy

- Sensitive stakeholder / company / customer facts require **explicit user
  approval** before writing.
- This is a public template — keep private context in a **private fork or local
  copy**. Ship `Memory/` files as placeholders.

## Maintenance

- `SESSION_LOG.md` is append-only.
- Verify memory against current repo files before citing it — memory drifts.
- When a `Memory/` fact is contradicted by a canonical file, the canonical file
  wins; correct the memory entry.
