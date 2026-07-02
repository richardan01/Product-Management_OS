# PM Command Center

![PM Workflows](https://img.shields.io/badge/PM-Workflows-blue)
![AI Assisted](https://img.shields.io/badge/AI-Assisted-purple)
![Agentic Workflows](https://img.shields.io/badge/Agentic-Workflows-orange)
![Templates](https://img.shields.io/badge/Reusable-Templates-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A reusable AI-assisted command center for product managers to run clearer, faster, and more reviewable product work.

PM Command Center is a practical workspace for daily and weekly PM execution, PRD drafting and review, stakeholder updates, research synthesis, launch readiness, reusable project context, and AI-assisted product workflows.

This is the reusable template: fork it, adapt it, and fill it with your own private goals, projects, tasks, stakeholders, and operating context. It is not a personal AI PM portfolio. For the public proof-of-work lab, see [AI Product Lab](https://github.com/richardan01/AI-Product-Lab).

Instead of using AI through random prompts, this repo gives product managers a command center for repeatable, reviewable work.

---

## What this helps with

- 🧭 Daily and weekly PM execution
- 📝 PRD drafting and review
- 🧪 LLM evals and quality gates
- 🤝 Stakeholder updates and meeting prep
- 🔍 Research synthesis
- ✅ Launch readiness review
- 🧠 Reusable project and stakeholder context

---

## How it works

```text
PM asks for help
   ↓
"Computer, [task]"
   ↓
Command center routes to the right workflow
   ↓
Context is pulled from files
   ↓
Artifact is created or reviewed
   ↓
Quality gate checks the output
```

---

## Folder structure

```text
PM-Command-Center/
├── CLAUDE.md      # Claude Code entry point
├── AGENTS.md      # Codex entry point
├── GEMINI.md      # Gemini entry point
├── GOALS.md       # What the PM is optimizing for
├── Tasks/         # Active work and backlog
├── Projects/      # Product/project context
├── Knowledge/     # Stakeholders and reusable context
├── Templates/     # PRDs, updates, reviews
├── Workflows/     # Repeatable PM workflows
├── Evals/         # Eval rubrics and quality checks
└── Examples/      # Sample PM artifacts
```

---

## Example commands

```text
Computer, onboard me into this command center
Computer, what should I focus on today?
Computer, draft an AI feature PRD
Computer, review this PRD before I share it
Computer, prepare my stakeholder update
Computer, run a launch readiness review
```

---

## What this is

PM Command Center is a reusable AI-assisted PM workspace. It combines lightweight files, workflow prompts, templates, quality gates, and repo-native context so a PM can run recurring work with more structure and less prompt drift.

It is designed for adoption: bring your own goals, stakeholders, active projects, and privacy boundaries. Keep real company, customer, and personal context in a private fork or local copy.

## Naming clarification

This repo was formerly named Product Management OS. The new name better reflects its purpose: a reusable command center for AI-assisted product management workflows.

---

## Who this is for

Product Managers who want to use AI more intentionally for real PM work — not just content generation.

You do not need to be an engineer.
You just need to be comfortable working with markdown files and AI assistants.

---

## Quick start

### 1. Fork or clone this repo

Fork it if you want your own GitHub copy, or clone it locally:

```bash
git clone https://github.com/richardan01/PM-Command-Center.git
cd PM-Command-Center
```

### 2. Open the repo in your AI tool

Use the entry file that matches your tool:

| Tool        | Entry file  | How to use it                      |
| ----------- | ----------- | ---------------------------------- |
| Claude Code | `CLAUDE.md` | Main PM workflow assistant         |
| Codex CLI   | `AGENTS.md` | Codex-based PM and repo workflows  |
| Gemini CLI  | `GEMINI.md` | Gemini-based PM workflow assistant |

The repo is designed so the same command center can work across different AI tools.

### 3. Run onboarding

Ask your AI assistant:

```text
Computer, onboard me into this command center.
```

The assistant should help you set up:

- Your PM role and working style
- Current goals
- Active projects
- Tasks and blockers
- Key stakeholders
- Privacy boundaries
- Preferred cadence for daily and weekly planning

### 4. Add your working context

Start with these files:

```text
GOALS.md
Tasks/active.md
Tasks/backlog.md
Projects/[your-project]/brief.md
Knowledge/People/[stakeholder-name].md
```

Do not add sensitive company, customer, credential, or private personal information into the public repo. Use a private fork or local copy for real work.

### 5. Start your first PM workflow

Try one of these:

```text
Computer, what should I focus on today?
Computer, prep me for my next stakeholder meeting.
Computer, help me draft a PRD for [feature].
Computer, review this PRD for gaps and risks.
Computer, run a launch readiness review.
```

### 6. Close the loop weekly

At the end of the week, ask:

```text
Computer, summarize my week and update my priorities.
```

Use the output to update your goals, backlog, and active tasks.

---

## Sample artifacts

The `Examples/` folder shows lightweight sample outputs from the command center.

- [`sample-ai-feature-prd.md`](Examples/sample-ai-feature-prd.md)
- [`sample-eval-review.md`](Examples/sample-eval-review.md)
- [`sample-launch-gate.md`](Examples/sample-launch-gate.md)

---

## Known scaffolding (read before relying on it)

Two things ship as structure, not as finished machinery:

- **Judge prompts are uncalibrated candidates.** The shipped `judge-prompt.md` files include calibration headers and few-shot anchors, but the labeled corpora (`_labeled/`, `_calibration/`) are local-only by design. Run `/judge-calibration` on your own labeled examples before trusting any judge-graded result.
- **`.claude/settings.json` ships without hooks.** Session-start steps and eval-CI registration are instructions the assistant follows, not enforced automation. The `/eval-ci` skill documents how to wire the optional PostToolUse hook yourself.

---

## Design principles

- Keep it lightweight
- Make workflows repeatable
- Store context in simple files
- Separate drafting from reviewing
- Make quality checks explicit
- Keep private context private
- Let the PM stay in control

---

## One-liner

A reusable command center for turning messy product work into repeatable AI-assisted workflows, stronger artifacts, and better product decisions.

---

## Acknowledgments

This command center started as a fork of [Carl Vellotti's Product OS](https://github.com/carlvellotti/carls-product-os) and has since been substantially extended into a harness-neutral template. Additions on top of the original:

- **Harness-neutral operation** — one configuration surface working across Claude Code, Codex CLI, and Gemini CLI (`CLAUDE.md` / `AGENTS.md` / `GEMINI.md`)
- **Offline eval suites** with author/grader separation, gold answer keys, run logs, and an **LLM-as-judge calibration protocol** (TPR/TNR ≥ 0.9 on held-out data before a judge is trusted) for the subjective criteria (`Evals/`)
- **Graded quality gates** — the gates themselves are eval'd by planted-flaw meta-eval suites (peer-review, prd-readiness, go/no-go, research-sufficiency, build-review), so the guardrails are measured, not assumed
- **Severity taxonomy + online-monitoring loop** — a "bad vs sad" model driving gate verdicts, plus a weekly sample→grade→error-analysis loop (`Evals/severity-taxonomy.md`, `Evals/monitoring/`)
- **Repo-native memory layer** with an explicit write-gate policy (`Memory/`)
- **Provenance-tagged knowledge layers** with a hypothesis/decision lifecycle (`Knowledge/`)
- **Interactive onboarding workflow** with per-file confirmation gates (`Workflows/interactive-onboarding.md`)

Thanks to Carl for the original foundation.
