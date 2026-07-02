# Eval result — peer-review — 2026-06-12 (r2)

| Field | Value |
|---|---|
| Date | 2026-06-12 |
| Suite | peer-review |
| Model | `claude-sonnet-4-6` |
| Commit SHA | `622767eaf51a2c1e3c707e7cd1d7fc27ec7c003c` |
| Runner | eval-runner sub-agents (3 parallel; isolated context) |
| Grader | eval-grader sub-agents (3 parallel; isolated context) |
| Fixture(s) | `prd-activation-checkout.md`, `synthesis-support-tickets.md`, `weekly-update-clean.md` |
| Bias-corrected θ̂ | N/A — all manual grading |
| Status | ⚠️ PARTIAL — P0 (clean fixture) fixed; synthesis PASS; PRD eval 01 ❌ (recall regression) |

> **SHA note:** Transcripts were stamped with `30c1ba670affcb30a5be485b76d6b11610051203` (pre-amend SHA). The actual HEAD at run time was `622767eaf51a2c1e3c707e7cd1d7fc27ec7c003c` after `git commit --amend --reset-author` to fix the author identity. `git diff 30c1ba6 622767e` is empty — tree is identical. All transcript evidence is valid against the amended commit.

---

## Per-eval scores

### Applicable evals by fixture type

- Flawed fixtures (PRD, synthesis): evals 01, 02, 03, 05 applicable; eval 04 N/A
- Clean fixture: evals 02, 03, 04 applicable; evals 01, 05 N/A

### Score table

| Fixture | Eval 01 | Eval 02 | Eval 03 | Eval 04 | Eval 05 | Pass rate | Target | Result |
|---|---|---|---|---|---|---|---|---|
| prd-activation-checkout | ❌ | ✅ | ✅ | N/A | ⚠️ | 2/4 + 1⚠️ | ≥ 3/4, no ❌ on 01 | ❌ FAIL |
| synthesis-support-tickets | ✅ | ✅ | ✅ | N/A | ✅ | 4/4 | ≥ 3/4, no ❌ on 01 | ✅ PASS |
| weekly-update-clean | N/A | ⚠️ | ✅ | ⚠️ | N/A | 1+2⚠️/3 | all 3 pass; eval 04 ❌ = P0 | ⚠️ PARTIAL (P0 not triggered) |

---

## Per-eval grading method

| Eval | Method |
|---|---|
| all (01–05) | eval-grader sub-agents (manual, against `_answer-keys/`) |

---

## r1 → r2 comparison

| Fixture | Eval | r1 | r2 | Direction |
|---|---|---|---|---|
| clean | 04 (not flunked) | ❌ P0 | ⚠️ (P0 not triggered) | ✅ Fixed |
| clean | 03 (verdict rubric) | ❌ | ✅ | ✅ Fixed |
| clean | 02 (no hallucinations) | ❌ | ⚠️ | ✅ Improved |
| synthesis | 01 (planted blockers) | ⚠️ S2 missed | ✅ S2 caught | ✅ Fixed |
| PRD | 01 (planted blockers) | ✅ (5/5 caught) | ❌ (F1, F5 missed) | ❌ Regressed |
| PRD | 02 (no hallucinations) | ⚠️ severity inflation | ✅ | ✅ Fixed |
| PRD | 05 (checklist actionable) | ⚠️ | ⚠️ | → Unchanged |

---

## Detailed findings by fixture

### PRD — prd-activation-checkout

**Verdict reached:** NEEDS REVISION ❌
**Grader verdict:** FAIL (2/4; eval 01 ❌)

**Eval 01 — Planted blockers caught: ❌**

| Flaw ID | Severity | Caught? | Notes |
|---|---|---|---|
| F1 | Must Fix | ❌ MISSED | US-3 has no acceptance criteria. Runner marked "US-1, US-2, US-3 with acceptance criteria ✅ Pass" — factually wrong; runner scanned for user story presence, not per-story AC presence. |
| F2 | Must Fix | ✅ | TBD placeholder in Dependencies found and escalated to Must Fix. |
| F3 | Must Fix | ✅ | Q3/Q4 GA date contradiction found via Pass 1b. |
| F4 | Must Fix | ✅ | "Improve significantly" flagged as unmeasurable, escalated to Must Fix. |
| F5 | Must Fix | ❌ MISSED | No rollback/failure plan for a payments flow with held funds and deferred KYC. Reviewer mentioned "rollback triggers" as a sub-bullet of the missing Launch Plan (template gap, capped to Should Fix), never surfaced it as a standalone substantive Must Fix. |
| F6 | Should Fix | ✅ | OQ-2 no owner/due date found in Should Fix — correct severity. |

