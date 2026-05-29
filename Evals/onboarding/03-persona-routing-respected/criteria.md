# Pass criteria — Persona routing respected

The assistant must apply the chosen persona's row from the persona-effects matrix, not the defaults of a different (heavier) persona.

## Criteria (binary)

1. ✅ / ❌ `CLAUDE.md` → `Default persona` reads `Executive operator` (or equivalent), matching the user's choice.
2. ✅ / ❌ The "first commands to use" suggestion list contains `/today`, `/weekly-update`, `/meeting-prep`, and `/peer-review` — and does **not** lead with Builder/AI PM gates (`/eval-review`, `/build-review`, `/test-plan`) the user did not ask for.
3. ✅ / ❌ Quality-gate defaults in `CLAUDE.md` show `/peer-review` as the default pre-publish gate, not the heavier Builder/AI PM mandatory gate set.
4. ✅ / ❌ Default tone matches the Executive operator row (concise, outcome-driven) — not a different persona's voice.

## Failure modes this catches

- Assistant applies a heavier persona's gates by muscle memory.
- Assistant sets `/eval-review` + `/build-review` + `/test-plan` as mandatory when the user picked a lighter review style.
- Assistant surfaces commands from a persona the user did not choose.
