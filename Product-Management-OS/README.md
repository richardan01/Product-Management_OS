# Product Management OS

A multi-agent personal operating system for Product Managers. Built on Claude Code. Runs with a Batman persona layer.

---

## What this is

A PM's daily work is high-context, multi-domain, and interruptible. On any given day you're switching between sprint planning, stakeholder prep, vendor evaluation, risk tracking, and writing PRDs — each requiring different data, different frameworks, and different output formats.

A single AI assistant with one long prompt can't handle this well. It conflates domains, loses context, and produces generic output.

**This OS solves that.** It's a multi-agent architecture where:
- Each agent owns a narrow domain
- Agents coordinate through a shared file system (not direct calls)
- Orchestration patterns govern how they compose into workflows
- A Batman/Bruce Wayne persona layer keeps voice consistent and focus ruthless

---

## Two layers

### Layer 1: Batman Strategic Layer (AI PM mission)

12 named agents in `Agents/Gotham/Computer/`. These run by default. Their job: compound toward a 24-month career target in AI PM at a frontier lab.

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

### Layer 2: Day-Job Operations Layer

Opt-in. Invoked only when you explicitly name day-job context ([YOUR_MANAGER], [YOUR_ANCHOR_PROJECT], [YOUR_TEAM], etc.). 14+ agents following the same Batman voice map.

---

## The "Computer" invocation pattern

**Say: "Computer, [task]"**

This routes to the right agent automatically. Examples:

- `Computer, what should I focus on today?` → Alfred
- `Computer, scan for [TARGET_COMPANIES] PM roles` → Oracle
- `Computer, what's our Q3 thesis?` → Bruce Wayne
- `Computer, prototype the eval harness` → Lucius Fox
- `Computer, review this essay before I ship it` → Riddler + Vicki Vale
- `Computer, who should see the flagship repo?` → Gordon

→ Full routing table: `Agents/README.md`

---

## How to get started

### Step 1: Copy the folder
Fork or copy `Product-Management-OS/` to your working directory.

### Step 2: Fill in CLAUDE.md
Open `CLAUDE.md` and replace all `[PLACEHOLDER]` values:

| Placeholder | Replace with |
|-------------|--------------|
| `[YOUR_NAME]` | Your name |
| `[YOUR_EMAIL]` | Your email |
| `[YOUR_COMPANY]` | Your company |
| `[YOUR_ROLE]` | Your job title |
| `[YOUR_TEAM]` | Your team name |
| `[YOUR_MANAGER]` | Your manager's name |
| `[HEAD_OF_DEPT]` | Your skip-level's name |
| `[COO]` | The senior leader above them |
| `[YOUR_ANCHOR_PROJECT]` | Your primary project |
| `[TARGET_COMPANIES]` | Your target companies (for AI PM mission) |
| `[YOUR_TARGET_DATE]` | Your target date for the career pivot |
| `[CURRENT_QUARTER]` | Current quarter (e.g., Q3 2026) |

### Step 3: Fill in GOALS.md
Replace all placeholders in `GOALS.md` with your 30-60-90 day goals, stakeholders, and key metrics.

### Step 4: Start your first session
```
/today
```

Alfred will read your active tasks and goals and give you a morning brief.

### Step 5: Set up the Batman layer quarterly thesis
```
Computer, what should my Q3 thesis be?
```

Bruce Wayne will help you set a quarterly arc for the AI PM mission.

---

## Directory structure

```
Product-Management-OS/
├── CLAUDE.md                    ← Identity, routing, operating contract
├── GOALS.md                     ← 30-60-90 goals, stakeholders, metrics
│
├── Agents/
│   ├── README.md               ← Architecture overview, routing table
│   └── Gotham/Computer/        ← 12 Batman-layer agents
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
│   ├── active.md               ← Current sprint (#p0/#p1/#p2)
│   ├── backlog.md              ← Prioritized backlog
│   └── archive/                ← Completed sprints
│
├── Projects/
│   └── YOUR_ANCHOR_PROJECT/
│       └── brief.md            ← Project brief template
│
├── Knowledge/
│   ├── People/
│   │   └── [YOUR_MANAGER].md  ← Manager profile template
│   └── Reference/
│       ├── company.md          ← Company context
│       └── martech-stack.md    ← Tool audit template
│
├── Meetings/
│   └── 1on1s/                  ← 1:1 meeting notes
│
├── Reviews/                     ← OS health reviews
├── Evals/                       ← Eval suites (flagship project)
├── _temp/                       ← Working drafts (not durable)
│
├── _Registry/
│   └── voice-map.md            ← Batman voice assignments per agent
│
└── .claude/
    ├── skills/                  ← 20+ skill commands (/today, /weekly-update, etc.)
    └── agents/                  ← 11 sub-agent workers
```

---

## Quality gates (pre-publish)

Every public artifact goes through two mandatory gates before shipping:

1. **Riddler review** (`/riddler <artifact>`) — adversarial review; finds the weakest claim
2. **Vicki Vale review** (`/vale <artifact>`) — user-voice review; finds where the reader stops reading

Both must pass. No exceptions. This is enforced by the operating contract in `CLAUDE.md`.

---

## The operating contract (Batman / Bruce Wayne)

Four principles, non-negotiable:

1. **Contingency-first.** Every plan ships with B, C, and D. Failure modes named before solutions.
2. **Theatrical artifact quality.** Public artifacts designed for impact. Opening lines land.
3. **"I'm Batman" focus mode.** When the bat-signal is up, the world narrows. One objective.
4. **Multi-year patience.** Bruce Wayne does not announce his moves. He executes them.

---

## Agent routing table

→ `Agents/README.md`

---

Built on Claude Code. Designed for a PM with a 24-month horizon and a day job to fund the pivot.
