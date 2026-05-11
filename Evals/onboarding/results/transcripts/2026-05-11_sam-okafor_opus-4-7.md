# Onboarding transcript — Sam Okafor

- **Fixture:** `Evals/onboarding/inputs/sam-okafor-batman-variant.md`
- **Persona under test:** Batman strategic operator
- **Model:** claude-opus-4-7
- **Date:** 2026-05-11
- **Runner:** runner-subagent-A
- **Workflow commit SHA:** 536e4ae35497b45b8b2211d1b291b8024b822532
- **Workflow file:** `Workflows/interactive-onboarding.md`

---

## Phase 0 — Confirm first-run context

> **User:** Computer, onboard me into this OS.

> **Assistant:** Standing up the OS. Small batches; no files written until you approve the full plan. First batch:
>
> 1. Is this OS for your day job, career work, a side project, learning, or a mix?
> 2. What name, role, company / organization, and team should the OS use?
> 3. Any placeholders you want to preserve for now?

> **User:** Day job plus career transition to a frontier lab. Name: Sam Okafor. Role: Senior Product Manager. Company: Acme AI. Team: Growth Platform. Manager: Priya Shah. No placeholders.

> **Assistant:** Captured:
>
> - **Name:** Sam Okafor
> - **Role:** Senior Product Manager
> - **Company:** Acme AI
> - **Team:** Growth Platform
> - **Manager:** Priya Shah
> - **Setup purpose:** Day-job execution + career transition (frontier lab)
>
> Moving to purpose.

## Phase 1 — Choose purpose

> **Assistant:** Three:
>
> 1. Primary purpose — day-job, career, founder, research, learning, mixed, or custom?
> 2. What should this OS help you do every week?
> 3. What would make it useful within 7 days?

> **User:** Mixed: day-job execution plus career transition to a frontier lab. Weekly: keep activation funnel work tight; build the frontier-lab thesis; prep for any external recon conversations. 7-day usefulness: discovery readout draft on day-job side; a coherent "Why frontier labs" narrative draft on career side.

> **Assistant:** Captured. Purpose recorded as **day-job execution + career transition**. Two parallel anchors for the first 7 days: discovery readout draft and "Why frontier labs" narrative draft.

## Phase 2 — Choose persona and voice

> **Assistant:** Persona options:
>
> - **Batman strategic operator** — direct, contingency-first; routes all 12 Batman agents; `/riddler` + `/vale` mandatory pre-publish.
> - **Executive operator** — concise, outcome-driven; skills + workflows only; `/peer-review` default.
> - **Research partner** — evidence-first.
> - **Product coach** — reflective.
> - **Builder / AI PM** — eval-first.
> - **Minimalist** — terse, checklist-only.
> - **Custom**.
>
> 1. Which persona?
> 2. When should I push back?
> 3. Tone to avoid?

> **User:** Batman strategic operator. Push back high — contingency-first; name failure modes before solutions. Tone: direct, terse, imperative. Batman idiom acceptable. Avoid: hedging, "maybe", soft framing, "I think".

> **Assistant:** Confirmed:
>
> - **Persona:** Batman strategic operator
> - **Tone:** direct, terse, imperative — Batman idiom acceptable
> - **Pushback:** high — contingency-first, failure modes named before solutions
> - **Avoid:** hedging, "maybe", soft framing, "I think"
>
> Effects (matrix row, locked in unless you change it):
>
> - Strategic layer: `Agents/Gotham/Computer/` — all 12 routed (Bruce Wayne, Alfred, Lucius Fox, Oracle, Batman, Robin, Nightwing, Riddler, Gordon, Selina Kyle, Henri Ducard, Vicki Vale)
> - Quality gates: `/riddler` + `/vale` mandatory pre-publish on every public artifact
> - Surfaced first: `/today`, `/cowl-up`, `/riddler`, `/vale`
> - No agents pruned
>
> Lock it in?

> **User:** Yes. Lock it in.

## Phase 3 — Define operating cadence

