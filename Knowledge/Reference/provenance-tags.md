# Provenance tags — evidence weight hierarchy

Every claim in the Knowledge wiki, Hypotheses, and Decisions layers **must carry one of these tags**. Tags prevent weak evidence from masquerading as verified truth and let the weekly sweep flag decay.

**Last updated:** 2026-05-21

---

## The five tags

| Tag | Meaning | Weight | Decay window |
|---|---|---|---|
| `[doc-decision]` | Formally logged decision (exists in `Knowledge/Decisions/`) | **Highest** | Quarterly — revisit if context changes |
| `[doc-research]` | Customer interviews, structured study, metrics with source | **High** | 90 days for interviews; 30–60 days for market data |
| `[verbal-stake]` | "X said…" on a specific date — stakeholder verbal input | **Medium** | 30 days — re-verify or downgrade to `[pm-intuition]` |
| `[pm-intuition]` | Personal hunch, pattern-matched from experience, unvalidated | **Low** | Flag at 30 days; resolve or explicitly keep as hunch |
| `[assumption]` | Taken as true without evidence; must be named to be managed | **Lowest** | 30 days — validate or escalate as a risk |

---

## How to use

Inline in any Knowledge file, hypothesis, decision, or research summary:

```markdown
Users prefer async communication over synchronous calls. [verbal-stake, 2026-04-10, Priya S.]
Competitor X is rebuilding their checkout flow. [pm-intuition]
Retention drops 12% in month 3. [doc-research, Q1 2026 cohort analysis]
```

**Rules:**
1. One claim = one tag. If a claim has multiple sources at different weights, use the **highest-weight tag** but note the others.
2. **Never strip a tag** when editing. Untagged claims are flagged by `/wiki-lint` as orphan evidence.
3. When two claims conflict, preserve both with their tags — do not merge. The `/wiki-maintain` weekly sweep will surface the contradiction.
4. Downgrade tags when evidence ages past its decay window. Do not delete the claim.

---

## Provenance laundering — what to avoid

These patterns inflate evidence weight and corrupt the system:

- Citing a single Slack message as `[doc-research]`
- Using `[verbal-stake]` without a name and date
- Treating `[pm-intuition]` as settled when it has never been validated
- Summarizing three contradictory interviews into one consensus claim — **preserve the minority signal**

---

## Weekly decay check

Run during `/wiki-maintain`. For each provenance tag in active files:

- `[verbal-stake]` older than 30 days → flag for re-verification
- `[pm-intuition]` older than 30 days → flag as unresolved assumption or validate
- `[assumption]` older than 30 days → surface as open risk in `/risk-register`
- `[doc-research]` (market intel) older than 60 days → flag for refresh
- `[doc-research]` (customer interviews) older than 90 days → flag for re-interview or archive

---

## Related

- `Knowledge/Hypotheses/README.md` — hypotheses always carry provenance tags on evidence rows
- `Knowledge/Decisions/README.md` — decisions record source provenance for their reasoning
- `.claude/skills/wiki-maintain/SKILL.md` — runs the decay check
- `.claude/skills/wiki-ingest/SKILL.md` — assigns tags at ingestion time
