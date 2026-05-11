# How This Works

The goal of this OS is simple: **automate 95% of the recurring work a product manager does in a week**, so the remaining 5% is the part that actually needs your judgment.

This doc explains how the pieces fit together — agents, skills, workflows, templates, and Knowledge — and how a typical week runs through them.

---

## Where work lives

For Richard's local setup, `ProductManager-OS/` is the parent folder with two paths:

- `My-OS/` is the private active Claude workspace for live tasks, stakeholders, company context, meeting notes, and private reviews.
- `ProductManagement-OS/` is the public GitHub template for product managers to fork and use.
- Promote reusable ideas from `My-OS/` into `ProductManagement-OS/` only after removing private names, company details, and one-off personal context.

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
│  Layer 2 — AGENTS  (Agents/)                        │
│  14 PM-domain specialists. Each owns a set of       │
│  skills and reads/writes specific files.            │
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
The more accurately your `CLAUDE.md`, `GOALS.md`, `Knowledge/People/`, and `Tasks/active.md` describe your real situation, the more an agent can do without asking you questions. Most "Claude doesn't get my context" complaints come from a thin Layer 1.

---

## A typical PM week, automated

Below is what a week looks like when the OS is set up. Each row shows: the moment in your week → the trigger → what gets automated.

| Moment | You type / say | What happens |
|---|---|---|
| **Mon 9am** — start the week | `/today` | Reads `Tasks/active.md` + this week's calendar context, surfaces 3 priorities, flags blockers, drafts a Slack standup message |
| **Mon 11am** — 1:1 with your manager | `/meeting-prep [your-manager]` | Pulls last 1:1 notes, scans `Tasks/active.md` for items they care about, drafts agenda + updates to give + asks to make |
| **Tue 2pm** — discovery interview done | `/synthesize-research` | Reads interview notes from `Projects/[project]/research/`, extracts pain points, themes, and use case implications into a structured synthesis |
| **Wed 10am** — solution question came up | Use `Templates/research-summary.md` + `/synthesize-research` | Builds a comparison matrix across sources with fit-for-use-case scoring |
| **Wed 4pm** — quick PRD needed | Use `Templates/prd.md` + `/prd-readiness [file]` | Drafts from the template, then checks readiness before handoff |
| **Thu 9am** — daily check | `/today` | Same as Monday — but now sees Wednesday's commits, retros what slipped, updates priorities |
| **Thu 3pm** — risk review | `/risk-register` | Logs risks, scores probability/impact, suggests mitigation, drafts an escalation message if it's a P0 |
| **Fri 11am** — manager wants an update | `/weekly-update` | Reads what got done this week from `Tasks/active.md` archive, drafts a <300-word update covering: completed, in progress, blockers, decisions needed |
| **Fri 4pm** — end of sprint | `/retro` | Runs a structured retro: what worked / what didn't / one change |
| **Quarter end** | `/quarterly-planning` | Scores last quarter's OKRs, drafts next quarter's objectives aligned to `GOALS.md` |
| **Project kickoff** | `new project [name]` | Creates `Projects/[name]/` with brief, research/, and decisions.md scaffolded from templates |
| **Project launch** | `/go-nogo [project]` → `/launch-plan [project]` | Launch readiness assessment and rollout checklist |
| **Post-launch** | `/retro` | 1-week and 4-week retrospective: adoption, issues, what to tweak |

What's left for you? **The judgment.** Reviewing the drafts, deciding the call, sending the message. The OS does not automate the thinking — it automates the typing, the looking-things-up, and the structure.

---

## How agents compose

Skills don't run in isolation. A single `/meeting-prep` triggers a chain:

