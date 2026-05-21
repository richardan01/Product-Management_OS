# Knowledge/Hypotheses

A hypothesis is a **testable belief about users, the market, or the product** that drives current work. This layer tracks the full investigation lifecycle so decisions can be traced back to their evidence — and wrong bets are preserved, not deleted.

---

## State machine

```
candidate → proposed → confirmed
                    ↘ rejected
```

| State | Meaning | Location |
|---|---|---|
| `candidate` | A hunch or signal worth investigating; not yet actively resourced | `candidate/` |
| `proposed` | Actively being tested; has a research plan or experiment | `proposed/` |
| `confirmed` | Evidence threshold met; a Decision record should exist or be drafted | `confirmed/` |
| `rejected` | Falsified; evidence showed the opposite | `rejected/` |

**Critical rule:** Rejected hypotheses are **never deleted**. They are the most valuable files in this folder — they prevent re-running dead ends.

---

## File naming

```
YYYY-MM-DD-[short-slug].md
```

Example: `2026-05-21-retention-drop-month3.md`

---

## Lifecycle rules

1. **candidate → proposed**: Assign a research method and timeframe. Update state header.
2. **proposed → confirmed**: Evidence must meet the confidence bar set in `CLAUDE.md` Thought frameworks. Log the confirming evidence rows. Draft or link a Decision record.
3. **proposed → rejected**: Log falsifying evidence. Move to `rejected/`. Add a one-line note to `Knowledge/log.md`.
4. **confirmed → rejected**: Allowed if new evidence overturns the prior. Add a reversal note to the file; move to `rejected/`. Update any linked Decision records.

---

## Relationship to Decisions

When a hypothesis is **confirmed**, it should trigger one of:
- A new Decision in `Knowledge/Decisions/pending/`
- An update to an existing Decision (evidence row added)

The hypothesis file should link to the decision: `See: Knowledge/Decisions/active/YYYY-MM-DD-slug.md`

---

## Template

Use `Templates/hypothesis.md` for all new entries.

---

## Related

- `Templates/hypothesis.md`
- `Knowledge/Decisions/README.md`
- `Knowledge/Reference/provenance-tags.md`
- `.claude/skills/wiki-ingest/SKILL.md` — ingestion can seed candidate hypotheses
- `.claude/skills/wiki-maintain/SKILL.md` — weekly sweep checks hypothesis hygiene
