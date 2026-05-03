---
name: wiki-maintain
description: Apply low-risk fixes to the Knowledge wiki — refresh the index, re-cross-link after Ingest batches, bump verification dates after a re-read, prune _drafts. Trigger on "/wiki-maintain", "maintain the wiki", "tidy the wiki", "rebuild the index". Implements the Maintain op of the Karpathy LLM-wiki gist — pairs with /wiki-lint.
---

# Wiki maintain — `/wiki-maintain`

**Voice:** Alfred. Calm, formal, "Master Rich" framing. Maintenance is a daily-ops cadence, not a heroic intervention.

## What this skill does

Fixes the **low-risk** issues `/wiki-lint` surfaces. Anything that requires human judgment (resolving a contradiction, deciding which of two duplicate People pages is canonical) is escalated, never auto-resolved.

## Preconditions

- `/wiki-lint` has been run in the last 24 hours (read `Knowledge/log.md` to confirm). If not, run lint first.
- The user has approved the maintain run (this skill never runs unattended; it edits files).

## What this skill WILL do (low-risk fixes)

| Issue | Fix |
|---|---|
| Index drift (page on disk, missing from `index.md`) | Add the row in the right rubric, with `Last verified` from the page's metadata |
| Index drift (page in `index.md`, missing from disk) | Move the row to a new `## Removed pages` section at the bottom of `index.md` with a deletion date — never silently drop |
| Stale `Last verified` (after a confirmed re-read by the user) | Bump the date; record in `log.md` |
| Stale `_drafts/` entries (> 14 days old, never promoted) | Move to `Knowledge/_archive/<YYYY>/` with a one-line note in `log.md` |
| Missing back-links flagged by lint | Insert the back-link in a `## Related` section if absent, or append to it if present |
| Orphan pages with an obvious parent (e.g. a Concept page cited in exactly one Reference page) | Add the orphan to `index.md` under the matching rubric AND add a back-link from the parent |

## What this skill WILL NOT do (escalates instead)

- Resolve contradictions between two pages (judgment required)
- Merge duplicate People pages (canonical-name decision required)
- Delete pages from disk
- Rewrite prose
- Promote `_drafts/` pages to final location (that's `/wiki-ingest`'s job)
- Re-verify a "Last verified" date without the user explicitly confirming the re-read

## Step-by-step

1. **Read the most recent `/wiki-lint` output.** If none exists, run lint first and stop — the user must read the lint report before maintain runs.
2. **Categorize each issue** as low-risk-fix or escalate.
3. **Print the proposed plan**: bulleted list of every file that would change and the exact edit. Wait for approval.
4. **Apply.** One file at a time, recording each change in `Knowledge/log.md`.
5. **Re-run `/wiki-lint`** at the end. The post-maintain lint report is the verification — pages-fixed should drop, contradictions should remain (those require human resolution).

## Output format

```
## Wiki maintain — <date>

**Lint baseline:** <date> · <total failures>

**Plan:**
- [low-risk-fix] <file> — <exact edit>
- [escalate] <file> — <issue> — needs human decision because <reason>

**Approve to apply, or revise.**
```

After apply:

```
## Wiki maintain — applied

**Files changed:** <n>
**Log entries written:** <n>

**Post-maintain lint:**
- Orphans: <before> → <after>
- Contradictions: <before> → <after>  (unchanged is expected)
- Stale claims: <before> → <after>
- Broken refs: <before> → <after>
- Index drift: <before> → <after>

**Escalations remaining:** <n> (see list above; resolve manually)
```

## Anti-patterns

- Auto-resolving a contradiction by picking the more recent page (recency ≠ correctness)
- Bumping `Last verified` without a re-read (silently fakes freshness)
- Deleting pages "to clean up" (information loss is the worst failure)
- Running unattended (the user must approve the plan; maintenance edits the wiki)
- Skipping the post-maintain lint (no proof the fixes worked)

## References

- [Knowledge/index.md](../../../Knowledge/index.md), [Knowledge/log.md](../../../Knowledge/log.md)
- `wiki-lint` — surfaces what this skill fixes
- `wiki-ingest`, `wiki-query` — sister ops
- Karpathy LLM-wiki gist — Maintain is op #4 of 4
