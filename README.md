# ProductManagement-OS

A downloadable multi-agent operating-system template for product managers. It combines PM templates, repeatable workflows, Claude/Codex skills, and a configurable persona layer so users can turn a fresh clone into a useful daily work system.

---

## What this is

A PM's daily work is high-context, multi-domain, and interruptible. On any given day you're switching between sprint planning, stakeholder prep, solution selection, risk tracking, and writing PRDs — each requiring different data, different frameworks, and different output formats.

A single AI assistant with one long prompt can't handle this well. It conflates domains, loses context, and produces generic output.

**This OS solves that.** It's a multi-agent architecture where:
- Each agent owns a narrow domain
- Agents coordinate through a shared file system (not direct calls)
- Orchestration patterns govern how they compose into workflows
- A configurable persona layer keeps voice, standards, and focus consistent

---

## Download-and-use template model

This repository is meant to be downloaded, forked, or cloned as the user's own working OS. Keep personal context inside the downloaded copy and keep it private unless the user intentionally publishes a sanitized version.

**Template rule:** replace placeholders such as `[YOUR_NAME]`, `[YOUR_COMPANY]`, `[YOUR_ANCHOR_PROJECT]`, and `[TARGET_COMPANIES]` during onboarding. Do not hard-code the original template author's personal setup into the repo.

---

## Interactive onboarding

Start a new setup by asking the assistant:

```text
Computer, onboard me into this OS.
```

The assistant should run `Workflows/interactive-onboarding.md` and collect the user's setup in a short interview instead of assuming a fixed purpose or persona.

### Onboarding choices

The onboarding interview lets the user choose:

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

---

## Two configurable layers

### Layer 1: Strategic persona layer

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
│       ├── company.md           ← Company context
│       └── martech-stack.md     ← Tool audit template
│
├── Meetings/
│   └── 1on1s/                   ← 1:1 meeting notes
│
├── Reviews/                     ← OS health reviews
├── Evals/                       ← Eval suites
├── Workflows/                   ← Repeatable operating workflows
├── Templates/                   ← Reusable PM document templates
├── _temp/                       ← Working drafts (not durable)
│
├── _Registry/
│   └── voice-map.md             ← Persona/voice assignments per agent
│
├── .claude/
│   ├── skills/                  ← Claude skill commands (/today, /weekly-update, etc.)
│   └── agents/                  ← Claude sub-agent workers
│
└── .codex/
    └── agents/                  ← Codex sub-agent worker specs
```

---

## Template privacy rule

This template is safe to use as a private working OS. If you publish, share, or upstream changes from your copy, remove private stakeholder names, company context, live tasks, meeting notes, credentials, personal reviews, and non-public strategy first.

---

## Quality gates (pre-publish)

Every public artifact goes through two mandatory gates before shipping:

1. **Riddler review** (`/riddler <artifact>`) — adversarial review; finds the weakest claim
2. **Vicki Vale review** (`/vale <artifact>`) — user-voice review; finds where the reader stops reading

Both must pass. No exceptions. This is enforced by the operating contract in `CLAUDE.md`.

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

Built on Claude Code and Codex. Designed as a configurable PM operating-system template.
