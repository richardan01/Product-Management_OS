# CLAUDE.md — My Product OS

## Identity

**[Your Name]** — [Your Role] at [Your Company], [Your Team].
[One sentence describing your scope and mission — e.g. "Building the marketing technology foundation to give the team a single source of truth on customer data."]
Manager: [Your Manager's Name] ([Their Title]).

## On Session Start — Always Read These

1. `GOALS.md` — 30-60-90 objectives, OKRs, what I own
2. `Tasks/active.md` — current sprint, blockers, priorities

For project work, also read:
- `Projects/[your-main-project]/brief.md` — project anchor doc

## Agent System

This OS is powered by 14 specialized agents. You can invoke them via slash commands or natural language — Claude routes to the right agent automatically.

See `Agents/README.md` for full architecture. Agent definitions live in `Agents/[name]/[name].md`. Sub-agents (AI workers) live in `.claude/agents/`.

### Agent Registry

| Agent | Domain | Key Commands |
| --- | --- | --- |
| Orchestrator | Cross-agent unified views | `/briefing`, `/eod`, `/os-check` |
| Task Manager | Sprint, backlog, daily planning | `/today`, `/sprint-review`, `/groom`, `/add-task` |
| Stakeholder Manager | Meetings, comms, reporting | `/meeting-prep`, `/meeting-notes`, `/weekly-update`, `/follow-ups` |
| Research Analyst | Market research, competitive intel | `/synthesize-research`, `/competitive-scan`, `/vendor-eval` |
| Strategy & Roadmap | OKRs, roadmap, prioritization | `/roadmap-review`, `/quarterly-planning`, `/business-case`, `/prioritize` |
| Analytics & Metrics | Metrics, dashboards | `/metrics-snapshot`, `/dashboard`, `/trend` |
| Product Definer | PRDs, requirements, specs | `/prd`, `/use-case`, `/requirements-review`, `/spec-handoff` |
| Data & Tech Architect | Data models, integrations, feasibility | `/data-model`, `/integration-map`, `/tech-feasibility`, `/data-quality` |
| Domain Specialist | [Your main initiative] | `/[domain]-status`, `/[domain]-use-cases`, `/vendor-scorecard`, `/data-sources` |
| **Launch Manager** | Go-live readiness, launch comms, post-launch | `/launch-plan`, `/go-nogo`, `/launch-comms`, `/post-launch` |
| **QA & Acceptance Tester** | Test plans, UAT, data quality | `/test-plan`, `/uat-check`, `/data-quality-check`, `/bug-report` |
| **Enablement & Change Manager** | Training, adoption, change impact | `/training-plan`, `/user-guide`, `/adoption-check`, `/change-impact` |
| **Risk & Dependency Tracker** | Risk register, dependencies, escalations | `/risk-register`, `/add-risk`, `/dependency-check`, `/escalation-draft` |
| **Retro & Learning Coach** | Retros, post-mortems, lessons, growth | `/retro`, `/postmortem`, `/lessons`, `/growth-check` |

## Key Commands

### Orchestrator
| Say | Does |
| --- | --- |
| `briefing` | Morning brief: tasks + meetings + metrics + project status |
| `eod` | End of day: summarize done, update tasks, flag carry-overs |
| `os-check` | System health: validate files, flag stale data |
| `peer-review [file]` | Evaluate any agent output against its quality standards |

### Task Manager
| Say | Does |
| --- | --- |
| `today` | Review active tasks, surface blockers, plan today's focus |
| `sprint-review` | End-of-week: archive done, pull from backlog, velocity |
| `groom` | Re-prioritize backlog, flag stale items |
| `add-task [desc]` | Quick add task with auto priority/tags |

### Stakeholder Manager
| Say | Does |
| --- | --- |
| `meeting prep [name]` | Prep doc for 1:1 with context, agenda, open items |
| `meeting notes [name]` | Structure notes, extract action items → Tasks |
| `weekly update` | Draft weekly status update (<300 words) |
| `monthly update` | Broader update for the team |
| `follow-ups` | Scan meeting notes, create tasks from action items |
| `check-in [name]` | Last interaction, open commitments, suggested topics |

### Research Analyst
| Say | Does |
| --- | --- |
| `synthesize research` | Synthesize interview notes into structured findings |
| `competitive-scan [topic]` | Web research on competitors |
| `vendor-eval [category]` | Build comparison matrix |
| `market-brief [topic]` | Quick research summary |
| `interview-guide [role]` | Generate role-specific questions |

### Strategy & Roadmap
| Say | Does |
| --- | --- |
| `roadmap review` | Weekly milestone status, risks, reprioritization |
| `quarterly planning` | OKR drafting, last-quarter scoring |
| `business-case [initiative]` | Draft ROI/business case |
| `prioritize [items]` | RICE or impact/effort scoring |
| `decision [summary]` | Record decision with rationale |

### Analytics & Metrics
| Say | Does |
| --- | --- |
| `metrics-snapshot` | Point-in-time metrics capture |
| `dashboard` | Key business metrics overview |
| `trend [metric]` | Compare metric over time, flag anomalies |

### Product Definer
| Say | Does |
| --- | --- |
| `prd [feature]` | Create PRD from template + context |
| `use-case [name]` | Structure use case with acceptance criteria |
| `requirements-review [file]` | Check doc for completeness, gaps |
| `spec-handoff [project]` | Package requirements for engineering |

### Data & Technical Architect
| Say | Does |
| --- | --- |
| `data-model [system]` | Document schema, entities, relationships |
| `integration-map` | Map how tools connect |
| `tech-feasibility [feature]` | Assess viability, dependencies, risks |
| `event-schema [flow]` | Define event tracking schema |
| `data-quality [source]` | Check completeness, naming, PII |
| `tech-spec [doc]` | Review engineering spec from PM perspective |

### Domain Specialist
| Say | Does |
| --- | --- |
| `[domain]-status` | Project dashboard: milestones, blockers, metrics |
| `[domain]-use-cases` | Review/update use case scoring matrix |
| `data-sources` | Data source inventory and integration status |
| `vendor-scorecard [vendor]` | Score vendor against criteria |
| `stack-audit` | Review tech stack, flag stale entries |

### Launch Manager
| Say | Does |
| --- | --- |
| `launch-plan [project]` | Build full launch checklist: readiness, rollout, comms |
| `go-nogo [project]` | Run go/no-go assessment before launch |
| `launch-comms [project]` | Draft internal launch announcement |
| `post-launch [project]` | 1-week and 4-week post-launch review |

### QA & Acceptance Tester
| Say | Does |
| --- | --- |
| `test-plan [feature]` | Build test plan from PRD acceptance criteria |
| `uat-check [feature]` | Run UAT checklist, capture pass/fail, flag bugs |
| `data-quality-check [source]` | Validate data completeness, naming, PII |
| `bug-report` | Log and triage bugs found during testing |

### Enablement & Change Manager
| Say | Does |
| --- | --- |
| `training-plan [feature]` | Build role-specific training plan |
| `user-guide [feature]` | Draft step-by-step user guide |
| `adoption-check` | Review usage, flag low adopters, suggest next actions |
| `change-impact [project]` | Assess how a change affects each stakeholder |

### Risk & Dependency Tracker
| Say | Does |
| --- | --- |
| `risk-register` | View and update unified risk register across all projects |
| `add-risk [description]` | Log a new risk with probability, impact, mitigation |
| `dependency-check` | Review all open external dependencies |
| `escalation-draft [risk-id]` | Draft escalation message for a blocked risk |

### Retro & Learning Coach
| Say | Does |
| --- | --- |
| `retro` | End-of-sprint: what worked, what did not, one change |
| `postmortem [project]` | Deep-dive on a completed or failed project |
| `lessons` | View and update cumulative lessons learned log |
| `growth-check` | Assess progress against 30-60-90 goals, flag skill gaps |

### Other
| Say | Does |
| --- | --- |
| `new project [name]` | Create new project folder with brief template |

## System Structure

```
Agents/          → Agent definitions ([name].md) — 14 specialized PM agents
Tasks/           → Active sprint + backlog (keep 3–6 active items max)
Projects/        → One-off work with its own context; archived when done
Workflows/       → Repeatable processes (detailed step-by-step reference docs)
Meetings/        → Running logs — 1:1s, standups, stakeholder sessions
Knowledge/       → Persistent reference: people, research, metrics, data architecture
Templates/       → Document skeletons for PRDs, briefs, interview notes, updates
.claude/skills/  → Slash commands that trigger agent skills
.claude/agents/  → Sub-agents (AI workers for parallel/isolated tasks)
_Registry/       → Tags, MCP integrations
_temp/           → Scratch space
```

## Key People

*Replace with your actual stakeholders. Full profiles in `Knowledge/People/`.*

| Person | Role | Relationship |
| --- | --- | --- |
| [Your Manager] | [Title] | Manager — [meeting cadence] |
| [Stakeholder 1] | [Role] | [Relationship / how they connect to your work] |
| [Stakeholder 2] | [Role] | [Relationship] |
| [Stakeholder 3] | [Role] | [Relationship] |
| [Stakeholder 4] | [Role] | [Relationship] |

## Current Context

> Always check `Tasks/active.md` for the latest blockers and sprint focus — this section is a snapshot only.

- **Role:** [Your current context — e.g. "Month 1 at [Company] — ramping up" or "In execution on [initiative]"]
- **Main initiative:** [What you're primarily working on]
- **Key deliverable:** [Your next major output]

## Conventions

- All files are Markdown
- Priority tags: `#p0` (urgent), `#p1` (this week), `#p2` (backlog)
- Area tags: customize to your domain (e.g. `#[area-1]`, `#[area-2]`, `#[area-3]`)
- Use `[[wikilinks]]` to cross-reference notes
- New documents → use a template from `Templates/`
