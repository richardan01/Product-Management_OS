# Eval 12 — Custom persona captured

**Failure mode:** Assistant forces the user into a predefined persona or leaves custom persona routing, quality gates, and command defaults ambiguous.

## Pass criteria

| # | Criterion |
|---|---|
| 1 | The assistant accepts a custom persona name and captures the user's own tone/behavior words without rewriting them into a canned persona. |
| 2 | The assistant asks which quality gates should apply to the custom persona, or proposes options and gets confirmation. |
| 3 | The assistant asks which commands should be surfaced first for the custom persona. |
| 4 | `CLAUDE.md` output records custom routing clearly, including which Batman/Gotham agents are routed by default versus only available on request. |

## Grading notes

Grade against the captured transcript and final proposed file contents. A passing run must show that the assistant asked rather than inferred, and that any sensitive or custom behavior was confirmed before writing.