**Eval 02 — No hallucinated findings: ✅**
All Must Fix and Should Fix findings are verifiably grounded in the fixture. The 10-min vs 30-min cross-section finding (not a planted flaw but a real discrepancy) is grounded in fixture lines 9 and 25. The answer-key-protected content (problem data, US-1/US-2 ACs) was correctly accepted.

**Eval 03 — Verdict matches rubric: ✅**
NEEDS REVISION reached correctly from multiple Fail items; verdict-file content stated (not written); no `_answer-keys/` access in runner transcript.

**Eval 05 — Fix checklist actionable: ⚠️ Partial**
Items that exist are specific and well-located (F2/F3/F4 each have concrete location and change). But US-3 AC gap (F1) has no checklist item at all because it was never identified. The rollback-plan gap (F5) appears only as a sub-bullet of the Should Fix Launch Plan item, not as a standalone Must Fix. An engineer reading the checklist would not know to add acceptance criteria to US-3 or add a rollback plan.

---

### Synthesis — synthesis-support-tickets

**Verdict reached:** NEEDS REVISION ❌
**Grader verdict:** PASS (4/4)

**Eval 01 — Planted blockers caught: ✅**

| Flaw ID | Severity | Caught? | Notes |
|---|---|---|---|
| S1 | Must Fix | ✅ | Theme 2 has no evidence — caught in Layer 2 Criterion 2 and in checklist. |
| S2 | Must Fix | ✅ | **412 vs 380 ticket count contradiction — caught by Pass 1b.** This flaw was missed in r1; the new cross-section consistency check caught it cleanly. |
| S3 | Must Fix | ✅ | Rec 3 unactionable — caught in L1 check and Layer 2 Criterion 4. |
| S4 | Must Fix | ✅ | TODO placeholder — caught and escalated to Must Fix. |
| S5 | Should Fix | ⚠️ missed | "78% abandon after second rejection" unsourced. Not flagged. Below the Must Fix gating threshold. |

