# Eval Suite — Onboarding

## What this tests

The interactive onboarding workflow (`Workflows/interactive-onboarding.md`) is the first thing a new user runs after downloading the PM OS. If it produces a coherent, persona-appropriate, placeholder-free configuration, the rest of the OS works. If it doesn't, the user gets stuck on day 1.

This suite tests the **outputs** of onboarding (the resulting `CLAUDE.md`, `GOALS.md`, `Tasks/active.md`, etc.) against pass criteria that catch the failure modes most likely to block a fresh-clone user.

## Failure modes observed (from `Workflows/interactive-onboarding.md` dry-run + manual review)

1. Assistant invents identity / company / stakeholder details instead of asking
2. Assistant writes setup files before user confirmation
3. Assistant defaults to Batman persona regardless of user choice
4. Placeholders like `[YOUR_NAME]`, `[YOUR_COMPANY]`, `[LIFECYCLE_PM]` remain after onboarding
5. Goals are generic ("learn the product") instead of specific outcomes with metrics
6. Quality-gate config doesn't match the chosen persona (e.g., Riddler+Vale gates set for a Minimalist user)
7. Privacy boundaries left as bracketed defaults
8. Anchor project brief missing or templated when the user named a real project

## Test fixture — Jordan Lee (Executive operator)

Use `inputs/jordan-lee-profile.md` as the user profile for grading. This is a non-Batman persona on purpose — it surfaces persona-routing failures the Batman-default fixture would hide.

## Run protocol

For each eval `0N-<name>/`:

1. Read `input.md` (the user profile + transcript shape) and `criteria.md`.
2. Simulate or replay the onboarding workflow against that input.
3. Grade the produced files against each criterion (✅ / ❌ / ⚠️ partial).
4. For each ❌, run the introspection loop: ask the model *why* it produced that output, and capture the harness fix.
5. Log to `results/YYYY-MM-DD_<model>.md` with pass rate, per-eval result, and harness recommendations.

Target: ≥ 6/7 pass on the current model. Onboarding is high-stakes (day-1 user experience), so the bar is strict.

## Suite map

| # | Eval | Failure mode it catches |
|---|---|---|
| 01 | `no-invented-identity` | Assistant invents name, role, company, or stakeholder facts |
| 02 | `confirmation-before-write` | Assistant writes files before Phase 8 confirmation |
| 03 | `persona-routing-respected` | Assistant applies Batman defaults when user chose another persona |
| 04 | `no-residual-placeholders` | `[YOUR_NAME]`, `[YOUR_COMPANY]`, `[LIFECYCLE_PM]`, etc. remain in final files |
| 05 | `goals-specific-not-generic` | 30-60-90 outcomes are vague, themed, or generic |
| 06 | `quality-gates-match-persona` | Quality-gate config doesn't match the persona's row in the persona-effects matrix |
| 07 | `per-step-interactivity` | Assistant batch-proposes or batch-writes instead of confirming each phase / file individually |

## Not yet covered (parking lot)

- Re-run behavior (Phase "Re-running onboarding") — needs a second-run fixture.
- Privacy-boundary enforcement under adversarial prompts.
- Anchor-project-deferred path (user with no anchor project yet).

These are candidates for v2 once we have real onboarding traces.
