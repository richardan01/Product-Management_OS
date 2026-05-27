# ProductManagement-OS

A personal AI Product Management operating system for repeatable PM workflows, AI feature PRDs, evals, product reviews, stakeholder updates, and daily execution.

It is designed to help PMs produce higher-quality artifacts with consistent operating rhythms, while keeping setup practical and lightweight in week one.

---

## If you're evaluating this repo

This is a personal AI PM operating system — a harness-neutral template that a PM configures once during onboarding and then runs daily for execution, research, and quality review. It is not a demo app; it is a working system designed to be forked, personalized, and used. Three things demonstrate AI PM craft here: **(1) multi-agent architecture** with clear domain separation (12 named agents, each owning a narrow domain, coordinated through a shared file system); **(2) offline eval suites** in `Evals/` with author/grader separation enforced as a hard protocol requirement; **(3) a quality gate framework** with pre-publish review gates that vary by persona and artifact type. The fastest path to seeing output without running onboarding is `examples/ai-builder-pm-demo/`. This is a harness-neutral template. The author's personal context lives in a private fork.

---

## Start here: first-run setup

The OS is harness-neutral. Onboarding works in **Claude Code**, **Codex CLI**, and **Gemini CLI** — each reads a different entry-point file at the repo root, but all three route to the same workflow and configuration surface.

| Harness | Entry-point file | What you do |
|---|---|---|
| Claude Code | `CLAUDE.md` | Open the repo in Claude Code (CLI, desktop, or VS Code extension). |
| Codex CLI | `AGENTS.md` | Run `codex` from the repo root. |
| Gemini CLI | `GEMINI.md` | Run `gemini` from the repo root. |

**These three files are intentional harness-neutral mirrors of the same OS.** You only need to maintain the one that matches your harness — onboarding writes to all three entry points automatically, so they stay in sync. Do not edit `AGENTS.md` or `GEMINI.md` directly if you use Claude Code.

Then, in any of the three:

1. Paste this exact prompt:

   ```text
   Computer, onboard me into this OS.
   ```

2. Answer the assistant's setup interview in short batches. You will choose your OS purpose, default tone, working style, goals, cadence, stakeholders, projects, and privacy boundaries.
3. Review the assistant's proposed file edits before approving. The workflow enforces a per-phase read-back, a full Phase 8 summary before any writes, and per-file confirmation in Phase 9 — polite acknowledgements ("sounds good") do not count as approval.
4. After setup, start your first working session with:

   ```text
   /today
   ```

**Expected first-run outcome:** a personalized PM OS where `CLAUDE.md` stores how the assistant should behave (read by all three harnesses — the filename is historical), `GOALS.md` stores what you are optimizing for, task files store what needs to move now, and project / people files store the context the assistant should reuse.

---

## First session walkthrough

If you are evaluating this repo as a recruiter, collaborator, or PM peer, this is the shortest path to seeing what the OS actually does. Plan for ~30–45 minutes including onboarding. For a no-onboarding skim, browse `examples/ai-builder-pm-demo/`.

1. Fork or clone this repository.
2. Run onboarding with:

   ```text
   Computer, onboard me into this OS
   ```

3. Choose **AI Builder PM** when prompted.
4. Create (or reuse) a demo project workspace.
5. Run:

   ```text
   /today
   ```

6. Draft one AI feature PRD with `Templates/prd-ai-feature.md`.
7. Review the draft with `/eval-review` and `/build-review`.
8. Run `/go-nogo` for launch-readiness framing.

This sequence shows the core promise: faster PM execution with stronger AI-product quality gates.

## First 7 days playbook