> **Assistant:** Cadence options — pick:
>
> - Daily `/today`
> - Weekly `/weekly-update`
> - Sprint planning + retro
> - Monthly strategy
> - Quarterly planning
> - Ad hoc only
>
> Plus:
>
> 1. What day does the week start?
> 2. Planning rhythm?
> 3. Meetings / reviews to prep for?

> **User:** Daily `/today`, Friday `/weekly-update`, weekly planning Monday. Manual `/cowl-up` only on high-stakes weeks — never auto. Week starts Monday. Meetings to prep: Priya 1:1 weekly, Marco eng review biweekly, Elena design sync weekly. Plus interview-loop prep when one is scheduled.

> **Assistant:** Captured. Weekly planning Monday, daily `/today`, Friday `/weekly-update`. `/cowl-up` reserved for manual invocation only. Prep targets: Priya weekly, Marco biweekly, Elena weekly, plus interview-loop activation as needed.

## Phase 4 — Capture current tasks

> **Assistant:** Tasks. I'll read each priority back individually before writing.
>
> 1. P0 this week (1–3)?
> 2. P1 soon (3–5)?
> 3. P2 / backlog?
> 4. Blockers + owners?
> 5. Follow-ups promised?

> **User:** P0: finish discovery readout draft; book Priya 1:1 for readout review. P1: stand up baseline metrics dashboard with Sam Rivera; align Marco on instrumentation gaps. P2: nothing yet on the day-job side; on career side, draft a frontier-lab target list — but that's not urgent this week. Blockers: no baseline dashboard; activation event definition disputed across eng/data. Follow-ups: send Elena a copy of the readout draft.

> **Assistant:** P0:
>
> - Finish discovery readout draft
> - Book Priya 1:1 for readout review
>
> Match? Anything missing?

> **User:** Match. Nothing missing.

> **Assistant:** P1:
>
> - Stand up baseline metrics dashboard with Sam Rivera
> - Align Marco on instrumentation gaps
>
> Correct?

> **User:** Correct.

> **Assistant:** P2:
>
> - Draft frontier-lab target list (career track, not urgent)
>
> Right?

> **User:** Right.

> **Assistant:** Blockers:
>
> - No baseline dashboard — owner: Sam Rivera
> - Activation event definition disputed — owners: Marco + Sam jointly
>
> Failure modes worth naming: if the event definition slips past week 2, the 60-day A/B test slips with it. Want that risk recorded?

> **User:** Yes — record it.

> **Assistant:** Logged. Follow-ups:
>
> - Send Elena the readout draft once ready
>
> Anything else?

> **User:** That's all.

> **Assistant:** All five categories confirmed individually. Tasks/active, Tasks/backlog, Tasks/follow-ups will be proposed at the Phase 8 summary.

## Phase 5 — Capture goals and metrics

> **Assistant:** Goals:
>
> 1. 30-day outcomes?
> 2. 60-day?
> 3. 90-day?
> 4. Metrics / evidence?
> 5. Personal development goals?

> **User:** 30-day: ship activation funnel discovery readout; align Priya on top 3 hypotheses. 60-day: A/B test running on top hypothesis; baseline metrics dashboard live. 90-day: first measurable activation lift shipped; v1 roadmap shared with skip. Metrics: activation rate, A/B power and lift, # stakeholders aligned per gate. Dev goal: build interview-ready PD-TOL inventory across 3–4 past launches; sharpen contingency thinking under high stakes.

> **Assistant:** Recommendation, since persona is Batman and pushback is high: separate **career-track goals** from **day-job goals** in `GOALS.md` so the frontier-lab thesis isn't buried under activation work. Two sections, same 30/60/90 cadence. Yes?

> **User:** Yes — split them.

> **Assistant:** Captured. `GOALS.md` will have a Day-job section and a Career-transition section.

## Phase 6 — Capture stakeholders and projects

> **Assistant:** Stakeholders + projects:
>
> 1. 4–6 people the OS should understand first?
> 2. Who approves, blocks, advises, uses?
> 3. Anchor project / workstream?
> 4. Open decisions?
> 5. Visible risks?

