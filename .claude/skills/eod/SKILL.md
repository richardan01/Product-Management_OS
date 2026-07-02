---
name: eod
description: End-of-day closing loop for task hygiene, blockers, and tomorrow priority planning.
allowed-tools: Read, Glob, Grep, Edit, Write
---

# /eod

Use this skill to close the daily loop so `/today` remains reliable.

## Required reads
1. `Tasks/active.md`
2. `GOALS.md`
3. `CLAUDE.md` (Current Context block only, if update is needed)

## Interaction flow
1. Ask the user what was completed today.
2. Ask what remains open from current P0/P1 work.
3. Ask for any new blockers discovered today.
4. Ask for any new follow-ups or commitments that must be captured.
5. Propose tomorrow's likely P0 focus.
6. **Online eval monitoring (Hamel §9.2).** Pick **one** AI-assisted output produced today (a synthesis, PRD draft, weekly update, meeting prep, or onboarding session). In ≤ 5 minutes, grade it against the relevant eval suite's criteria. Log any ❌ to `Evals/run-log.md` under a `production-monitoring` header so drift is caught before the next full suite run. If nothing AI-assisted shipped today, skip.
7. **Trace capture (weekly, not daily).** On Fridays only, invoke the `trace-collector` sub-agent to sweep the week's outputs into `Evals/<suite>/_traces/`. It is read-only on the originals and only appends to the CSV — no edits to actual artifacts.
8. **Durable memory capture (the maintenance loop).** Scan today's session for **at most one** durable takeaway — a revealed user preference, a recurring working pattern, or an operating decision. Run it through the 5-question write-gate in `Memory/MEMORY_POLICY.md`. If it passes, propose appending a single dated one-line entry to `Memory/SESSION_LOG.md` (the append-only staging log `/retro` later distills). If nothing clears the gate, skip — most days will. This is the capture half of the loop; `/retro` does the distill half.

## Update behavior (proposal-only until confirmed)
- Move completed items into **Done This Sprint** in `Tasks/active.md`.
- Carry unfinished P0/P1 work forward in `Tasks/active.md`.
- Add new blockers to the blocker section in `Tasks/active.md`.
- Add new follow-ups to `Tasks/follow-ups.md` when relevant.
- Update the **Current Context** block in `CLAUDE.md` only when one of these triggers fires: active P0 changed, new live risk or blocker, or a key date/deadline shifted.
- Append a durable takeaway to `Memory/SESSION_LOG.md` only when step 8 produced one that cleared the write-gate.

## Hard rule
Do **not** edit any file until the user gives explicit confirmation.

## Output format
Return exactly these sections:

- **Done today**
- **Still open**
- **Blockers**
- **Follow-ups captured**
- **Tomorrow's recommended P0**
- **Durable takeaway** (the one memory line proposed for `Memory/SESSION_LOG.md`, or "none today")
- **Files proposed for update**

In the last section, list the specific files you want to update and why.
