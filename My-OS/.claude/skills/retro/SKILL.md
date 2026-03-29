# Sprint Retro

**Agent:** Retro & Learning Coach — see `Agents/retro-coach/retro-coach.md` for full context.

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
   - Be concrete: not "comms were good" but "sending the brief 2 days ahead meant Jervis had context"

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
7. **Update** `Knowledge/Reference/lessons-learned.md` with any durable insight

---

**Next Steps:**
- `today` — start the new sprint with updated priorities from the retro
- `lessons` — review the full cumulative log if you want broader patterns
- `growth-check` — run at your 30, 60, and 90 day marks to assess personal progress
