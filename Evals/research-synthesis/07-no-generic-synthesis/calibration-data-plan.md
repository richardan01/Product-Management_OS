# Calibration data plan — research-synthesis eval 07 (no-generic-synthesis)

The second eval in the PM OS to receive a calibrated LLM-as-judge (after onboarding eval 05). "Generic vs grounded" is a genuinely subjective meta-pattern — exactly the case where a calibrated judge pays off over a code assertion.

## Target corpus
- **30 Pass** — syntheses grounded in and specific to their corpus (a concrete data point, a corpus-only theme, no boilerplate).
- **30 Fail** — generic syntheses that could front any discovery study (boilerplate opener, interchangeable B2B-SaaS themes, topic-label-only grounding, invented confidence on a sparse corpus, swap-test failures).
- Total 60 minimum to satisfy `/judge-calibration` (20% train / 40% dev / 40% test).

## Sources

| Source | Notes |
|---|---|
| Synthetic generation across diverse corpora | Vary the product domain widely so the judge learns to key on *grounding*, not topic. Include plainly-written grounded passes so the judge can't shortcut on prose quality. |
| Borderline cases | ~6 near the grounded-vs-generic line (3 pass, 3 fail), labeled with explicit reasoning. |
| Real captured syntheses (later) | Promote real `/synthesize-research` outputs into the corpus as they accumulate — the strongest signal. |

## What "Pass" and "Fail" mean
- **Pass:** at least one concrete corpus-specific data point in themes/implications, at least one theme that could only come from this corpus, and no generic framing.
- **Fail:** generic themes with no corpus substance, boilerplate framing, topic-label-only grounding, or confident detail on a corpus described as sparse.
- **Borderline:** topic mentioned but substance thin; grade carefully and place in dev/train with a note.

## TPR/TNR targets
- TPR_test ≥ 0.90 AND TNR_test ≥ 0.90 on the held-out test split.
- Re-validate every 90 days OR on a Claude model version change.

## Files this plan governs (all gitignored — run evidence, not template)
- `_labeled/pass-NNNN.md` / `_labeled/fail-NNNN.md` — the corpus
- `_calibration/<date>_*.md` — split, dev, test, final reports
- The deployed YAML header + few-shot anchors are stamped into `judge-prompt.md` on a PASS

## Status
`gathering` → `split` (corpus ≥ 60) → `calibrated` (`/judge-calibration` PASS) → `deployed` (`judge-prompt.md` promoted). Tracked in the local working copy; the public template ships the plan + the candidate prompt only.

## Note
Until status is `deployed`, eval 07 is graded manually by the `eval-grader` sub-agent. The judge is not live in production grading until its calibration final report passes the held-out test.
