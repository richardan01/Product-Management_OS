#!/usr/bin/env bash
# Programmatic grader for eval 04 — no-residual-placeholders
# Usage: grade.sh <repo-root> [--strict]
#
# Exits 0 if all 5 criteria pass; non-zero if any fail.
# Prints one line per criterion in the form:
#   C<N>: PASS|FAIL — <one-line reason>
# followed by a JSON summary.
#
# Pairs with the eval-grader sub-agent: that agent invokes this script,
# captures its output, and returns the JSON to the orchestrator.

set -u

ROOT="${1:-.}"
STRICT="${2:-}"

CLAUDE_MD="$ROOT/CLAUDE.md"
GOALS_MD="$ROOT/GOALS.md"
TASKS_MD="$ROOT/Tasks/active.md"

# Allowlist: bracketed strings that are NOT placeholders even though they
# match the broader pattern (e.g. annotated deferrals, the literal
# "# TODO: ask user" marker).
ALLOWLIST_RE='# TODO: ask user|Unknown / TBD'

count_placeholders () {
  local file="$1"
  local pattern="$2"
  if [ ! -f "$file" ]; then
    echo "MISSING"
    return
  fi
  # Find matches not on lines containing the allowlist
  grep -E -o "$pattern" "$file" 2>/dev/null \
    | grep -v -E "$ALLOWLIST_RE" \
    | wc -l \
    | tr -d ' '
}

PASS_ALL=0

# C1 — CLAUDE.md placeholders
PATTERN_C1='\[YOUR_[A-Z_]+\]|\[HEAD_OF_DEPT\]|\[STAKEHOLDER_[0-9]+\]|\[METRIC_[A-Z_0-9]+\]|\[PRIMARY_PURPOSE\]|\[YOUR_ANCHOR_PROJECT\]|\[YOUR_ROLE\]|\[YOUR_COMPANY\]|\[YOUR_MANAGER\]|\[YOUR_NAME\]|\[TARGET_COMPANY_INTERVIEWERS\]|\[your-[a-z-]+\]'
C1=$(count_placeholders "$CLAUDE_MD" "$PATTERN_C1")
if [ "$C1" = "MISSING" ]; then
  echo "C1: FAIL — CLAUDE.md not found at $CLAUDE_MD"
  PASS_ALL=1
elif [ "$C1" -eq 0 ]; then
  echo "C1: PASS — CLAUDE.md placeholders absent"
else
  echo "C1: FAIL — $C1 placeholder(s) remain in CLAUDE.md"
  PASS_ALL=1
fi

# C2 — GOALS.md core placeholders
PATTERN_C2='\[YOUR_[A-Z_]+\]|\[AREA_[A-Z_0-9]+\]|\[METRIC_[A-Z_0-9]+\]|\[STAKEHOLDER_[0-9]+\]|\[DEV_GOAL_[0-9]+\]'
C2=$(count_placeholders "$GOALS_MD" "$PATTERN_C2")
if [ "$C2" = "MISSING" ]; then
  echo "C2: FAIL — GOALS.md not found at $GOALS_MD"
  PASS_ALL=1
elif [ "$C2" -eq 0 ]; then
  echo "C2: PASS — GOALS.md core placeholders absent"
else
  echo "C2: FAIL — $C2 placeholder(s) remain in GOALS.md"
  PASS_ALL=1
fi

# C3 — GOALS.md marketing-legacy placeholders
PATTERN_C3='\[LIFECYCLE_PM\]|\[PAID_ADS_PM\]|\[WEBSITE_PM\]|\[CONTENT_PM\]|\[CURRENT_QUARTER\]'
C3=$(count_placeholders "$GOALS_MD" "$PATTERN_C3")
if [ "$C3" = "MISSING" ]; then
  echo "C3: FAIL — GOALS.md not found"
  PASS_ALL=1
elif [ "$C3" -eq 0 ]; then
  echo "C3: PASS — marketing-legacy placeholders absent"
else
  echo "C3: FAIL — $C3 marketing-legacy placeholder(s) remain"
  PASS_ALL=1
fi

# C4 — Tasks/active.md populated rows
PATTERN_C4='\[Task description\]|\[Sprint [0-9N]+\]|\[Start Date\]'
C4=$(count_placeholders "$TASKS_MD" "$PATTERN_C4")
if [ "$C4" = "MISSING" ]; then
  echo "C4: FAIL — Tasks/active.md not found"
  PASS_ALL=1
elif [ "$C4" -eq 0 ]; then
  echo "C4: PASS — Tasks/active.md row placeholders absent"
else
  echo "C4: FAIL — $C4 placeholder(s) remain in Tasks/active.md"
  PASS_ALL=1
fi

# C5 — any explicitly-deferred placeholder must be annotated
# This is satisfied by definition of count_placeholders (the allowlist).
# If any bare placeholder remains without "# TODO: ask user" or "Unknown / TBD"
# nearby, it's a C1-C4 failure already. We surface C5 as PASS when C1-C4 pass.
TOTAL_REMAIN=$(( C1 + C2 + C3 + C4 ))
if [ "$TOTAL_REMAIN" -eq 0 ]; then
  echo "C5: PASS — all surviving deferrals are annotated"
else
  echo "C5: FAIL — $TOTAL_REMAIN unannotated placeholder(s) total"
  PASS_ALL=1
fi

# JSON summary
cat <<EOF
---JSON---
{
  "eval_id": "04-no-residual-placeholders",
  "grader": "programmatic",
  "results": [
    {"criterion_id": "C1", "verdict": $([ "$C1" = "0" ] && echo '"pass"' || echo '"fail"'), "count": "${C1}"},
    {"criterion_id": "C2", "verdict": $([ "$C2" = "0" ] && echo '"pass"' || echo '"fail"'), "count": "${C2}"},
    {"criterion_id": "C3", "verdict": $([ "$C3" = "0" ] && echo '"pass"' || echo '"fail"'), "count": "${C3}"},
    {"criterion_id": "C4", "verdict": $([ "$C4" = "0" ] && echo '"pass"' || echo '"fail"'), "count": "${C4}"},
    {"criterion_id": "C5", "verdict": $([ "$TOTAL_REMAIN" = "0" ] && echo '"pass"' || echo '"fail"'), "count": "${TOTAL_REMAIN}"}
  ],
  "overall": "$([ "$PASS_ALL" = "0" ] && echo "pass" || echo "fail")"
}
EOF

exit $PASS_ALL
