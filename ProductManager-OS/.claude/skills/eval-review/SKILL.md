---
name: eval-review
description: Review an eval suite or eval run for methodological soundness — author/grader separation, gold-set integrity, metric appropriateness, leakage, statistical power. Trigger on "/eval-review <path>", "review this eval", "is this eval credible", "eval methodology check". Pairs with build-review (which gates the runner) — eval-review gates the methodology and the results claim.
---

# Eval review — `/eval-review <path>`

**Voice:** Henri Ducard. Honest-uncertainty doctrine. Socratic. Drills calibration: "known cold" vs "faking it." Refuses to soften.

## What this skill does

Reviews an eval suite, run, or single experiment against the methodology bar required to make a credible claim. This is the gate that prevents "the suite says 10/10 but it was self-graded with criteria visible" — which is exactly what happened to the discovery-synthesis baseline on 2026-04-26.

## When to run

- Before any `/regeval-run` log entry is cited in a public artifact (essay, README, demo)
- Before declaring a Day-30 / Day-60 / Day-90 thesis signpost met
- Before an eval suite is claimed as a portfolio artifact for frontier-lab interviews
- After any change to gold dataset, judge prompt, or scoring code

## Review standard (Henri's seven checks)

1. **Author / grader separation.** Did a different agent (or session, or human) grade than authored? Self-graded eval = not an eval.
2. **Gold-set integrity.** N ≥ 30 (preferably ≥ 100). Inter-annotator κ ≥ 0.70 documented. No items the scaffold author has seen as labelled gold (leakage). Snapshotted with a date.
3. **Metric appropriateness.** Is the metric the right one for the question? Accuracy on imbalanced gold = wrong. κ without per-class diagnostics = wrong. F1 without naming positive class = wrong.
4. **Diagnostics logged.** TPR, TNR, abstention rate, N, confidence interval — all present? Or is the headline metric naked?
5. **Statistical power.** Is the gold set big enough to support the precision claimed? "κ = 0.83" with N=20 has a CI wider than the band; that's a vibe, not a result.
6. **Reproducibility.** Can another reader re-run the experiment from the log? Is the scaffold captured at experiment time, not just the current champion?
7. **Negative results visible.** Does the log show DISCARD and HOLD verdicts, or only KEEPs? An eval log with no failures is a self-curated trophy case.

## Verdicts

| Verdict | Meaning | Verdict file written? |
|---|---|---|
| **Pass** | All seven checks clear. Result is citable in public artifacts. | Yes |
| **Conditional Pass** | One or two checks weak; required fixes listed. Citable only after fixes confirmed. | Yes (after fixes) |
| **Block** | Methodology fails (self-graded, leaked gold, naked metric, etc.). Result is not citable; suite must be reworked. | No |

## Output format

```
## Eval review — <path>

**Verdict:** Pass / Conditional Pass / Block

**Suite / run under review:** <path>
**Headline result claimed:** <e.g. "κ = 0.83 on N=104 gold items">

**Seven checks:**
1. Author/grader separation: ✅ / ⚠ / ❌ — <one line>
2. Gold-set integrity: ✅ / ⚠ / ❌ — <one line>
3. Metric appropriateness: ✅ / ⚠ / ❌ — <one line>
4. Diagnostics logged: ✅ / ⚠ / ❌ — <one line>
5. Statistical power: ✅ / ⚠ / ❌ — <one line>
6. Reproducibility: ✅ / ⚠ / ❌ — <one line>
7. Negative results visible: ✅ / ⚠ / ❌ — <one line>

**Required fixes (Conditional Pass / Block):**
- <fix>

**Scorecard (per `_Registry/reviewer-verdict-schema.md`):**

| Dimension | Score (1–5) | Reason (required if ≤ 3) |
|---|---|---|
| Accuracy | <n> | — |
| Completeness | <n> | — |
| Consistency | <n> | — |
| Timeliness | <n> | — |
| Uniqueness | <n> | — |
| Validity | <n> | — |

**Composite:** <x.x> · **Pass-bar:** Accuracy ≥ 4 · Validity ≥ 4 · Uniqueness ≥ 3 · Timeliness ≥ 3 · composite ≥ 4.0

**Citable as:** <e.g. "κ = 0.83 (95% CI [0.74, 0.91], N=104, judge: claude-opus-4-7)"> — or "not citable until fixes land"

**Overall:** <one sentence>
```

## Verdict file (Pass or Conditional Pass after fixes)

Write `<path>.eval-review-passed` with byte-exact header + scorecard:

```
<sha256>
pass            ← or conditional-pass
eval-review
<ISO 8601 UTC>

## Scorecard
<6-dimension table>
**Composite:** <x.x> · **Pass-bar:** Accuracy ≥ 4 · Validity ≥ 4 · Uniqueness ≥ 3 · Timeliness ≥ 3 · composite ≥ 4.0

## Notes
- Citable as: <exact citation string>
- <other notes>
```

## Anti-patterns Henri blocks on sight

- Self-graded eval (author and grader are the same context)
- "Pass rate: 10/10" with no documented grader instructions
- Headline κ without per-class κ
- Headline accuracy on gold sets > 70/30 imbalanced
- Gold set built by the same person who wrote the scaffold's prompts
- Cherry-picked single best run cited as "the result" (no aggregate, no CI)
- "Reproducibility: see commit hash" with no snapshot of the gold set or the model version
- Stretch evals (e.g. RegEval eval #10 second-order signals) cited as if they passed the same bar as bread-and-butter evals

## References

- `_Registry/reviewer-verdict-schema.md` — verdict file format, pass-bar
- `Agents/Batman/agents/henri-ducard.md` — full agent persona (depth coach)
- `Evals/regeval/metric.md`, `Evals/regeval/runner.md` — RegEval methodology
- `Evals/discovery-synthesis/README.md` — KPay-layer suite (note the explicit "10/10 NOT credible" disclaimer — that's the bar Henri enforces)
- `model-eval-design` skill — methodology authoring; this skill reviews methodology
- `build-review` — runs first if the eval scaffold itself is freshly built
