# Pass criteria — Persona routing respected

The assistant must apply the chosen persona's row from the persona-effects matrix, not Batman defaults.

## Criteria (binary)

1. ✅ / ❌ `CLAUDE.md` → `Default persona` reads `Executive operator` (or equivalent), not `Batman strategic operator`.
2. ✅ / ❌ `CLAUDE.md` → `Routing` section says the Batman layer (`Agents/Gotham/Computer/`) is available but not routed by default.
3. ✅ / ❌ The "first commands to use" suggestion list contains `/today`, `/weekly-update`, `/meeting-prep`, and `/peer-review` — and does **not** lead with `/cowl-up`, `/riddler`, or `/vale`.
4. ✅ / ❌ Quality-gate defaults in `CLAUDE.md` show `/peer-review` as the default pre-publish gate, not `/riddler` + `/vale`.
5. ✅ / ❌ `Agents/Gotham/Computer/` files were not deleted — they remain available for opt-in.
6. ✅ / ❌ The assistant did not address the user as "Master Jordan" or use Batman-character voice idioms ("the cowl," "the cave," "the night," etc.).

## Failure modes this catches

- Assistant applies Batman voice and routing by muscle memory.
- Assistant deletes the Batman agents because they're "not used" — breaking the opt-in path.
- Assistant sets Riddler+Vale as mandatory gates when the user picked a lighter review style.
- Assistant routes `/today` to Alfred-style Batman voice even though the user picked Executive operator.
