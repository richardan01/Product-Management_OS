# Workflow: Interactive Onboarding

Use this workflow when a user first downloads, forks, or clones ProductManagement-OS and asks to set it up.

This workflow is harness-neutral. It runs the same way in **Claude Code** (entry point: `CLAUDE.md`), **Codex CLI** (entry point: `AGENTS.md`), and **Gemini CLI** (entry point: `GEMINI.md`). Each entry-point file points back here. The configuration the workflow writes — persona, tone, routing, quality gates, privacy boundaries — lives in `CLAUDE.md` and is respected by all three harnesses regardless of which one ran the setup. The filename is historical; do not duplicate the file per harness.

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
- OS mode:
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
- Taste — turns me off:
- Taste — ideal response feel:

### Thought frameworks
- Tradeoff priority:
- Evidence standard:
- Decision certainty bar:
- Acceptable failure:

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
- OKR ladder-up:
- Single proof metric:
- Goal 1 kill condition:

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

**Step 0a — OS context (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below. Set `multiSelect: true` so the user can pick more than one if their situation spans multiple contexts.

```
question: "What is this OS primarily for? (Select all that apply)"
header: "OS context"
multiSelect: true
options:
  - label: "Day job"
    description: "Current role — product execution, stakeholder updates, roadmap hygiene"
  - label: "Career work"
    description: "Positioning, interviews, frontier-lab prep, or narrative building"
  - label: "Side project / build"
    description: "Founder work, personal product, or AI prototype"
  - label: "Research or writing"
    description: "Discovery, synthesis, evidence quality, long-form thinking"
```

> **Note:** The tool auto-adds an "Other" option — users who select it for **learning / personal development** or a mix not covered above should describe it in the follow-up text. Record their answer verbatim.

**Step 0b — Identity and placeholders (ask conversationally):**

Ask in one message:
1. "What name, role, company / organization, and team should the OS use?"
2. "Are there any placeholders you'd prefer to leave blank for now rather than fill in?"

Record identity details in the setup capture. If the user prefers not to store company or people names, preserve placeholders and reflect that boundary in `CLAUDE.md`.

## Phase 1 — Choose purpose and OS mode

Start by offering the user a practical **OS mode**. Explain that this is a customizable starting package — not a permanent choice — and that the user can override commands, gates, persona, and routing before any files are written.

| OS mode | Use when | Default surface |
|---|---|---|
| **Day-job PM** | The main job is current product execution, stakeholder updates, and roadmap hygiene | `/today`, `/weekly-update`, `/meeting-prep`, `/peer-review` |
| **AI Builder PM** | The user builds AI/LLM products or wants AI PM craft: evals, model-risk reviews, prompt/tool design, launch gates | `Templates/prd-ai-feature.md`, `/evals`, `/eval-review`, `/build-review`, `/test-plan` |
| **Research PM** | The user needs discovery, synthesis, evidence quality, and decision readiness | `/synthesize-research`, `/research-sufficiency`, `/wiki-ingest`, `/wiki-query` |
| **Career transition** | The user is positioning for roles, interviews, or frontier-lab research | `/career-narrative`, `/frontier-lab-interview-prep`, optional Gotham strategic layer |
| **Minimalist** | The user wants low ceremony and few default commands | `/today`, `/weekly-update`, light `/peer-review` |
| **Custom** | The user wants to mix surfaces manually | User-chosen commands, quality gates, persona, and routing |

**Step 1a — OS mode (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below. Remind the user this is not a permanent choice — they can override commands, gates, persona, and routing before any files are written.

```
question: "Which OS mode should we start from?"
header: "OS mode"
multiSelect: false
options:
  - label: "Day-job PM"
    description: "Current role execution: stakeholder updates, roadmap hygiene. Surfaces /today, /weekly-update, /meeting-prep, /peer-review"
  - label: "AI Builder PM"
    description: "Building AI/LLM products or developing AI PM craft: evals, model-risk, prompt/tool design. Surfaces /evals, /eval-review, /build-review, /test-plan"
  - label: "Research PM"
    description: "Discovery, synthesis, evidence quality, decision readiness. Surfaces /synthesize-research, /research-sufficiency, /wiki-ingest, /wiki-query"
  - label: "Career transition"
    description: "Positioning for roles, interviews, or frontier-lab research. Surfaces /career-narrative, /frontier-lab-interview-prep, optional Gotham layer"
```

> If the user needs **Minimalist** or **Custom**, they will select "Other" and describe their preference. Record it accordingly.

**Step 1b — Primary purpose (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below.

```
question: "What is the primary purpose of this OS?"
header: "Primary purpose"
multiSelect: false
options:
  - label: "Day-job execution"
    description: "Ship the roadmap, manage stakeholders, run the product cadence"
  - label: "Career transition"
    description: "Position for a new role, prep for interviews, build narrative"
  - label: "Founder / product build"
    description: "Validate ideas, build prototypes, make fast decisions with limited data"
  - label: "Research and writing"
    description: "Synthesize evidence, produce high-quality artifacts, build knowledge"
```

> For **Learning / personal development** or **Mixed setup**, the user will select "Other." Record their free-text answer as-is.

**Step 1c — Weekly jobs and first-week usefulness (ask conversationally):**

Ask in one message:
1. "What should this OS help you do every week?"
2. "What would make this OS feel useful within the first 7 days?"

Record the OS mode and operating purpose in `CLAUDE.md`, and reflect the goal framing in `GOALS.md`. If the user picks **AI Builder PM**, prefer `Templates/prd-ai-feature.md` for AI/LLM product work unless they explicitly request the generic PRD template.

## Phase 2 — Choose persona and voice

**Step 2a — Default persona (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below. Tell the user: "Each persona turns on a different set of quality gates, routing, and slash commands — see the effects matrix below the question."

```
question: "What persona should the assistant use by default?"
header: "Persona"
multiSelect: false
options:
  - label: "Batman strategic operator"
    description: "Direct, terse, contingency-first, high standards. Gates: /riddler + /vale mandatory pre-publish. Routes all 12 Gotham agents."
  - label: "Executive operator"
    description: "Concise, outcome-driven, low drama. Gates: /peer-review default, /go-nogo for launches. Batman layer available but not routed."
  - label: "Research partner"
    description: "Evidence-first, careful, citation-aware. Gates: /research-sufficiency + /peer-review. Routes Oracle patterns."
  - label: "Product coach"
    description: "Reflective, asks good questions, developmental. Gates: /peer-review light edit."
```

> For **Builder / AI PM**, **Minimalist**, or **Custom**, the user selects "Other." Record their free-text answer and map it to the closest effects-matrix row or ask for clarification.

**Step 2b — Pushback level (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below.

```
question: "When should the assistant push back on your thinking?"
header: "Pushback"
multiSelect: false
options:
  - label: "Low — mostly execute, flag only serious issues"
    description: "Challenge only when something is clearly wrong or risky; otherwise run with the request"
  - label: "Medium — challenge unclear goals and missing evidence"
    description: "Push back when goals are vague, evidence is weak, or tradeoffs are hidden"
  - label: "High — adversarial review is the default"
    description: "Actively stress-test every plan, decision, and claim; assume the user wants to be challenged"
```

**Step 2c — Tone and taste (ask conversationally):**

Ask in one message:
1. "What tone should the assistant avoid? (e.g., 'Never start with Certainly!', 'Don't bullet-point everything')"
2. "When an assistant gives a great response to a hard question — what does that feel like? Describe it in your own words."

Record the answers in the capture schema as `Taste — turns me off` and `Taste — ideal response feel`. These are free text, not dropdowns — use the user's exact words.

Update `CLAUDE.md` and `_Registry/voice-map.md` only after the user confirms.

### Persona effects matrix

Tell the user explicitly which parts of the OS each persona turns on or off. This is what they are actually configuring.

| Persona | Default tone | Strategic layer | Quality gates | Slash commands surfaced first | Agents pruned from routing |
|---|---|---|---|---|---|
| **Batman strategic operator** | Direct, terse, imperative | `Agents/Gotham/Computer/` (all 12) | `/riddler` + `/vale` mandatory pre-publish | `/today`, `/cowl-up`, `/riddler`, `/vale` | None |
| **Executive operator** | Concise, outcome-driven | Skills + Workflows only | `/peer-review` default; `/go-nogo` for launches | `/today`, `/weekly-update`, `/meeting-prep`, `/peer-review` | All Batman agents (kept as optional reference, not routed by default) |
| **Research partner** | Evidence-first, careful, citation-aware | Skills + `Oracle` reference patterns | `/research-sufficiency` + `/peer-review` | `/synthesize-research`, `/research-sufficiency`, `/wiki-ingest`, `/wiki-query` | Batman, Selina Kyle, Henri Ducard, Nightwing |
| **Product coach** | Reflective, asks good questions | Skills + Workflows | `/peer-review` light edit | `/today`, `/retro`, `/meeting-prep` | Batman, Selina Kyle, Robin |
| **Builder / AI PM** | Pragmatic, eval-first, model-aware | Skills + `Lucius Fox` + `Oracle` reference (build + research) | `/eval-review` + `/build-review` + `/test-plan` mandatory pre-deployment | `/today`, `/evals`, `/eval-review`, `/build-review`, `/test-plan`, `/synthesize-research` | Batman, Selina Kyle, Bruce Wayne (career) |
| **Minimalist** | Terse, checklist-only | Skills only | `/peer-review` light edit | `/today`, `/weekly-update` | All Batman agents |
| **Custom** | User-defined | User-chosen | User-chosen | User-chosen | User-chosen |

When the user selects a non-Batman persona:

1. Record the persona in `CLAUDE.md` → `Default persona`.
2. Note in `CLAUDE.md` → `Routing` that the Batman layer is **available but not routed by default**.
3. Do **not** delete `Agents/Gotham/Computer/` — preserve the files so the user can opt back in later by re-running onboarding.
4. Set the quality-gate defaults in `CLAUDE.md` to match the persona's row above.

Confirm the persona and the routed agent set with the user before writing.

## Phase 3 — Define operating cadence

**Step 3a — Operating cadence (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below. Set `multiSelect: true` — the user may use more than one cadence.

```
question: "Which cadences do you want the OS to support? (Select all that apply)"
header: "Cadence"
multiSelect: true
options:
  - label: "Daily brief via /today"
    description: "Start each day with a priority check, calendar prep, and follow-up scan"
  - label: "Weekly update via /weekly-update"
    description: "End-of-week stakeholder summary and progress snapshot"
  - label: "Sprint planning and retro"
    description: "Two-week sprints with structured planning and retrospective"
  - label: "Monthly / quarterly planning"
    description: "OKR-level goal-setting, strategy reviews, and portfolio check-ins"
```

> **Note:** The tool auto-adds an "Other" option — users who work **ad hoc only** or have a non-standard cadence should select it and describe their rhythm. Record their answer verbatim.

**Step 3b — Week anchor and meetings (use `AskUserQuestion` + conversational):**

> **Tool:** Call `AskUserQuestion` for the week-start question.

```
question: "What day does your work week start?"
header: "Week start"
multiSelect: false
options:
  - label: "Monday"
    description: "Standard Mon–Fri week"
  - label: "Sunday"
    description: "Sun–Sat week"
  - label: "Tuesday"
    description: "Rolling or shift-based week"
```

Then ask conversationally:
- "Which recurring meetings or reviews should the OS help you prepare for? (e.g., weekly team sync, monthly business review, quarterly planning)"

Reflect the answers in `CLAUDE.md`, `Tasks/active.md`, and recurring workflow suggestions.

## Phase 4 — Capture current tasks

Ask the user for:

1. 1–3 P0 tasks that must move this week
2. 3–5 P1 tasks that should move soon
3. P2 / backlog items
4. Blockers and who owns them
5. Follow-ups already promised to other people

**Interactive read-back rule.** After capture, do **not** propose any file updates yet. Read each priority level back to the user as a separate list:

1. "Here are the P0 tasks I captured: [list]. Does this match what you're working on? Anything missing or wrong?"
2. After user confirms P0 — repeat for P1.
3. After user confirms P1 — repeat for P2.
4. After P2 — repeat for blockers, then for follow-ups.

Do not bulk-approve all five categories in one ask. Only after each category is individually confirmed, propose updates to:

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

Then ask three follow-up questions to capture strategic alignment:

> "Three quick ones on strategy:
> 1. What company or team OKR does your 90-day goal ladder up to? If you don't know or it's not set yet, say so — that's data too.
> 2. If you had to name the ONE metric that, if it moves, proves your quarter was a success — what would it be?
> 3. What specific thing would force you to abandon or pivot your top goal?"

Record answers in the capture schema as `OKR ladder-up`, `Single proof metric`, and `Goal 1 kill condition`. "Unknown / not yet set" is a valid answer for OKR ladder-up — do not skip the question or invent a company OKR. The kill condition must be a specific event or trigger, not a category (e.g., "If Priya kills the activation funnel project" not just "stakeholder change").

Propose updates to `GOALS.md` including the new "Strategic alignment" section.

## Phase 5B — How you think

Open with: "Four quick questions about how you make decisions — skip any you want."

**Question 1 — Tradeoff hierarchy (ask conversationally):**

Ask: "When speed, quality, and learning are in tension, what's your default order? (e.g., quality > speed > learning)"

This is free text — the user defines their own order. Do not offer a dropdown.

**Question 2 — Evidence standard (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below.

```
question: "What convinces you most when making a decision?"
header: "Evidence"
multiSelect: false
options:
  - label: "Good quantitative data"
    description: "Metrics, experiment results, analytics — numbers move me"
  - label: "Expert judgment"
    description: "I weight domain expertise and trusted advisors heavily"
  - label: "Direct user feedback"
    description: "What users say in research, support, or interviews carries most weight"
  - label: "My own synthesis"
    description: "I integrate multiple signals and trust my pattern-matching"
```

**Question 3 — Decision bar (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below.

```
question: "What confidence level do you need before committing to a significant decision?"
header: "Decision bar"
multiSelect: false
options:
  - label: "~70% — good enough to move"
    description: "Speed matters; I'd rather iterate than wait for certainty"
  - label: "~80% — reasonable confidence"
    description: "I want a solid majority of signals pointing the same way"
  - label: "90%+ — high certainty required"
    description: "I don't commit until most unknowns are resolved"
```

**Question 4 — Acceptable failure (ask conversationally):**

Ask: "What kind of failure is OK — a learning you'd accept — versus what kind is not OK because it was avoidable? Give me a concrete example of each if you can."

This is free text — the kill condition must be a specific pattern, not a category.

---

Record answers in the capture schema under `Thought frameworks`. If the user skips a question, record it as `Not specified` — do not invent a default. These answers flow into `CLAUDE.md` → `Thought frameworks` section and will be used in every session to calibrate how tradeoffs, evidence, and risk are framed.

## Phase 6 — Capture stakeholders and projects

Ask:

1. Who are the 4–6 people the OS should understand first?
2. Who approves, blocks, advises, or uses your work?
3. What is your anchor project or primary workstream?
4. What decisions are open on that project?
5. What risks are already visible?

**Per-stakeholder confirmation rule.** Do **not** draft any `Knowledge/People/` file upfront. For each person the user named, before drafting a profile, ask in conversational back-and-forth:

1. "[Name] — what's their role and seniority?"
2. "Why do they matter to your work — approver, blocker, advisor, user, partner?"
3. "Anything I should know about their working style or preferences?"

Only after the user has confirmed those three fields for that person do you propose a `Knowledge/People/[name].md` draft. Confirm each person's draft before moving to the next.

Then propose updates to:

- `Projects/[YOUR_ANCHOR_PROJECT]/brief.md`
- `Tasks/active.md`

## Phase 7 — Privacy and editing boundaries

**Step 7a — Privacy scan (use `AskUserQuestion`):**

> **Tool:** Call `AskUserQuestion` with the configuration below. Set `multiSelect: true`. Tell the user: "For anything you select, I'll flag when a response might touch that category and ask before writing."

```
question: "Which of these should be kept out of all files? (Select all that apply)"
header: "Privacy scan"
multiSelect: true
options:
  - label: "Compensation or equity"
    description: "Salary, bonus, equity, offers, or counter-offers"
  - label: "Health or family"
    description: "Personal health, medical, or family situation"
  - label: "Customer names or data"
    description: "Specific customer names, contracts, usage data, or PII"
  - label: "Competitive intelligence"
    description: "Company strategy, M&A activity, pricing, or unreleased plans"
```

> **Note:** The tool auto-adds an "Other" option — use it for **HR feedback** (performance reviews, 360s, PIPs), **political or social stances**, or any other category the user names. Record each flagged category verbatim; do not collapse into a generic note.

**Step 7b — Editing permissions (use `AskUserQuestion` + conversational):**

> **Tool:** Call `AskUserQuestion` for the repo visibility question.

```
question: "What is the visibility of this repository?"
header: "Repo visibility"
multiSelect: false
options:
  - label: "Private"
    description: "Only I (and invited collaborators) can see this repo"
  - label: "Public"
    description: "Anyone can view this repo — I'm careful about what gets committed"
  - label: "Sanitized public template"
    description: "I intend to publish this as a template, so all personal data must be replaced with placeholders before committing"
```

Then ask conversationally:
1. "Which files or folders may I edit freely without asking each time? (e.g., Tasks/, GOALS.md)"
2. "Which files require explicit confirmation before I touch them? (e.g., CLAUDE.md, Knowledge/People/)"

Record the checked categories as the user's `Privacy boundaries` in `CLAUDE.md`. Do not collapse the list into a generic note — name each category that the user flagged so future sessions can check against the actual list.

## Phase 8 — Confirmation summary

Before writing, show:

```markdown
## Proposed setup

### Purpose
- OS mode: ...
- Primary purpose: ...

### Persona and taste
- Persona: ...
- Tone: ...
- Turn-offs: ...
- Ideal response feel: ...

### Thought frameworks
- Tradeoff priority: ...
- Evidence standard: ...
- Decision certainty bar: ...
- Acceptable failure: ...

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

### Strategic alignment
- OKR ladder-up: ...
- Single proof metric: ...
- Goal 1 kill condition: ...

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
- `CLAUDE.md`: identity, OS mode, operating style (incl. taste), thought frameworks, routing, cadence, privacy boundaries
- `GOALS.md`: 30-60-90 outcomes, strategic alignment (OKR, proof metric, kill condition), stakeholders, development goals
- `Tasks/active.md`: P0/P1 work, blockers, near-term commitments
- `Tasks/backlog.md`: P2 work and future candidates
- `Tasks/follow-ups.md`: promised follow-ups and owners
- `Knowledge/People/...`: confirmed stakeholder profiles only
- `Projects/.../brief.md`: anchor project context, open decisions, risks
```

**Mandatory display rule.** You must display the Phase 8 summary in the exact format shown above, including the file-by-file edit plan, **before** asking for approval. Do not ask "Ready to onboard?" or any short-form approval question without first showing the full summary. If the user asks for changes, revise the summary and re-display the full block before re-asking.

Ask: `Should I apply these setup changes? (Yes / No / Change X)`

Only proceed after the user replies with an explicit "yes." Polite acknowledgements ("ok", "sounds good", "looks fine") do not count as approval — re-confirm explicitly.

## Phase 9 — Write and next actions

**Per-file write rule.** Do **not** batch-write multiple files. For each file in the confirmed Phase 8 file-by-file edit plan, in order:

1. Ask: "Ready for me to update `[filename]`?"
2. Wait for an explicit "yes." Polite acknowledgements do not count.
3. Write the file.
4. Show a one-line confirmation: "Updated `[filename]`. Next: `[next filename]`."
5. Move to the next file and repeat.

Only after every file in the plan is written:

1. Show a concise change summary listing every file written.
2. Recommend the first three commands:
   - `/today`
   - `/meeting-prep [person]`
   - `/weekly-update`
3. Ask whether the user wants to run `/today` immediately.

## Phase 10 — Verify onboarding completed cleanly

Run this check before declaring onboarding finished. If any item fails, ask the user how to resolve it instead of inventing a value.

| Check | How to verify | If it fails |
|---|---|---|
| **Placeholders filled** | Grep `CLAUDE.md`, `GOALS.md`, `Tasks/active.md` for `[YOUR_`, `[STAKEHOLDER_`, `[METRIC_`, `[AREA_`. Any remaining bracket placeholders must be explicit user choices (e.g., the user opted to keep a placeholder). | Ask the user to fill the specific placeholder or confirm keeping it. |
| **Persona set** | `CLAUDE.md` → `Default persona` is not a bracketed list. | Re-run Phase 2. |
| **Quality gates match persona** | `CLAUDE.md` → `Quality gates` line matches the persona-effects matrix row. | Re-run Phase 2 confirm step. |
| **30-60-90 outcomes are specific** | Each phase in `GOALS.md` has at least 2 outcomes that name a deliverable, decision, or evidence — not just a theme. | Re-run Phase 5. |
| **Active tasks present** | `Tasks/active.md` has ≥1 P0 or P1 item that is not a template placeholder. | Re-run Phase 4. |
| **At least one stakeholder profile started** | `Knowledge/People/` contains at least one non-template file, or the user has explicitly said they will fill it later. | Re-run Phase 6 or capture the deferral. |
| **Privacy boundaries recorded** | `CLAUDE.md` → `Privacy boundaries` is not a bracketed list. | Re-run Phase 7. |
| **Anchor project brief exists or skipped intentionally** | `Projects/[YOUR_ANCHOR_PROJECT]/brief.md` exists with non-template content, OR the user has said no anchor project yet. | Re-run Phase 6. |

Report verification results as a short checklist (✅ / ❌ per row) to the user.

**Three-way resolution rule for ❌ items.** Do **not** declare onboarding complete with warnings. For each ❌, ask the user to choose one of:

- **(a) Fill it now** — capture the value in conversation and update the file.
- **(b) Defer with a follow-up** — record the gap in `Tasks/follow-ups.md` with a date so it doesn't silently survive.
- **(c) Accept the placeholder intentionally** — the user states a written reason why the placeholder should remain; record that reason in `CLAUDE.md` next to the field so future sessions don't re-flag it.

Only after every ❌ row has been resolved via (a), (b), or (c) may you say "Onboarding complete."

## Re-running onboarding

The user can re-run this workflow at any time by saying `Computer, onboard me into this OS` again. The assistant should:

1. Read the current `CLAUDE.md`, `GOALS.md`, `Tasks/active.md` to see what is already set.
2. **Always re-confirm critical settings explicitly**, even if they have not changed — at minimum the **persona**, the **tone**, and the **quality-gate set**. Ask each as a fresh question, e.g.:
   - "You previously chose `Builder / AI PM` persona. Still right for you, or do you want to change?"
   - "Your tone was `pragmatic, eval-first, model-aware`. Still right?"
   - "Your pre-publish quality gates are `/eval-review` + `/build-review` + `/test-plan`. Still right?"
3. For non-critical fields, ask which sections the user wants to change rather than restarting from scratch.
4. Preserve an existing answer only after the user explicitly confirms it in this run. Do **not** silently carry over persona, tone, or quality gates.

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
3. Uses `AskUserQuestion` for all enumerable-choice questions: OS context (Phase 0), OS mode (Phase 1a), primary purpose (Phase 1b), persona (Phase 2a), pushback level (Phase 2b), cadence (Phase 3a), week-start day (Phase 3b), evidence standard (Phase 5B), decision bar (Phase 5B), privacy scan (Phase 7a), and repo visibility (Phase 7b).
4. Asks taste, tone-to-avoid, goals, task descriptions, tradeoff hierarchy, acceptable failure, and stakeholder details **conversationally** — not as dropdowns.
5. Captures purpose, operating style (including taste), thought frameworks, cadence, active work, goals (with OKR alignment), stakeholders, projects, and privacy boundaries.
6. Preserves unknowns as placeholders or `Unknown` instead of inventing facts.
7. Produces a Phase 8 confirmation summary with a file-by-file edit plan.
8. Does not edit files until the user explicitly approves the proposed setup.
9. Recommends `/today`, `/meeting-prep [person]`, and `/weekly-update` after confirmed setup.

### Fail signals

Tighten this workflow before merging if the assistant:

- Assumes Batman mode when the user chose another persona.
- Writes files before confirmation.
- Stores private information the user excluded.
- Produces generic goals that do not reflect the user's stated purpose.
- Proposes new top-level folders or unrelated architecture changes during onboarding.
- Skips the first-week usefulness question.
- Presents enumerable choices (OS mode, persona, cadence, privacy scan, etc.) as plain-text lists instead of using `AskUserQuestion`.
- Uses `AskUserQuestion` for free-text questions (taste, tone-to-avoid, goal descriptions, acceptable failure) — these must stay conversational.
