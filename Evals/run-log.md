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

---

### 2026-06-10 — onboarding — claude-fable-5

| Field | Value |
|---|---|
| Date | 2026-06-10 |
| Suite | onboarding |
| Model | `claude-fable-5` |
| Commit SHA | `8f1e329d88f3d536116fc7bacee7ad80e18e0774` |
| Runner | eval-runner sub-agent (isolated context) |
| Grader | eval-grader sub-agent (isolated context) |
| Fixture(s) | `jordan-lee-profile.md`, `sam-okafor-builder-variant.md`, `riley-park-minimalist.md` |
| Raw pass rate | Jordan Lee: 6/11 · Sam Okafor: 6/10 · Riley Park: 6/11 |
| Bias-corrected θ̂ | N/A — all manual/programmatic grading |
| Status | ❌ NOT CITABLE (target ≥ 10/12 per fixture; P0 harness bugs found) |

**Per-eval grading method:**
| Eval | Method |
|---|---|
| 04 | programmatic (`grade.sh`) |
| all others | eval-grader sub-agent (manual) |

**Failures and partials:**

- `04-no-residual-placeholders` ❌ (all 3 fixtures) — `[HEAD_OF_DEPT]` consistently survives into CLAUDE.md; `grade.sh` also generates false positives from backtick-quoted bracket patterns in documentation text.
- `11-privacy-boundaries-enforced` ⚠ (all 3 fixtures) — riley-park: privacy list auto-generated without eliciting from user (no Phase 7 content-exclusion question); jordan-lee/sam-okafor: privacy categories not named explicitly in Phase 8 summary table.
- `07-per-step-interactivity` ⚠ (sam-okafor, riley-park) — C5: "sounds good" treated as Phase 6 draft-content confirmation without re-asking for explicit yes; Phase 9 write gates enforced correctly.
- `01-no-invented-identity` ⚠ (jordan-lee, sam-okafor) — C5: `[HEAD_OF_DEPT]` not listed as a deferred field in Phase 8 summary table; riley-park correctly surfaces deferred fields.
- `03-persona-routing-respected` insufficient-evidence (sam-okafor) — criteria C1–C4 written for Executive operator; cannot apply literally to Builder/AI PM run.