> **User:** People: Priya Shah, Marco Chen, Elena Torres, Sam Rivera. Priya approves direction. Marco can block on eng capacity. Elena partners on design. Sam Rivera owns data. Anchor project: Activation funnel redesign. Open decisions: activation event definition; top-3 hypotheses for A/B. Risks: data quality on existing events; Marco's team stretched.

> **Assistant:** I'll walk through each person one at a time before drafting any profile.
>
> Priya Shah — role and seniority?

> **User:** Director of Growth, two levels above me. My direct manager.

> **Assistant:** Why does she matter — approver, blocker, advisor, user, partner?

> **User:** Approver for direction and headcount. Translator upward to skip-level.

> **Assistant:** Working style?

> **User:** Wants written readouts with a clear recommendation and 2-3 alternatives. Weekly 1:1 Monday. Hates ambiguity.

> **Assistant:** Drafting `Knowledge/People/priya-shah.md`: Director of Growth, manager, approver + translator-up, weekly 1:1 Monday, written readouts with rec + alternatives. OK?

> **User:** Yes.

> **Assistant:** Marco Chen — role and seniority?

> **User:** Engineering lead, Growth Platform. Senior staff.

> **Assistant:** Approver, blocker, advisor, user, partner?

> **User:** Capacity blocker. Scoping partner.

> **Assistant:** Working style?

> **User:** Pragmatic. Distrusts vague PM asks. Wants written scope before he commits.

> **Assistant:** Drafting `Knowledge/People/marco-chen.md`: Eng lead Growth Platform, capacity blocker + scoping partner, written scope required. OK?

> **User:** Yes.

> **Assistant:** Elena Torres — role and seniority?

> **User:** Staff product designer on Growth.

> **Assistant:** Approver, blocker, advisor, user, partner?

> **User:** Partner on design; advisor on UX research.

> **Assistant:** Working style?

> **User:** Collaborative; wants early involvement before mocks. Strong opinion on user-research rigor.

> **Assistant:** Drafting `Knowledge/People/elena-torres.md`: Staff designer, partner + UX-research advisor, early involvement. OK?

> **User:** Yes.

> **Assistant:** Sam Rivera — role and seniority?

> **User:** Senior data scientist supporting Growth.

> **Assistant:** Approver, blocker, advisor, user, partner?

> **User:** Owns activation metrics + dashboard. Blocker if instrumentation gaps stay unresolved.

> **Assistant:** Working style?

> **User:** Detailed. Slow to commit but reliable. Async-first.

> **Assistant:** Drafting `Knowledge/People/sam-rivera.md`: Senior DS, metrics owner + instrumentation blocker, async-first. OK?

> **User:** Yes.

> **Assistant:** Anchor project — Activation funnel redesign. Open decisions: event definition, top-3 hypotheses. Risks: data quality, eng capacity. Pre-mortem failure mode (Batman default): if event definition slips past week 2, 60-day A/B slips with it. I'll propose `Projects/activation-funnel-redesign/brief.md` covering context, decisions, risks, pre-mortem. OK?

> **User:** Yes.

## Phase 7 — Privacy and editing boundaries

> **Assistant:** Privacy:
>
> 1. Never write?
> 2. May edit without asking?
> 3. Requires confirmation?
> 4. Repo visibility?

> **User:** Never: compensation, health, private HR feedback, sensitive customer data. Plus on the career side — do not store recruiter names, offer details, or interview-loop debriefs in this repo. Those live elsewhere. Free to edit: `Tasks/active.md`, `Tasks/follow-ups.md`, daily notes. Ask first: `CLAUDE.md`, `GOALS.md`, `Knowledge/People/*`, `Projects/*/brief.md`. Repo: private.

## Phase 8 — Confirmation summary

