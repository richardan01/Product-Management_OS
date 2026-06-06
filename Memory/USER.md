# User — durable identity & preferences

Canonical durable copy of who the user is and how the assistant should behave.
The runtime memory cache mirrors a compact subset of this file. On conflict,
this file wins.

> Filled during interactive onboarding. Keep placeholders until the user
> confirms. No sensitive data here — see `MEMORY_POLICY.md`.

## Identity
- **Name:** [YOUR_NAME]
- **Role:** [YOUR_ROLE]
- **Company / org:** [YOUR_COMPANY]
- **Team / domain:** [YOUR_TEAM]
- **Manager / sponsor:** [YOUR_MANAGER]

## Operating style (durable preferences)
- **Default persona:** [persona]
- **Tone:** [tone]
- **Detail level:** [brief / standard / thorough]
- **Pushback level:** [low / medium / high]
- **Decision style:** [tradeoff-first / recommendation-first / options-first]
- **Review style:** [light edit / strict / adversarial]
- **Turn-offs:** [what makes the user tune out]
- **Ideal response feel:** [what a great response looks like]

## Thought frameworks
- **Tradeoff priority:** [e.g., quality > speed > learning]
- **Evidence standard:** [e.g., data > expert judgment > user feedback]
- **Decision certainty bar:** [70% / 80% / 90%+]
- **Acceptable failure:** [learning vs. avoidable]

> `CLAUDE.md` remains the live behavior contract the runtimes apply each turn.
> This file is the durable, harness-neutral record onboarding writes and the
> runtime cache mirrors.
