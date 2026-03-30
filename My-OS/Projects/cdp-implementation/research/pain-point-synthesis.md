# Research Synthesis: CDP Discovery — Pain Points

**Author:** Richard Ng
**Date:** 2026-03-30
**Project:** CDP Implementation — Flight 1 Use Case Selection
**Method:** Stakeholder interviews + inferred signals
**N:** ~62% discovery complete (Rachel, Xinyi, Lina, Mardiana done; Eric, Raymondo, Patrick, Yuji TBD)

---

## Executive Summary

Kpay's martech infrastructure has no unified identity layer, no end-to-end attribution, and no self-serve segmentation across 4 markets (HK, SG, AU, JP). Discovery across ~62% of stakeholders identified 12 pain points in 5 categories — 4 Critical, 5 High, 3 Medium. The root blocker is identity: the absence of a unified merchant profile cascades into attribution failure, funnel blindness, and vendor complexity. SensorData schema debt is the only pain point actively compounding today. Compliance engagement hasn't started and structurally blocks Month 2 data model design. **Recommended flight 1 direction: unified merchant identity + SensorData schema remediation as prerequisites, then funnel visibility (MQL→SQL) as the value-proving use case.**

---

## Research Objectives

1. What are the biggest data and tooling pain points across the Digital Growth team?
2. Which pain points are blocking the most downstream work?
3. Which use case should CDP flight 1 solve — and what prerequisites are needed?

---

## Methodology

**Approach:** 1:1 stakeholder discovery interviews
**Participants:** Rachel (lifecycle), Xinyi (paid ads), Lina (website), Mardiana (content) — 4 of ~6.5 planned sessions complete
**Timeframe:** March 2026
**Limitations:** ~38% of discovery incomplete (compliance, data eng, CDP expert, JP market not yet covered). Inferred pain points (PP-007, PP-012) not yet directly validated. No system data verified — impact claims are stakeholder-reported.

---

## Key Findings

### Finding 1: Identity is the root blocker — fix it first or nothing else works

No unified merchant identity exists across touchpoints, markets, or systems. This directly blocks:
- Campaign attribution (PP-002) — can't connect ad spend to merchant quality
- Funnel visibility (PP-003) — MQL→SQL handoff breaks because no shared ID
- Vendor selection (PP-004) — B2B2C hierarchy is complex enough to disqualify many CDPs

**Evidence:**
- PP-001 confirmed across all 4 markets
- PP-004 confirmed: B2B2C identity (merchant + sub-merchant + end customer) is atypical for most CDP vendors
- PP-002 confirmed: no campaign-to-merchant-quality attribution exists

**Confidence:** High — confirmed by multiple participants, cross-cutting across all markets

---

### Finding 2: SensorData schema debt is the only problem that gets worse every day

SensorData was deployed without event schema governance or naming conventions. Unlike identity (blocked until CDP exists), schema debt is accumulating right now — every new event tracked without standards deepens the cleanup cost.

**Evidence:**
- PP-005 confirmed across all markets
- No event naming conventions, no schema documentation
- Remediation will be required before any CDP ingestion

**Confidence:** High — confirmed, not inferred

---

### Finding 3: Compliance is a silent blocker — if Eric/Raymondo sessions slip, Month 2 is at risk

Compliance engagement hasn't started. Data residency requirements across HK, SG, AU, JP (+ UK/Canada/EU for Ayden) are unknown. This blocks data model design, vendor shortlisting, and cross-market architecture.

**Evidence:**
- PP-010 confirmed: compliance team not yet engaged
- PP-011 suspected: multi-market residency requirements unverified
- Ayden expansion adds UK/Canada/EU jurisdictions not yet mapped

**Confidence:** Medium — confirmed that gap exists, but scope of compliance requirements unknown until interviews done

---

## Themes & Patterns

| Theme | Pain Points | Priority |
|-------|-------------|----------|
| Identity is the root blocker — cascades into 80% of use cases | PP-001, PP-002, PP-003, PP-004, PP-007 | P0 |
| Schema debt compounds daily without action | PP-005 | P0 |
| Compliance is the silent structural blocker | PP-010, PP-011 | P1 — urgent to engage |
| Governance has no single owner | PP-009, PP-012 | P1 — prerequisite to design |
| CRM fragmentation limits lifecycle + retention | PP-006, PP-008 | P1–P2 |

---

## Pain Point Register

