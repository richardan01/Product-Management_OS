# Changelog

All notable changes to this project will be documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). This project uses semantic versioning anchored to OS capability milestones, not package releases.

---

## [Unreleased]

### Removed
- **Named-persona strategic layer** — deleted the persona-agent directory (12 named persona agents, persona files, gate schemas) and `Agents/README.md` to make this a pure day-to-day PM OS
- Career tooling — `career-narrative` and `frontier-lab-interview-prep` skills; "Career transition" OS mode and the strategic-operator persona removed from onboarding
- Adversarial gate machinery — adversarial-review, user-voice, and voice-conformance skills and `Workflows/gate-dispatch.md` + `gate-merge.md`; `/peer-review` is now the default pre-publish gate for every persona
- `_Registry/voice-map.md`, `Tasks/dayjob-active.md`, and the `examples/` demo workspaces
- `Evals/gate-group/` suite (tested the removed gate-dispatch workflow)

### Changed
- Stripped named-persona/voice references from all skill `SKILL.md` files, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `README.md`, and `HOW-IT-WORKS.md`; skills now use neutral PM role labels
- `Evals/onboarding/` suite re-pointed from the named-persona contrast to a Builder / AI PM contrast (`sam-okafor-builder-variant.md` replaces the prior persona fixture)

### Added
- `GOALS.md` Demo Instance section (Alex Chen, AI Builder PM) showing a filled example alongside the template scaffolding
- `## If you're evaluating this repo` section in README — evaluator-facing orientation under 10 lines
- `## See it in action` section in README — points to the `GOALS.md` demo instance
- `Evals/README.md` — eval system overview: suites, run protocol, scoring thresholds, cadence, sample log format
- `Evals/run-log.md` — persistent run log stub with one completed past entry
- `.github/workflows/lint.yml` — CI: markdownlint on all `.md` files + placeholder-residue check enforcing template hygiene
- `.markdownlint.json` — markdownlint ruleset (disables line-length and first-heading rules for template compatibility)

---

## [0.4.0] — 2025-01

### Added
- Interactive onboarding workflow (`Workflows/interactive-onboarding.md`) — structured 10-phase interview with per-step confirmation, Phase 8 summary before any writes, Phase 9 per-file confirmation; polite acknowledgements explicitly not treated as authorization
- Six OS modes selectable at onboarding start: Day-job PM, AI Builder PM, Research PM, Career transition, Minimalist, Custom
- Persona-effects matrix in `Workflows/interactive-onboarding.md` — maps each persona to default commands, quality gates, and surfaced skills
- Phase 5B thought-framework capture (tradeoff priority, evidence standard, decision certainty bar, acceptable failure)
- Phase 10 verification checklist — ✅/❌ report run at the end of every onboarding session
- `dev-rerun-persona-switch.md`, `taylor-polite-acks.md`, `wei-ambiguous-anchor.md` eval fixtures covering re-run persona preservation, polite-ack authorization, and ambiguous anchor project handling
- `eval-audit-checklist.md` — P0/P1/P2 methodological audit framework for citation-readiness, judgment quality, and hygiene

### Changed
- Onboarding refactored from freeform to `AskUserQuestion`-driven structured choices (respects 4-option UI limit per question)
- Phase 7 privacy scan replaced with post-write eval-agent review
- Current Context block added to `CLAUDE.md` as a resilient live-state snapshot

---

## [0.3.0] — 2024-Q4

### Added
- `AGENTS.md` — harness-neutral agent contract for Codex CLI; mirrors CLAUDE.md's configuration surface
- `GEMINI.md` — Gemini CLI entry point; routes to the same OS workflow and configuration surface
- Harness-neutral OS principle documented in README and all three entry-point files
- `.codex/agents/` directory — Codex sub-agent worker specs
- Stable Core / Research Layer change-management policy in AGENTS.md (90% stable core, 10% research layer updated weekly)

### Changed
- README updated to document all three harness entry points in a single table
- CLAUDE.md positioned as the shared configuration surface read by all three harnesses (filename is historical)

---

## [0.2.0] — 2024-Q3

### Added
- `Evals/onboarding/` suite — 12 criteria covering placeholder residue, persona-routing bugs, batch-write violations, and invented identity; target ≥ 10/12 pass per fixture
- `Evals/research-synthesis/` suite — 7 criteria covering invented quotes, generic synthesis, and missing conflicting signals
- Seven onboarding test fixtures: jordan-lee (Executive operator), sam-okafor (strategic operator), riley-park (Minimalist), morgan-chen (Custom persona), plus three targeted fixtures
- Per-eval `sample-pass.md` and `sample-fail.md` anchors for judgment criteria (evals 05, 07, 11, 12)
- `Evals/onboarding/protocol.md` and `Evals/research-synthesis/protocol.md` — run protocols enforcing author/grader separation and transcript capture
- Knowledge layer structure: `Hypotheses/`, `Decisions/`, `Ingestion/`, `Source/`, `Maintenance/` with provenance-tag hierarchy (`[doc-decision]` → `[assumption]`)
- `Knowledge/Reference/provenance-tags.md` — decay windows and canonicality rules

### Changed
- README eval system section updated to document offline-only grading rationale

---

## [0.1.0] — 2024-Q2

### Added
- Core PM OS structure: `Tasks/`, `Projects/`, `Knowledge/`, `Meetings/`, `Templates/`, `Workflows/`, `Reviews/`, `_temp/`, `_Registry/`
- `CLAUDE.md` — identity, persona, routing, operating contract, and memory conventions
- `GOALS.md` — 30-60-90 goals template with stakeholders, metrics, and strategic alignment sections
- `HOW-IT-WORKS.md` — 3-layer model walkthrough (Skills → Agents → Knowledge), typical PM week, automation patterns
- Named-persona strategic agent layer — 12 named persona agents covering daily ops, strategy, research, build, junior tasks, writing, adversarial review, user-voice review, network, negotiation, and technical-depth coaching roles
- `Agents/README.md` — architecture overview and full routing table
- 28 slash commands in `.claude/skills/` across daily ops, quality gates, planning, writing/review, research/knowledge, and specialty categories
- 10 Claude sub-agent workers in `.claude/agents/`
- `_Registry/voice-map.md` — persona/voice assignments per agent
- Two sanitized example workspaces: `examples/ai-builder-pm-demo/`, `examples/martech-cdp-demo/`
- Core daily loop: `/today` → work → `/eod` → `/weekly-update` / `/retro`
- Pre-publish quality gates: adversarial-review + user-voice review skills for the strategic persona; `/peer-review` default for all others
- `README.md` — full OS documentation with directory structure, skill reference, and first-run setup guide
