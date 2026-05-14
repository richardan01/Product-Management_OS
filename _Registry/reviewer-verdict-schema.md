# Reviewer Verdict Schema

Canonical format for verdict files written by `/peer-review`, `/prd-readiness`, and `/eval-review`.

A verdict file is a lightweight audit trail. It proves a gate ran, by whom (which skill), on what (file path + date), and at what score. It does not replace the full review output — it's a four-line header plus the scorecard table.

---

## Verdict file naming

| Skill | Suffix |
|---|---|
| `/peer-review` | `<doc-path>.peer-review-passed` |
| `/prd-readiness` | `<prd-path>.prd-readiness-passed` |
| `/eval-review` | `<suite-path>.eval-review-passed` |

Place the verdict file in the same directory as the reviewed artifact.

Example:
```
Projects/activation-funnel/prd-v2.md
Projects/activation-funnel/prd-v2.md.prd-readiness-passed   ← verdict file
```

---

## Verdict file format

Every verdict file must contain exactly this header block, followed by the scorecard:

```
Gate:     <skill name>
File:     <reviewed file path>
Date:     YYYY-MM-DD
Verdict:  PASS | CONDITIONAL | FAIL
```

Followed immediately (no blank line) by the scorecard table from the skill output.

### Peer review verdict file example

```
Gate:     peer-review
File:     Projects/activation-funnel/vendor-scorecard.md
Date:     2026-05-14
Verdict:  PASS

| Layer | Check | Status |
|---|---|---|
| L1 — Agent quality | Structure complete | ✅ |
| L1 — Agent quality | Placeholders cleared | ✅ |
| L2 — Ground truth | Structure & completeness | ✅ |
| L2 — Ground truth | Clarity & writing quality | ✅ |
| L2 — Ground truth | Strategic alignment | ✅ |
| L2 — Ground truth | Actionability | ✅ |
| L2 — Ground truth | External reviewer comments | N/A |
```

### PRD readiness verdict file example

```
Gate:     prd-readiness
File:     Projects/activation-funnel/prd-v2.md
Date:     2026-05-14
Verdict:  CONDITIONAL

| Gate | Status |
|---|---|
| Problem statement | ✅ |
| User stories | ✅ |
| Acceptance criteria | ⚠️ Partial |
| Data requirements | ✅ |
| Scope boundaries | ✅ |
| Dependencies | ✅ |
| Priority tags | ✅ |
| Feasibility input | ✅ |
```

### Eval review verdict file example

```
Gate:     eval-review
File:     Evals/onboarding/results/2026-05-14_opus-4-7.md
Date:     2026-05-14
Verdict:  CONDITIONAL

| Check | Status |
|---|---|
| Author/grader separation | ✅ |
| Gold-set integrity | ⚠️ N < 30 (acknowledged) |
| Metric appropriateness | ✅ |
| Diagnostics logged | ✅ |
| Statistical power | ⚠️ low N; flagged |
| Reproducibility | ✅ |
| Negative results visible | ✅ |
```

---

## Verdict levels

| Verdict | Meaning | Who can use it |
|---|---|---|
| **PASS** | All gates clear. Artifact is approved for next step (engineering handoff, publication, citation). | Any skill |
| **CONDITIONAL** | 1–2 items partial; none failing. Approved to proceed if listed conditions are met before external sharing. | Any skill |
| **FAIL** | Any item is Fail, or 3+ items Partial. Artifact must be revised before use. | Any skill |

---

## Rules

1. Verdict files are only written on PASS or CONDITIONAL — never on FAIL.
2. A FAIL result is documented in the skill's full output only; no verdict file is created.
3. Do not back-date verdict files. The date is the date the skill ran.
4. Verdict files are not edited after creation. If a re-review changes the verdict, write a new file with a new date suffix: `<doc-path>.prd-readiness-passed.2026-06-01`.
5. Verdict files are committed alongside the artifact they cover — they are part of the artifact's history.
