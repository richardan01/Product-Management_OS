# Memory — canonical durable memory

This folder is the OS's **canonical durable memory**. It is harness-neutral:
Claude Code, Codex CLI, Gemini CLI, and other compatible runtimes all read it
on session start.

**The repository is the source of truth.** Each runtime's own memory feature
(e.g. an auto-loaded `MEMORY.md`) is only a *lightweight pointer/cache* holding
compact durable preferences and environment facts. The canonical record lives
here, so memory persists across runtimes and survives a fresh clone.
**On conflict, the repo files win** — refresh the runtime cache to match.

## File map

| File | Holds |
|---|---|
| `USER.md` | Durable identity and operating-style preferences |
| `OPERATING_CONTEXT.md` | Durable cadence, week anchor, recurring meetings, anchor-project pointer |
| `DECISIONS.md` | Durable operating / meta decisions about how the OS runs |
| `PATTERNS.md` | Recurring patterns the assistant should reuse |
| `STAKEHOLDER_MEMORY.md` | Compact stakeholder pointers (approval-gated) |
| `SESSION_LOG.md` | Append-only durable takeaways per session |
| `MEMORY_POLICY.md` | The write-gate, conflict, and sensitivity rules — read this first |

## What belongs here — and what does not

Memory is for **durable** preferences, patterns, decisions, and operating
context. It is **not** for:

- Temporary task state → `Tasks/`
- Project context → `Projects/`
- Validated reference facts → `Knowledge/`
- Meeting dumps, PRD drafts → the relevant artifact file
- Credentials, API keys, private customer data, sensitive company data → never

Before writing anything here, pass the 5-question gate in `MEMORY_POLICY.md`.

## Source-of-truth boundaries

- `Tasks/active.md` — current task state
- `Projects/` — project context
- `Knowledge/` — validated reference facts
- `Memory/` — durable preferences, patterns, decisions, operating context

## Privacy

This is a public template. Ship these files as placeholders. Sensitive
stakeholder / company / customer facts require **explicit approval** before
writing. Keep real private context in a private fork or local copy.
