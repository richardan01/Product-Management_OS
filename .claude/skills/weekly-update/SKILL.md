# Weekly Update

**Agent:** Stakeholder Manager
**Sub-agents:** Spawn `task-analyzer` and `metrics-reader` in parallel to gather task progress and latest metrics.

Read the following files to draft [YOUR_NAME]'s weekly update for [YOUR_MANAGER] and the [YOUR_TEAM]:
1. **`Tasks/weekly-updates/archive/`** — read the **last 2 sent updates** (most recent filenames). This is the most important step for tone continuity: match the voice, structure, and level of detail [YOUR_NAME] has already established. If the folder is empty, fall back to `Templates/weekly-update.md` for structure only.
2. `Tasks/active.md` — what was completed and what's in progress
3. `GOALS.md` — check against 30-60-90 day targets
4. `Projects/[YOUR_ANCHOR_PROJECT]/brief.md` — milestone status
5. `Meetings/1on1s/[YOUR_MANAGER].md` (if exists) — any context from last 1:1
6. Check `Meetings/` folder for any relevant meeting notes from this week

Then draft a weekly update using `Templates/weekly-update.md`. Keep it:
- Under 300 words
- Concise and scannable — [YOUR_MANAGER] is busy
- Honest about blockers — don't bury risks
- Focused on what matters to [YOUR_MANAGER]: progress toward goals, blockers that need them, decisions needed

Status assessment:
- 🟢 On Track — milestones are progressing as planned
- 🟡 At Risk — a dependency or blocker could affect the timeline
- 🔴 Blocked — cannot progress without external input

After drafting, show it to [YOUR_NAME] and ask:
- "Does this accurately reflect your week?"
- "Any metrics or results to add?"
- "Any decisions you need from [YOUR_MANAGER] to call out?"

Revise based on feedback.

Also pull latest metrics from `Knowledge/Reference/metrics/latest.md` if it exists, and include key numbers in the update.

> **MCP fallback:** If no metrics MCP is connected and `metrics/latest.md` doesn't exist, leave a `[METRICS: add manually]` placeholder in the update rather than omitting the section.

**After [YOUR_NAME] confirms and sends the update:** save the final version to `Tasks/weekly-updates/archive/YYYY-MM-DD.md` so the next run can read it for tone continuity.

---

## Weekly eval-monitoring hook

Once per week (here is the natural place), run the online-monitoring loop in `Evals/monitoring/README.md`: sample 10–15 recent real artifacts, grade them async against the relevant suite + answer key (and the deployed eval-05 judge once calibrated), bucket findings `bad`/`sad` per `Evals/severity-taxonomy.md`, and log the **bad-rate** to `Evals/monitoring/<YYYY-Www>.md`. If the bad-rate rose or a new `bad` failure mode recurs, note it here for [YOUR_MANAGER] ("eval monitoring caught a hallucinated-metric trend — fixing the harness") and register any needed re-run via `/eval-ci`. This is the loop that makes "every response is evaluated" real without grading in the authoring context.

---

**After sending this update:**
- `meeting prep [YOUR_MANAGER]` — prep for the alignment conversation if 1:1 is upcoming
- `follow-ups` — scan for open action items from recent meetings
- `roadmap review` — if you haven't done one this week, check milestone status next
