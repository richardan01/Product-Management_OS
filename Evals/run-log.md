# Eval run log

Append new entries below. Do not edit past runs — they are the historical record. For full result files and transcripts, see `<suite>/results/`.

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
| Runner      | session/agent identifier |
| Grader      | separate session/agent identifier |
| Fixture(s)  | file(s) from inputs/ |
| Score       | X / N |
| Status      | ✅ pass / ❌ regression |

**Failures:**
- <criterion-id> ❌ — <one-line description of what failed>

**Introspection:**
> Why did the runner produce this output? What in the workflow or context led to this?

**Remediation:**
- <what was changed, or "none — accepted as known limitation">

**Result file:** `<suite>/results/YYYY-MM-DD_<model>.md`
```

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

### 2026-05-27 — gate-group — opus-4-7 / sonnet-4-6

| Field | Value |
|---|---|
| Date | 2026-05-27 |
| Suite | gate-group |
| Model | Riddler/Ducard `claude-opus-4-7`, Vale `claude-sonnet-4-6` |
| Commit SHA | `cd25485` + remediation |
| Runner | Dispatcher session (executed `gate-dispatch` per fixture, captured responses) |
| Grader | Separate agent context (responses + criteria only) |
| Fixture(s) | F1–F5 (`gate-group/fixtures.md`) |
| Score | 6 / 8 first pass → **8 / 8 after remediation** |
| Status | ✅ pass (post-fix); C2 + C4 mandatory both passed first pass |

**Failures (first pass):**

- `C5 verdict-axis adherence` ⚠ and `C7 schema conformance` ⚠ — both traced to one root cause: `depth_gap_flag` (a Riddler-only escalation signal) was emitted by Vicki Vale and Henri Ducard on the F4 escalation path.

**Introspection:**

> The schema said Vale/Ducard "always return `false`" for `depth_gap_flag`, which kept the field on their responses. Under the live run the agents filled it `true`, leaking a signal they don't own. Harmless to the merge (the merger reads it only from Riddler), but a schema-hygiene defect. The fix is to remove the field from their contract entirely, not to set it false.

**Remediation:**

- `depth_gap_flag` redefined as Riddler-only and **omitted** on Vale/Ducard responses; validation rule added (`present ⟹ agent == "riddler"`). `verdict_file: null` documented as valid for additive agents.
- Re-validated the F4 escalation path with the corrected contract: both Vale and Ducard omitted the field → C5 + C7 resolved → 8/8.

**Findings carried forward:** No clean SHIP observed across 5 fixtures (Riddler caught a legitimate issue in every one) — author a deliberately airtight fixture next run to confirm the SHIP path.

**Result file:** `gate-group/results/2026-05-27_validation.md`

---

*Next scheduled runs: onboarding — on next model upgrade; gate-group — after any dispatcher/merger/agent-I/O edit, or on the 60-day cadence.*