| ID | Pain Point | Severity | Markets | AAARRR Stage | Confidence |
|----|-----------|----------|---------|--------------|------------|
| PP-001 | No unified merchant identity across touchpoints | Critical | All | Acquisition → Activation | Confirmed |
| PP-002 | No campaign-to-merchant-quality attribution | Critical | All | Acquisition | Confirmed |
| PP-003 | Funnel visibility dies at MQL→SQL handoff | Critical | HK primary | Acquisition → Activation | Confirmed |
| PP-004 | B2B2C identity hierarchy too complex for most CDPs | High | All | Cross-cutting | Confirmed |
| PP-005 | SensorData deployed without schema or naming conventions | Critical | All | Cross-cutting | Confirmed |
| PP-006 | CRM fragmented across markets | High | All | Acquisition → Revenue | Reported |
| PP-007 | No self-serve segmentation for marketing | High | All | Retention → Revenue | Inferred |
| PP-008 | Wati/WhatsApp signals unaccounted in martech stack | Medium | HK | Retention | Reported |
| PP-009 | Warehouse and CDP governance layers undefined | High | All | Cross-cutting | Confirmed |
| PP-010 | Compliance engagement hasn't started — blocks data model | High | All | Cross-cutting | Confirmed |
| PP-011 | Multi-market data residency requirements unknown | Medium | All + Ayden | Cross-cutting | Suspected |
| PP-012 | SSOT definition misaligned between engineering and growth | Medium | Cross-team | Cross-cutting | Suspected |

---

## Priority Matrix

| ID | Pain Point | Impact | Breadth | Urgency | Priority |
|----|-----------|--------|---------|---------|----------|
| PP-001 | No unified merchant identity | High | 4 markets | Blocking | P0 |
| PP-005 | SensorData schema debt | High | 4 markets | Compounding now | P0 |
| PP-002 | No campaign attribution | High | 4 markets + Ayden | Ayden Q3 deadline | P0 |
| PP-003 | MQL→SQL visibility gap | High | HK → expanding | Blocking | P0 |
| PP-010 | Compliance not engaged | High | 4 markets | Blocks Month 2 | P1 |
| PP-009 | Governance layers undefined | High | 4 markets | Blocks data model | P1 |
| PP-004 | B2B2C identity complexity | High | 4 markets | Blocks vendor eval | P1 |
| PP-006 | CRM fragmented | Medium | 4 markets | Ongoing | P1 |
| PP-007 | No self-serve segmentation | Medium | 4 markets | Month 3 target | P1 |
| PP-012 | SSOT misalignment | Medium | Cross-team | Pre-design | P2 |
| PP-011 | Data residency unknown | Medium | 4+ markets | Pre-vendor eval | P2 |
| PP-008 | Wati signals missing | Low | HK only | Low | P2 |

---

## Recommendations

### Immediate Actions

- [ ] **Start compliance engagement now** — book Eric and Raymondo before April; this is the critical path risk
- [ ] **Define SensorData schema standards** — assign owner, establish naming conventions, stop the bleeding
- [ ] **Validate PP-007 and PP-012** — these are inferred; confirm with Rachel (segmentation) and engineering (SSOT)
- [ ] **Use PP-004 as a vendor filter** — B2B2C identity complexity should be a hard requirement in vendor RFP

### Future Considerations

- Ayden GTM team discovery — UK/Canada/EU pain points not yet surfaced
- JieHuan session for data warehouse/attribution verification
- Establish data governance council (no single owner exists — PP-009, PP-012)

### What NOT to Do

- Don't shortlist flight 1 use case before compliance requirements are known — risks rework
- Don't build on SensorData as-is — schema remediation must happen before CDP ingestion
- Don't select a CDP vendor that can't handle B2B2C identity hierarchy (PP-004)

---

## CDP Use Case Implications

**Strongest candidate for flight 1:** MQL→SQL funnel visibility (PP-003)
- High urgency, confirmed across HK (primary market), clear business metric (activation rate)
- Prerequisites: unified identity (PP-001), SensorData cleanup (PP-005)
- Dependencies: compliance sign-off on data model (PP-010)

**Alternative candidate:** Paid ads audience segmentation (PP-002 + PP-007)
- Ayden Q3 deadline creates external forcing function
- Requires same identity foundation + CRM unification

**Prerequisites regardless of use case:**
1. SensorData schema remediation
2. Compliance engagement + data residency mapping
3. Vendor shortlist filtered against B2B2C identity requirement

---

## Open Questions

- What are the actual compliance requirements per market (Eric, Raymondo)?
- Who owns data engineering for CDP implementation?
- What is the SensorData event schema remediation timeline and owner?
- What does Ayden's Q3 attribution deadline actually require?
- Can any CDP vendor handle Kpay's B2B2C identity hierarchy out of the box?

---

## Known Gaps

- **~38% discovery incomplete:** Eric (compliance HK), Raymondo (SG/AU compliance), Patrick (CDP expert), Yuji (JP GM)
- **Unvalidated inferences:** PP-007 (segmentation gap), PP-012 (SSOT alignment)
- **No system data verified:** impact claims are stakeholder-reported, not cross-checked against actual data
- **Ayden-specific gaps:** UK/Canada/EU expansion pain points not yet surfaced

---

## Appendix

- Source: Pain point register pasted by Richard, March 30, 2026
- Related: `Knowledge/Reference/cdp.md`, `Projects/cdp-implementation/brief.md`
- Stakeholders covered: Rachel, Xinyi, Lina, Mardiana
- Stakeholders pending: Eric, Raymondo, Patrick, Yuji
