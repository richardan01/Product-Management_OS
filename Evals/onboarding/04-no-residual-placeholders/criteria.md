# Pass criteria — No residual placeholders

After a complete onboarding (no deferrals), zero template placeholders should remain in core config files.

## Criteria (binary)

1. ✅ / ❌ `CLAUDE.md` contains zero `[YOUR_*]`, `[HEAD_OF_DEPT]`, `[STAKEHOLDER_*]`, or `[METRIC_*]` placeholders.
2. ✅ / ❌ `GOALS.md` contains zero `[YOUR_*]`, `[AREA_*]`, `[METRIC_*]`, `[STAKEHOLDER_*]`, or `[DEV_GOAL_*]` placeholders.
3. ✅ / ❌ `GOALS.md` does not contain marketing-team-legacy placeholders: `[LIFECYCLE_PM]`, `[PAID_ADS_PM]`, `[WEBSITE_PM]`, `[CONTENT_PM]`, `[CURRENT_QUARTER]`.
4. ✅ / ❌ `Tasks/active.md` has no bracketed `[Task description]`, `[Sprint N]`, or `[Start Date]` placeholders in the populated rows.
5. ✅ / ❌ Any placeholder the user explicitly chose to defer is annotated with a visible `# TODO: ask user` comment or `Unknown / TBD` marker so it doesn't silently survive.

## Failure modes this catches

- Assistant leaves marketing-team-legacy placeholders untouched because they "weren't asked about."
- Assistant copies the template verbatim into the user's `GOALS.md` 30-60-90 section.
- Assistant fills some placeholders but skips others without telling the user.
- Assistant treats `[YOUR_NAME]` and `[YOUR_COMPANY]` as literal values to preserve.
