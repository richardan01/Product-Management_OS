# Sample passing output — eval 03 (persona routing respected)

Based on the Jordan Lee fixture (Executive operator persona). Graders use this as the anchor for correct non-Batman persona handling.

---

## CLAUDE.md excerpt — passes C1, C2, C4

```markdown
## Onboarding mode

Default persona: Executive operator

## Routing

**Strategic layer:** Skills + Workflows only (default). `Agents/Gotham/Computer/` is available but not routed by default. To activate Batman-layer routing, re-run onboarding and select Batman strategic operator.

## Quality gates

Before any public artifact ships:
- `/peer-review` — default pre-publish gate
- `/go-nogo` for launches
- `/riddler` + `/vale` — available as optional add-ons; not mandatory for this persona
```

**Why C1 passes:** `Default persona` is `Executive operator`, not `Batman strategic operator`.
**Why C2 passes:** routing section explicitly states Batman layer is available but not routed.
**Why C4 passes:** `/peer-review` is the default gate; `/riddler` + `/vale` are listed as optional, not mandatory.

---

## First commands recommendation — passes C3

> "Here are the first three commands to try with your new setup:
> - `/today` — start each workday with a morning brief
> - `/meeting-prep [person]` — prep for any 1:1 or stakeholder meeting
> - `/weekly-update` — end-of-week update for your manager
> - `/peer-review [file]` — pre-publish gate for any artifact you share externally"

**Why C3 passes:** list leads with `/today`, `/weekly-update`, `/meeting-prep`, `/peer-review`. Does not contain `/cowl-up`, `/riddler`, or `/vale` in the recommended-first-commands list.

---

## Batman agents preserved — passes C5

`Agents/Gotham/Computer/` still contains all 12 files:
```
alfred.md, batman.md, bruce-wayne.md, gordon.md, henri-ducard.md,
lucius-fox.md, nightwing.md, oracle.md, riddler.md, robin.md,
selina-kyle.md, vicki-vale.md
```

None were deleted. The opt-in path is intact.

---

## Voice — passes C6

The assistant addressed the user as "Jordan" throughout, not "Master Jordan." No Batman idioms used ("the cowl," "the cave," "tonight's mission"). Tone was concise and outcome-driven throughout.
