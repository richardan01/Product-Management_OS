# Sample Eval Review 🧪

## Evaluation target

Finance Assistant response quality.

## Main question

Is the assistant good enough to support finance-related workflow questions in an internal pilot?

## Evaluation dimensions

| Dimension | What good looks like |
|---|---|
| Helpfulness | Answers the user’s question clearly |
| Grounding | Uses available context instead of inventing facts |
| Reasoning clarity | Explains how it reached the answer |
| Calculation accuracy | Avoids incorrect numbers or formulas |
| Escalation behavior | Routes uncertain or risky cases to human review |
| Safety | Avoids unsupported financial advice |

## Example failure modes

- Inventing numbers not present in the source material
- Giving financial advice without caveats
- Hiding uncertainty
- Failing to ask for missing context
- Producing a confident but unsupported answer
- Ignoring policy or compliance constraints

## Human review rule

Human review is required when:

- The assistant makes a financial recommendation
- The source data is missing or ambiguous
- The answer impacts external reporting
- The answer involves sensitive or regulated information
- The confidence level is low

## PM recommendation

Proceed only with an internal pilot.

Do not expand usage until the assistant passes eval thresholds for grounding, calculation accuracy, and escalation behavior.
