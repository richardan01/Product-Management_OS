# Go / No-Go

**Agent:** Launch Manager

Run a structured go/no-go decision for [project]. Use this 24–48 hours before planned launch.

## Steps

1. **Read:**
   - `Projects/[project]/launch-plan.md` — checklist status
   - `Projects/[project]/uat-results.md` — QA sign-off
   - `Knowledge/Reference/risk-register.md` — unmitigated risks
   - `Tasks/active.md` — any open P0 items

2. **Score each gate:**

| Gate | Criteria | Status | Decision |
|------|----------|--------|----------|
| Product | All P0 acceptance criteria met and tested | 🟢/🟡/🔴 | Go/No-Go |
| Data | Quality checks passing, PII confirmed | 🟢/🟡/🔴 | Go/No-Go |
| Stakeholders | Training done, users confirmed ready | 🟢/🟡/🔴 | Go/No-Go |
| Comms | Announcement drafted, [YOUR_MANAGER] briefed | 🟢/🟡/🔴 | Go/No-Go |
| Risk | No unmitigated 🔴 risks | 🟢/🟡/🔴 | Go/No-Go |
| Rollback | Rollback plan documented and tested | 🟢/🟡/🔴 | Go/No-Go |

3. **Final decision** (map gate colors to the `bad`/`sad` taxonomy in `Evals/severity-taxonomy.md`: 🔴 = `bad`, 🟡 = `sad`):
   - Any 🔴 (`bad`) → **NO-GO** — list blockers with owners and ETAs
   - 0 🔴 but **≥ 3 🟡** (`sad` stacking rule) → **NO-GO** — too many open conditions to ship safely
   - 0 🔴, 1–2 🟡 → **CONDITIONAL GO** — list conditions with hard deadlines
   - All green → **GO** — confirm launch date and send comms

4. **Output:**

```
**Go/No-Go Decision — [Project] — [Date]**

**Planned Launch:** [date/time]

**Gate Results:**
[table]

**Decision: GO / NO-GO / CONDITIONAL GO**

**Conditions / Blockers:**
- [item — owner — must resolve by: date]

**Next action:** [confirmed launch / rescheduled to: date]
```

---

**Next Steps:**
- Decision is GO → `launch-comms [project]` — send the announcement now
- Decision is NO-GO → `risk-register` — log the blockers as tracked risks
- Post-launch → `post-launch [project]` — schedule 1-week review

---

## Verdict file (per `_Registry/reviewer-verdict-schema.md`)

On GO (or CONDITIONAL-GO), write `<launch-doc-path>.go-nogo-passed` with the byte-exact header + scorecard:

```
<sha256>
go                  ← or conditional-go
go-nogo
<ISO 8601 UTC>

## Scorecard

| Dimension | Score (1–5) | Reason (required if ≤ 3) |
|---|---|---|
| Accuracy | <n> | — |
| Completeness | <n> | — |
| Consistency | <n> | — |
| Timeliness | <n> | — |
| Uniqueness | <n> | — |
| Validity | <n> | — |

**Composite:** <x.x> · **Pass-bar:** Completeness ≥ 4 · Validity ≥ 4 · Timeliness ≥ 4 · composite ≥ 4.0
```

NO-GO writes no verdict file; instead, log blockers to `risk-register`.
