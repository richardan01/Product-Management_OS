---
name: wiki-maintain
description: Apply low-risk fixes to the Knowledge wiki — refresh the index, re-cross-link after Ingest batches, bump verification dates after a re-read, prune _drafts. Trigger on "/wiki-maintain", "maintain the wiki", "tidy the wiki", "rebuild the index". Implements the Maintain op of the Karpathy LLM-wiki gist — pairs with /wiki-lint.
---

# Wiki maintain — `/wiki-maintain`

**Voice:** Calm, methodical. Maintenance is a daily-ops cadence, not a heroic intervention.

## What this skill does

Two modes:

1. **Structural fixes** — fixes the low-risk issues `/wiki-lint` surfaces (index drift, back-links, stale drafts).
2. **Weekly sweep** — runs the 8-check PM Brain health report. Run every Friday. If skipped once, momentum breaks.

## Preconditions

- `/wiki-lint` has been run in the last 24 hours (read `Knowledge/log.md` to confirm). If not, run lint first.
- The user has approved the maintain run (this skill never runs unattended; it edits files).

## What this skill WILL do (low-risk fixes)

| Issue | Fix |
|---|---|
| Index drift (page on disk, missing from `index.md`) | Add the row in the right rubric, with `Last verified` and lifecycle state |
| Index drift (page in `index.md`, missing from disk) | Move the row to a `## Removed pages` section with a deletion date |
| Stale `Last verified` (after a confirmed re-read by the user) | Bump the date; record in `log.md` |
| Stale `_drafts/` entries (> 14 days old, never promoted) | Move to `Knowledge/_archive/<YYYY>/` with a one-line note in `log.md` |
| Missing back-links flagged by lint | Insert back-link in a `## Related` section |
| Lifecycle state missing on an index row | Add `Active` / `Candidate` / `Archive` based on last-updated date |

## What this skill WILL NOT do (escalates instead)

- Resolve contradictions between two pages — **preserve both, surface the conflict**
- Merge duplicate People pages
- Delete pages from disk
- Rewrite prose
- Promote `_drafts/` pages (that's `/wiki-ingest`'s job)
- Re-verify a "Last verified" date without the user explicitly confirming the re-read

## Contradiction preservation rule

When two claims in the wiki conflict, **both must remain visible** with their respective provenance tags. The weekly sweep surfaces the conflict for the PM to resolve. Flattening contradictions into false consensus is the primary way a brain loses signal — never do it.

## The 8-check weekly sweep

Run every Friday. Output a `Knowledge/Maintenance/YYYY-MM-DD-sweep.md` report. Flag items by severity (🔴 action needed / 🟡 watch / ✅ clean).

### Check 1 — Stale knowledge audit
Files in `Knowledge/` (excluding `_archive/`, `Source/`, `Ingestion/`) unchanged for 6+ weeks → flag 🔴 if core reference, 🟡 if supplemental.

### Check 2 — Evidence decay by type
Scan all provenance tags across active files. Flag when past decay window:
- `[verbal-stake]` > 30 days → 🔴 re-verify or downgrade
- `[pm-intuition]` > 30 days → 🟡 validate or keep explicitly as hunch
- `[assumption]` > 30 days → 🔴 surface as risk in `/risk-register`
- `[doc-research]` market intel > 60 days → 🟡 flag for refresh
- `[doc-research]` interviews > 90 days → 🟡 flag for re-interview or archive

### Check 3 — Hypothesis hygiene
Scan `Knowledge/Hypotheses/proposed/`:
- Any hypothesis with no evidence update in 30 days → 🔴 stalled
- Any `confirmed/` hypothesis with no linked Decision record → 🔴 decision debt
- Any `candidate/` hypothesis untouched for 60 days → 🟡 promote or archive

### Check 4 — Stakeholder cadence
Scan `Knowledge/People/` for `last_contact` fields. Flag:
- High-influence contacts untouched 3+ weeks → 🔴
- Medium-influence contacts untouched 6+ weeks → 🟡

### Check 5 — Strategy tension detection
Read `Knowledge/Reference/company.md` and any `strategy.md` files. Compare against `Knowledge/Decisions/active/` records. Flag any active decision or recent signal that appears to diverge from documented strategy → 🔴 surface tension, do not resolve.

### Check 6 — Knowledge synthesis
Scan `Knowledge/Research/` and `Knowledge/Hypotheses/confirmed/` for:
- Recurring patterns across 3+ sources → 🟡 candidate for synthesis page
- **Minority signals** (dissenting interviews, contrarian metrics) not yet captured → 🔴 risk of false consensus

### Check 7 — Archival sweep
Scan `Knowledge/` for:
- Shipped features / resolved hypotheses inactive 90+ days → 🟡 candidate for `_archive/`
- Before archiving: extract one durable lesson sentence and add to the file

### Check 8 — Compression health
Count total files in `Knowledge/Ingestion/`. If > 10 unprocessed items → 🔴 ingestion backlog.
Check `Knowledge/Source/` growth — it should grow linearly (fine). Check durable layers (`Hypotheses/confirmed/`, `Decisions/active/`) — should grow logarithmically. If durable layers growing faster than source layer, flag as compression failure.

## Step-by-step (structural fixes mode)

1. **Read the most recent `/wiki-lint` output.** If none exists, run lint first.
2. **Categorize each issue** as low-risk-fix or escalate.
3. **Print the proposed plan**: bulleted list of every file that would change and the exact edit. Wait for approval.
4. **Apply.** One file at a time, recording each change in `Knowledge/log.md`.
5. **Re-run `/wiki-lint`** at the end to verify.

## Step-by-step (weekly sweep mode)

1. Run all 8 checks.
2. Write report to `Knowledge/Maintenance/YYYY-MM-DD-sweep.md`.
3. Surface a prioritized action list: all 🔴 items first.
4. Do not auto-fix; present for PM review.

## Anti-patterns

- Auto-resolving a contradiction by picking the more recent page
- Bumping `Last verified` without a re-read
- Deleting pages "to clean up"
- Running unattended
- Skipping Friday sweep — one miss breaks the compounding habit

## References

- `wiki-lint` — surfaces what this skill fixes
- `wiki-ingest`, `wiki-query` — sister ops
- `Knowledge/Reference/provenance-tags.md` — decay rules for evidence tags
