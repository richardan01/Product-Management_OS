# Martech Stack — Audit & Reference

**Owner:** Richard Ng
**Last updated:** 2026-03-27
**Status:** Framework complete — tool mapping in progress (some layers TBD)
**Feeds into:** CDP vendor selection, Martech Roadmap v1.0

---

## How to Use This Document

This is the living reference for Kpay's marketing technology stack. It tracks:

1. **Tool Inventory** — every tool in use, by category, with key metadata
2. **Tool Scorecards** — per-tool deep dive on usage, data, integrations, and gaps
3. **Integration Map** — how data flows between tools today
4. **Scoring Summary** — prioritization of tools: keep / expand / replace / sunset
5. **Gap Analysis** — missing capabilities vs. Kpay Digital Growth goals
6. **Stakeholder Interview Questions** — role-specific questions for discovery sessions
7. **Audit Log** — who was spoken to and when

Update this file after each discovery session. Goal: complete picture by Day 30 (April 2026).

---

## 1. Tool Inventory

*Summary view — one row per tool. Expand in Section 2 for full detail.*

### Category Definitions

| Category | What It Covers |
| --- | --- |
| CDP | Customer data unification and activation |
| CRM | Merchant relationship and account management |
| Email / Lifecycle | Email, push, in-app messaging and journey automation |
| Paid Ads — Search | SEM, Google Ads, Bing |
| Paid Ads — Social | Meta, TikTok, LinkedIn, programmatic |
| Web Analytics | Traffic, behavior, conversion tracking on Kpay website |
| Tag Management | Script/pixel deployment and management |
| CMS | Website content management |
| SEO / Content | Keyword research, content performance, on-page SEO |
| Attribution | Cross-channel attribution and marketing mix modeling |
| Data Warehouse | Centralized data storage and querying |
| Creative / Media | Ad creative production, image/video editing, AI creative tools |
| Collaboration | Internal tools used for marketing workflows |

### Current Stack Summary

Legend: ✅ Confirmed active · 🟡 Partial / in progress · ⬜ TBD / not yet mapped

| Layer | Category | Tool | Status | Primary Owner | Notes |
| --- | --- | --- | --- | --- | --- |
| L1 Data Sources | Web | GA4 / GTM | ✅ Active | Lina | Marketing site, lead forms, DMO entry |
| L1 Data Sources | Product Analytics | SensorData | 🟡 Live since Jan | — | In-app behavioral events; full funnel dashboard submitted to JieHuan/BI |
| L1 Data Sources | POS / Transactions | KPay system → DB | ✅ Active | Engineering | Terminal transaction events; GPV scoring source |
| L1 Data Sources | Marketing Automation | HubSpot | ✅ Active | — | Email, form submits, nurture; marketing engagement layer |
| L1 Data Sources | CRM | KPay built-in CRM | ✅ Active (HK only) | — | Merchant records, BD activity, SQL status |
| L1 Data Sources | Ad Platforms | Meta / Google / LinkedIn | ⬜ TBD | Xinyi | Vendor eval pending; connectors needed |
| L1 Data Sources | DocuSign | DocuSign | ⬜ TBD | — | DMO document submission events; identity gap |
| L1 Data Sources | Offline / CS Referrals | — | ⬜ TBD | — | CS-sourced leads; Friends of KPay referral (SG) |
| L3 CDP Backbone | CDP | None | Planned | Richard | Vendor TBD; evaluation in progress |
| L4A Warehouse | Data Warehouse | AWS Redshift | ✅ Active | Data team | Central store; existing ETL from KPay DBs |
| L4A Warehouse | ETL Pipeline | Existing ETL | ✅ Active | Engineering | KPay DBs → Redshift batch ingestion |
| L4A Warehouse | Enrichment Models | TBD | ⬜ TBD | — | GPV scoring, LTV, churn propensity; ML tooling needed |
| L4A Warehouse | Reverse ETL | TBD | ⬜ TBD | — | Push scores from Redshift → CDP + activation tools |
| L4B Activation | Lifecycle Messaging | TBD | ⬜ TBD | Rachel | Candidates: Braze, Customer.io, HubSpot MH, Iterable |
| L4B Activation | Paid Media | Ad platform connectors | ⬜ TBD | Xinyi | CDP segment sync to Meta, Google, LinkedIn |
| L4B Activation | In-App Personalization | SensorData (planned) | 🟡 Planned | — | Triggered in-app messages by lifecycle stage |
| L4B Activation | WhatsApp / Conversational | — | 🟡 Pilot (HK) | — | CS chatbot pilot |
| L5 Measurement | BI / Reporting | Tableau | ✅ Active | — | Dashboards from Redshift; future CDP views + ChatBI |
| L5 Measurement | BI / Reporting | ChatBI | 🟡 Early dev | — | Conversational BI layer in development |
| L5 Measurement | Web Analytics | GA4 | ✅ Active | Lina | Traffic, DMO attribution, form conversions |
| L5 Measurement | Product Analytics | SensorData | 🟡 Live since Jan | — | In-app funnel, feature adoption, session depth |
| L5 Measurement | Attribution | TBD | ⬜ TBD | — | Multi-touch model needed; currently broken at MQL→BD handoff |
| L5 Measurement | Experimentation | TBD | ⬜ TBD | — | A/B testing; SensorData paid module or standalone |
| CDP | None | Planned | Richard | — | Flight 1 target: June 2026 |

