# Sprint Retro

**Agent:** Retro & Learning Coach
**Methodology:** Four Ls (Liked / Learned / Lacked / Longed For); Sailboat variant

Run an end-of-sprint retrospective. Keep it focused — aim to complete in under 15 minutes.

## Steps

1. **Read:**
   - `Tasks/active.md` — what completed, what carried over, what was blocked
   - `Tasks/archive/` — last sprint's archived items (velocity reference)
   - `Tasks/archive/retro-*.md` — last retro (check if previous action was done)
   - `Knowledge/Reference/lessons-learned.md` — prior patterns (for context)

2. **Three questions:**

   **What worked well?**
   - 2–3 specific things that went smoothly or exceeded expectations
   - Be concrete: not "comms were good" but "sending the brief 2 days ahead meant [YOUR_MANAGER] had context"

   **What didn't work?**
   - 2–3 friction points, blockers, or surprises
   - Diagnose the system: estimation error? unclear ownership? external dependency? wrong priority?

   **What's the one change to make next sprint?**
   - ONE change. Not five. The single highest-leverage adjustment.
   - Format: "We will [specific action] so that [expected outcome]"

3. **Check last retro's action:**
   - Was the one change from last sprint implemented? Yes / No / Partial
   - If No — carry it forward or explicitly decide to drop it (with reason)

4. **Velocity:**
   - Tasks completed vs planned: [n]/[n] ([%])
   - Flag if consistently <70% — likely an estimation or priority problem

5. **Output:**

```
**Sprint Retro — [Date] — Sprint [n]**

**Velocity:** [n completed] / [n planned] ([%])

**Worked well:**
- [item]

**Didn't work:**
- [item]

**One change next sprint:**
> We will [X] so that [Y].

**Last retro's action:** [Done ✓ / Not done — carrying forward / Dropping because: reason]
```

6. **Save to** `Tasks/archive/retro-[date].md`
7. **Distill the memory loop (proposal-only).** Read `Memory/SESSION_LOG.md` — the daily takeaways `/eod` staged this sprint. For any that **recurred** or proved durable:
   - A repeated *working/behavior* pattern → propose promoting it to `Memory/PATTERNS.md`.
   - A settled *operating decision* (with its reasoning) → propose promoting it to `Memory/DECISIONS.md`.
   Then propose pruning the promoted lines from `Memory/SESSION_LOG.md` so it stays a short staging area, not an archive. Apply the 5-question write-gate in `Memory/MEMORY_POLICY.md` to each promotion. Product/process learnings that aren't durable *operating* facts stay in this retro's archive entry, not in `Memory/`. Do not edit any `Memory/` file until the user confirms.

---

**What to run next:**
- `today` — start the new sprint with updated priorities from the retro
- `risk-register` — capture any new risks or blockers surfaced during the retro
- `quarterly-planning` — if this is the last sprint of the quarter, plan the next quarter now
- `lessons` — review the full cumulative log if you want broader patterns
- `growth-check` — run at your 30, 60, and 90 day marks to assess personal progress