- **Day 1 — Onboard the OS:** run `Computer, onboard me into this OS` and confirm file updates.
- **Day 2 — Set direction:** fill `GOALS.md` and `Tasks/active.md` with your real priorities.
- **Day 3 — Add stakeholders:** create 3–5 key profiles in `Knowledge/People/`.
- **Day 4 — Run daily ops:** use `/today` in the morning and `/meeting-prep` before key meetings.
- **Day 5 — Produce one artifact:** draft one PRD (or research summary) from templates.
- **Day 6 — Run review gates (mode-conditional):**
  - AI Builder PM → `/eval-review` + `/build-review`
  - Day-job PM → `/peer-review` + `/prd-readiness`
  - Research PM → `/research-sufficiency` + `/peer-review`
  - Minimalist / Career transition → `/peer-review`
- **Day 7 — Close the week:** run `/eod` (each evening to keep task state fresh), then `/weekly-update` and `/retro` to lock learning and next steps.

The goal of week one is not full customization; it is proving the OS helps you ship better PM work immediately.

## What this is

A PM's daily work is high-context, multi-domain, and interruptible. On any given day you're switching between sprint planning, stakeholder prep, solution selection, risk tracking, and writing PRDs — each requiring different data, different frameworks, and different output formats.

A single AI assistant with one long prompt can't handle this well. It conflates domains, loses context, and produces generic output.

The Gotham/Batman layer is intentionally optional: useful for users who like a strategic persona system, but not required for day-to-day AI PM execution.

**This OS solves that.** It's a multi-agent architecture where:
- Each agent owns a narrow domain
- Agents coordinate through a shared file system (not direct calls)
- Orchestration patterns govern how they compose into workflows
- A configurable persona layer keeps voice, standards, and focus consistent

For a full walkthrough of the 3-layer model (Skills → Agents → Knowledge) and how a typical PM week runs through the system, see `HOW-IT-WORKS.md`.

---

## Download-and-use template model

This repository is meant to be downloaded, forked, or cloned as the user's own working OS. Keep personal context inside the downloaded copy and keep it private unless the user intentionally publishes a sanitized version.

**Template rule:** replace placeholders such as `[YOUR_NAME]`, `[YOUR_COMPANY]`, `[YOUR_ANCHOR_PROJECT]`, and `[TARGET_COMPANIES]` during onboarding. Do not hard-code the original template author's personal setup into the repo.

---

## See it in action

The repo ships as a template: every file uses `[PLACEHOLDER]` scaffolding that onboarding replaces with your real context. A live personal instance looks nothing like the template — goals have real metrics, stakeholder profiles have real people, and quality gates are tuned to the PM's chosen persona.

Two reference points show what a filled instance looks like without requiring you to run onboarding:

- **`GOALS.md` → Demo Instance section** — Alex Chen, Senior PM at a fictional frontier AI lab, with real 30-60-90 goals, activation metrics, and a stakeholder table. This is what the file looks like the day after onboarding.
- **`examples/ai-builder-pm-demo/`** — A complete AI Builder PM workflow: onboarding → PRD draft → eval/review loop → go/no-go framing. Browse this to see the OS in motion.

Clone → run `Computer, onboard me into this OS` → your instance. The placeholders become your context.

---

## Interactive onboarding

Start a new setup by asking the assistant:

```text
Computer, onboard me into this OS.
```

The assistant should run `Workflows/interactive-onboarding.md` and collect the user's setup in a short interview instead of assuming a fixed purpose or persona.

### Onboarding choices

The onboarding interview starts with an **OS mode chooser** so users can customize the template without reading every agent file first. The mode is a starting package, not a lock-in; the user can override persona, quality gates, surfaced commands, and privacy boundaries before any files are written.

| OS mode | Best for | Default commands and gates |
|---|---|---|
| **Day-job PM** | Sprint execution, stakeholder updates, roadmap hygiene | `/today`, `/weekly-update`, `/meeting-prep`, `/peer-review` |
| **AI Builder PM** | AI/LLM features, evals, model-risk reviews, launch gates | `Templates/prd-ai-feature.md`, `/evals`, `/eval-review`, `/build-review`, `/test-plan` |
| **Research PM** | Discovery, synthesis, evidence quality, decision readiness | `/synthesize-research`, `/research-sufficiency`, `/wiki-ingest`, `/wiki-query` |
| **Career transition** | Positioning, interview prep, target-company research | `/career-narrative`, `/frontier-lab-interview-prep`, optional Gotham strategic layer |
| **Minimalist** | Low-ceremony daily execution | `/today`, `/weekly-update`, light `/peer-review` |
| **Custom** | Any mixed setup | User chooses commands, quality gates, persona, and routing |

