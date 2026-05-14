# Sample passing output — eval 06 (quality gates match persona)

Shows both the Executive operator (Jordan Lee) and Batman (Sam Okafor) configurations side by side. Graders use this to verify the two runs produce different gate configs.

---

## Executive operator — CLAUDE.md quality gates section (Jordan Lee)

```markdown
## Quality gates

- After PRD / business case / research → `/peer-review [file]`
- Before engineering handoff → `/prd-readiness [file]`
- Before decision from research → `/research-sufficiency [file]`
- Before launch → `/go-nogo [project]`
- **Before any public artifact ships → `/peer-review` (default gate)**
- `/riddler` and `/vale` available as optional add-ons; not mandatory for this persona
```

**Why C1 passes:** `/peer-review` is the explicit default pre-publish gate.
**Why C2 passes:** `/riddler` and `/vale` are listed as optional, not mandatory.
**Why C4 passes:** standard PM gates (`/prd-readiness`, `/research-sufficiency`, `/go-nogo`) are all present.

---

## Batman — CLAUDE.md quality gates section (Sam Okafor)

```markdown
## Quality gates

- After PRD / business case / research → `/peer-review [file]`
- Before engineering handoff → `/prd-readiness [file]`
- Before decision from research → `/research-sufficiency [file]`
- Before launch → `/go-nogo [project]`
- **Before any public artifact ships → `/riddler` + `/vale` (mandatory — no exceptions)**
```

**Why C3 passes:** `/riddler` + `/vale` are explicitly mandatory.
**Why C4 passes:** same standard PM gates present.
**Why C5 passes:** Batman section does not list `/riddler` + `/vale` as optional — it lists them as mandatory. Executive operator section lists them as optional. The two sections are different.
