# Introspection prompts

Extracted from the "Introspection Loop (The AI PM Move)" section of `evals/SKILL.md`.

This is the highest-leverage habit in the suite. After any eval failure:

1. Show the model its own output
2. Show it the criterion it missed
3. Ask: *"Why did you produce this output? What in your context led to this decision?"*

The model will often surface the actual harness bug — a confusing line in the
skill, a missing piece of context, a misinterpreted instruction. **That's the
fix.** Apply it, re-run the eval, verify it passes.

Cat Wu's exact framing: *"A lot of times just being very curious about why
the model made the decision that it did will show you what misled it so that
you can fix the harness in order to close this gap."*
