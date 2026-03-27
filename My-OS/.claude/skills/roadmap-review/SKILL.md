# Roadmap Review

**Agent:** Strategy & Roadmap — see `Agents/strategy-roadmap/AGENT.md` for full context.
**Sub-agent:** Spawn `project-scanner` to assess milestone status across projects.
**Detailed process:** See `Workflows/roadmap-review/workflow-spec.md` for full step-by-step.

Usage: "roadmap review" — weekly check-in on roadmap progress and deliverable status. Best run Monday or Friday.

## Steps

1. **Pull current state** — read:
   - `Tasks/active.md` — what's in flight
   - `Tasks/backlog.md` — what's queued
   - `Projects/cdp-implementation/brief.md` — milestone status
   - `GOALS.md` — 30-60-90 day targets
   - `Knowledge/Reference/metrics/latest.md` — key metrics (if available)

2. **Review milestones** — for each active milestone:

| Milestone | Target Date | Status | On Track? | Notes |
|-----------|-------------|--------|-----------|-------|
| | | | 🟢/🟡/🔴 | |

3. **Identify risks & blockers** — for each 🟡 or 🔴 item:
   - Root cause
   - What's needed to unblock
   - Who to talk to
   - Whether timeline adjustment needed

4. **Reprioritize active tasks:**
   - Archive completed items
   - Pull next-up from backlog
   - Ensure alignment to nearest milestone
   - Confirm: highest-leverage work in focus?

5. **Prepare for Jervis** (if 1:1 or weekly update coming):
   - 2–3 key updates
   - Decisions needed from him
   - Suggest running `/weekly-update` to draft the update

## Output Format

```
**Roadmap Review — [Date]**

**Overall Status:** [🟢/🟡/🔴]

**Milestones:**
[table]

**Risks & Blockers:**
- [risk/blocker with mitigation]

**Task Reprioritization:**
- Archived: [items]
- Pulled in: [items]
- Focus this week: [top 2-3 items]

**For Jervis:**
- [key updates / decisions needed]
```

After review, offer:
- "Update `Tasks/active.md` with these changes?"
- "Run `/weekly-update` to draft a status update?"
