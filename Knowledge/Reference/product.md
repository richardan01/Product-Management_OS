# KPay Martech Stack Overview

## What I'm Building

As Martech PM, I own the end-to-end marketing technology stack — the tools and data infrastructure that power how KPay acquires, retains, and grows its merchant customer base.

**Current flagship initiative:** CDP implementation — establishing a single source of truth for event tracking and customer lifecycle management.

---

## Martech Stack Categories

| Category | Purpose | Current Tool(s) | Status |
|----------|---------|-----------------|--------|
| CDP | Unified customer profiles, segmentation, activation | *(fill in after day 1)* | In evaluation / implementation |
| CRM | Customer relationship management, sales pipeline | *(fill in)* | *(fill in)* |
| Analytics | Product and marketing analytics | *(fill in)* | *(fill in)* |
| Email / SMS | Lifecycle and campaign messaging | *(fill in)* | *(fill in)* |
| Ad Platforms | Paid acquisition (search, social, display) | *(fill in)* | *(fill in)* |
| AI Tools | Generative content, predictive modelling | *(fill in)* | *(fill in)* |
| Tag Management | Event collection and routing | *(fill in)* | *(fill in)* |

---

## Data Flow Architecture

```
Sources (event data)
  ├── Web (website, product)
  ├── Mobile (app)
  ├── Email (opens, clicks)
  ├── Ads (impressions, conversions)
  └── 2nd/3rd-party (partner data, enrichment)
        │
        ▼
    CDP (ingest → unify → profile)
    - Unified customer profiles
    - Customer lifecycle tags
    - Real-time segmentation
        │
        ▼
Activation channels
  ├── Email / SMS (triggered campaigns)
  ├── Paid ads (lookalike audiences, retargeting)
  ├── CRM (sales signals, account enrichment)
  └── Analytics / BI (reporting, insights)
```

---

## Data Types

| Type | Description | Examples |
|------|-------------|---------|
| 1st-party | Data KPay collects directly from users | Website events, app usage, transaction history |
| 2nd-party | Partner data shared under agreement | *(fill in)* |
| 3rd-party | Purchased/licensed enrichment data | Firmographic data, intent signals |

---

## Cross-Functional Consumers

| Team | How they use the martech stack | My role |
|------|-------------------------------|---------|
| Marketing | Campaign execution, segmentation, lifecycle journeys | Build tooling, train on self-service |
| Digital Growth | Paid acquisition, ROAS optimisation, lookalike audiences | Surface insights, translate goals → requirements |
| Sales | Lead enrichment, account signals from CRM | Ensure data flows to CRM correctly |
| Analytics / BI | Reporting on campaign and customer performance | Ensure clean, reliable event data |

---

## Compliance Requirements

- **GDPR** — applicable for EU users/merchants
- **CCPA** — applicable for California users/merchants
- Consent management, data deletion, and audit logging are all in scope for the CDP implementation

---

## Roadmap Themes

1. **CDP foundation** — unified profiles, event standardisation, lifecycle tagging
2. **Stack consolidation** — eliminate redundant tools, reduce cost/latency
3. **AI adoption** — generative content tools for marketing, predictive modelling for segmentation
4. **Self-service enablement** — empower marketing to build segments and journeys without engineering dependency
