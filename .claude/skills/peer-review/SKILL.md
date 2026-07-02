# Peer Review

**Agent:** Review Orchestrator

Evaluate any agent's output file against **two layers of quality standards**:
1. **Agent-specific checks** — the quality gates defined in the producing agent's agent file
2. **Personal ground truth** — [YOUR_NAME]'s 5 criteria in `Knowledge/Reference/ground-truth.md`

Run this before passing any output to the next agent in the chain, and before sharing anything externally with [YOUR_MANAGER], [HEAD_OF_DEPT], or the broader team.

Usage: `peer-review [file path]`
Example: `peer-review Projects/[YOUR_ANCHOR_PROJECT]/vendor-scorecard.md`

---

## Step 1 — Read the Target File

Read the file the user specified. Identify:
- What type of document it is (PRD, research synthesis, strategy, proposal, business case, etc.)
- Which agent produced it (infer from file path, structure, or content)
- Whether it is intended for internal use or external sharing ([YOUR_MANAGER], [HEAD_OF_DEPT], engineering)

---

## Step 2 — Check for External Reviewer Comments

Before scoring, scan the conversation and the document itself for evidence of prior reviewer feedback:
- Has the user mentioned [YOUR_MANAGER], [HEAD_OF_DEPT], or any named reviewer?
- Has the user pasted comments, markup, or a review note alongside the file?
- Does the document contain a comments section, tracked changes, or explicit "Reviewer notes"?

If yes: extract all comments into a numbered list. Evaluate each under Layer 2, Criterion 5.
If no: mark Criterion 5 as N/A.

---

## Step 3 — Layer 1: Agent-Specific Quality Checks

Identify the producing agent and read its quality checks from the appropriate agent file.

**Pass 1 — Structural scan**
Check the document type against `Knowledge/Reference/ground-truth.md` → "Document-Type Templates" to find the required sections for that type. For each required section, test **information presence, not header presence**: a section is only Missing if its *information* is absent from the document — before marking anything missing, check whether the content lives under a different heading or in prose, and name where you looked. A missing header whose information is present elsewhere is at most a Nice to Fix formatting note, never a Fail. Flag any placeholders (TBD, TODO, insert here).

**Per-element completeness (do not grade a section by presence alone).** When a required section contains a list of repeated elements — user stories, requirements, milestones, API endpoints — check **each element individually**, not the section as a whole. For a PRD specifically: for *each* user story, verify that story has its own testable acceptance criteria. "US-1, US-2, US-3 present ✅" is not a valid finding if US-3 has no acceptance criteria — a single story missing its ACs is a Must Fix (not handoff-ready), even when its siblings are complete. Name the specific element that fails (e.g., "US-3 has no acceptance criteria").

**Pass 1b — Cross-section consistency**
Check every quantity that appears more than once (counts, dates, percentages, deadlines, totals) for agreement across sections — executive summary vs. timeline, method vs. findings, goals vs. body. Also verify derived figures: when a percentage and its base count both appear, confirm the arithmetic matches. A contradiction between sections is a Fail-severity finding; it is the class of flaw section-by-section reading misses.

**Pass 2 — Agent quality check**
Score each quality check from the producing agent's file:

```
**Layer 1 — Agent Quality Checks ([Agent Name])**

| Check | Status | Evidence / Gap |
|-------|--------|----------------|
| [check from agent file] | ✅ Pass / ❌ Fail / ? Cannot Assess | [specific finding] |

Layer 1 Score: [n Pass] / [n total checks]
```

---

## Step 4 — Layer 2: Personal Ground Truth

Read `Knowledge/Reference/ground-truth.md`. Apply all 5 criteria to the document regardless of type.

**Degraded mode:** if `ground-truth.md` still contains placeholder brackets (`[YOUR_NAME]`, bracketed example bars), say so explicitly at the top of the review, do **not** apply the bracketed example text as if it were the user's actual bar, and cap purely structural/template findings at Should Fix — without a personalized quality bar, template-completeness judgments lack the authority to block.