> **Assistant:**
>
> ## Proposed setup
>
> ### Purpose
> - Day-job execution + career transition to a frontier lab
> - 7-day usefulness anchors: discovery readout draft (day-job); "Why frontier labs" narrative draft (career)
>
> ### Persona
> - Batman strategic operator
> - Tone: direct, terse, imperative — Batman idiom acceptable
> - Pushback: high — contingency-first, failure modes named before solutions
> - Quality gates: `/riddler` + `/vale` mandatory pre-publish on any public artifact
> - Strategic layer: `Agents/Gotham/Computer/` — all 12 agents routed
> - `/cowl-up` available manually only; never auto
>
> ### Cadence
> - Weekly planning Monday
> - Daily `/today`
> - Friday `/weekly-update`
> - Prep targets: Priya 1:1 (weekly), Marco review (biweekly), Elena sync (weekly), interview-loop activation on demand
>
> ### Initial tasks
> - P0: finish discovery readout draft; book Priya 1:1 for readout review
> - P1: stand up baseline metrics dashboard with Sam; align Marco on instrumentation gaps
> - P2: draft frontier-lab target list
> - Blockers: no baseline dashboard (Sam); activation event definition disputed (Marco + Sam)
> - Pre-mortem: event-definition slip past wk 2 → 60-day A/B slips
> - Follow-ups: send Elena the readout draft
>
> ### Goals
> - Day-job 30 days: ship discovery readout; align Priya on top 3 hypotheses
> - Day-job 60 days: A/B test running on top hypothesis; baseline metrics dashboard live
> - Day-job 90 days: first measurable activation lift shipped; v1 roadmap shared with skip
> - Career 30 days: complete PD-TOL inventory across 3–4 past launches; draft frontier-lab thesis v0
> - Career 60 days: warm intros initiated with 2–3 lab insiders; thesis v1
> - Career 90 days: interview-ready PD-TOL set; thesis v2; first screen scheduled
>
> ### Stakeholders
> - Priya Shah (Director of Growth, manager, approver)
> - Marco Chen (eng lead, capacity blocker + scoping partner)
> - Elena Torres (staff designer, partner + UX-research advisor)
> - Sam Rivera (senior DS, metrics owner + instrumentation blocker)
>
> ### Files I propose to update
> - `CLAUDE.md`
> - `GOALS.md`
> - `Tasks/active.md`
> - `Tasks/backlog.md`
> - `Tasks/follow-ups.md`
> - `Knowledge/People/priya-shah.md`
> - `Knowledge/People/marco-chen.md`
> - `Knowledge/People/elena-torres.md`
> - `Knowledge/People/sam-rivera.md`
> - `Projects/activation-funnel-redesign/brief.md`
>
> ### Boundaries
> - Never write: compensation, health, private HR feedback, sensitive customer data, recruiter names, offer details, interview-loop debriefs
> - May edit without asking: `Tasks/active.md`, `Tasks/follow-ups.md`, daily notes
> - Ask first: `CLAUDE.md`, `GOALS.md`, `Knowledge/People/*`, `Projects/*/brief.md`
> - Repo: private
>
> ### File-by-file edit plan
> - `CLAUDE.md`: identity, Batman persona, all 12 Gotham agents routed, cadence, privacy boundaries (with career-side additions)
> - `GOALS.md`: day-job and career 30-60-90, metrics, development goals (PD-TOL, contingency thinking)
> - `Tasks/active.md`: P0/P1/blockers/pre-mortem
> - `Tasks/backlog.md`: P2 frontier-lab target list seed
> - `Tasks/follow-ups.md`: Elena readout-draft follow-up
> - `Knowledge/People/priya-shah.md`
> - `Knowledge/People/marco-chen.md`
> - `Knowledge/People/elena-torres.md`
> - `Knowledge/People/sam-rivera.md`
> - `Projects/activation-funnel-redesign/brief.md`: context, open decisions, risks, pre-mortem
>
> Apply these setup changes? (Yes / No / Change X)

> **User:** Yes.

## Phase 9 — Write and next actions

> **Assistant:** Ready to update `CLAUDE.md`?

> **User:** Yes.

> **Assistant:** Updated `CLAUDE.md`. Next: `GOALS.md`.
>
> Ready to update `GOALS.md`?

> **User:** Yes.

> **Assistant:** Updated `GOALS.md`. Next: `Tasks/active.md`.
>
> Ready to update `Tasks/active.md`?

> **User:** Yes.

> **Assistant:** Updated `Tasks/active.md`. Next: `Tasks/backlog.md`.
>
> Ready to update `Tasks/backlog.md`?

