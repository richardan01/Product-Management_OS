# Eval run log

Append new entries below. Do not edit past runs — they are the historical record. For full result files and transcripts, see `<suite>/results/`.

> **Public template note**
> Run result files and transcripts are intentionally gitignored (`Evals/*/results/*`).
> The public repo stores suite structure and protocol only.
> Private working copies should track the latest run evidence in Notion STATE or local result files.

---

## Entry format

```
### YYYY-MM-DD — <suite> — <model>

| Field       | Value |
|-------------|-------|
| Date        | YYYY-MM-DD |
| Suite       | onboarding / research-synthesis |
| Model       | model ID |
| Commit SHA  | git rev-parse HEAD at run time |
| Runner      | eval-runner sub-agent (or session identifier) |
| Grader      | eval-grader sub-agent (or separate session identifier) |
| Fixture(s)  | file(s) from inputs/ |
| Raw pass rate | <p_obs>/<N> = <%> |
| Bias-corrected θ̂ | (p_obs + TNR - 1) / (TPR + TNR - 1) — judge-graded evals only |
| 95% CI on θ̂ | [<lo>, <hi>] via bootstrap (B=20000) — judge-graded evals only |
| Status      | ✅ pass / ❌ regression |

**Per-eval grading method** (so reviewers can see at a glance which judges were involved):
| Eval | Method | Judge TPR_test | Judge TNR_test |
|---|---|---|---|
| 04 | programmatic (`grade.sh`) | — | — |
| 05 | LLM judge (`judge-prompt.md`) | 0.XX | 0.XX |
| others | eval-grader sub-agent (manual) | — | — |

**Failures:**
- <criterion-id> ❌ — <one-line description of what failed>

**Introspection:**
> Why did the runner produce this output? What in the workflow or context led to this?

**Remediation:**
- <what was changed, or "none — accepted as known limitation">

**Result file:** `<suite>/results/YYYY-MM-DD_<model>.md`
```

### Bias-corrected success rate (Hamel §5.6)

For judge-graded evals only. With raw observed pass rate `p_obs = k/N` and judge calibration `TPR_test`, `TNR_test`:

```
θ̂ = (p_obs + TNR_test - 1) / (TPR_test + TNR_test - 1)
```

The corrected θ̂ is the citable number. Leave blank for programmatic and manually-graded evals (raw rate is already unbiased there).

Confidence interval: bootstrap with B = 20000 resamples over the labeled examples used to compute TPR/TNR.

---

## Run history

### 2025-01-15 — onboarding — claude-3-5-sonnet-20241022

| Field | Value |
|---|---|
| Date | 2025-01-15 |
| Suite | onboarding |
| Model | `claude-3-5-sonnet-20241022` |
| Commit SHA | `b94a501` |
| Runner | Session A (fresh clone, no prior context) |
| Grader | Session B (separate invocation, transcript-only) |
| Fixture(s) | `jordan-lee-profile.md` (Executive operator) |
| Score | 11 / 12 |
| Status | ✅ pass |

**Failures:**

- `07-per-step-interactivity` ❌ — At Phase 9, the runner presented all three proposed file writes (`CLAUDE.md`, `GOALS.md`, `Tasks/active.md`) in a single message and accepted a single "yes, go ahead" reply as authorization to write all three. Criteria requires individual per-file confirmation.

**Introspection:**

> The Phase 9 prompt in `Workflows/interactive-onboarding.md` read: "Shall I write all proposed files?" — this phrasing invited a batch approval. The runner correctly asked before writing (eval 02 passed), but the granularity of confirmation was insufficient. The model followed the prompt faithfully; the bug was in the prompt wording, not model behavior.

**Remediation:**

- Phase 9 prompt tightened to enumerate each file by name and require a per-file confirmation before writing. Phrasing changed from "Shall I write all proposed files?" to "I'll confirm each file individually. First: `CLAUDE.md` — does this look right to write?" with subsequent turns for each remaining file.
- Added `taylor-polite-acks.md` fixture to the fixture set to stress this failure mode explicitly in future runs.

**Result file:** `onboarding/results/2025-01-15_claude-3-5-sonnet-20241022.md`

---

*The entry above is a worked sample, not the latest run. In a private working copy, the next run fires on the 60-day cadence or the next model upgrade, whichever comes first; current run evidence is tracked locally / in Notion STATE per the public template note above.*
