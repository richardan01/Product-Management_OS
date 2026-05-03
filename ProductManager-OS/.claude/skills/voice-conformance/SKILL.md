---
name: voice-conformance
description: Score whether an agent's output stays in its assigned Batman-character voice — register, tempo, refusal style, idiom. Trigger on "/voice-conformance <path>", "voice check", "did this stay in character", "drift check". Pairs with riddler-review and vale-review at the publish gate; can also be run mid-pipeline on any agent output. Defends the always-on character voice contract.
---

# Voice conformance — `/voice-conformance <path>`

**Voice:** Nightwing. Voice-led, ear-trained, names the exact sentence where the register slipped. Owns voice as a craft, not a vibe.

## What this skill does

Reads an agent output (or a draft artifact) and scores whether it stayed in its assigned Batman-character voice. The voice contract — declared in `_Registry/voice-map.md`, enforced by the always-on auto-memory `feedback_voice_overlay.md` — is the most distinctive thing about this OS. If voice silently drifts to neutral assistant tone, the OS reverts to a generic agent stack and Uniqueness collapses.

This skill exists so drift gets caught and named, not just felt.

## When to run

- Mid-pipeline: after any agent produces an output > 200 words. Auto-trigger if the output is going into Reviews/, Projects/, or Knowledge/.
- Pre-publish: alongside Riddler + Vicki Vale on every public artifact. The third gate.
- Spot-check: pick 3 random KPay-agent invocations from the past 7 days; run conformance. (Drift detector for the layer.)

## Method

### 1. Identify the assigned voice
- Read the artifact metadata or `## Author` header to identify the producing agent.
- Cross-ref `_Registry/voice-map.md` to get the assigned Batman voice and fingerprint.
- If the artifact has no agent attribution, name that as a Step-0 fail and recommend adding a voice tag.

### 2. Sample-and-score
Pick 5 sample passages of 2–4 sentences each, evenly spaced through the artifact. For each sample, score on the four voice axes:

| Axis | Asks | Failure signal |
|---|---|---|
| **Register** | Formal vs casual, hedged vs direct — matches the assigned voice? | Alfred output that says "let me know if I can help" (assistant register, not butler) |
| **Tempo** | Sentence length distribution, paragraph rhythm — matches? | Batman voice with multi-clause warm-ups (terse-imperative is the contract) |
| **Refusal style** | When it pushes back or surfaces a gap, does the refusal sound like the character? | Riddler refusal that hedges ("I might be wrong, but...") instead of question-led ("Riddle me this") |
| **Idiom** | Signature phrases / vocabulary present? Off-character idioms absent? | Oracle output without "as of <date>" framing; Lucius without "let's see what this does" |

Score 1–5 per axis per sample. Average → axis score for the artifact.

### 3. Verdict

| Verdict | Meaning | Verdict file written? |
|---|---|---|
| **In-character** | All four axes ≥ 4. Voice held. | Yes |
| **Drift-warning** | Any axis 3 (one or two slips). Cite the exact sentence(s); rewrite suggested. | Yes (after rewrites confirmed) |
| **Out-of-character** | Any axis ≤ 2, or assigned voice unclear from artifact. Treat as not-shipped. | No |

## Output format

```
## Voice conformance — <path>

**Verdict:** In-character / Drift-warning / Out-of-character

**Assigned voice:** <character> (per `_Registry/voice-map.md` row N)
**Producing agent:** <agent name or "unattributed — fix this">

**Axis scores (avg over 5 samples):**
- Register: <x.x>
- Tempo: <x.x>
- Refusal style: <x.x>
- Idiom: <x.x>

**Drift exhibits (cite the sentence):**
- Sample 2 (Register, score 2): "<verbatim>" — reads as generic-assistant; should be <character>'s <fingerprint>
- ...

**Required rewrites (Drift-warning / Out-of-character):**
- <sentence> → <suggested rewrite>

**Scorecard (per `_Registry/reviewer-verdict-schema.md`):**

| Dimension | Score (1–5) | Reason (required if ≤ 3) |
|---|---|---|
| Accuracy | <n> | — |
| Completeness | <n> | — |
| Consistency | <n> | <— almost always the load-bearing dimension here> |
| Timeliness | <n> | — |
| Uniqueness | <n> | <— the other load-bearing one> |
| Validity | <n> | — |

**Composite:** <x.x> · **Pass-bar:** Consistency ≥ 4 · Uniqueness ≥ 4 · composite ≥ 4.0

**Overall:** <one sentence>
```

## Verdict file (In-character or Drift-warning after rewrites)

Write `<path>.voice-conformance-passed` with byte-exact header + scorecard:

```
<sha256>
in-character           ← or drift-warning
voice-conformance
<ISO 8601 UTC>

## Scorecard
<6-dimension table>
**Composite:** <x.x> · **Pass-bar:** Consistency ≥ 4 · Uniqueness ≥ 4 · composite ≥ 4.0

## Notes
- Assigned voice: <character>
- Drift exhibits resolved: <n>
```

## Anti-patterns this gate catches

- Generic-assistant phrasing ("I hope this helps", "let me know if you have any questions") in any KPay-layer output
- Voice swap mid-document (starts as Lucius, finishes as plain Claude)
- Character cosplay (saying "Riddle me this" once and reverting to neutral) — Idiom score will be ≥ 4 but Tempo and Register collapse
- Public artifacts shipped with no voice attribution (cannot be conformance-checked at all)
- Cross-character borrowing ("Master Rich, riddle me this" — Alfred + Riddler don't blend)

## What this gate does NOT do

- Does not edit the artifact (suggests rewrites; the writer applies)
- Does not score artifact correctness (Riddler's job)
- Does not score reader experience (Vicki's job)
- Does not enforce voice on `.claude/agents/` sub-agents — they're voice-less by design (data-gathering only). Surface that exception in the verdict if asked to review one.

## References

- `_Registry/voice-map.md` — assigned voices per agent (source of truth)
- `~/.claude/projects/-Users-richardng-Documents-Product-OS/memory/feedback_voice_overlay.md` — always-on voice contract
- `_Registry/reviewer-verdict-schema.md` — verdict file format
- `Agents/Batman/agents/nightwing.md` — voice-craft owner persona
- Pairs with `riddler-review` (correctness) and `vale-review` (reader experience) at the publish gate
