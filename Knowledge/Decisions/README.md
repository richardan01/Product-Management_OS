# Knowledge/Decisions

Decisions are **irreversible-until-reversed choices** with recorded reasoning. The moment a decision is made, the *why* and *alternatives rejected* are more valuable than the outcome itself — they prevent revisiting dead debates and make strategy legible to future collaborators (including future-you).

---

## State machine

```
pending → active → archived
```

| State | Meaning | Location |
|---|---|---|
| `pending` | Decision needed; options defined, not yet called | `pending/` |
| `active` | Decision in force; guiding current work | `active/` |
| `archived` | Superseded, shipped, or no longer relevant | `archived/` |

---

## File naming

```
YYYY-MM-DD-[short-slug].md
```

Example: `2026-05-21-drop-android-v1.md`

---

## Lifecycle rules

1. **Creating a pending decision:** Draft from a confirmed hypothesis or when a real fork in the road appears. Must include at least two options.
2. **pending → active:** Call the decision. Record the chosen option, alternatives rejected with reasoning, and the provenance tag for the deciding evidence. Add the date.
3. **active → archived:** When the decision is superseded (new decision overrides it), the feature ships, or context changes enough that the decision no longer applies. Extract durable lessons before archiving.
4. **Reversal condition:** Every active decision should have a stated reversal condition — the signal that would cause you to revisit it. If that condition triggers, move back to pending.

---

## Decision debt

Decision debt accumulates when:
- Pending decisions have no owner or deadline
- Active decisions have no reversal condition
- Confirmed hypotheses exist without a linked decision

The `/wiki-maintain` weekly sweep reports decision debt.

---

## Template

Use `Templates/decision.md` for all new entries.

---

## Related

- `Templates/decision.md`
- `Knowledge/Hypotheses/README.md` — hypotheses feed decisions
- `Knowledge/Reference/provenance-tags.md` — decisions cite evidence provenance
- `.claude/skills/wiki-maintain/SKILL.md` — weekly sweep checks decision hygiene
