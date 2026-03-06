# Product-OS

Personal PM operating system for **Richard Constantine**, Martech Product Manager at KPay.

This workspace is designed to be used with Claude Code (or claude.ai). Claude reads the files here to act as a context-aware thinking partner — helping with planning, meeting prep, research synthesis, and stakeholder communication.

---

## How to Use

Open this folder in Claude Code and run any of the commands below. Claude will read the relevant files automatically.

| Command | What it does |
|---------|-------------|
| `/standup` | Morning briefing — today's tasks, blockers, meetings, suggested focus |
| `/meeting-prep [person]` | Context-loaded prep before any meeting |
| `/weekly-update` | Draft end-of-week stakeholder update |
| `/synthesize-research [path]` | Turn raw notes into structured insights |
| `/draft-prd-section [section] [project]` | Write a PRD section grounded in project research |

---

## Folder Structure

```
Product-OS/
├── CLAUDE.md                        ← Claude's entry point — identity, context, commands
├── GOALS.md                         ← Ownership areas, quarterly goals, key stakeholders
├── README.md                        ← You are here
│
├── Tasks/
│   ├── active.md                    ← Current sprint tasks and blockers
│   ├── backlog.md                   ← Future ideas and captured work
│   └── archive/                     ← Completed tasks by month
│
├── Projects/
│   └── cdp-implementation/
│       └── brief.md                 ← CDP project brief, scope, decisions, open questions
│
├── Meetings/
│   ├── 1on1s/                       ← Notes from recurring 1:1s
│   ├── standups/                    ← Daily standup notes
│   └── one-offs/                    ← Ad hoc meeting notes
│
├── Knowledge/
│   ├── People/                      ← Stakeholder profiles (communication style, preferences)
│   ├── Reference/
│   │   ├── company.md               ← KPay company overview
│   │   ├── product.md               ← Martech stack + data flow architecture
│   │   ├── team.md                  ← Team structure and rituals
│   │   └── okr-history.md           ← Past OKRs and learnings
│   └── Research/                    ← Domain research, competitor intel
│
├── Templates/                       ← Reusable note templates (PRD, brief, interview, etc.)
├── Workflows/                       ← Multi-step recurring processes (quarterly planning, etc.)
├── Tools/                           ← Python utilities (metrics pull, meeting prep)
├── _Registry/                       ← MCP config, tool registry, tags taxonomy
└── _temp/                           ← Scratch space for quick notes
```

---

## Current Focus

**Initiative:** CDP Implementation — building a single source of truth for event tracking and customer lifecycle tagging/tracking at KPay.

See [Projects/cdp-implementation/brief.md](Projects/cdp-implementation/brief.md) for the full brief.

---

## Getting Started (First Week)

Priority files to fill in as you learn things at KPay:

1. **[GOALS.md](GOALS.md)** — add your actual baselines and targets once you have them
2. **[Tasks/active.md](Tasks/active.md)** — add your first sprint tasks
3. **[Knowledge/People/](Knowledge/People/)** — create a profile for your manager and key stakeholders
4. **[Knowledge/Reference/company.md](Knowledge/Reference/company.md)** — fill in KPay basics
5. **[Knowledge/Reference/team.md](Knowledge/Reference/team.md)** — add your team structure

Tip: Use `_temp/` to capture raw notes during your first week, then ask Claude to help sort them into the right places.
