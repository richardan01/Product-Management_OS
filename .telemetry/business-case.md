# Product Telemetry: Business Case for Kpay CDP

**Audience:** Jervis (Head of Digital Growth)
**Date:** March 2026
**Owner:** Richard Ng

---

## The Problem: What Our Analytics Can't Tell Us

Kpay's Digital Growth team is paying for analytics tools across every channel — GA4, SensorData, HubSpot, Tableau — but none of them can answer the questions that matter most. The tools aren't broken. The data going in is incomplete.

Right now, these questions have no answer:

- **Which merchants are about to churn?** No unified engagement signal exists — transaction data, email activity, and in-app behavior all live in separate tools. Analytics can't connect them.
- **Which merchants came in from paid ads and actually activated?** Attribution is broken — there's a 1+ month lag between MQL and conversion data, and no identity bridge from web visitor to known merchant. Xinyi's ROAS figures are estimates at best.
- **Are new merchants reaching value, or stalling?** SensorData has in-app events. HubSpot has email. The transaction DB has GPV. No tool can see all three at once — so the onboarding funnel is invisible.
- **Which merchants are high-LTV?** The signal exists in Redshift, but it can't reach the ad platforms. Xinyi is building audiences from stale exports, not real-time scores.
- **What does the Kpay merchant actually look like?** No unified identity exists. The same merchant may exist as a web visitor in GA4, a contact in HubSpot, and a transaction record in Redshift — and the tools don't know it's the same person.

---

## What Proper Instrumentation Unlocks

This isn't about buying new tools. It's about making the stack Kpay already pays for actually work. Once the right data is flowing into a CDP — unified, clean, and connected — the existing tools can finally deliver:

| What Becomes Possible | Why It Matters |
|----------------------|----------------|
| **Analytics can surface at-risk merchants before they churn** | CS and Rachel can act on engagement signals, not quarterly reviews. Retention becomes proactive, not reactive. |
| **Xinyi's ad platforms can receive real-time high-LTV audiences** | Less wasted spend on existing customers; better ROAS from lookalike audiences built on actual behavior, not stale lists. |
| **Rachel's lifecycle tool can trigger on real merchant events** | Onboarding drop-off, first transaction, 30-day inactivity — all become triggers for automated journeys. Today, they're invisible. |
| **Tableau and Redshift can finally show a merchant-level funnel** | From first web visit to activation to GPV growth — one view, one source of truth, powering the full team. |

---

## What's Involved

This is a focused implementation project, not a rebuild. AI-assisted tooling eliminates most of the heavy lifting:

**Step 1 — Audit what's already tracked.**
AI scans the codebase and produces an inventory of every tracking call — what events exist, what's misconfigured, what properties are missing. This takes minutes, not days. It's the first honest picture of what data is actually flowing to analytics today.

**Step 2 — Design the tracking plan.**
Historically the hardest part. AI generates a best-practice event schema tailored to Kpay's specific entity model (merchant, terminal, transaction, lifecycle stage) and the team's use cases. The team reviews and adjusts — a conversation, not a project. Roughly 80% is automated.

**Step 3 — Implement.**
Tracking follows established patterns. AI generates typed event definitions and SDK wrappers that match existing conventions. Engineering reviews and integrates. Not a new system — additions to existing code paths.

**What this is NOT:**
- Not a data warehouse project — Redshift and Tableau stay as-is
- Not a rip-and-replace — HubSpot, GA4, and SensorData continue to function
- Not a manual spec exercise — AI eliminates the blank-page problem

Effort: days of engineering time, not weeks. Ongoing cost per new feature: under an hour.

---

## Getting Started

The first step is free of risk and produces immediate value:

1. **Audit** — AI scans the codebase and maps everything currently flowing to analytics tools. Takes minutes. Shows exactly what data is reaching CDP candidates today vs. what should be.
2. **Design** — AI generates a tracking plan for Kpay's merchant model. Team reviews and signs off.
3. **Implement** — AI generates the instrumentation code. Engineering integrates.

The audit alone answers a question the team doesn't currently know the answer to: *what data is actually in our stack right now?* That's worth doing before CDP vendor selection, not after.
