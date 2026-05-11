# Workflow: Interactive Onboarding

Use this workflow when a user first downloads, forks, or clones ProductManagement-OS and asks to set it up.

Trigger phrases:
- `Computer, onboard me into this OS`
- `Set up this template for me`
- `Help me configure my PM OS`
- `Start onboarding`

## Operating rules

1. Be interactive. Do not assume the user's purpose, persona, tasks, goals, company, or career target.
2. Ask in small batches. Prefer 3–5 questions at a time so the user can answer quickly.
3. Offer choices, but always allow a custom answer.
4. Summarize the proposed setup before editing files.
5. Only write files after explicit confirmation.
6. Preserve placeholders when the user is unsure.
7. Keep the setup template-friendly: no references to the original template author's local folder structure.

## Phase 1 — Choose purpose

Ask:

1. What is the primary purpose of this OS?
   - Day-job execution
   - Career transition
   - Founder / product build
   - Research and writing
   - Learning / personal development
   - Mixed setup
   - Custom
2. What should this OS help you do every week?
3. What would make this OS feel useful within the first 7 days?

Record the answer as the user's operating purpose in `CLAUDE.md` and goal framing in `GOALS.md`.

## Phase 2 — Choose persona and voice

Ask:

1. What persona should the assistant use by default?
   - Batman strategic operator — direct, contingency-first, high standards
   - Executive operator — concise, outcome-driven, low drama
   - Research partner — careful, evidence-first, source-aware
   - Product coach — reflective, developmental, asks good questions
   - Builder — pragmatic, prototype-first, implementation-oriented
   - Minimalist — terse, checklist-first, low ceremony
   - Custom
2. When should the assistant push back?
3. What tone should it avoid?

Update `CLAUDE.md` and `_Registry/voice-map.md` only after the user confirms.

## Phase 3 — Define operating cadence

Ask which cadence the user wants:

- Daily brief via `/today`
- Weekly update via `/weekly-update`
- Sprint planning and retro
- Monthly strategy review
- Quarterly planning
- Ad hoc only

Then ask:

1. What day does the week start?
2. What cadence do you use for planning: weekly, sprint, monthly, quarterly, or custom?
3. Which meetings or reviews should the OS prepare you for?

Reflect the answer in `CLAUDE.md`, `Tasks/active.md`, and recurring workflow suggestions.

## Phase 4 — Capture current tasks

Ask the user for:

1. 1–3 P0 tasks that must move this week
2. 3–5 P1 tasks that should move soon
3. P2 / backlog items
4. Blockers and who owns them
5. Follow-ups already promised to other people

Propose updates to:

- `Tasks/active.md`
- `Tasks/backlog.md`
- `Tasks/follow-ups.md`

## Phase 5 — Capture goals and metrics

Ask:

1. What are your 30-day outcomes?
2. What are your 60-day outcomes?
3. What are your 90-day outcomes?
4. Which metrics or evidence will prove progress?
5. What personal development goals should the OS reinforce?

Propose updates to `GOALS.md`.

## Phase 6 — Capture stakeholders and projects

Ask:

1. Who are the 4–6 people the OS should understand first?
2. Who approves, blocks, advises, or uses your work?
3. What is your anchor project or primary workstream?
4. What decisions are open on that project?
5. What risks are already visible?

Propose updates to:

- `Knowledge/People/[name].md`
- `Projects/[YOUR_ANCHOR_PROJECT]/brief.md`
- `Tasks/active.md`

## Phase 7 — Privacy and editing boundaries

Ask:

1. What information should never be written into files?
2. Which files may the assistant edit without asking every time?
3. Which files require confirmation before edits?
4. Is this repo private, public, or intended to become a sanitized public template?

Add the boundaries to `CLAUDE.md`.

## Phase 8 — Confirmation summary

Before writing, show:

```markdown
## Proposed setup

### Purpose
- ...

### Persona
- ...

### Cadence
- ...

### Initial tasks
- P0: ...
- P1: ...
- P2: ...

### Goals
- 30 days: ...
- 60 days: ...
- 90 days: ...

### Stakeholders
- ...

### Files I propose to update
- `CLAUDE.md`
- `GOALS.md`
- `Tasks/active.md`
- `Tasks/backlog.md`
- `Tasks/follow-ups.md`
- `Knowledge/People/...`
- `Projects/.../brief.md`

### Boundaries
- Never write: ...
- Ask before editing: ...
```

Ask: `Should I apply these setup changes?`

Only proceed after the user says yes.

## Phase 9 — Write and next actions

After confirmed edits:

1. Write only the confirmed files.
2. Show a concise change summary.
3. Recommend the first three commands:
   - `/today`
   - `/meeting-prep [person]`
   - `/weekly-update`
4. Ask whether the user wants to run `/today` immediately.
