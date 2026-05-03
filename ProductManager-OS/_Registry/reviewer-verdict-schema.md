# Reviewer verdict schema (canonical)

**Owner:** _Registry · **Status:** v1, effective 2026-05-03
**Applies to:** every reviewer skill in `.claude/skills/` that produces a verdict file (Riddler, Vicki Vale, peer-review, prd-readiness, research-sufficiency, go-nogo, plus future build-review, eval-review, voice-conformance).

The point of this schema: one shape, six named quality dimensions, scored at every stage. Roll-up dashboard becomes a `grep` away.

---

## File location and naming

| Reviewer | Verdict file path |
|---|---|
| any | `<artifact-path>.<reviewer-slug>-passed` |

Examples:
- `Projects/regeval/essay.md.riddler-passed`
- `Projects/regeval/essay.md.vicki-passed`
- `Projects/cdp/prd.md.prd-readiness-passed`

If a verdict is **block / fail**, no file is written. The reviewer must reply with the failure narrative and required edits.

## File format

The file has two parts:

### Part A — header (lines 1–4, byte-exact, never reordered)

```
<sha256 hash of the artifact, hex, no filename suffix>
<verdict>
<reviewer-slug>
<ISO 8601 UTC timestamp, e.g. 2026-05-03T08:42:11Z>
```

This 4-line header is **frozen** for backward compatibility — existing hooks parse by line index. Do not insert blank lines, comments, or fields above line 5.

Allowed verdict values per reviewer:

| Reviewer | Allowed verdicts on a written file |
|---|---|
| riddler | `pass`, `conditional-pass` |
| vicki-vale | `read`, `skim` |
| peer-review | `pass`, `conditional-pass` |
| prd-readiness | `ready`, `ready-with-conditions` |
| research-sufficiency | `sufficient`, `sufficient-with-gaps` |
| go-nogo | `go`, `conditional-go` |
| build-review *(new)* | `pass`, `conditional-pass` |
| eval-review *(new)* | `pass`, `conditional-pass` |
| voice-conformance *(new)* | `in-character`, `drift-warning` |

### Part B — scorecard (line 5 onward)

```markdown

## Scorecard

| Dimension | Score (1–5) | Reason (one sentence; required if score ≤ 3) |
|---|---|---|
| Accuracy | <n> | <reason or — if n≥4> |
| Completeness | <n> | — |
| Consistency | <n> | — |
| Timeliness | <n> | — |
| Uniqueness | <n> | — |
| Validity | <n> | — |

**Composite:** <weighted average to 1 dp> · **Bar to ship:** <pass-bar for this reviewer, see table below>

## Notes
- <one bullet per advisory observation>
```

Composite is the unweighted mean unless the reviewer's pass-bar (below) overrides.

---

## The six dimensions (one definition, used by every reviewer)

| Dimension | Asks | Bad signal |
|---|---|---|
| **Accuracy** | Are the facts right? Sources verifiable? | Numbers without baseline, unverifiable claims |
| **Completeness** | Is anything material missing? | Failure modes unnamed, edge cases ignored |
| **Consistency** | Does it cohere internally and against canon? | Name drift (Richard Ng vs Constantine), tone shift, contradicting earlier sections |
| **Timeliness** | Is it current and on-cadence? | Stale claim, missed signpost, late-shipping artifact |
| **Uniqueness** | Is it differentiated, not generic? | Reads like a generic SaaS post / template output |
| **Validity** | Are claims falsifiable / testable? | "This is safe" without eval or threshold |

Score 1–5 (5 = excellent, 1 = unusable). Any score ≤ 3 requires a one-sentence reason.

## Pass-bars per reviewer

A reviewer may write a `pass` verdict only if the scorecard meets the bar.

| Reviewer | Required minimums | Composite floor |
|---|---|---|
| riddler | Accuracy ≥ 4 · Validity ≥ 4 · Consistency ≥ 4 | 4.0 |
| vicki-vale | Uniqueness ≥ 4 · Consistency ≥ 4 | 3.8 |
| peer-review | Accuracy ≥ 4 · Completeness ≥ 4 · Consistency ≥ 4 | 4.0 |
| prd-readiness | Completeness ≥ 4 · Consistency ≥ 4 · Validity ≥ 4 | 4.0 |
| research-sufficiency | Accuracy ≥ 4 · Completeness ≥ 4 · Validity ≥ 3 · Timeliness ≥ 3 · Uniqueness ≥ 3 | 3.8 |
| go-nogo | Completeness ≥ 4 · Validity ≥ 4 · Timeliness ≥ 4 | 4.0 |
| build-review | Validity ≥ 4 · Accuracy ≥ 4 · Completeness ≥ 3 | 3.8 |
| eval-review | Accuracy ≥ 4 · Validity ≥ 4 · Uniqueness ≥ 3 · Timeliness ≥ 3 | 4.0 |
| voice-conformance | Consistency ≥ 4 · Uniqueness ≥ 4 | 4.0 |

If the bar is not met, the reviewer downgrades to `conditional-*` and lists the required edits to clear the bar, or refuses to write the file (`block` / `bounce` / `fail`).

## Hash discipline

The hash on line 1 is computed **after** all required edits are applied, against the final artifact bytes. A stale hash invalidates the verdict — the publish hook recomputes and rejects on mismatch.

```bash
HASH=$(shasum -a 256 "$ARTIFACT" 2>/dev/null | awk '{print $1}' || sha256sum "$ARTIFACT" | awk '{print $1}')
```

## Roll-up

Any tool can compute a 30-day quality dashboard with:

```bash
grep -h '^| [A-Z]' Reviews/**/*-passed | sort | uniq -c
```

(or a smarter script that parses the scorecard table). The point is the format is grep-able by design.

## Anti-patterns

- Skipping the scorecard "to save time" → verdict is invalid; treat as no review
- Scoring everything 5 with no reasons → the reviewer is doing nothing useful; Riddler will block
- Editing a verdict file post-write → hash mismatch invalidates it; write a new one instead
- Composite ≥ bar but a required minimum is missed → still a fail; the bar is the conjunction of both

## Migration

Existing verdict files (4-line header, no scorecard) remain valid as historical artifacts but should be re-issued with a scorecard the next time the underlying artifact is touched. Do not back-fill; that's busywork.
