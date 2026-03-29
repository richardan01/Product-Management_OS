# Go / No-Go

**Agent:** Launch Manager — see `Agents/launch-manager/launch-manager.md` for full context.

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
| Comms | Announcement drafted, Jervis briefed | 🟢/🟡/🔴 | Go/No-Go |
| Risk | No unmitigated 🔴 risks | 🟢/🟡/🔴 | Go/No-Go |
| Rollback | Rollback plan documented and tested | 🟢/🟡/🔴 | Go/No-Go |

3. **Final decision:**
   - All green → **GO** — confirm launch date and send comms
   - Any red → **NO-GO** — list blockers with owners and ETAs
   - Yellow items → **CONDITIONAL GO** — list conditions with hard deadlines

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
