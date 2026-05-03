# RegEval gold dataset

**Format:** `gold.jsonl` — one JSON object per line.

```json
{"id": "reg-0001", "input": "<scenario text>", "gold_label": "accept|reject|abstain", "gold_rationale": "<one sentence>", "annotators": ["RC", "X"], "agreement": "unanimous|majority|tied"}
```

**Domain:** regulated-fintech LLM output decisions (the RegEval thesis domain). Each item is a scenario where a downstream LLM is asked to produce a customer-facing answer, and the gold label is whether the *scaffold* should let the answer ship (`accept`), block it (`reject`), or refuse to decide (`abstain`).

## Day-30 target

- N ≥ 100 items
- Annotators: 2 minimum, with documented inter-annotator agreement (Cohen's κ ≥ 0.70 between annotators before any item enters gold)
- Item distribution: 40% accept · 40% reject · 20% abstain (do not over-weight the easy class)
- Adversarial planted items: ≥ 10% of total (analogous to discovery-synthesis fixture practice)

## Build protocol

1. Draft items in `_drafts/` (not in this folder until labelled).
2. Two annotators label independently. Disagreements adjudicated by a third reader; if still tied, the item is excluded from gold (logged in `_excluded.md`).
3. Promote labelled items into `gold.jsonl` only after κ ≥ 0.70 between annotators on the batch.
4. Snapshot `gold.jsonl` weekly into `snapshots/YYYY-MM-DD.jsonl` so experiment lineage is reproducible.

## Files

- `gold.jsonl` — the live gold set (does not yet exist; Day-30 deliverable)
- `test_kappa.jsonl` — small fixture for verifying the κ implementation produces 0.40 ± 0.01 (see metric.md)
- `_drafts/` — unlabelled candidates
- `_excluded.md` — items rejected from gold, with reason
- `snapshots/` — weekly snapshots for lineage

## Anti-patterns

- Adding to `gold.jsonl` mid-week without a snapshot first (breaks lineage)
- Single-annotator labels (Riddler will block any claim built on these)
- Reusing draft items the scaffold author has already seen as labelled gold (leakage)