### Evaluating / Planned

| Tool | Category | Why Evaluating | Status | Decision Target |
| --- | --- | --- | --- | --- |
| CDP vendor (TBD) | CDP | Unify customer data, enable activation | Evaluation in progress | April 2026 |
| Lifecycle messaging tool | Activation | Email/push/SMS for onboarding + retention journeys | Candidates: Braze, Customer.io, HubSpot MH, Iterable | TBD |
| Reverse ETL tool | Data Warehouse | Push enrichment scores from Redshift → CDP + activation | TBD | TBD |
| Attribution tool | Measurement | Multi-touch model; MQL→SQL→merchant funnel visibility | TBD | TBD |
| Experimentation tool | Measurement | A/B testing for messaging + onboarding flows | SensorData paid module or standalone | TBD |
| Ad platform connectors | Activation | CDP segment sync to Meta / Google / LinkedIn | TBD | TBD |
| Video / image editing + AI creative tools | Creative / Media | Evaluate options for content and ads creative production | Research phase | TBD |

---

## 2. Tool Scorecards

*One scorecard per tool. Copy the template block below for each tool discovered.*

### Scoring Rubric

Rate each tool on three dimensions (1–5 scale):

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| **Business Value** | Low impact on KPIs; unclear ROI | Moderate impact; some attribution to key metrics | Direct, measurable impact on ROAS, retention, activation, or CAC |
| **Usage Depth** | Shelfware or minimal use; only 1 person touches it | Moderate use; used regularly but not to full capability | Core tool; team depends on it daily; used to near-full capability |
| **Integration Readiness** | Isolated; no connections to other tools; manual exports only | Partially connected; some integrations but gaps exist | Well-connected; native integrations with key tools; clean data flows |

**Composite Score:** Sum of three dimensions (max 15).
- **12–15:** Invest / Expand
- **8–11:** Maintain / Optimize
- **5–7:** Review / Consolidate
- **3–4:** Sunset / Replace

---

### TEMPLATE — Tool Scorecard

*Copy this block for each tool discovered:*

