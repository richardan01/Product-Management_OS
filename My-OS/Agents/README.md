# Agentic PM System

This system organizes Richard's PM work across 14 specialized agents. Each agent owns a domain, provides skills (slash commands), and can spawn sub-agents for parallel work.

## Architecture

```
Agent Definitions (Agents/[name]/[name].md)  →  passive context docs
Skills (.claude/skills/[name]/SKILL.md)     →  user-facing commands
Sub-Agents (.claude/agents/[name].md)       →  AI workers (isolated, parallel)
```

## Invocation

**Slash commands:** `/briefing`, `/cdp-status`, `/add-task`, etc.
**Natural language:** "how's the CDP project?" → Claude routes via CLAUDE.md

## Agent Registry

### Think & Plan (Strategy Layer)
| # | Agent | Domain | Key Skills |
| --- | --- | --- | --- |
| 1 | Orchestrator | Cross-agent assembly | `/briefing`, `/eod`, `/os-check` |
| 2 | Task Manager | Sprint, backlog, daily planning | `/today`, `/sprint-review`, `/groom`, `/add-task` |
| 3 | Stakeholder Manager | Meetings, comms, reporting | `/meeting-prep`, `/meeting-notes`, `/weekly-update`, `/follow-ups` |
| 4 | Research Analyst | Market research, competitive intel | `/synthesize-research`, `/competitive-scan`, `/vendor-eval` |
| 5 | Strategy & Roadmap | OKRs, roadmap, prioritization | `/roadmap-review`, `/quarterly-planning`, `/business-case`, `/prioritize` |
| 6 | Analytics & Metrics | Metrics tracking, dashboards | `/metrics-snapshot`, `/dashboard`, `/trend` |
| 7 | Product Definer | PRDs, requirements, specs | `/prd`, `/use-case`, `/requirements-review`, `/spec-handoff` |
| 8 | Data & Tech Architect | Data models, integrations, feasibility | `/data-model`, `/integration-map`, `/tech-feasibility`, `/data-quality` |
| 9 | CDP Specialist | CDP implementation | `/cdp-status`, `/cdp-use-cases`, `/vendor-scorecard`, `/data-sources` |

### Ship, Run & Learn (Execution Layer)
| # | Agent | Domain | Key Skills |
| --- | --- | --- | --- |
| 10 | Launch Manager | Go-live readiness, launch comms, post-launch review | `/launch-plan`, `/go-nogo`, `/launch-comms`, `/post-launch` |
| 11 | QA & Acceptance Tester | Test plans, UAT, data quality, bug tracking | `/test-plan`, `/uat-check`, `/data-quality-check`, `/bug-report` |
| 12 | Enablement & Change Manager | Training, user guides, adoption, change impact | `/training-plan`, `/user-guide`, `/adoption-check`, `/change-impact` |
| 13 | Risk & Dependency Tracker | Unified risk register, dependencies, escalations | `/risk-register`, `/add-risk`, `/dependency-check`, `/escalation-draft` |
| 14 | Retro & Learning Coach | Sprint retros, post-mortems, lessons log, growth | `/retro`, `/postmortem`, `/lessons`, `/growth-check` |

## Coordination

Agents coordinate through **shared files** — no direct agent-to-agent calls.

```
Agent A writes → shared file (Tasks/, Knowledge/, Projects/)
Agent B reads  → same file when its skill is invoked
```

### Key shared files (the "message bus")

| File | Written by | Read by |
| --- | --- | --- |
| `Tasks/active.md` | Task Manager, Orchestrator | All agents |
| `GOALS.md` | Strategy & Roadmap | All agents |
| `Projects/cdp-implementation/brief.md` | CDP Specialist | Orchestrator, Launch Manager, Risk Tracker |
| `Knowledge/Reference/risk-register.md` | Risk Tracker | Launch Manager, Orchestrator |
| `Projects/[project]/uat-results.md` | QA Tester | Launch Manager |
| `Projects/[project]/training-plan.md` | Enablement Manager | Launch Manager |
| `Knowledge/Reference/lessons-learned.md` | Retro Coach | Strategy, Orchestrator |

## Sub-Agents (`.claude/agents/`)

| Sub-Agent | Spawned by | Purpose |
| --- | --- | --- |
| task-analyzer | `/briefing`, `/eod`, `/sprint-review` | Analyze tasks, priorities, blockers |
| meeting-scanner | `/briefing`, `/follow-ups`, `/meeting-prep` | Scan meetings, extract action items |
| metrics-reader | `/briefing`, `/weekly-update`, `/dashboard` | Read metrics from files + MCPs |
| research-worker | `/competitive-scan`, `/market-brief`, `/vendor-eval` | Web research in isolated context |
| file-analyzer | `/os-check`, `/data-quality`, `/requirements-review` | Validate file structure and quality |
| project-scanner | `/cdp-status`, `/roadmap-review` | Assess project milestones and risks |
| stakeholder-profiler | `/meeting-prep`, `/check-in` | Build person context from profiles + history |
| prd-drafter | `/prd`, `/use-case`, `/business-case` | Draft structured documents |
| tech-reviewer | `/tech-feasibility`, `/tech-spec`, `/integration-map` | Analyze technical architecture |

## File Ownership

See individual agent files for detailed file read/write permissions per agent.
