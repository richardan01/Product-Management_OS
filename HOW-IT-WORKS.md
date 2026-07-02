# How This Works

The goal of this OS is simple: **automate the recurring structure around product management work** so the user can spend more time on judgment, communication, and decisions.

This doc explains how the pieces fit together — agents, skills, workflows, templates, and Knowledge — and how a typical week runs through them.

---

## Where work lives

This repository is the working OS after a user forks, clones, or downloads it. The user fills in the placeholders during onboarding, keeps the resulting workspace private by default, and sanitizes any personal/company context before publishing or sharing.

Run onboarding first:

```text
Computer, onboard me into this OS.
```

The onboarding workflow lets the user choose purpose, persona, cadence, tasks, goals, stakeholders, and privacy boundaries before the assistant writes setup files.

---

## The 3-layer model

```
┌─────────────────────────────────────────────────────┐
│  Layer 3 — SKILLS  (.claude/skills/)                │
│  Slash commands. One-shot triggers.                 │
│  e.g. /today  /weekly-update  /meeting-prep         │
└─────────────────────────────────────────────────────┘
                       ↑
┌─────────────────────────────────────────────────────┐
│  Layer 2 — SUB-AGENTS  (.claude/agents/)            │
│  PM-domain workers spawned by skills to handle      │
│  parallel/isolated reads and drafting.              │
└─────────────────────────────────────────────────────┘
                       ↑
┌─────────────────────────────────────────────────────┐
│  Layer 1 — KNOWLEDGE  (CLAUDE.md, GOALS.md,         │
│  Knowledge/, Tasks/, Projects/, Meetings/)          │
│  Persistent context. The "memory" agents read       │
│  before they answer.                                │
└─────────────────────────────────────────────────────┘
```

**The trick to high automation: Layer 1 quality.**
The more accurately `CLAUDE.md`, `GOALS.md`, `Knowledge/People/`, and `Tasks/active.md` describe the user's real situation, the more an agent can do without asking repeated questions. Most "the assistant doesn't get my context" complaints come from a thin Layer 1.

---

## A typical PM week, automated

Below is what a week looks like when the OS is set up. Each row shows: the moment in the week → the trigger → what gets automated.

| Moment | You type / say | What happens |
|---|---|---|
| **First setup** | `Computer, onboard me into this OS` | Runs an interactive interview, proposes setup edits, and asks for confirmation before writing files |
| **Mon 9am** — start the week | `/today` | Reads `Tasks/active.md` + calendar context if available, surfaces 3 priorities, flags blockers, drafts a standup message |
| **Mon 11am** — 1:1 with your manager | `/meeting-prep [your-manager]` | Pulls last 1:1 notes, scans `Tasks/active.md` for items they care about, drafts agenda + updates + asks |
| **Tue 2pm** — discovery interview done | `/synthesize-research` | Reads interview notes from `Projects/[project]/research/`, extracts pain points, themes, and use case implications |
| **Wed 10am** — solution question came up | Use `Templates/research-summary.md` + `/synthesize-research` | Builds a comparison matrix across sources with fit-for-use-case scoring |
| **Wed 4pm** — quick PRD needed | Use `Templates/prd.md` + `/prd-readiness [file]` | Drafts from the template, then checks readiness before handoff |
| **Thu 9am** — daily check | `/today` | Sees what changed, retros what slipped, updates priorities |
| **Every evening** — close the day | `/eod` | Asks what moved, captures blockers and follow-ups, proposes carry-forward edits to `Tasks/active.md` and the `CLAUDE.md` Current Context block |
| **Thu 3pm** — risk review | `/risk-register` | Logs risks, scores probability/impact, suggests mitigation, drafts an escalation message if needed |
| **Fri 11am** — manager wants an update | `/weekly-update` | Reads what got done this week from `Tasks/active.md`, drafts a concise update covering completed, in progress, blockers, decisions needed |
| **Fri 4pm** — end of sprint | `/retro` | Runs a structured retro: what worked / what didn't / one change |
| **Quarter end** | `/quarterly-planning` | Scores last quarter's OKRs, drafts next quarter's objectives aligned to `GOALS.md` |
| **Project kickoff** | `new project [name]` | Creates `Projects/[name]/` with brief, research/, and decisions.md scaffolded from templates |
| **Project launch** | `/go-nogo [project]` → `/launch-plan [project]` | Launch readiness assessment and rollout checklist |
| **Post-launch** | `/retro` | 1-week and 4-week retrospective: adoption, issues, what to tweak |

What's left for the user? **The judgment.** Reviewing drafts, deciding the call, sending the message. The OS does not automate the thinking — it automates the typing, the looking-things-up, and the structure.

---

## Core daily loop

The core loop is intentionally simple:

1. `/today` starts the day with priorities and blockers from your active context.
2. Work happens (meetings, drafting, decisions, execution).
3. `/eod` closes the day by updating what moved, what is blocked, and what carries forward.
4. `/weekly-update` summarizes progress and decisions for stakeholders.

When task files are stale, the OS gets weaker. Fresh `Tasks/active.md` context is the highest-leverage habit in this system.

---

## How agents compose

Skills don't run in isolation. A single `/meeting-prep` triggers a chain:

