# Agent: Orchestrator

## Purpose
Compose multi-agent outputs into unified views. Route compound requests that span multiple agent domains. Monitor system health.

## Scope
Cross-cutting — reads from all agent domains but owns no content files. The Orchestrator assembles, it doesn't create.

## Skills

| Skill | Command | Description |
|-------|---------|-------------|
| Morning Briefing | `/briefing` | Combine tasks + meetings + metrics + CDP status into one view |
| End of Day | `/eod` | Summarize work done, update active.md, flag carry-overs |
| OS Health Check | `/os-check` | Validate agent files, flag stale data, suggest maintenance |

## Files

### Reads
- `Tasks/active.md` — current sprint state (via Task Manager)
- `GOALS.md` — objectives and OKR status (via Strategy)
- `Meetings/` — today's meetings and recent notes (via Stakeholder Manager)
- `Knowledge/Reference/metrics/latest.md` — key metrics (via Analytics)
- `Projects/cdp-implementation/brief.md` — CDP milestone status (via CDP Specialist)
- `Agents/*/AGENT.md` — all agent definitions for routing context

### Writes
- `Tasks/active.md` — mark items done/carry-over during `/eod`

## Sub-Agents Used
- `task-analyzer` — parallel: read and analyze task priorities
- `meeting-scanner` — parallel: scan meetings and calendar
- `metrics-reader` — parallel: pull latest metrics

## Coordination

### Receives from
- All agents (indirectly via shared files)

### Sends to
- User — assembled unified views

## Quality Checks
- [ ] All data sources read successfully (degrade gracefully if a file is missing)
- [ ] Output is scannable in under 30 seconds
- [ ] Blocked items are highlighted prominently
- [ ] Suggested focus aligns with #p0 priorities
