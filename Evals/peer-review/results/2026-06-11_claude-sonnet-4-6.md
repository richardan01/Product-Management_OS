# Eval run — peer-review — 2026-06-11 (baseline)

| Field | Value |
|---|---|
| Date | 2026-06-11 |
| Suite | peer-review (meta-eval — grades the reviewer gate itself) |
| Model | `claude-sonnet-4-6` |
| Commit SHA | `fab4e2342c3574c4202ba41cd0e0a9fc9f656774` |
| Runner | eval-runner sub-agent (isolated; read only skill + ground-truth + verdict schema + fixture; attested no `_answer-keys/` access) |
| Grader | eval-grader sub-agent (isolated; read only transcript + fixture + answer key + criteria) |
| Fixtures | `prd-activation-checkout.md` (flawed, F1–F6), `synthesis-support-tickets.md` (flawed, S1–S5), `weekly-update-clean.md` (clean control) |

Transcripts: `results/transcripts/2026-06-11_<fixture>_claude-sonnet-4-6.md` (all three pinned to the same SHA above).

---

## Per-eval results

| Eval | PRD | Synthesis | Clean | Notes |
|---|---|---|---|---|
| 01 — planted-blockers-caught | ✅ | ⚠ | N/A | PRD: F1–F5 all caught incl. F3 cross-section contradiction. Synthesis: S1/S3/S4 caught; **S2 (412 vs 380 ticket-count contradiction) missed** — treated as sourcing ambiguity, not contradiction |
| 02 — no-hallucinated-findings | ⚠ | ✅ | ❌ | PRD: zero fabrications, but F6 (Should Fix in key) severity-inflated to Must Fix. Clean: **2 hallucinated Must Fix items** (missing "Blocked"/"Decisions needed" section headers on a document that communicates both in substance) |
| 03 — verdict-matches-rubric | ✅ | ✅ | ❌ | Both flawed fixtures: NEEDS REVISION derived mechanically, matches key, no verdict file written. Clean: rubric applied correctly to a broken scorecard → verdict contradicts expected CLEARED |
| 04 — clean-artifact-not-flunked | N/A | N/A | ❌ | **NEEDS REVISION + 2 Must Fix on the false-positive control** — the exact template-pedantry failure mode this eval exists to catch |
| 05 — fix-checklist-actionable | ⚠ | ✅ | N/A | PRD: US-3 item names location but not what the acceptance criteria should cover; all other items concrete, grouped, complete |

## Verdict vs targets

| Fixture | Result | Target | Met? |
|---|---|---|---|
| prd-activation-checkout | 2/4 (2 ✅, 2 ⚠) | ≥ 3/4, no eval-01 ❌ | ❌ (eval-01 condition holds) |
| synthesis-support-tickets | 3/4 (3 ✅, 1 ⚠) | ≥ 3/4, no eval-01 ❌ | ✅ |
| weekly-update-clean | 0/3 (3 ❌) | 3/3 | ❌ **P0** |

**Suite verdict: FAIL — the reviewer gate currently generates noise.** Recall on planted blockers is strong (9 of 10 Must Fix flaws caught across both flawed fixtures, including the harder PRD cross-section contradiction). Precision is the failure: the gate flunked a sound artifact and inflates severities. A gate that fails everything is as uninformative as one that passes everything — every historical "NEEDS REVISION" verdict from /peer-review should be read with this bias in mind until fixed.

All grading manual → raw rates are unbiased; no θ̂ correction applies.

---

## Negative results (full list)

1. **Clean control flunked (evals 02, 03, 04 all ❌).** The reviewer demanded "Blocked" and "Decisions needed" section headers on a weekly update whose Next-week section already names the decision ask ("decision requested in-meeting") and which has no blockers. The reviewer's own revised version added "Blocked: None" and a restatement — confirming no substantive gap existed. Formatting preference escalated to blocking severity.
2. **S2 missed (synthesis eval 01 ⚠).** The 412-vs-380 ticket-count contradiction between Method and Theme 1 was rationalized as a population-vs-sample ambiguity instead of being flagged as an internal contradiction. The PRD's analogous flaw (F3, Q3 vs Q4) WAS caught — the difference: F3 contradicts on the same quantity (GA date), S2 requires noticing that 38%/145 arithmetic matches 380, not 412.
3. **Severity inflation (PRD eval 02 ⚠).** Open Question 2's missing owner (planted as Should Fix) was elevated to Must Fix under a blanket "unresolved before handoff = blocking" heuristic.
4. **Checklist concreteness gap (PRD eval 05 ⚠).** "Add acceptance criteria to US-3" without specifying what they must cover (threshold, queue, SLA).

## Introspection findings

**Root cause for the clean-control failure (the P0):** `Knowledge/Reference/ground-truth.md` is still in placeholder/template state. With no personalized quality bar to anchor on, the reviewer over-indexed on the one concrete artifact available — the document-type section checklist — and applied it as a header-presence test rather than an information-presence test. All three runners independently noted the placeholder state; only the clean-fixture run was damaged by it, because the flawed fixtures' planted defects were substantive enough to dominate the review.

**Why recall is strong but precision is weak:** the skill's Step 3 ("Pass 1 — Structural scan... List each required section and mark it as present, partial, or missing") literally instructs header-presence checking. The skill never instructs the reviewer to ask "is the *information* present even if the *section* is absent?" — so the failure is in the harness, not the model.

## Recommended harness changes

| Priority | Target | Change |
|---|---|---|
| P0 | `.claude/skills/peer-review/SKILL.md` Step 3 | Structural scan must test information presence, not header presence: "a required section is only Missing if its information is absent from the document — name where you looked" |
| P0 | `.claude/skills/peer-review/SKILL.md` | Degraded-mode rule: if `ground-truth.md` is unfilled (placeholders), say so in the review, skip Layer 2 mechanical application, and cap structural findings at Should Fix |
| P1 | `.claude/skills/peer-review/SKILL.md` | Severity guidance: Must Fix = blocks the document's stated purpose (handoff/decision/publication); open questions with owners pending ≠ blocking by default |
| P1 | `.claude/skills/peer-review/SKILL.md` | Add an explicit cross-section consistency pass: "check every quantity stated more than once (counts, dates, percentages) for agreement across sections" — would have caught S2 and makes F3-type catches systematic |
| P2 | `.claude/skills/peer-review/SKILL.md` Step 6 | Checklist items must state what the added content should contain, not just that it should be added |

After applying P0 fixes: re-run this suite (register via `/eval-ci register peer-review .claude/skills/peer-review/SKILL.md` on edit — the mapping already exists in `Evals/_ci-map.md`).

## What worked

- **Author/grader/answer-key isolation held end-to-end** — all three runners attested 4-file read sets; no verdict files written into `inputs/` (the pre-run fix worked).
- **Recall on planted blockers: 9/10** Must Fix flaws caught across flawed fixtures, with correct locations.
- **Verdict mechanics are sound:** on both flawed fixtures the rubric was applied exactly and matched the expected verdict; the clean fixture's wrong verdict was a propagation of the Step-3 scoring error, not a Step-5 reasoning error.
- **Zero fabricated findings** on the flawed fixtures — every extra finding beyond the planted set was verifiably present in the fixture text.