```
#### [Tool Name] — [Category]

**Status:** Active / Shelfware / Evaluating / Sunset
**Primary Owner:** [Name]
**Secondary Users:** [Names]
**Contract:** [Vendor | Renewal date | Approx. cost]
**Procurement contact:** [Name / how to access contract]

##### What It Does
*1-2 sentences on what the tool does and why Kpay uses it.*

##### Use Cases at Kpay
- [Use case 1]
- [Use case 2]

##### Data Inputs
*What data flows INTO this tool?*
- [Source → data type]

##### Data Outputs
*What data or signals come OUT of this tool?*
- [Output → destination]

##### Current Integrations
| Connected To | Direction | Method | Notes |
|-------------|-----------|--------|-------|
| [Tool] | In / Out / Both | Native / Webhook / Manual | |

##### Known Gaps
- [Gap 1: what's missing or broken]

##### CDP Relevance
- Data this tool should SEND to CDP:
- Data this tool should RECEIVE from CDP:
- Integration complexity: Low / Medium / High

##### Scores
| Dimension | Score (1–5) | Notes |
|-----------|------------|-------|
| Business Value | | |
| Usage Depth | | |
| Integration Readiness | | |
| **Composite** | **/15** | |

##### Recommendation
Keep / Expand / Optimize / Review / Sunset

##### Open Questions
- [ ]
```

---

### Completed Scorecards

*Add scorecards here as discovery sessions complete.*

*(None completed yet — audit in progress)*

---

## 3. Integration Map

*How data flows between tools today. Text-based notation — no tooling dependency.*

### Notation

```
[Source] --[data type]--> [Destination]
[Source] <--[data type]--> [Destination]   (bidirectional)
[Source] --[data type]--> ?                (unknown destination)
? --[data type]--> [Destination]           (unknown source)
```

### Current State (as of March 2026)

```
[KPay POS / Hive / Transaction DBs]
  --batch transaction events--> [AWS Redshift] (via existing ETL pipeline)

[KPay built-in CRM (HK only)]
  --merchant records, BD activity, SQL status--> [AWS Redshift?] (confirm)

[Website / Marketing Site]
  --pageview, form fill, DMO entry, conversions--> [GA4] (via GTM)

[GTM]
  --pixels, tracking scripts--> [Ad Platforms: Meta / Google / LinkedIn]
  --events--> [GA4]

[HubSpot]
  --email opens, form submits, nurture activity--> [HubSpot internal]
  <--merchant list--> ? (source TBD)

[SensorData]
  --in-app behavioral events, feature adoption, session data--> [SensorData]
  --full funnel dashboard--> [JieHuan/BI] (submitted Jan 2026)

[AWS Redshift]
  --BI queries--> [Tableau]
  --enrichment scores (future)--> [Reverse ETL: TBD] --> [CDP: TBD]

[Lark Webhooks]
  --lead form submissions--> [Collection layer] (real-time trigger)

[CDP: None yet]
[Attribution: Broken] — MQL→BD handoff gap; 1+ month lag to conversion data
```

### Target State (Post-CDP, Flight 1)

```
[Transaction System] --merchant events--> [CDP]
[CRM] --merchant profile--> [CDP]
[Web Analytics] --behavioral events--> [CDP]

[CDP] --unified segments--> [Email / Lifecycle]
[CDP] --audience lists--> [Paid Ads — Social]
[CDP] --audience lists--> [Paid Ads — Search]
```

---

## 4. Scoring Summary & Prioritization

*Populate after all scorecards are complete.*

| Tool | Category | Business Value | Usage Depth | Integration Readiness | Composite | Recommendation |
| --- | --- | --- | --- | --- | --- | --- |
| TBD |  |  |  |  |  |  |

### Decision Framework

|  | High Business Value | Low Business Value |
| --- | --- | --- |
| **High Usage** | **EXPAND** — double down, integrate deeply | **REVIEW** — high dependency but poor ROI; candidate for replacement |
| **Low Usage** | **ACTIVATE** — unlock value that exists but isn't captured | **SUNSET** — shelfware; cut or consolidate |

---

## 5. Gap Analysis

*Missing capabilities vs. Kpay Digital Growth goals. Anchored to CDP flight 1 impact.*

### Gap Analysis Fields

For each gap: capability missing → business impact → current workaround → CDP dependency → flight 1 blocker → resolution path.

### Gaps Identified

