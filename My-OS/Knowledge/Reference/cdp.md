# Customer Data Platform (CDP) — Reference

*Running reference on the CDP initiative. Update as the project evolves.*

---

## What We're Trying to Achieve

A CDP at Kpay will create a **single source of truth** for customer data across the Digital Growth team, enabling:

- **Retention** — Identify at-risk merchants and trigger proactive lifecycle campaigns
- **Activation** — Accelerate new merchant time-to-first-transaction
- **Growth** — Surface high-value segments for upsell and expansion
- **Paid efficiency** — First-party audiences for suppression, retargeting, lookalikes
- **ROAS improvement** — Better signals → smarter bidding → lower CAC
- **Personalization** — Segment-driven content and web experiences

---

## CDP Use Case Candidates

*Shortlist in progress — validate with team in discovery sessions*

| Use Case | Team | Business Impact | Data Needed | Complexity |
|----------|------|----------------|-------------|------------|
| Lifecycle re-engagement | Rachel | Retention ↑ | Behavioral + transaction | Medium |
| Onboarding activation journey | Rachel | Activation ↑ | Sign-up + product usage | Medium |
| Paid ads suppression | Xinyi | CAC ↓, ROAS ↑ | Customer list | Low |
| Lookalike audience creation | Xinyi | Acquisition ↑ | High-LTV segment | Low-Medium |
| Web personalization | Lina | Conversion ↑ | Segment + web behavior | High |
| Content targeting by segment | Mardiana | Engagement ↑ | Segment data | Medium |

**Flight 1 candidates:** Paid suppression or lifecycle re-engagement (high impact, lower complexity)

---

## CDP Vendor Landscape

*Shortlist TBD after use case is finalized*

| Vendor | Type | Best For | Notes |
|--------|------|---------|-------|
| Segment (Twilio) | Composable CDP | Dev-heavy teams, flexible | Strong integrations |
| Rudderstack | Composable CDP | Open-source option | Good for cost-conscious |
| mParticle | Enterprise CDP | Mobile-heavy use cases | More complex |
| Bloomreach | Marketing CDP | Lifecycle + personalization bundled | SME-friendly |
| Treasure Data | Enterprise CDP | Large data volumes | Heavier implementation |
| Insider | Marketing CDP | Personalization-first | Strong SEA presence |

---

## Key Data Sources to Unify

- **Transaction data** — payment events, merchant volume, transaction frequency
- **CRM / merchant profile** — sign-up data, segment, industry, size
- **Web behavior** — page visits, feature exploration, drop-off
- **Email engagement** — opens, clicks, unsubscribes
- **Paid ads** — click-through, conversion events
- **In-app / product usage** — feature adoption, session data

---

## Success Metrics for CDP

| Metric | Target | Timeframe |
|--------|--------|-----------|
| Data sources unified | ≥ 3 | Day 90 |
| Flight 1 use case live | 1 | Day 90 |
| Team members activated on CDP | ≥ 2 | Day 90 |
| Retention rate improvement | TBD | Q3 2026 |
| ROAS improvement | TBD | Q3 2026 |

---

## Open Questions

- What is the current state of data infrastructure at Kpay? Is there a data warehouse?
- Who owns data engineering — is there a data team we'll partner with?
- What's the existing identity resolution setup (how do we stitch web + transaction + CRM)?
- Are there any compliance / data privacy constraints (PDPA, GDPR-equivalents)?
- What's the budget range for CDP tooling?
