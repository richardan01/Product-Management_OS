# Synthesize Research

**Agent:** Research Analyst — see `Agents/research-analyst/research-analyst.md` for full context.

Usage: "synthesize research" — run after completing a round of discovery or validation interviews

Steps:

1. **Find interview notes** — look in `Projects/[project]/research/` or ask where the notes are
2. **Read each interview** — extract pain points, needs, quotes, and themes
3. **Extract patterns** — cluster themes across interviews, count frequency

Pattern extraction table:
| Theme | # Mentions | Best Quote | Participants |
|-------|-----------|-----------|-------------|
| | | | |

4. **Rank by impact** — combine frequency with business impact (retention, ROAS, activation, etc.)

5. **Draft synthesis** using `Templates/research-summary.md`:
   - Executive summary (3–5 sentences: what we learned, what to do)
   - Top 3 findings with evidence and confidence level
   - Themes table
   - Recommendations: immediate actions + what NOT to do

6. **Suggest use case implications:**
   - Based on findings, which use case(s) have the strongest case for flight 1?
   - What data sources are needed to support them?
   - Any blockers or dependencies to flag?

7. **Ask user to review:**
   - "Does this match what you heard?"
   - "Any key finding I missed?"
   - "Which use case does this point to for flight 1?"

8. **Update knowledge base:**
   - Offer to update `Knowledge/Reference/[domain].md` use case table with findings
   - Offer to update `Projects/[project]/brief.md` open questions based on what was learned

9. **Chain to Domain Specialist:**
   - After synthesis is complete, suggest: "Run `/[domain]-use-cases` to update the use case scoring matrix with these findings?"