| Gap | Business Impact | Current Workaround | CDP Dependency | Flight 1 Blocker | Resolution Path |
| --- | --- | --- | --- | --- | --- |
| No unified customer identity (web + transaction + email) | ROAS, retention, activation all suffer | Manual list exports; siloed reporting | Yes — core CDP function | Yes | CDP implementation |
| No first-party audience segments for paid ads | CAC higher than necessary; no suppression | TBD | Yes | Partial | CDP → ad platform integration |
| No behavioral triggers for lifecycle campaigns | Reactive rather than proactive retention | TBD | Yes | Partial | CDP → lifecycle tool integration |
| *[Discover more in stakeholder interviews]* |  |  |  |  |  |

### Gaps to Validate in Discovery Sessions

- Is there a current attribution model? Is it accurate?
- Is there any identity stitching between web visitors and known merchants today?
- What data is the email/lifecycle tool missing to build proper journeys?
- Is there a data warehouse? If so, what data is in it and who can query it?
- Are there any tools the team has access to but isn't using (shelfware)?
- What compliance / data privacy constraints exist on customer data?

---

## 6. Stakeholder Interview Questions

*Role-specific questions for discovery sessions. Use alongside **`Templates/interview-notes.md`**.*

---

### Universal Questions (ask everyone)

**Tool inventory:**
1. What tools do you use day-to-day? (Get full list including tools not on my radar.)
2. Which tools do you pay for but barely use?
3. What was the last thing you couldn't do because you didn't have the right data or tool?

**Data:**
4. What data do you wish you had but don't?
5. How do you currently get data you need — self-serve or request from someone?
6. Where does your tool's data live after you're done with it? Does it go anywhere else?

**Integrations:**
7. Which of your tools talk to each other? Which ones don't but should?
8. Are there any manual exports or copy-paste workflows you do regularly?

**Contracts:**
9. Do you know when your tool contracts renew? Are there any you'd drop if you could?

---

### Rachel — Lifecycle Marketing

**Goal:** Understand her lifecycle tool, what data it has, what triggers she can/can't build, and what CDP unlocks for her.

1. Walk me through how a typical lifecycle campaign gets built end to end — from idea to launched.
2. What data does your email/messaging tool have today about each merchant? (Behavioral? Transactional? Just email engagement?)
3. What triggers can you set today — time-based, event-based, or manual?
4. What's the campaign you most wish you could run but can't because of data or tooling limitations?
5. When a merchant goes quiet, how do you know? How quickly?
6. How do you currently segment merchants — rule-based, manual, or something else?
7. If you had a unified merchant profile with transaction data, web behavior, and email engagement — what would you build first?
8. What's your biggest retention challenge — identifying at-risk merchants, deciding what to send, or measuring what's working?

---

### Xinyi — Paid Ads

**Goal:** Understand her current audience building process, how she suppresses existing customers, and where she loses efficiency.

1. Walk me through how you build an audience for a new campaign today.
2. How do you suppress existing Kpay customers from acquisition campaigns? Automated or manual?
3. What first-party data do you currently use for audience targeting?
4. Which platforms are you running on, and which are delivering the best ROAS?
5. How are conversion events currently passed to Google / Meta / TikTok — pixel, server-side, or both?
6. What's the freshness of your audience lists — how often are they updated?
7. If you could push a real-time high-LTV segment to your ad platforms, what would you do with it?
8. Where do you think you're losing the most efficiency — audience quality, bid strategy, creative, or landing page?
9. Is there an attribution model in place? Do you trust it?

---

### Lina — Website / CMS

**Goal:** Understand tracking setup, tag management, analytics, and whether any identity resolution is happening today.

1. What analytics tool are you using? What can you see in it today?
2. Do you have a tag manager set up? What pixels and scripts are currently firing?
3. How is web behavior currently linked to known merchants — any identity stitching happening?
4. When a merchant visits the website after signing up, can you tell who they are? How?
5. What events are you currently tracking on the site?
6. Is there a personalization layer on the site today?
7. What's on your web roadmap for the next quarter — any changes that would affect tracking?
8. What data from the website do you wish you could share with Rachel or Xinyi but currently can't?
9. What are the biggest tracking gaps — things happening on the site you're not capturing?

---