The onboarding interview then lets the user choose or override:

1. **Purpose** — day-job execution, career transition, founder/product build, research/writing, learning system, or a mixed setup.
2. **Persona** — Batman default, executive operator, researcher, coach, builder, minimalist, or a custom persona.
3. **Operating cadence** — daily brief, weekly review, sprint planning, monthly strategy review, quarterly reset.
4. **Core tasks** — current sprint tasks, recurring meetings, projects, decisions, risks, and follow-ups.
5. **Goals** — 30-60-90 outcomes, key metrics, target companies or markets, and personal development goals.
6. **Context boundaries** — what the OS may store, what must stay out, and what should require confirmation before editing.

### Onboarding outputs

By the end of onboarding, the assistant should propose updates to:

- `CLAUDE.md` — identity, purpose, routing, persona, and operating contract
- `GOALS.md` — 30-60-90 goals, metrics, stakeholders, and development focus
- `Tasks/active.md` — current sprint priorities and blockers
- `Tasks/backlog.md` — ranked future work
- `Knowledge/People/` — key stakeholder profiles
- `Projects/[YOUR_ANCHOR_PROJECT]/brief.md` — anchor project context

The assistant should summarize the proposed edits first and only write files after the user confirms.

### What each persona changes

The persona choice in onboarding is not cosmetic — it changes which agents are routed, which quality gates run pre-publish, and which slash commands are surfaced first. See the **persona-effects matrix** in `Workflows/interactive-onboarding.md` (Phase 2) for the full table. Highlights:

- **Batman** — all 12 Gotham agents active, `/riddler` + `/vale` mandatory pre-publish.
- **Executive operator** — skills + workflows only, `/peer-review` default gate, Batman agents preserved but not routed.
- **Research partner** — research-oriented commands surfaced first (`/synthesize-research`, `/wiki-ingest`), `/research-sufficiency` gate.
- **Builder / AI PM** — `Templates/prd-ai-feature.md`, `/build-review`, `/eval-review`, `/test-plan` surfaced first.
- **Minimalist** — skills only, low-ceremony.

Non-Batman personas keep `Agents/Gotham/Computer/` on disk so the user can opt back in by re-running onboarding.

### Verifying onboarding completed cleanly

Phase 10 of the onboarding workflow runs a verification checklist (placeholders filled, persona set, quality gates match persona, goals specific, active tasks present, privacy boundaries recorded). The assistant reports a ✅ / ❌ checklist; anything ❌ must be resolved before treating onboarding as done.

The `Evals/onboarding/` suite tests these properties against a non-Batman fixture (Jordan Lee, Executive operator) to catch persona-routing and placeholder-residue bugs across model upgrades.

---

## Two configurable layers

### Layer 1: Strategic persona layer (optional)

12 named agents in `Agents/Gotham/Computer/`. These can run as the default if the user chooses the Batman persona during onboarding. Their job is to maintain long-horizon strategy, artifact quality, and ruthless focus.

| Agent | Domain |
|-------|--------|
| **Alfred** | Daily ops, calendar, prep, accountability |
| **Bruce Wayne** | Career strategy, quarterly thesis, positioning |
| **Oracle** | Research, intel, JD scans, hiring-manager recon |
| **Lucius Fox** | Build, prototype, MCP/skill authoring |
| **Batman** | High-stakes execution (manual `/cowl-up` only) |
| **Robin** | Junior parallel chores, draft-zero |
| **Nightwing** | Essays, posts, threads, talks, public voice |
| **The Riddler** | Adversarial review (mandatory pre-publish gate) |
| **Vicki Vale** | User-voice review (mandatory pre-publish gate) |
| **Commissioner Gordon** | Network, warm intros, relationship graph |
| **Selina Kyle** | Comp negotiation, offers, counter-offers |
| **Henri Ducard** | Technical-depth coaching and drilling |