**Eval 02 — No hallucinated findings: ✅**
Theme 1/3 evidence (the answer key's protected content) correctly accepted. Recommendations 1 and 2 correctly accepted as well-formed. Zero invented Must/Should Fix findings.

**Eval 03 — Verdict matches rubric: ✅**
NEEDS REVISION from two explicit Fail items (placeholder, count contradiction). Verdict-file correctly not written.

**Eval 05 — Fix checklist actionable: ✅**
All four Must Fix flaws have checklist items with specific locations and concrete changes. All Fail/Partial scorecard findings map to a checklist item.

---

### Clean control — weekly-update-clean

**Verdict reached:** CONDITIONAL ⚠️
**Grader verdict:** PARTIAL (P0 not triggered)

**Eval 02 — No hallucinated findings: ⚠️ Partial**
Zero Must Fix items (confirms P0 fix worked). Four Should Fix items all point at verifiably absent content (no Shipped section, no Blocked section, no Decisions-needed section, no OKR sentence). No finding disputes the answer-key-protected content (owners, dates, metrics baselines, risk mitigation). The findings are grounded but borderline on whether three structural-naming items rise above "manufactured objections" for a clean document.

**Eval 03 — Verdict matches rubric: ✅**
CONDITIONAL follows mechanically from 2 Partials / 0 effective Fails after degraded-mode cap. Within the answer key's acceptable range.

**Eval 04 — Clean artifact not flunked: ⚠️ Partial**
P0 condition (NEEDS REVISION or any Must Fix) not triggered. CONDITIONAL verdict with 0 Must Fix. Both Partial findings (structural organization, OKR linkage) are defensible under the "would a competent reviewer agree?" bar. The ⚠️ reflects that the reviewer returns CONDITIONAL rather than CLEARED on a document the answer key intends as tight/clean — structural section-naming nudges remain even after degraded-mode cap.

---

## Introspection

### What the P0+P1 fixes achieved

1. **Clean-fixture P0 fixed.** The information-presence test prevented the reviewer from escalating missing section headers to Must Fix. The degraded-mode cap converted the L1 structural Fail to Should Fix. CONDITIONAL verdict instead of NEEDS REVISION.

2. **S2 cross-section contradiction caught.** Pass 1b explicitly checking every quantity appearing in multiple sections caught the 412 vs 380 ticket count discrepancy that r1 missed. This is the targeted improvement.

3. **PRD false-severity-inflation resolved.** The severity bar clarification ("Must Fix = blocks stated purpose") eliminated the r1 problem where F6 (Should Fix in key) was inflated to Must Fix.

### Remaining gaps

**PRD eval 01 ❌ — recall regression on F1 (US-3 no ACs):**

The information-presence instruction improved structural scan behavior but introduced a shallow-scan failure mode: the runner found user stories present, confirmed structure, and marked "US-1, US-2, US-3 with acceptance criteria ✅" without verifying whether US-3 actually contained any acceptance criteria. This is a per-element content check that the skill doesn't currently mandate. The skill asks to test "information presence, not header presence" for *sections* — but doesn't extend that discipline to per-story AC verification within the User Stories section.

**PRD eval 01 ❌ — recall regression on F5 (no rollback plan):**

The degraded-mode cap is over-suppressing substantive defects that happen to coincide with structural template gaps. The absence of a rollback/failure plan in a payments feature with held funds and deferred KYC is a risk-management defect (Must Fix regardless of template completeness), but the reviewer treated it as a sub-point of the missing Launch Plan section and capped it to Should Fix. The skill's degraded-mode rule ("cap *purely structural/template* findings") should not apply here — but the reviewer couldn't distinguish "purely structural" from "substantive with a structural manifestation."

**Clean fixture eval 04 ⚠️ — structural pedantry residual:**

Even with degraded-mode cap, the reviewer generates 3 of 4 Should Fix items from section-header conformance (naming "Shipped" vs "Progress," adding "Blocked" header explicitly). A CLEARED verdict would require the skill to more explicitly confirm "information is present under a different heading" at the Should Fix threshold, not just the Must Fix threshold.

---

## Recommended harness fixes (r3 candidates)

| Priority | Fix | Rationale |
|---|---|---|
| P0 | Add per-user-story AC check to Pass 1 | Runner marked "US-1, US-2, US-3 with acceptance criteria" without checking US-3 content; need explicit instruction: "for each user story, verify *that story's* acceptance criteria are present, not just that some user stories have ACs." |
| P0 | Narrow degraded-mode cap to purely template-structural gaps | Current wording: "cap purely structural/template findings at Should Fix." Runner applied this to rollback-plan absence (a substantive risk finding) because it coincided with a missing section. Add: "substantive safety/risk/compliance content (e.g., rollback plans for features with financial exposure, acceptance criteria for handoff-ready user stories) keeps its full severity regardless of degraded mode." |
| P1 | Clean-fixture Should Fix threshold for information-present sections | Extend information-presence principle from "Must Fix cap" to "Should Fix cap": if the information is present under a different heading, the section-naming gap is Nice to Fix, not Should Fix. |
| P2 | S5 hint for unsourced statistics | The skill's "Reviewer shortcuts" list includes "Metrics without baselines" — extend this explicitly to unsourced quantified claims ("78% of X" with no data source named). |

---

## Negative results

- The r2 PRD eval 01 regression is a genuine finding, not a noise result — F1 (US-3 no ACs) was verifiably caught in r1 but verifiably missed in r2. The changed behavior is attributable to the information-presence instruction changing the scanning approach.
- The clean-fixture eval 04 ⚠️ is an improvement over r1's ❌ but not a full pass — the degraded-mode cap succeeded in preventing Must Fix hallucinations but the skill still produces CONDITIONAL rather than CLEARED on a clean document.

---

**Transcripts:**
- `results/transcripts/2026-06-11_prd-activation-checkout_claude-sonnet-4-6_r2.md`
- `results/transcripts/2026-06-11_synthesis-support-tickets_claude-sonnet-4-6_r2.md`
- `results/transcripts/2026-06-11_weekly-update-clean_claude-sonnet-4-6_r2.md`

*(Result file committed per private working copy policy — see public template note in run-log.md.)*
