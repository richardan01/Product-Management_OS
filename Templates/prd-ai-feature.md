# PRD: [AI Feature / Initiative Name]

**Author:** [Your Name]
**Status:** [Draft / In Review / Approved]
**Last Updated:** YYYY-MM-DD
**Target Launch:** YYYY-MM-DD
**AI Risk Level:** [Low / Medium / High] — see Risk section

---

## Overview

### Problem Statement

*What problem are we solving? For whom? Why does AI specifically address it better than a deterministic approach?*

### Goals

*What does success look like? Make it measurable. Include both product and model-quality goals.*

- Product goal:
- Model quality goal (e.g., ≥ X% task completion rate, ≤ Y% hallucination rate):
- Business goal:

### Non-Goals

*What are we explicitly NOT doing in this version?*

-
-

---

## Background

*Context, history, why now. Prior approaches tried (rules-based, manual, etc.). Why AI/LLM is the right fit.*

---

## User Stories

| As a... | I want to... | So that... |
|---------|-------------|-----------|
| | | |

---

## Requirements

### Must Have

- [ ]
- [ ]

### Should Have

- [ ]
- [ ]

### Nice to Have

- [ ]

---

## Model Design

### Model selection

| Dimension | Decision | Rationale |
|---|---|---|
| Provider / model | [e.g., Claude Sonnet 4.6] | [Why this model vs alternatives] |
| Inference mode | [Streaming / batch / async] | |
| Context window needed | [Approx. tokens] | |
| Expected latency budget | [ms P50 / P99] | |
| Cost per call (estimated) | [$/1k tokens × expected volume] | |

*If model choice is not yet made, document the decision criteria and timeline.*

### Prompt design

*Key design decisions: system prompt scope, user turn format, tool use, output format constraints.*

### Tool use / agentic steps (if applicable)

| Step | Tool / action | Expected output | Failure mode |
|---|---|---|---|
| | | | |

---

## Eval Criteria

*Define eval criteria before building. This section is required — no model ship without it.*

### Success metrics

| Metric | Measurement method | Baseline | Target | Gate (ship / no-ship) |
|---|---|---|---|---|
| [e.g., Task completion rate] | [LLM judge / human eval / code assertion] | [current] | [target] | [≥ X%] |
| [e.g., Hallucination rate] | | | | [≤ Y%] |
| [e.g., Refusal rate] | | | | |

### Eval suite plan

- Suite location: `Evals/[feature-name]/`
- Fixture sources: [production traces / synthetic / both]
- Number of evals planned: [aim for 5–10]
- LLM judge required: [Yes / No] — if yes, document TPR/TNR calibration plan
- Human review cadence: [before launch / weekly / monthly]

### Model upgrade audit plan

*How will this feature be re-evaluated when the underlying model is upgraded?*

- Regression suite: [which evals to re-run on every model release]
- Responsible party: [who owns the re-run]
- Blocking criteria: [what pass rate drop blocks the upgrade]

---

## Failure Modes and Guardrails

*Name failure modes before building. This is not optional.*

| Failure mode | Probability | User impact | Mitigation / guardrail |
|---|---|---|---|
| Hallucination of [specific entity/fact] | [Low/Med/High] | [describe] | [guardrail: filter / fallback / disclaimer] |
| Refusal on valid input | | | |
| Context window overflow | | | |
| Latency spike > budget | | | |
| Output format violation | | | |

### Fallback paths

*What happens when the model fails, is unavailable, or returns a low-confidence output?*

| Trigger condition | Fallback behavior | User experience |
|---|---|---|
| Model unavailable | | |
| Confidence below threshold | | |
| Output fails guardrail check | | |

### Guardrails implemented

- [ ] Input validation: [what's blocked / sanitized before the model sees it]
- [ ] Output validation: [what's checked before the response reaches the user]
- [ ] Rate limiting: [per-user / per-session limits]
- [ ] PII / sensitive data handling: [how it's handled]
- [ ] Human-in-the-loop: [when human review is required before output is acted on]

---

## Design

*Link to mockups / wireframes. Note which UI elements surface model uncertainty or fallback states.*

---

## Technical Considerations

*Key technical decisions, constraints, dependencies.*

- Infra: [serving, caching, logging strategy]
- Latency: [how latency budget is met in the stack]
- Cost controls: [token limits, caching, batching]
- Observability: [what's logged for monitoring and eval purposes]
- Data retention: [how long prompts/completions are stored; privacy implications]

---

## Launch Plan

| Phase | Who | Timeline | Exit criteria |
|-------|-----|----------|--------------|
| Internal / dogfood | | | Eval suite passes; no P0 failures |
| Beta / limited rollout | | | [X]% task completion; no critical failures |
| Full launch | | | [Metrics from Eval Criteria met] |

---

## Success Metrics (post-launch)

| Metric | Baseline | Target | How Measured | Cadence |
|--------|----------|--------|-------------|---------|
| | | | | |

---

## Open Questions

- [ ] Model choice confirmed?
- [ ] Eval suite built and passing?
- [ ] Fallback paths tested?
- [ ] Privacy / data retention reviewed?
- [ ]

---

## Appendix

*Supporting research, competitive examples, prior experiment results, eval run logs*
