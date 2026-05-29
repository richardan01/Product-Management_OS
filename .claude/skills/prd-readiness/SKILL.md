# PRD Readiness

**Agent:** Product Definer
**Methodology:** Dan Olsen's Lean Product Process — gap analysis vs. target conditions
**Pattern:** Evaluator/Gate — applied before a PRD is shared with engineering or used for task extraction.

Run this gate before handing off a PRD to engineering, before `/spec-handoff`, or before `/add-task` extracts implementation work from a PRD.

## Steps

1. **Read:**
   - The target PRD file (user provides path, or infer from `Projects/*/prd-*.md`)
   - The relevant agent file — quality checks section
   - `Projects/[YOUR_ANCHOR_PROJECT]/brief.md` — project context for alignment check

2. **Detect PRD type:**
   - If the PRD uses `Templates/prd-ai-feature.md` structure OR contains a "Model Design" or "Eval Criteria" section, apply **both** the standard gates (8) and the AI-specific gates (4) below.
   - Otherwise apply the standard gates only.

3. **Score standard gates (all PRDs):**

| Gate | Criteria | Status | Notes |
|------|----------|--------|-------|
| Problem statement | Clearly defines the user problem and business impact | Pass/Fail | |
| User stories | All key user stories present with persona, action, outcome | Pass/Fail | |
| Acceptance criteria | Every requirement has testable acceptance criteria | Pass/Fail | |
| Data requirements | Data sources, schemas, and dependencies identified | Pass/Fail | |
| Scope boundaries | Explicit in/out of scope section — no ambiguity | Pass/Fail | |
| Dependencies | External dependencies listed with owners and ETAs | Pass/Fail | |
| Priority tags | Requirements tagged must/should/nice-to-have | Pass/Fail | |
| Feasibility input | Data & Tech Architect has reviewed (or flagged as needed) | Pass/Fail | |

4. **Score AI-specific gates (AI-feature PRDs only):**

| Gate | Criteria | Status | Notes |
|------|----------|--------|-------|
| Model choice justified | Model selected with rationale, OR decision criteria + timeline documented | Pass/Fail | |
| Eval criteria defined | Success metrics table present with measurement method, baseline, target, and ship/no-ship threshold | Pass/Fail | |
| Failure modes named | At least 3 failure modes listed with mitigation or guardrail for each | Pass/Fail | |
| Fallback paths specified | At least one fallback path per critical failure trigger | Pass/Fail | |

5. **Final decision:**
   - All applicable gates pass → **READY** — safe to hand off or extract tasks
   - Any fail → **NOT READY** — list gaps with specific fix actions
   - Most pass, minor gaps → **CONDITIONAL** — list conditions, safe to proceed if flagged

6. **Output:**

```
**PRD Readiness — [filename] — [Date]**

**PRD type:** Standard | AI-feature
**Score:** [n] / [8 or 12] gates passed

**Standard Gate Results:**
[table]

**AI Gate Results (if applicable):**
[table]

**Decision: READY / NOT READY / CONDITIONAL**

**Gaps to resolve:**
- [gate — what's missing — suggested fix]

**Next action:** [proceed to spec-handoff / return to Product Definer for revision]
```

---

**Next Steps:**
- PRD is READY → `spec-handoff [project]` to package for engineering
- PRD is NOT READY → fix gaps, then re-run `prd-readiness`
- Need feasibility input → `tech-feasibility [feature]` before re-checking
- AI PRD missing eval criteria → build `Evals/[feature-name]/` suite first, then re-run

---

## Verdict file (per `_Registry/reviewer-verdict-schema.md`)

On READY (or READY-WITH-CONDITIONS), write `<prd-path>.prd-readiness-passed` with the byte-exact 4-line header followed by the scorecard.