### Layer 2: PM operations layer

Used for the user's day-to-day product work. It is implemented through shared tasks, knowledge files, templates, workflows, and PM skills. Add dedicated agents only when a workflow becomes common enough to deserve its own owner.

---

## Eval system

The `Evals/` directory contains **offline audit suites** — not real-time response graders. There are no inline graders that automatically evaluate Claude's output as it's produced. This is intentional: grading in the same context window as authoring violates author/grader separation, which the eval protocol enforces as a hard requirement.

**Two suites ship with the OS:**

| Suite | Criteria | What it catches |
|---|---|---|
| `Evals/onboarding/` | 12 | Placeholder residue, persona-routing bugs, batch-write violations, invented identity |
| `Evals/research-synthesis/` | 7 | Invented quotes, generic synthesis, missing conflicting signals |

**When to run:** after a model upgrade, after changing the onboarding workflow, or on a 60-day cadence. Target: ≥ 10/12 pass per fixture.

**How to run:** use `/evals` to design or execute a suite. Use `/eval-review` to audit eval methodology (author/grader separation, gold-set integrity, metric appropriateness). The grader must run in a fresh context — never the same session that produced the output being graded.

---

## The "Computer" invocation pattern

**Say: "Computer, [task]"**

This routes to the right agent automatically. Examples:

- `Computer, onboard me into this OS` → interactive onboarding workflow
- `Computer, what should I focus on today?` → Alfred
- `Computer, scan for [TARGET_COMPANIES] PM roles` → Oracle
- `Computer, what's our quarterly thesis?` → Bruce Wayne
- `Computer, prototype the eval harness` → Lucius Fox
- `Computer, review this essay before I ship it` → Riddler + Vicki Vale
- `Computer, who should see the flagship repo?` → Gordon

→ Full routing table: `Agents/README.md`

---

## How to get started

### Step 1: Fork, clone, or download this template

`ProductManagement-OS` is the public template. The OS files live at the repo root so users can fork it directly.

### Step 2: Run interactive onboarding

```text
Computer, onboard me into this OS.
```

The assistant should ask about purpose, persona, operating cadence, current tasks, goals, stakeholders, and privacy boundaries before changing files.

### Step 3: Review proposed file updates

Do not blindly accept generated setup. Review the proposed updates to `CLAUDE.md`, `GOALS.md`, `Tasks/active.md`, `Tasks/backlog.md`, `Knowledge/People/`, and `Projects/[YOUR_ANCHOR_PROJECT]/brief.md`.

### Step 4: Start your first session

```text
/today
```

Alfred will read your active tasks and goals and give you a morning brief.

### Step 5: Set up the strategic thesis

```text
Computer, what should my quarterly thesis be?
```

The strategic layer will help you set a quarterly arc for the purpose you selected during onboarding.

---

## Directory structure

