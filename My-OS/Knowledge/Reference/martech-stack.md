# Tech Stack — Audit & Reference

**Owner:** [Your Name]
**Last updated:** YYYY-MM-DD
**Status:** [Framework complete / In progress / TBD]
**Feeds into:** [Your main initiative, roadmap]

*Note: This is an example martech stack audit document. Adapt the category structure to your own tech stack.*

---

## How to Use This Document

This is the living reference for your marketing technology stack. It tracks:

1. **Tool Inventory** — every tool in use, by category, with key metadata
2. **Tool Scorecards** — per-tool deep dive on usage, data, integrations, and gaps
3. **Integration Map** — how data flows between tools today
4. **Scoring Summary** — prioritization: keep / expand / replace / sunset
5. **Gap Analysis** — missing capabilities vs. your team's goals
6. **Stakeholder Interview Questions** — role-specific questions for discovery sessions
7. **Audit Log** — who was spoken to and when

Update this file after each discovery session.

---

## 1. Tool Inventory

*Summary view — one row per tool. Expand in Section 2 for full detail.*

### Category Definitions

| Category | What It Covers |
| --- | --- |
| CDP | Customer data unification and activation |
| CRM | Customer relationship and account management |
| Email / Lifecycle | Email, push, in-app messaging and journey automation |
| Paid Ads — Search | SEM, Google Ads, Bing |
| Paid Ads — Social | Meta, TikTok, LinkedIn, programmatic |
| Web Analytics | Traffic, behavior, conversion tracking on website |
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
| L1 Data Sources | [Category] | [Tool] | ⬜ TBD | [Owner] | [Notes] |
| L1 Data Sources | [Category] | [Tool] | ⬜ TBD | [Owner] | [Notes] |
| L3 CDP Backbone | CDP | [Tool or None] | ⬜ TBD | [Owner] | [Notes] |
| L4A Warehouse | Data Warehouse | [Tool] | ⬜ TBD | [Owner] | [Notes] |
| L4B Activation | Lifecycle Messaging | [Tool] | ⬜ TBD | [Owner] | [Notes] |
| L5 Measurement | BI / Reporting | [Tool] | ⬜ TBD | [Owner] | [Notes] |
| L5 Measurement | Attribution | [Tool or TBD] | ⬜ TBD | [Owner] | [Notes] |

### Evaluating / Planned

| Tool | Category | Why Evaluating | Status | Decision Target |
| --- | --- | --- | --- | --- |
| [Tool] | [Category] | [Reason] | [Status] | [Date] |

---

## 2. Tool Scorecards

*One scorecard per tool. Copy the template block below for each tool discovered.*

### Scoring Rubric

Rate each tool on three dimensions (1–5 scale):

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| **Business Value** | Low impact on KPIs; unclear ROI | Moderate impact; some attribution to key metrics | Direct, measurable impact on key metrics |
| **Usage Depth** | Shelfware or minimal use | Moderate use; used regularly but not to full capability | Core tool; team depends on it daily |
| **Integration Readiness** | Isolated; no connections to other tools | Partially connected; some integrations but gaps exist | Well-connected; native integrations; clean data flows |

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
*1-2 sentences on what the tool does and why [Company] uses it.*

##### Use Cases
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

##### CDP / Data Platform Relevance
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

### Current State

```
[Tool A]
  --[data type]--> [Tool B]

[Tool B]
  --[data type]--> [Tool C]

[Attribution: Unknown] — document gaps here
```

### Target State (Post-[Main Initiative])

```
[Data Source 1] --[data]--> [CDP / Central Platform]
[Data Source 2] --[data]--> [CDP / Central Platform]

[CDP] --unified segments--> [Activation Tool 1]
[CDP] --audience lists--> [Activation Tool 2]
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

*Missing capabilities vs. your team's goals.*

### Gap Analysis Fields

For each gap: capability missing → business impact → current workaround → initiative dependency → launch blocker → resolution path.

### Gaps Identified

| Gap | Business Impact | Current Workaround | Initiative Dependency | Launch Blocker | Resolution Path |
| --- | --- | --- | --- | --- | --- |
| [Gap 1] | [Impact] | [Workaround] | [Yes/No] | [Yes/Partial/No] | [How to resolve] |
| *[Discover more in stakeholder interviews]* |  |  |  |  |  |

---

## 6. Stakeholder Interview Questions

*Role-specific questions for discovery sessions. Use alongside `Templates/interview-notes.md`.*

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

### [Role 1 — e.g. Lifecycle Marketing]

**Goal:** [What you want to learn from this person]

1. [Question 1]
2. [Question 2]
3. [Question 3]

---

### [Role 2 — e.g. Paid Ads]

**Goal:** [What you want to learn from this person]

1. [Question 1]
2. [Question 2]
3. [Question 3]

---

### [Role 3 — e.g. Website / Analytics]

**Goal:** [What you want to learn from this person]

1. [Question 1]
2. [Question 2]
3. [Question 3]

---

## 7. Audit Log

*Track who you've spoken to, what was covered, and where the notes live.*

| Date | Stakeholder | Topics Covered | Notes Location | Follow-Up |
| --- | --- | --- | --- | --- |
| — | [Name] | — | — | Scheduled? |
| — | [Name] | — | — | Scheduled? |
| — | [Name] | — | — | — |

---

## 8. Roadmap Snapshot

### Phase 1 — Foundation (Now → [Target Date])

- Complete stack audit (this document)
- [Key initiative milestone 1]
- [Key initiative milestone 2]

### Phase 2 — Activation ([Date range])

- [What you're building in this phase]
- [Key milestone]

### Phase 3 — Optimization ([Date range])

- [What you're optimizing for]
- [Key milestone]

---

## 9. Open Questions

| Question | Priority | Status | Answer |
| --- | --- | --- | --- |
| [Question 1] | P0 | Open | |
| [Question 2] | P0 | Open | |
| [Question 3] | P1 | Open | |

---

## Links

- [[Knowledge/Reference/cdp]] — CDP initiative reference and vendor landscape
- [[Knowledge/Reference/your-company]] — Company context
- [[GOALS.md]] — 30-60-90 day objectives
- [[Projects/[your-main-project]/brief.md]] — Project anchor doc
- [[Templates/interview-notes.md]] — Template for discovery sessions