The cap is **narrow**: it applies only to *purely* structural/template-completeness findings (a missing summary header, an absent "Background" section). It does **not** apply to substantive defects, which keep their full severity regardless of degraded mode:
- contradictions and cross-section inconsistencies
- unmeasurable metrics (no baseline/target)
- placeholders (TBD/TODO) in the artifact
- missing acceptance criteria on any user story
- **safety, risk, compliance, or failure-handling content** — e.g., no rollback/failure plan for a payments or held-funds flow, missing data-loss handling, absent security/privacy treatment. A missing rollback plan in a payments PRD is a substantive Must Fix even though it coincides with a missing section; never demote it to a template gap.

When unsure whether a finding is "purely structural" or substantive, treat it as substantive — the cap exists to suppress pedantry, not to hide risk.

```
**Layer 2 — Personal Ground Truth**

| # | Criterion | Score | Finding |
|---|-----------|-------|---------|
| 1 | Structure & Completeness | ✅ Pass / ⚠️ Partial / ❌ Fail | [specific finding] |
| 2 | Clarity & Writing Quality | ✅ Pass / ⚠️ Partial / ❌ Fail | [specific finding] |
| 3 | Strategic Alignment ([YOUR_COMPANY]) | ✅ Pass / ⚠️ Partial / ❌ Fail | [specific finding] |
| 4 | Actionability | ✅ Pass / ⚠️ Partial / ❌ Fail | [specific finding] |
| 5 | External Reviewer Comments | ✅ Pass / ⚠️ Partial / ❌ Fail / ⏭️ N/A | [finding or "N/A — no reviewer comments detected"] |

Layer 2 Score: [n Pass] / 5 criteria
```

---

## Step 5 — Overall Verdict

```
**Overall Verdict: CLEARED ✅ / CONDITIONAL ⚠️ / NEEDS REVISION ❌**
```

Rules (driven by the `bad`/`sad` taxonomy in `Evals/severity-taxonomy.md`):
- **CLEARED** — all Layer 1 checks pass AND all Layer 2 criteria are Pass or N/A (0 `bad`, 0 `sad`)
- **CONDITIONAL** — 1–2 `sad` items (Partials) across both layers, no `bad`
- **NEEDS REVISION** — any `bad` item (a Fail), **or** 3+ `sad` items across both layers (the stacking rule: stacked sads become bad)

A `bad` finding (hallucinated content, missed Must-Fix blocker, unpreserved contradiction, safety/risk gap) blocks regardless of degraded mode.

---

## Step 6 — Fix Checklist

List every gap as a checkbox, grouped by severity.

**Severity bar:** Must Fix = the gap blocks the document's *stated purpose* (engineering handoff, decision, publication) — an engineer can't build, a decider can't decide, a reader is actively misled. Open questions that already have owners and due dates are tracked work, not blockers. Missing section headers whose information is present elsewhere are Nice to Fix. When in doubt between Must and Should, ask: "would shipping with this gap cause rework or a wrong decision?" — if not, it is not Must Fix.

```
**🔧 Fix Checklist**

### Must Fix (Blocking)
- [ ] [L2 · Criterion 3] Tie metric to specific [YOUR_COMPANY] context — Section 2 is generic.

### Should Fix (Important — fix before external sharing)
- [ ] [L2 · Criterion 4] Assign owner to open action — Section 3.

### Nice to Fix (Minor — polish)
- [ ] [L2 · Criterion 2] Remove filler phrase — Executive Summary, line 1.
```

---

## Step 7 — Revised Version (if needed)

If verdict is NEEDS REVISION or CONDITIONAL, produce a corrected version applying all Must Fix and Should Fix items.

---

## Step 8 — Outcome & Next Steps

```
**🎯 Outcome & Next Steps**

**Expected outcome after fixes:** [1–2 sentences]

**Your action sequence:**
1. [Highest-severity fix first]
2. [Next item]
```

---

## Verdict file (per `_Registry/reviewer-verdict-schema.md`)

On PASS (or CONDITIONAL-PASS), write `<doc-path>.peer-review-passed` with the byte-exact 4-line header + scorecard.

---

**What to run next:**
- Verdict is NEEDS REVISION → apply fixes, then re-run `peer-review` before sharing
- Document is a PRD → `prd-readiness` for engineering-handoff gate
- Document is a research synthesis → `research-sufficiency` for decision-readiness gate