```
ProductManagement-OS/
├── CLAUDE.md                    ← Identity, routing, persona, operating contract
├── GOALS.md                     ← 30-60-90 goals, stakeholders, metrics
│
├── Agents/
│   ├── README.md                ← Architecture overview, routing table
│   └── Gotham/Computer/         ← 12 optional Batman-layer agents
│       ├── alfred.md
│       ├── bruce-wayne.md
│       ├── batman.md
│       ├── oracle.md
│       ├── lucius-fox.md
│       ├── nightwing.md
│       ├── riddler.md
│       ├── robin.md
│       ├── gordon.md
│       ├── selina-kyle.md
│       ├── henri-ducard.md
│       └── vicki-vale.md
│
├── Tasks/
│   ├── active.md                ← Current sprint (#p0/#p1/#p2)
│   ├── dayjob-active.md         ← Optional separate day-job task lane
│   ├── backlog.md               ← Prioritized backlog
│   └── follow-ups.md            ← Commitments from meetings and reviews
│
├── Projects/
│   └── YOUR_ANCHOR_PROJECT/
│       └── brief.md             ← Project brief template
│
├── Knowledge/
│   ├── People/
│   │   └── [YOUR_MANAGER].md    ← Manager/stakeholder profile template
│   └── Reference/
│       └── company.md           ← Company context
│
├── Reviews/                     ← OS health reviews
├── Evals/                       ← Eval suites
├── Workflows/                   ← Repeatable operating workflows
├── Templates/                   ← Reusable PM document templates
├── _Registry/
│   └── voice-map.md             ← Persona/voice assignments per agent
│
├── .claude/
│   ├── skills/                  ← 28 Claude slash commands (see skill reference below)
│   └── agents/                  ← 10 Claude sub-agent workers (spawned by skills)
│
└── .codex/
    └── agents/                  ← Codex sub-agent worker specs
```

### Skill reference

28 slash commands ship with the OS. Onboarding surfaces the most relevant ones for your chosen mode; the full set is available immediately after setup.

| Category | Skills |
|---|---|
| **Daily ops** | `/today`, `/eod`, `/weekly-update`, `/meeting-prep`, `/retro`, `/risk-register` |
| **Quality gates** | `/peer-review`, `/prd-readiness`, `/research-sufficiency`, `/build-review`, `/eval-review`, `/go-nogo`, `/voice-conformance` |
| **Planning** | `/quarterly-planning`, `/roadmap-review`, `/launch-plan` |
| **Writing & review** | `/riddler`, `/vale`, `/career-narrative`, `/training-plan`, `/test-plan` |
| **Research & knowledge** | `/synthesize-research`, `/wiki-ingest`, `/wiki-query`, `/wiki-maintain`, `/wiki-lint` |
| **Specialty** | `/evals`, `/eval-review`, `/frontier-lab-interview-prep` |

All skills live in `.claude/skills/`. Each skill's `SKILL.md` file contains the full orchestration logic, sub-agent spawning, and output format.

---

## Template privacy rule

This template is safe to use as a private working OS. If you publish, share, or upstream changes from your copy, remove private stakeholder names, company context, live tasks, meeting notes, credentials, personal reviews, and non-public strategy first.

---

## Quality gates (pre-publish)

The pre-publish gate depends on the persona chosen during onboarding.

**Batman-persona setups** — two mandatory gates before any public artifact ships:

1. **Riddler review** (`/riddler <artifact>`) — adversarial review; finds the weakest claim
2. **Vicki Vale review** (`/vale <artifact>`) — user-voice review; finds where the reader stops reading

Both must pass. These gates are **complementary, not redundant.** Riddler attacks argument strength and unsupported claims. Vicki Vale finds where a real reader stops reading. Run in sequence: Riddler first, then Vicki Vale after the argument is tight.

**Non-Batman setups (Executive operator, Researcher, Coach, Builder, Minimalist)** — `/peer-review` is the default pre-publish gate. `/riddler` and `/vale` remain available and can be opted in during onboarding (Phase 2 persona-effects matrix). For high-stakes artifacts in any persona, add `/peer-review` before adversarial / user-voice gates to catch structural PM craft issues first.

The active gate set is recorded in `CLAUDE.md` and enforced by the operating contract.

---

## The operating contract

Four default principles, configurable during onboarding:

1. **Contingency-first.** Every plan ships with B, C, and D. Failure modes named before solutions.
2. **Artifact quality.** Public artifacts are designed for impact. Opening lines land.
3. **Focus mode.** When a priority is active, the system narrows to one objective.
4. **Long-horizon compounding.** Patient execution beats reactive context switching.

---

## Agent routing table

→ `Agents/README.md`

---

Built on Claude Code, Codex CLI, and Gemini CLI. Designed as a configurable, harness-neutral PM operating-system template.
