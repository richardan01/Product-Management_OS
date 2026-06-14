# Sample Launch Gate ✅

## Product

Finance Assistant internal pilot.

## Launch decision

Status: Conditional Go

## What must be true before launch

- Users understand this is an assistant, not a final decision-maker
- Human review path is clear
- Risky answers are escalated
- Feedback capture is enabled
- Known failure modes are documented
- Sensitive data handling is reviewed
- Eval results meet the agreed threshold

## Go / no-go checklist

| Area | Status | Notes |
|---|---|---|
| User problem is clear | ✅ | Internal finance workflow support |
| Target users are defined | ✅ | Finance and operations users |
| Eval rubric exists | ✅ | Covers helpfulness, grounding, reasoning, and safety |
| Failure modes reviewed | ✅ | Hallucination, wrong numbers, overconfidence |
| Human review path exists | ⚠️ | Needs pilot owner confirmation |
| Feedback loop exists | ⚠️ | Needs lightweight tracking setup |
| External launch ready | ❌ | Internal pilot only |

## PM decision

Launch as an internal pilot only.

The assistant is useful enough to test with a small group, but not ready for broad or external usage.

## Learning goal

Use the pilot to learn:

- Which questions users ask most often
- Where the assistant is helpful
- Where it fails
- How often human review is needed
- What quality threshold is required before broader rollout