```
/meeting-prep your-manager
       │
       ▼
meeting-prep skill
       │
       ├──► reads Knowledge/People/your-manager.md      (Knowledge layer)
       ├──► reads Meetings/1on1s/your-manager.md        (history)
       ├──► reads Tasks/active.md                       (current focus)
       ├──► reads Projects/[your-project]/brief.md      (context)
       │
       ├──► spawns stakeholder-profiler sub-agent
       │       └─► builds person context in parallel
       │
       └──► drafts prep doc (agenda, updates to give, asks to make)
```

This is the pattern across the board. **Skills** are the trigger surface and carry the domain judgment. **Sub-agents** in `.claude/agents/` or `.codex/agents/` handle parallel/isolated work.

---

## What the implemented surface automates

| Capability | Implemented surface | Frees you from |
|---|---|---|
| **Onboarding** | `Workflows/interactive-onboarding.md` | Starting from a blank template and guessing what to edit |
| **Daily ops** | `/today` | Reassembling context every morning |
| **Stakeholder prep** | `/meeting-prep`, `/weekly-update` | Meeting prep and status updates |
| **Research synthesis** | `/synthesize-research`, `/research-sufficiency` | Synthesizing interviews and checking decision readiness |
| **Strategy & roadmap** | `/roadmap-review`, `/quarterly-planning` | OKR drafting and roadmap review |
| **Product definition** | `Templates/prd.md`, `/prd-readiness`, `/peer-review` | PRD structure and handoff checks |
| **Build review** | `/build-review`, `/eval-review`, `/test-plan` | Reviewing artifacts, evals, and test coverage |
| **Launch readiness** | `/launch-plan`, `/go-nogo` | Launch checklists and readiness calls |
| **Risk tracking** | `/risk-register` | Risk hygiene and mitigation framing |
| **Eval discipline** | `Evals/` suites + planted-flaw meta-evals for each gate + a calibrated LLM-as-judge + `Evals/monitoring/` | Guessing whether an AI workflow actually works instead of measuring it |
| **Learning loop** | `/retro`, `/wiki-lint`, `/wiki-maintain` | Retros and wiki health checks |

---

## Templates vs Workflows vs Skills — when to use what

These three are easy to confuse:

- **Template** (`Templates/*.md`) = a document **shape**. Static. Use when you want consistent structure across many docs of the same kind. Example: `Templates/prd.md`.
- **Workflow** (`Workflows/*.md`) = a **process**. Step-by-step instructions the assistant follows. Use for repeatable multi-step work that doesn't fit into a single skill. Example: `Workflows/interactive-onboarding.md`.
- **Skill** (`.claude/skills/*/SKILL.md`) = a **shortcut**. Fast trigger for a common task, often invoking a workflow + template behind the scenes. Example: `/synthesize-research`.

**Rule of thumb:** Start with workflows. Promote to skills once you've used the workflow 3+ times and want one-keystroke access. Use templates inside both.

---

## How to push automation further

The first 80% comes from filling out `CLAUDE.md` and `GOALS.md` with real, specific context. The remaining gains come from these habits:

1. **Update `Tasks/active.md` daily.** This is what `/today` and `/weekly-update` read from. Stale tasks → stale automation.
2. **Capture meeting notes immediately.** Use `Templates/1on1-notes.md` right after every 1:1 / stakeholder session. The agents stitch these into context next time.
3. **Keep `Knowledge/People/` warm.** When you learn something new about a colleague's priorities or working style, update their file. Every future `meeting-prep` and `weekly-update` gets sharper because of it.

Done well, the work that *isn't* automated shrinks down to:
- Approving the draft
- The actual conversation in the meeting
- The strategic call only you can make

Everything else — finding files, recalling what was said, structuring the doc, drafting the language — is the OS's job.

---

## Going further: connect calendar, Slack, and your tools

The OS works standalone out of the box. Wire up MCPs to push automation further:

- **Calendar MCP** → so `/today` and `/meeting-prep` know who you're actually meeting
- **Slack MCP** → so `/follow-ups` can post action items to the right channel
- **Notion / Linear MCP** → so task updates can write to the actual ticketing system, not just `Tasks/active.md`
- **Email MCP** → so `/weekly-update` lands in your manager's inbox without a copy-paste

The pattern stays the same: **agent reads context, agent does work, agent writes output where you live.**

---

## Quick start checklist

If you've cloned this repo and want to be running automated by end of week:

- [ ] Day 1 (30 min): fork, clone, or download `Product-Management_OS`
- [ ] Day 1 (20 min): run `Computer, onboard me into this OS`
- [ ] Day 1 (15 min): review and approve proposed edits to `CLAUDE.md`, `GOALS.md`, and task files
- [ ] Day 2 (15 min): list your 4–6 closest stakeholders in `Knowledge/People/`
- [ ] Day 2: try `/today` — see what's missing, fill in those gaps
- [ ] Day 3: try `/meeting-prep [your-manager]` before your next 1:1 — adjust `Knowledge/People/[your-manager].md` based on what came out
- [ ] Day 4: try `/weekly-update` on Friday
- [ ] Day 5: pick one workflow from `Workflows/` that matches a recurring pain point — run it once

By week 2 you'll have a feel for which agents and skills you actually use. Keep the useful parts and simplify anything that does not earn its maintenance cost.