```
/meeting-prep your-manager
       │
       ▼
Alfred / meeting-prep skill
       │
       ├──► reads Knowledge/People/your-manager.md      (Knowledge layer)
       ├──► reads Meetings/1on1s/your-manager.md        (history)
       ├──► reads Tasks/active.md                       (current focus)
       ├──► reads Projects/[your-project]/brief.md      (context)
       │
       ├──► spawns stakeholder-profiler sub-agent
       │       └─► builds rich person context in parallel
       │
       └──► drafts prep doc (agenda, updates to give, asks to make)
```

This is the pattern across the board. **Skills** are the trigger surface. **Named agents** provide voice and domain judgment. **Sub-agents** (in `.claude/agents/`) handle parallel/isolated work.

---

## What the implemented surface automates

| Capability | Implemented surface | Frees you from |
|---|---|---|
| **Daily ops** | `/today` | Reassembling context every morning |
| **Stakeholder prep** | `/meeting-prep`, `/weekly-update` | Meeting prep and status updates |
| **Research synthesis** | `/synthesize-research`, `/research-sufficiency` | Synthesizing interviews and checking decision readiness |
| **Strategy & roadmap** | `/roadmap-review`, `/quarterly-planning` | OKR drafting and roadmap review |
| **Product definition** | `Templates/prd.md`, `/prd-readiness`, `/peer-review` | PRD structure and handoff checks |
| **Build review** | `/build-review`, `/eval-review`, `/test-plan` | Reviewing artifacts, evals, and test coverage |
| **Launch readiness** | `/launch-plan`, `/go-nogo` | Launch checklists and readiness calls |
| **Risk tracking** | `/risk-register` | Risk hygiene and mitigation framing |
| **Learning loop** | `/retro`, `/wiki-lint`, `/wiki-maintain` | Retros and wiki health checks |

---

## Templates vs Workflows vs Skills — when to use what

These three are easy to confuse:

- **Template** (`Templates/*.md`) = a document **shape**. Static. Use when you want consistent structure across many docs of the same kind. Example: `Templates/prd.md`.
- **Workflow** (`Workflows/*.md`) = a **process**. Step-by-step instructions Claude follows. Use for repeatable multi-step work that doesn't fit into a single skill. Example: `Workflows/user-research-synthesis/`.
- **Skill** (`.claude/skills/*/SKILL.md`) = a **shortcut**. Fast trigger for a common task, often invoking a workflow + template behind the scenes. Example: `/synthesize-research`.

**Rule of thumb:** Start with workflows. Promote to skills once you've used the workflow 3+ times and want one-keystroke access. Use templates inside both.

---

## How to push automation past 95%

The first 80% comes from filling out `CLAUDE.md` and `GOALS.md` with real, specific context. The last 15% comes from these three habits:

1. **Update `Tasks/active.md` daily.** This is what `/today` and `/weekly-update` read from. Stale tasks → stale automation.
2. **Capture meeting notes immediately.** Use `Templates/1on1-notes.md` right after every 1:1 / stakeholder session. The agents stitch these into context next time.
3. **Keep `Knowledge/People/` warm.** When you learn something new about a colleague's priorities or working style, update their file. Every future `meeting-prep` and `weekly-update` gets sharper because of it.

Done well, the work that *isn't* automated shrinks down to:
- Approving the draft (5 seconds)
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

- [ ] Day 1 (30 min): fork or clone `ProductManagement-OS`; keep private day-to-day work in `My-OS/`
- [ ] Day 1 (15 min): list your 4–6 closest stakeholders in `Knowledge/People/team.md`
- [ ] Day 2 (15 min): seed `Tasks/active.md` with your real current sprint
- [ ] Day 2: try `/today` — see what's missing, fill in those gaps
- [ ] Day 3: try `/meeting-prep [your-manager]` before your next 1:1 — adjust `Knowledge/People/your-manager.md` based on what came out
- [ ] Day 4: try `/weekly-update` on Friday
- [ ] Day 5: pick one workflow from `Workflows/` that matches a recurring pain point — run it once

By week 2 you'll have a feel for which agents and skills you actually use. Delete the rest.
