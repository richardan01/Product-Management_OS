# ProductManagement-OS — Gemini CLI Entry Point

This file is the entry point for **Gemini CLI**. The OS is harness-neutral — Claude Code reads `CLAUDE.md`, Codex CLI reads `AGENTS.md`, and Gemini CLI reads this file. All three route to the same configuration surface and the same workflows.

## Configuration surface

- **`CLAUDE.md`** — user identity, persona, tone, routing, cadence, privacy boundaries, quality gates. Filename is historical; the contents apply to every harness. Read this on session start and respect what's there.
- **`AGENTS.md`** — agent behavior contract (change management, review dimensions, output format). Read this too.
- **`GOALS.md`** — 30-60-90 outcomes and metrics.
- **`Tasks/active.md`** — current sprint focus.
- **`Workflows/`** — repeatable interactive workflows.
- **`Templates/`** — document templates.
- **`Knowledge/People/`** — stakeholder profiles.
- **`Projects/`** — per-project briefs and artifacts.

## Onboarding mode

When the user says `Computer, onboard me into this OS`, `set up this template`, or similar:

1. Run `Workflows/interactive-onboarding.md` phase by phase.
2. Ask the user — never invent — for identity, purpose, persona, cadence, current tasks, goals, stakeholders, and privacy boundaries.
3. Confirm each phase's read-back before moving on. Do not batch-propose tasks or stakeholders.
4. Show the Phase 8 summary in full before asking for write approval.
5. Write files one at a time in Phase 9, asking explicitly per file. Polite acknowledgements ("ok", "sounds good") do not count as approval — require an explicit "yes" per file.
6. On re-run, re-confirm persona / tone / quality gates even if previously set.

## Operating contract (after onboarding)

Once `CLAUDE.md` is filled, treat it as the source of truth for how to respond — persona, tone, pushback level, review style, decision style, privacy boundaries. The principles, routing rules, quality gates, and DO-NOT list there apply regardless of harness.

## DO NOT

- Commit, push, or delete files without explicit approval.
- Write setup files during onboarding before the user confirms the Phase 8 summary.
- Replace placeholders (`[YOUR_NAME]`, `[YOUR_COMPANY]`, etc.) with invented values — ask the user.
- Create new top-level folders — extend existing structure.
- Ship any public artifact without the reviewer gates selected during onboarding.

## Trigger phrases

- `Computer, onboard me into this OS` → `Workflows/interactive-onboarding.md`
- `Computer, what should I focus on today?` → daily brief workflow
- `/today`, `/peer-review`, `/prd-readiness`, `/go-nogo`, `/eval-review`, `/build-review`, `/test-plan` → corresponding skill or workflow under `Workflows/` or `.claude/skills/`.

Full routing table: `Agents/README.md`.