> **User:** Yes.

> **Assistant:** Updated `Tasks/backlog.md`. Next: `Tasks/follow-ups.md`.
>
> Ready to update `Tasks/follow-ups.md`?

> **User:** Yes.

> **Assistant:** Updated `Tasks/follow-ups.md`. Next: `Knowledge/People/priya-shah.md`.
>
> Ready to update `Knowledge/People/priya-shah.md`?

> **User:** Yes.

> **Assistant:** Updated `Knowledge/People/priya-shah.md`. Next: `Knowledge/People/marco-chen.md`.
>
> Ready to update `Knowledge/People/marco-chen.md`?

> **User:** Yes.

> **Assistant:** Updated `Knowledge/People/marco-chen.md`. Next: `Knowledge/People/elena-torres.md`.
>
> Ready to update `Knowledge/People/elena-torres.md`?

> **User:** Yes.

> **Assistant:** Updated `Knowledge/People/elena-torres.md`. Next: `Knowledge/People/sam-rivera.md`.
>
> Ready to update `Knowledge/People/sam-rivera.md`?

> **User:** Yes.

> **Assistant:** Updated `Knowledge/People/sam-rivera.md`. Next: `Projects/activation-funnel-redesign/brief.md`.
>
> Ready to update `Projects/activation-funnel-redesign/brief.md`?

> **User:** Yes.

> **Assistant:** Updated `Projects/activation-funnel-redesign/brief.md`. All files written.
>
> **Change summary:**
> - `CLAUDE.md`, `GOALS.md`, `Tasks/active.md`, `Tasks/backlog.md`, `Tasks/follow-ups.md`
> - `Knowledge/People/priya-shah.md`, `marco-chen.md`, `elena-torres.md`, `sam-rivera.md`
> - `Projects/activation-funnel-redesign/brief.md`
>
> **Recommended first commands:**
> - `/today`
> - `/meeting-prep priya-shah`
> - `/weekly-update`
>
> Run `/today` now?

> **User:** Verify first.

## Phase 10 — Verify onboarding completed cleanly

> **Assistant:** Verification:
>
> | Check | Result |
> |---|---|
> | Placeholders filled | ✅ |
> | Persona set | ✅ Batman strategic operator |
> | Quality gates match persona | ✅ `/riddler` + `/vale` mandatory pre-publish |
> | 30-60-90 outcomes specific | ✅ deliverables named on both day-job and career tracks |
> | Active tasks present | ✅ 2 P0, 2 P1 |
> | Stakeholder profile started | ✅ 4 profiles drafted |
> | Privacy boundaries recorded | ✅ includes career-side exclusions |
> | Anchor project brief exists | ✅ |
>
> All clear. Onboarding complete. Run `/today` when ready. `/cowl-up` available manually for high-stakes weeks.

> **User:** Got it.

---

## File-write log

| Order | File | Approval reply |
|---|---|---|
| 1 | `CLAUDE.md` | "Yes." |
| 2 | `GOALS.md` | "Yes." |
| 3 | `Tasks/active.md` | "Yes." |
| 4 | `Tasks/backlog.md` | "Yes." |
| 5 | `Tasks/follow-ups.md` | "Yes." |
| 6 | `Knowledge/People/priya-shah.md` | "Yes." |
| 7 | `Knowledge/People/marco-chen.md` | "Yes." |
| 8 | `Knowledge/People/elena-torres.md` | "Yes." |
| 9 | `Knowledge/People/sam-rivera.md` | "Yes." |
| 10 | `Projects/activation-funnel-redesign/brief.md` | "Yes." |

## Phase 10 verification

| Check | Result | Resolution |
|---|---|---|
| Placeholders filled | ✅ | n/a |
| Persona set | ✅ | n/a |
| Quality gates match persona | ✅ | n/a |
| 30-60-90 outcomes specific | ✅ | n/a |
| Active tasks present | ✅ | n/a |
| Stakeholder profile started | ✅ | n/a |
| Privacy boundaries recorded | ✅ | n/a |
| Anchor project brief exists | ✅ | n/a |

No ❌ rows. Onboarding declared complete.
