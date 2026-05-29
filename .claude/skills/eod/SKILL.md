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

## Update behavior (proposal-only until confirmed)
- Move completed items into **Done This Sprint** in `Tasks/active.md`.
- Carry unfinished P0/P1 work forward in `Tasks/active.md`.
- Add new blockers to the blocker section in `Tasks/active.md`.
- Add new follow-ups to `Tasks/follow-ups.md` when relevant.
- Update the **Current Context** block in `CLAUDE.md` only when one of these triggers fires: active P0 changed, new live risk or blocker, or a key date/deadline shifted.

## Hard rule
Do **not** edit any file until the user gives explicit confirmation.

## Output format
Return exactly these sections:

- **Done today**
- **Still open**
- **Blockers**
- **Follow-ups captured**
- **Tomorrow's recommended P0**
- **Files proposed for update**

In the last section, list the specific files you want to update and why.
