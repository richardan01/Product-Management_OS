# Sample failing output — eval 03 (persona routing respected)

Examples of each failure mode. Graders use these as anchors.

---

## C1 fails — Batman persona applied by default

```markdown
Default persona: Batman strategic operator
```

User chose Executive operator. The assistant defaulted to Batman, either by muscle memory or by treating the Batman layer as the "real" persona regardless of what the user chose.

---

## C2 fails — Batman routing note missing

```markdown
## Routing

**Strategic layer:** Skills + Workflows only (default).
```

The routing section says "Skills + Workflows only" but does not say Batman is available for opt-in. A future session re-running onboarding would not know Batman is available. C2 requires the explicit note that `Agents/Gotham/Computer/` is available but not routed.

---

## C3 fails — Batman commands surfaced first

> "Here are the first three commands to try:
> - `/cowl-up` — activate Batman execution mode for high-stakes moments
> - `/riddler` — adversarial review before shipping anything
> - `/vale` — user-voice review
> - `/today` — morning brief"

`/cowl-up` and `/riddler` lead the list. These are Batman-layer commands. For an Executive operator, they should not be surfaced as primary commands.

---

## C4 fails — Riddler + Vale set as mandatory

```markdown
## Quality gates

Before any public artifact ships:
- `/riddler` + `/vale` mandatory pre-publish
```

Jordan Lee chose Executive operator with `/peer-review` as the default gate. Setting `/riddler` + `/vale` as mandatory applies Batman gates to a non-Batman persona. C4 fails.

---

## C5 fails — Batman agents deleted

```
Agents/Gotham/Computer/
  (empty — all 12 agent files removed)
```

The assistant deleted the Batman agents because "the user chose Executive operator and won't use them." This destroys the opt-in path. Once deleted, the user cannot re-run onboarding and activate Batman mode without restoring from git or re-downloading the template.
