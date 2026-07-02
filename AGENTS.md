# Product-Management_OS Agent Instructions

This repo is a personal Product Management operating system.

This file is the canonical agent contract read by **Codex CLI** and any other harness that respects the `AGENTS.md` convention. Claude Code reads `CLAUDE.md` and Gemini CLI reads `GEMINI.md` — all three point at the same configuration surface (`CLAUDE.md` for the user's identity / persona / operating style) and the same workflows under `Workflows/`. The onboarding workflow is harness-neutral.

## Onboarding mode

When the user says `Computer, onboard me into this OS`, `set up this template`, or similar:

1. Run `Workflows/interactive-onboarding.md`. Follow it phase by phase.
2. Ask the user — do not invent — for identity, purpose, persona, cadence, current tasks, goals, stakeholders, and privacy boundaries.
3. Confirm each phase's read-back before moving on. Do not batch-propose tasks or stakeholders.
4. Show the Phase 8 summary in full before asking for write approval.
5. Write files one at a time in Phase 9, asking explicitly per file. Polite acknowledgements ("ok", "sounds good") do not count — require an explicit "yes" per file.
6. On re-run, re-confirm persona / tone / quality gates even if previously set.

`CLAUDE.md` is the configuration file the onboarding workflow writes to. Codex CLI and Gemini CLI should also respect the persona, tone, routing, and privacy boundaries captured there — the file is harness-neutral, the filename is historical.

## Purpose
Help me think, write, review, and improve PM artifacts for AI product management.

**AI product management** in this OS means three things: (1) building products powered by AI / LLMs, (2) using AI as a tool in your own PM workflow (evals, synthesis, automation), and (3) reasoning about AI / model risks, tradeoffs, and brittleness. This OS supports all three modes, and is designed for PMs who already do generalist PM work and want to develop AI PM expertise.

## Core daily loop
- `/today` — morning brief from `Tasks/active.md` + `GOALS.md`.
- `/eod` — end-of-day update to `Tasks/active.md`, follow-ups, and (when triggered) the `CLAUDE.md` Current Context block.
- `/weekly-update` and `/retro` — close the week.

Stale task files weaken the OS. Running `/eod` daily is the highest-leverage habit.

## Memory

Memory is repo-native. The canonical durable memory lives in `Memory/` — read it on session start; do **not** rely only on Codex's runtime memory. Runtime memory is a lightweight pointer/cache for compact durable preferences and environment facts; the repo is the source of truth.

- **Read on session start:** `Memory/USER.md`, `Memory/OPERATING_CONTEXT.md`, `Memory/MEMORY_POLICY.md`.
- **Write durable** decisions, preferences, patterns, and operating context into the matching `Memory/` file — after passing the 5-question gate in `Memory/MEMORY_POLICY.md`.
- **Do not put in Memory:** task state (→ `Tasks/`), project context (→ `Projects/`), validated reference facts (→ `Knowledge/`), or credentials / customer / sensitive company data (→ never).
- **On conflict, repo files win over runtime memory.** Sensitive stakeholder/company/customer facts require explicit approval before writing; public-template users keep private context in a private fork.

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
- Core sub-agent specs in `.claude/agents/` and `.codex/agents/`
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
- **Monthly** — architecture review; approved changes implemented after explicit sign-off

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
