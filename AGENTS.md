# ProductManagement-OS Agent Instructions

This repo is a personal Product Management operating system.

## Purpose
Help me think, write, review, and improve PM artifacts for AI product management.

## Core principles
- Make the OS useful daily, not theoretically perfect.
- Optimize for clarity, repeatability, and decision quality.
- Separate thinking from execution.
- Review before changing.
- Prefer simple workflows over over-engineered agent systems.

## Agent behavior
Agents must:
- inspect existing structure before recommending changes
- explain tradeoffs
- identify duplicated or stale templates
- recommend improvements by priority
- avoid destructive changes unless explicitly approved
- keep changes small, isolated, and easy to review or revert
- avoid modifying files outside the approved scope
- avoid unrelated refactors, folder renames, or cascading architecture changes unless explicitly approved
- never commit without explicit instruction
- never push to GitHub without explicit instruction

## Review dimensions
- PM craft quality
- AI PM relevance
- document structure
- template usability
- agentic workflow design
- eval/reviewer loop quality
- repo maintainability

## Change Management Policy

The OS has two layers:

**Stable Core (90%)** — changes slowly, quarterly at most:
- Templates/, Workflows/, Evals/, Knowledge/
- Core agent specs in Agents/
- Operating principles and eval rubrics

**Research Layer (10%)** — monitors and recommends only:
- New Claude Code features, Codex updates, agentic workflow patterns
- AI PM best practices, eval methodology advances

### Change acceptance criteria

A recommended change must pass ALL of these before implementation:
1. **Relevance** — directly improves daily PM output quality or eval rigor
2. **Simplicity** — does not add maintenance burden without proportional gain
3. **Stability** — does not destabilize existing working workflows
4. **Signal** — based on verified signal, not trend-chasing

Reject changes that are:
- Trendy but not materially useful
- Complex without clear payoff
- Driven by "cool AI workflow" impulse rather than PM execution quality

It is acceptable, and often preferred, to recommend **no structural changes** when the OS is already clear, stable, and useful.

### Recommendation calibration

Every recommendation must include:
- **Priority** — P0 / P1 / P2
- **Confidence** — low / medium / high
- **Expected impact** — what improves for daily PM work or eval rigor
- **Maintenance cost** — low / medium / high
- **Implementation complexity** — low / medium / high

### Complexity guardrail

- Prefer removing, consolidating, or simplifying over adding.
- New agents require strong justification and clear ownership.
- New workflows should only be recommended after the workflow has been repeated manually 3+ times.
- Minimize overlapping responsibilities across agents, workflows, templates, and skills.

### Implementation safety

Implementation agents must:
- implement only explicitly approved changes
- preserve existing content unless removal is explicitly approved
- work in an isolated branch or local diff only
- preserve rollback simplicity
- summarize changed files and tradeoffs before considering the work done
- flag uncertainty or assumptions instead of silently expanding scope

For each implemented change, explain:
- why it was made
- what problem it solves
- tradeoffs introduced
- future maintenance implications

### Cadence

- **Daily** — no structural changes; only task execution
- **Weekly** — research summary; flag candidates for review; no implementation
- **Monthly** — architecture review; approved changes implemented by Lucius Fox

## Output format
Use:
1. Summary
2. Findings
3. Recommendations
4. Priority
5. Confidence
6. Expected impact
7. Maintenance cost
8. Implementation complexity
9. Files impacted
10. Execution plan
11. Risks
12. Questions