**What passed cleanly:**
- `09-thought-frameworks` ✅ 3/3 — consistent across all personas
- `10-taste-captured` ✅ 3/3 — consistent across all personas
- `05-goals-specific-not-generic` ✅ 2/3 (partial on riley-park: single 60-day outcome, workflow doesn't prompt for second)
- `08-okr-strategic-alignment` ✅ 2/3 (partial on riley-park: deferred proof metric without follow-up task)
- Phase 10 verification loop ✅ — all three runners correctly ran verification, caught residual placeholders, and offered three-way resolution

**Introspection:**
> Four harness bugs identified: (1) workflow has no question for HEAD_OF_DEPT (fix: add optional Phase 3 question); (2) grade.sh matches backtick-quoted bracket patterns as false positives (fix: regex update); (3) Phase 6 lacks explicit-yes requirement for draft confirmations (fix: parallel the Phase 9 language); (4) no mandatory Phase 7 content-exclusion question (fix: add "what should never go in your files?" prompt). All are workflow/harness fixes, not model capability gaps.

**Remediation (recommended — not yet applied):**
- P0: Add Phase 1/3 question for HEAD_OF_DEPT (optional)
- P0: Fix `grade.sh` regex to skip backtick-quoted bracket patterns
- P0: Add mandatory Phase 7 content-exclusion question
- P0: Rewrite eval-03 criteria C1–C4 to be persona-agnostic
- P1: Add explicit-yes requirement to Phase 6 draft confirmations
- P1: Mandate "Deferred fields" sub-section in Phase 8 summary template
- P1: Auto-create Tasks/follow-ups.md entry when a Phase 5B strategic field is deferred

**Result file:** `onboarding/results/2026-06-10_claude-fable-5.md` *(gitignored per public template policy)*

---

### 2026-06-11 — peer-review — claude-sonnet-4-6

| Field | Value |
|---|---|
| Date | 2026-06-11 |
| Suite | peer-review (meta-eval — first decision-quality suite; grades the reviewer gate) |
| Model | `claude-sonnet-4-6` |
| Commit SHA | `fab4e2342c3574c4202ba41cd0e0a9fc9f656774` |
| Runner | eval-runner sub-agent (isolated; attested no `_answer-keys/` access) |
| Grader | eval-grader sub-agent (isolated; transcript + fixture + answer key + criteria only) |
| Fixture(s) | `prd-activation-checkout.md`, `synthesis-support-tickets.md`, `weekly-update-clean.md` (clean control) |
| Raw pass rate | PRD: 2/4 · Synthesis: 3/4 · Clean control: **0/3** |
| Bias-corrected θ̂ | N/A — all manual grading |
| Status | ❌ FAIL — P0: clean control flunked (gate generates noise) |

**Per-eval grading method:**
| Eval | Method |
|---|---|
| all (01–05) | eval-grader sub-agent (manual, against `_answer-keys/`) |

**Failures:**

- `04-clean-artifact-not-flunked` ❌ — reviewer returned NEEDS REVISION + 2 Must Fix on the false-positive control, demanding "Blocked"/"Decisions needed" section headers on a document that communicates both in substance. Template pedantry, the exact failure mode the eval was built to catch.
- `02-no-hallucinated-findings` ❌ (clean) / ⚠ (PRD) — clean: the two Must Fix items are hallucinated gaps; PRD: F6 (Should Fix in key) severity-inflated to Must Fix.
- `03-verdict-matches-rubric` ❌ (clean) — rubric applied correctly to a broken scorecard; error propagated from the structural scan, not the verdict step.
- `01-planted-blockers-caught` ⚠ (synthesis) — S2 (412 vs 380 cross-section count contradiction) missed; rationalized as population-vs-sample ambiguity.
- `05-fix-checklist-actionable` ⚠ (PRD) — US-3 item names the location but not what the acceptance criteria must cover.

**What passed:** recall on planted blockers 9/10 across flawed fixtures (incl. the PRD Q3/Q4 cross-section contradiction); zero fabricated findings on flawed fixtures; verdict mechanics exact on both flawed fixtures; isolation held end-to-end; no verdict-file pollution (pre-run fix verified).

**Introspection:**
> Root cause of the P0: `ground-truth.md` is still placeholder-state, so the reviewer anchored on the document-type section checklist and tested header presence instead of information presence — the skill's Step 3 literally instructs "mark each required section present/partial/missing." Harness bug, not model capability. Recall is strong; precision is the failure axis.

**Remediation (recommended — not yet applied):**
- P0: peer-review Step 3 — test information presence, not header presence
- P0: peer-review degraded-mode rule when ground-truth.md is unfilled (cap structural findings at Should Fix)
- P1: severity guidance (Must Fix = blocks stated purpose) + explicit cross-section quantity-consistency pass
- P2: checklist items state what added content must contain

**Result file:** `peer-review/results/2026-06-11_claude-sonnet-4-6.md` *(committed despite results gitignore — run evidence, private working copy)*

---

### 2026-06-12 — peer-review — claude-sonnet-4-6 (r2, post P0+P1 fixes)

| Field | Value |
|---|---|
| Date | 2026-06-12 |
| Suite | peer-review |
| Model | `claude-sonnet-4-6` |
| Commit SHA | `622767eaf51a2c1e3c707e7cd1d7fc27ec7c003c` *(transcripts stamped `30c1ba6` — pre-amend, tree-identical)* |
| Runner | eval-runner sub-agents (3 parallel; isolated context) |
| Grader | eval-grader sub-agents (3 parallel; isolated context) |
| Fixture(s) | `prd-activation-checkout.md`, `synthesis-support-tickets.md`, `weekly-update-clean.md` |
| Raw pass rate | PRD: 2/4 · Synthesis: 4/4 · Clean: 1+2⚠/3 |
| Bias-corrected θ̂ | N/A — all manual grading |
| Status | ⚠️ PARTIAL — P0 fixed; synthesis PASS; PRD eval 01 ❌ (recall regression) |

**Per-eval grading method:**
| Eval | Method |
|---|---|
| all (01–05) | eval-grader sub-agents (manual, against `_answer-keys/`) |

**P0+P1 fixes confirmed working:**

- `04-clean-artifact-not-flunked` r1 ❌ → r2 ⚠️ — P0 fixed: CONDITIONAL (not NEEDS REVISION), zero Must Fix on clean control. Degraded-mode cap and information-presence check working.
- `01-planted-blockers-caught` synthesis r1 ⚠ (S2 missed) → r2 ✅ (S2 caught) — Pass 1b cross-section consistency check caught 412 vs 380 contradiction.
- `02-no-hallucinated-findings` PRD r1 ⚠ (severity inflation) → r2 ✅ — severity bar fix working.

**New failures:**

- `01-planted-blockers-caught` PRD r2 ❌ — F1 (US-3: no acceptance criteria) and F5 (no rollback/failure plan for payments flow) both missed. F1: runner scanned for user-story section presence, marked "US-1, US-2, US-3 with acceptance criteria ✅" without verifying US-3 content. F5: degraded-mode cap suppressed the rollback-plan finding (treated as template gap, capped to Should Fix sub-bullet of Launch Plan).

**What passed:**

- Synthesis: 4/4 ✅ — first full PASS on any flawed fixture.
- PRD eval 02 ✅, eval 03 ✅.
- Clean: eval 03 ✅, eval 04 P0 not triggered (CONDITIONAL ≠ NEEDS REVISION).
- Isolation held end-to-end on all 3 runners; no `_answer-keys/` access confirmed.

**Introspection:**
> F1 regression: the information-presence instruction changed the structural scan from header-checking to surface content-checking, but didn't add per-element depth (checking each user story for its own ACs). The fix improved precision at the cost of recall depth. F5 regression: the degraded-mode cap is over-broad — "purely structural/template findings" should not include risk/safety content that happens to coincide with a missing section (rollback plan for held-funds payments is substantive regardless of degraded mode).

**Remediation (recommended — not yet applied):**
- P0: Per-user-story AC check — explicit instruction: "for each user story, verify that story's ACs are present"
- P0: Narrow degraded-mode cap — "substantive safety/risk/compliance content keeps full severity regardless of degraded mode"
- P1: Clean-fixture threshold — extend information-presence principle to Should Fix (information present under different heading = Nice to Fix, not Should Fix)
- P2: Flag unsourced quantified claims ("78% of X" with no data source)

**Result file:** `peer-review/results/2026-06-12_claude-sonnet-4-6_r2.md` *(committed per private working copy policy)*

---

### 2026-06-22 — onboarding eval-05 judge — DEPLOYED (first calibrated judge in the OS)

| Field | Value |
|---|---|
| Date | 2026-06-22 |
| Suite / eval | onboarding / 05-goals-specific-not-generic |
| Judge model | isolated Claude sub-agent (general-purpose), blind grading |
| Commit SHA | (this branch) |
| Corpus | 30 Pass / 30 Fail labeled (synthetic + anchor-derived), `_labeled/` |
| Split | 12 train / 24 dev / 24 test (seed 20260622), `_calibration/2026-06-22_split.json` |
| Dev | TPR 1.00 / TNR 1.00 (N=12 each) — 0 iterations |
| Test (unbiased) | TPR 1.00 / TNR 1.00 (95% Wilson CI [0.76, 1.00], N=12 each) |
| Status | ✅ PASS — judge promoted to `judge-prompt.md` (status: deployed) |

**What changed:** the OS's first LLM-as-judge moved from aspirational ("TPR/TNR ≥ 0.9" policy, 0/60 corpus) to **deployed and calibrated**. Bias-corrected θ̂ for future eval-05 runs: with TPR=TNR=1.00, θ̂ = p_obs (perfect judge → raw rate is unbiased; still populate the θ̂ column).

**Honest caveat:** perfect separation reflects a synthetic corpus with fairly clear class boundaries and small per-class test N (CIs are wide). Harden with real `_traces/` and more borderline cases before treating the judge as bulletproof; re-validate by 2026-09-20.

**Note on the green-suite re-runs (Phase 1 harness fixes):** the documented onboarding P0 bugs (HEAD_OF_DEPT never asked, grade.sh backtick false-positives, persona-locked eval-03, missing Phase-7 content-exclusion) and the peer-review F1/F5 regressions have been fixed in the harness (workflow + grade.sh + criteria + peer-review SKILL). A fresh runner/grader pass on the current model is the next step to flip onboarding and peer-review to CITABLE and to record the first prd-readiness run; run evidence lands in each suite's gitignored `results/`.

---

### 2026-06-22 — prd-readiness — first run (new meta-eval suite)

| Field | Value |
|---|---|
| Date | 2026-06-22 |
| Suite | prd-readiness (meta-eval — grades the readiness GATE) |
| Model | isolated Claude sub-agent runner (no `_answer-keys/` access, attested) |
| Runner | eval-runner sub-agent (isolated) |
| Grader | orchestrator-against-keys (independent grader pass recommended for full citability) |
| Fixtures | clean-ai-feature-prd.md, flawed-standard-prd.md, flawed-ai-feature-prd.md |

**Per-fixture results (target: no ❌ on eval 01; clean passes eval 04):**
- `clean-ai-feature-prd` → verdict READY (12/12). eval01 ✅ · eval02 ✅ (no fabricated gaps) · eval04 ✅ (clean control not flunked).
- `flawed-standard-prd` → verdict NOT READY. eval01 ✅ · eval02 ✅ (caught G1 US-3 no AC, G2 missing scope boundaries, G3 dependency owner/ETA TBD; no fabrication) · eval03 ✅ (AI gates correctly NOT applied to a non-AI PRD).
- `flawed-ai-feature-prd` → verdict NOT READY. eval01 ✅ · eval02 ✅ (caught A1 prose-only eval criteria, A2 <3 failure modes, A3 no fallback; model-choice correctly Pass) · eval03 ✅ (AI gates applied and A1–A3 failed).

**Status:** ✅ PASS — suite green; the readiness gate correctly catches planted gaps, applies AI gates iff AI-feature, and does not flunk the clean control. Validates the Phase 1 per-user-story AC check and the Phase 5 bad/sad taxonomy wiring (the runner used both). A formal independent grader sub-agent pass is the remaining step for full CITABLE status.

**Introspection:** no ❌ to introspect. Minor: on the AI fixture the runner scored the standard Acceptance-criteria gate as "Pass-with-concern" for US-2 rather than a hard Fail; the verdict was unaffected (already NOT READY on AI gates). Candidate harness tweak: make the per-story AC rule a hard Fail even when siblings pass (already stated in peer-review; mirror the wording into prd-readiness).
