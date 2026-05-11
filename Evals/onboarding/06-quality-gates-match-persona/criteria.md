# Pass criteria — Quality gates match persona

The quality-gate config must reflect the persona the user chose, per the persona-effects matrix.

## Criteria (binary)

1. ✅ / ❌ Executive operator run: `CLAUDE.md` → `Quality gates` lists `/peer-review` as the default pre-publish gate.
2. ✅ / ❌ Executive operator run: `/riddler` and `/vale` are listed only as optional opt-ins, not mandatory.
3. ✅ / ❌ Batman run: `CLAUDE.md` → `Quality gates` lists `/riddler` + `/vale` as mandatory pre-publish gates.
4. ✅ / ❌ Both runs preserve the standard PM gates (`/peer-review`, `/prd-readiness`, `/research-sufficiency`, `/go-nogo`) regardless of persona.
5. ✅ / ❌ The two runs produce **different** `Quality gates` sections — if they're identical, persona-aware gating failed.

## Failure modes this catches

- Assistant applies Batman gates by default regardless of persona.
- Assistant strips standard PM gates when downgrading from Batman.
- Assistant produces identical configs for Batman vs Executive operator (silent persona collapse).
- Assistant lists `/riddler` and `/vale` as mandatory for a persona row that doesn't require them.
