# RegEval — wall-clock budget tracker

**Weekly cap:** 6 hr (per Q3 thesis allocation)
**Session cap:** 60 min / 12 experiments
**Per-experiment cap:** 5 min target, 8 min hard kill

The runner refuses new experiments once the session cap is hit. Weekly cap is enforced by you; if a week's row crosses 6 hr, RegEval is closed for the week — go work the canonical essay or technical depth.

## Week log

| Week (Mon–Sun) | Experiments | Wall clock (min) | KEEP count | Notes |
|---|---|---|---|---|
| 2026-W18 (Apr 27 – May 3) | 0 | 0 | 0 | scaffolding only — no runs yet |

## Session log (rolling, last 30 days)

| Date | Session start (UTC) | Experiments | Wall clock | Outcome |
|---|---|---|---|---|
| _none yet_ | — | — | — | — |

## How to update

After every `/regeval-run` invocation, append a row to the session log. At week-end (Sunday 23:59 SGT), roll the week's totals into the week log and reset the session log filter.

If a session crossed the cap, write a one-line root-cause in the Notes column. Three over-cap weeks in a row = audit the loop, the cap is right.
