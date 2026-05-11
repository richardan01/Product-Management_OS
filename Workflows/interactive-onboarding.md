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

## Setup capture schema

Maintain this working schema during the interview. Preserve placeholders or mark `Unknown` when the user is unsure; do not invent details.

```markdown
## Setup capture

### Identity
- Name:
- Role:
- Company / organization:
- Team / domain:
- Manager or primary sponsor:

### OS purpose
- Primary purpose:
- Weekly jobs-to-be-done:
- Useful within 7 days if:

### Operating style
- Default persona:
- Tone:
- Detail level:
- Pushback level:
- Work style:
- Decision style:
- Review style:
- Tone to avoid:

### Cadence
- Planning rhythm:
- Week starts on:
- Recurring meetings / reviews:
- First commands to use:

### Active work
- P0 this week:
- P1 soon:
- P2 / backlog:
- Blockers:
- Promised follow-ups:

### Goals and metrics
- 30-day outcomes:
- 60-day outcomes:
- 90-day outcomes:
- Metrics / evidence:
- Development goals:

### Stakeholders and projects
- Key people:
- Approvers / blockers / users:
- Anchor project:
- Open decisions:
- Known risks:

### Boundaries
- Never write to files:
- May edit without asking:
- Requires confirmation:
- Repo visibility:
```

Use the schema to generate the Phase 8 confirmation summary and the file-by-file edit plan.

## Phase 0 — Confirm first-run context

Ask:

1. Is this OS for your day job, career work, a side project, learning, or a mix?
2. What name, role, company / organization, and team should the OS use?
3. Are there any placeholders you want to preserve for now instead of filling in?

Record identity details in the setup capture. If the user prefers not to store company or people names, preserve placeholders and reflect that boundary in `CLAUDE.md`.

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

### File-by-file edit plan
- `CLAUDE.md`: identity, operating style, routing, cadence, privacy boundaries
- `GOALS.md`: 30-60-90 outcomes, metrics, stakeholders, development goals
- `Tasks/active.md`: P0/P1 work, blockers, near-term commitments
- `Tasks/backlog.md`: P2 work and future candidates
- `Tasks/follow-ups.md`: promised follow-ups and owners
- `Knowledge/People/...`: confirmed stakeholder profiles only
- `Projects/.../brief.md`: anchor project context, open decisions, risks
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

## Dry-run acceptance test

Use this test before merging onboarding changes or after changing the setup flow. The goal is to validate that a new user can configure the OS without the assistant inventing private context or writing files too early.

### Test profile

Run the workflow with this fake user profile:

```markdown
- Name: Jordan Lee
- Role: Senior Product Manager
- Company / organization: Acme AI
- Team / domain: Growth Platform
- Manager or primary sponsor: Priya Shah
- Primary purpose: Day-job execution plus stakeholder management
- Default persona: Executive operator
- Tone: concise, direct, low-drama
- Detail level: standard
- Pushback level: medium; challenge unclear goals, missing evidence, and risky tradeoffs
- Work style: weekly planning plus daily focus check
- Decision style: recommendation-first with tradeoffs
- Review style: strict PM craft review for PRDs and roadmap artifacts
- Planning rhythm: weekly planning, daily `/today`, Friday `/weekly-update`
- Anchor project: Activation funnel redesign
- Key stakeholders: Priya Shah, Marco Chen, Elena Torres, Sam Rivera
- Privacy boundaries: never store compensation, health, private HR feedback, or sensitive customer data
```

### Pass criteria

The dry run passes only if the assistant:

1. Starts from the trigger phrase without requiring the user to know internal file structure.
2. Asks questions in small batches instead of dumping the full schema at once.
3. Captures purpose, operating style, cadence, active work, goals, stakeholders, projects, and privacy boundaries.
4. Preserves unknowns as placeholders or `Unknown` instead of inventing facts.
5. Produces a Phase 8 confirmation summary with a file-by-file edit plan.
6. Does not edit files until the user explicitly approves the proposed setup.
7. Recommends `/today`, `/meeting-prep [person]`, and `/weekly-update` after confirmed setup.

### Fail signals

Tighten this workflow before merging if the assistant:

- Assumes Batman mode when the user chose another persona.
- Writes files before confirmation.
- Stores private information the user excluded.
- Produces generic goals that do not reflect the user's stated purpose.
- Proposes new top-level folders or unrelated architecture changes during onboarding.
- Skips the first-week usefulness question.