### Mardiana — Content

**Goal:** Understand content production workflow, visibility into content performance, and what segment-level insights would change how she works.

1. How do you currently decide what content to produce — data, intuition, requests, or a mix?
2. What tools do you use for SEO research and content performance tracking?
3. Can you currently see how content performance connects to business outcomes — signups, activations, retention?
4. Do you ever tailor content for different merchant types or segments? How do you do that today?
5. What's the biggest content question you can't answer right now because of data gaps?
6. If you knew exactly which merchant segments were reading which content — and what happened after — what would you do differently?
7. What are your current creative production tools — for images, video, social assets? Any AI tools in use?
8. Are there any content workflows that feel unnecessarily manual or slow?

---

## 7. Audit Log

*Track who you've spoken to, what was covered, and where the notes live.*

| Date | Stakeholder | Topics Covered | Notes Location | Follow-Up |
| --- | --- | --- | --- | --- |
| — | Rachel | — | — | Scheduled? |
| — | Xinyi | — | — | Scheduled? |
| — | Lina | — | — | Scheduled? |
| — | Mardiana | — | — | Scheduled? |
| — | Jervis | — | — | — |
| — | Data/Eng team (TBD) | Data warehouse, event tracking | — | Identify contact first |

---

## 8. Martech Roadmap Snapshot

### Phase 1 — Foundation (Now → Day 90 / June 2026)

- Complete martech audit (this document)
- Select CDP vendor
- Implement CDP flight 1 use case
- Unify 3+ core data sources into CDP
- Onboard Rachel + 1 other team member on CDP

### Phase 2 — Activation (Q3 2026)

- Expand CDP to all primary use cases (lifecycle, paid audiences, web behavior)
- Enable self-serve segmentation for Digital Growth team
- Establish attribution model

### Phase 3 — Optimization (Q4 2026+)

- AI-driven segmentation
- Web personalization at scale
- Marketing mix modeling
- Evaluate: tools to consolidate or replace now that CDP is the data hub

---

## 9. Open Questions

| Question | Priority | Status | Answer |
| --- | --- | --- | --- |
| Is there a data warehouse at Kpay? If so, what's in it and who owns it? | P0 | **Answered** | AWS Redshift — existing ETL pipeline from KPay DBs; owns enrichment and BI layer |
| Who is the engineering / data partner for CDP implementation? | P0 | Open | |
| What is the budget range for CDP tooling? | P0 | Open | |
| Is there any existing identity resolution (web visitor → known merchant)? | P0 | Open | No CDP yet; no stitching confirmed — gap to close |
| What compliance / data privacy constraints exist? | P0 | **Partial** | PDPO (HK) / PDPA (SG/TH) / Privacy Act (AU) / APPI (JP) — consent + suppression required at profile level |
| Does CRM extend beyond HK? | P0 | **Partial** | KPay built-in CRM is HK only — other markets TBD |
| What tools are currently paid for but barely used (shelfware candidates)? | P1 | Open | |
| Is there an existing attribution model? Is it trusted? | P1 | **Partial** | Currently broken — MQL→BD handoff gap; 1+ month lag to conversion data |
| What is the renewal date and cost of the email/lifecycle tool? | P1 | Open | Lifecycle tool not yet selected |
| What video/image editing and AI creative tools are in use or being considered? | P2 | Open | |
| What is the current CMS and how does it integrate with analytics? | P1 | Open | |
| Who owns / built the Merchant Identity Model (B2B2C hierarchy)? | P1 | Open | Design required — not yet modelled |
| What is the SensorData contract scope — which paid modules are active? | P1 | Open | In-app behavioral live; paid modules (experimentation) not confirmed |

---

## Links

- [[Knowledge/Reference/cdp]] — CDP initiative reference and vendor landscape
- [[Knowledge/Reference/kpay]] — Company context
- [[GOALS.md]] — 30-60-90 day objectives
- [[Projects/cdp-implementation/brief.md]] — CDP project anchor doc
- [[Templates/interview-notes.md]] — Template for discovery sessions
