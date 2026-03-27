# Quarterly Planning

**Agent:** Strategy & Roadmap — see `Agents/strategy-roadmap/AGENT.md` for full context.
**Sub-agents:** Spawn `task-analyzer` (velocity/shipped items) and `project-scanner` (milestone status) in parallel.
**Detailed process:** See `Workflows/quarterly-planning/workflow-spec.md` for full step-by-step.

Usage: "quarterly planning" — run at the start of each quarter to define OKRs and deliverables.

## Steps

### Step 1: Review Last Quarter
Read `GOALS.md` and `Tasks/archive/` to score each OKR:

| OKR | Target | Actual | Score | Why |
|-----|--------|--------|-------|-----|
| | | | | |

Write "what worked / what didn't" for each goal. Document 3 lessons learned.

### Step 2: Gather Inputs
Check these sources:
- `Meetings/1on1s/jervis.md` — Jervis's stated priorities
- `Knowledge/Reference/metrics/latest.md` — metric trends
- `Knowledge/People/team.md` — what Rachel, Xinyi, Lina, Mardiana need
- `Projects/cdp-implementation/brief.md` — CDP milestone target for the quarter
- `Tasks/backlog.md` — anything that should be pulled in

Flag missing inputs with `[NEEDS INPUT]` — Richard may need to gather these in 1:1s.

### Step 3: Draft OKRs
Framework:
- 2–4 Objectives (qualitative, inspiring direction)
- 2–3 Key Results per Objective (measurable, binary at end of quarter)

Martech PM OKR areas:
- CDP implementation progress
- Team adoption and enablement
- Business impact (ROAS, retention, activation)
- Roadmap clarity and stakeholder alignment

### Step 4: Review & Finalize
1. Present draft to Richard for review
2. Suggest: "Run `/meeting-prep jervis` to prepare for OKR alignment meeting"
3. After Jervis feedback: update `GOALS.md` with finalized OKRs
4. Update milestones in `Projects/cdp-implementation/brief.md`
5. Suggest: "Run `/roadmap-review` to align the roadmap with new OKRs"

## Timing

| Quarter | Planning Window |
|---------|----------------|
| Q2 (Apr–Jun) | Last 2 weeks of March |
| Q3 (Jul–Sep) | Last 2 weeks of June |
| Q4 (Oct–Dec) | Last 2 weeks of September |
| Q1 (Jan–Mar) | Last 2 weeks of December |

## Common Pitfalls
- Too many OKRs → max 4 objectives, ruthlessly cut
- Vague KRs ("improve retention") → every KR needs a number and date
- OKRs set without Jervis → always align before finalizing
- Ignoring dependencies → map in project brief before committing
