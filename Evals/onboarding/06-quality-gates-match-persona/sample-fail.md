# Sample failing output — eval 06 (quality gates match persona)

Examples of each failure mode. Graders use these as anchors.

---

## C1 fails — /peer-review not set as default for Executive operator

```markdown
## Quality gates

- **Before any public artifact ships → `/riddler` + `/vale` (mandatory)**
```

Jordan Lee chose Executive operator. The assistant applied Batman's mandatory `/riddler` + `/vale` instead of `/peer-review`. C1 fails — `/peer-review` is not the default gate.

---

## C2 fails — /riddler and /vale listed as mandatory for Executive operator

Same as above. The problem is not just that `/peer-review` is missing — it's that the heavier Batman gates are set as mandatory for a persona that explicitly does not require them.

---

## C3 fails — Batman config uses /peer-review instead of /riddler + /vale

```markdown
## Quality gates

- **Before any public artifact ships → `/peer-review` (default gate)**
- `/riddler` available as optional add-on
```

Sam Okafor explicitly chose Batman strategic operator. The assistant did not update the mandatory gate from `/peer-review` (the template default) to `/riddler` + `/vale`. Batman mode requires both as mandatory.

---

## C4 fails — standard PM gates stripped for Minimalist persona

```markdown
## Quality gates

- **Before any public artifact ships → `/peer-review` (light edit)**
```

Standard PM gates (`/prd-readiness`, `/research-sufficiency`, `/go-nogo`) were removed because Riley Park chose Minimalist. Minimalist persona reduces ceremony but does not strip the standard PM quality gates — those are universal.

---

## C5 fails — identical configs across Batman and Executive operator runs

Batman config:
```markdown
- **Before any public artifact ships → `/peer-review` (default gate)**
```

Executive operator config:
```markdown
- **Before any public artifact ships → `/peer-review` (default gate)**
```

Both runs produce the same quality-gate config. The persona-aware gating collapsed silently. The most likely cause: the assistant set the config once in Phase 2 and did not change it based on the Batman vs. non-Batman distinction.
