# Eval CI map

Maps source files to eval suites. When a source file is edited, `/eval-ci register <suite> <source-file>` should be called to flag the suite as pending re-run. `/peer-review` and `/go-nogo` consult `_pending-reruns.md` before allowing any artifact to cite a suite's pass rate.

Extend this table as new suites are added.

| Source file | Affected suite |
|---|---|
| Workflows/interactive-onboarding.md | onboarding |
| Templates/profile.md | onboarding |
| Evals/onboarding/04-no-residual-placeholders/grade.sh | onboarding |
| .claude/skills/synthesize-research/SKILL.md | research-synthesis |
| Templates/synthesis.md | research-synthesis |
| .claude/skills/peer-review/SKILL.md | peer-review |
| _Registry/reviewer-verdict-schema.md | peer-review |
| Knowledge/Reference/ground-truth.md | peer-review |

## Notes

- `CLAUDE.md` edits do NOT trigger re-runs by default — that file is the user's identity and changes often. Edits to the **Operating contract** section of `CLAUDE.md`, however, can affect onboarding behavior. If unsure, register manually.
- Adding a new suite? Add its source-file rows here and update `/eval-ci` SKILL.md if the mapping logic needs to change.
- Removing a suite? Move its rows to a `## Retired` section below with a one-line reason and date.
- The memory-loop skills (`.claude/skills/eod`, `.claude/skills/retro`) now propose writes to `Memory/`, but there is no dedicated `memory` suite yet, so they are intentionally unmapped. If a memory-maintenance suite is added later, map them here.
