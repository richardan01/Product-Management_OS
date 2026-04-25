# Peer Review

**Agent:** Orchestrator — see `Agents/orchestrator/orchestrator.md` for full context.

Evaluate any agent's output file against that agent's quality standards. Use this before passing research, analytics, PRDs, or any key output to the next agent in the chain.

Usage: `peer-review [file path]`
Example: `peer-review Knowledge/Research/cdp-vendor-scan.md`

## Steps

1. **Read the target file** — understand what it contains and what agent produced it.

2. **Identify the producing agent** — infer from:
   - File path (e.g., `Knowledge/Research/` → Research Analyst)
   - File content and structure
   - Frontmatter if present

3. **Read that agent's AGENT.md** — specifically the Quality Checks section:
   - `Agents/research-analyst/research-analyst.md` for research outputs
   - `Agents/analytics-metrics/analytics-metrics.md` for metrics and dashboards
   - `Agents/product-definer/product-definer.md` for PRDs and requirements
   - `Agents/cdp-specialist/cdp-specialist.md` for CDP-specific outputs
   - (any other agent as applicable)

4. **Score each quality check:**

| Quality Check | Status | Notes / Evidence |
|---------------|--------|-----------------|
| [check from AGENT.md] | Pass / Fail / Cannot Assess | [specific finding or gap] |

   - **Pass** — criterion is clearly met with evidence in the file
   - **Fail** — criterion is not met; note exactly what's missing
   - **Cannot Assess** — insufficient information to evaluate (flag this too)

5. **Output peer review report:**

```
**Peer Review — [filename] — [Date]**
**Produced by:** [Agent name]
**Evaluated against:** [Agent name] quality standards
**Reviewed for use by:** [next agent — e.g., Product Definer, Orchestrator, Launch Manager]

**Quality Score:** [n Pass] / [n total checks]

| Check | Status | Notes |
|-------|--------|-------|
| [check] | ✓ Pass / ✗ Fail / ? Cannot Assess | |

**Gaps to fix before using this output:**
- [specific gap] — suggested fix: [action]

**Verdict:**
- ✅ Cleared — ready to use downstream
- ⚠️ Conditional — usable but flag [specific gap] to the next agent
- ❌ Needs revision — do not use until [specific issue] is resolved
```

6. **If gaps found:** ask "Would you like me to flag these to the producing agent to fix, or proceed with caveats?"

---

**Next Steps:**
- Output is cleared → proceed with downstream agent (e.g., `prd [feature]`, `roadmap review`)
- Output needs revision → return to producing agent with specific gaps
- Analytics output → `metrics-snapshot` to refresh data if numbers are outdated
- Research output → `synthesize research` to add missing evidence or address gaps
