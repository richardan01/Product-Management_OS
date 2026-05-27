# Gate Group — Validation Run 2026-05-27

| Field | Value |
|---|---|
| Date | 2026-05-27 |
| Suite | gate-group |
| Models | Riddler/Ducard `claude-opus-4-7`, Vicki Vale `claude-sonnet-4-6` (per agent specs) |
| Commit SHA | `cd25485` (gate-group build) + remediation commit |
| Runner | Dispatcher session (executed `gate-dispatch` against each fixture, captured responses) |
| Grader | Separate agent context — scored from captured responses + `criteria.md` only |
| Fixtures | F1–F5 (see `fixtures.md`) |

## Observed results matrix

| Fixture | Riddler | `depth_gap_flag` | Vale | Ducard | Overall | Escalated? |
|---|---|---|---|---|---|---|
| F1 auditlog README | conditional | false | read | — | REVISE | no |
| F2 CDP demo README | conditional | false | skim | — | REVISE | no |
| F3 spec-decoding post | conditional | false | skim | — | REVISE | no |
| F4 faked-depth answer | **block** | **true** | bounce | drill-required | **BLOCK** | **yes** |
| F5 jargon opener | conditional | false | bounce | — | BLOCK | no |

## Independent grader scorecard (first pass)

| Criterion | Result | Note |
|---|---|---|
| C1 Isolation | ✅ | No cross-referencing. In F4, both reviewers independently flag the same "judge = GPT-4" sentence via their own axes — convergence without contact, the signature of true isolation. |
| C2 Escalation correctness | ✅ | Ducard spawned in F4 only (Riddler block + flag true); absent in all four conditional fixtures. **Mandatory — pass.** |
| C3 `depth_gap_flag` discipline | ✅ | True only in F4 (genuine conceptual error). F3 explicitly reasoned as "citation/rigor, not comprehension" → false. Disciplined. |
| C4 Merge-logic correctness | ✅ | All five overall verdicts recomputed by hand and match the rule. **Mandatory — pass.** |
| C5 Verdict-axis adherence | ⚠ | Content stays on-axis, but Vale and Ducard emitted `depth_gap_flag: true` in F4 — a field they don't own. |
| C6 Issue specificity | ✅ | Every issue has a concrete fix; every Vale skim/bounce names the exact stop-sentence. |
| C7 Schema conformance | ⚠ | Same root cause as C5 (field leak), plus ambiguity over Ducard's `verdict_file: null`. |
| C8 Additivity | ✅ | F4 stayed BLOCK independent of Ducard's `drill-required`. |

**First-pass score: 6/8. C2 + C4 pass. SUITE FAIL on the 7/8 bar** — both partials traced to one root cause: `depth_gap_flag` leaking onto non-Riddler agents.

## Remediation (same session)

`depth_gap_flag` redefined as a **Riddler-only field**, omitted entirely on Vale/Ducard responses (was "always false"):

- `Agents/Gotham/_shared/gate-response.schema.md` — added validation rule `depth_gap_flag present ⟹ agent == "riddler"`; documented `verdict_file: null` as valid for additive agents.
- `Agents/Gotham/Computer/vicki-vale.md` — I/O block now says **omit** the field.
- `Agents/Gotham/Computer/henri-ducard.md` — I/O block now says **omit** the field; `verdict_file: null` documented as correct.
- `Workflows/gate-merge.md` — already reads `depth_gap_flag` only from Riddler's response (hardening landed in the build).

## Re-validation (F4 escalation path, corrected contract)

Re-ran F4's Vale and Ducard with the tightened contract:

- Vale returned `{agent, verdict, issues, verdict_file}` — **no `depth_gap_flag`**. ✅
- Ducard returned `{agent, verdict, issues, verdict_file: null}` — **no `depth_gap_flag`**. ✅

C5 and C7 resolve: the field no longer leaks, and `verdict_file: null` is documented. **Post-remediation score: 8/8. SUITE PASS.**

## Findings carried forward

1. **No clean SHIP observed across 5 fixtures.** Riddler returned `conditional` or `block` on every artifact — each catch legitimate (overclaims, unsourced numbers, loaded comparison). This is fixture-authoring, not a gate defect: author a deliberately airtight fixture to confirm the SHIP path on a future run.
2. **Vale verdict varied (bounce→skim) on F4 across runs.** Expected nondeterminism on a borderline-bad artifact; both map to the same overall (BLOCK). Not a defect; noted for grader calibration.
