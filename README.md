# Product Management OS 🧠

![AI PM](https://img.shields.io/badge/AI%20PM-Product%20Workflows-blue)
![LLM Evals](https://img.shields.io/badge/LLM-Evals-purple)
![Agentic Workflows](https://img.shields.io/badge/Agentic-Workflows-orange)
![PM OS](https://img.shields.io/badge/PM-Operating%20System-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)

A lightweight AI Product Management OS for PMs who want to run clearer workflows, write better PRDs, manage stakeholder updates, and add eval thinking into product execution.

Instead of using AI through random prompts, this repo gives Product Managers a simple operating system for repeatable work.

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
OS routes to the right workflow
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
Product-Management_OS/
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
Computer, onboard me into this OS
Computer, what should I focus on today?
Computer, draft an AI feature PRD
Computer, review this PRD before I share it
Computer, prepare my stakeholder update
Computer, run a launch readiness review
```

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
git clone https://github.com/richardan01/Product-Management_OS.git
cd Product-Management_OS
```

### 2. Open the repo in your AI tool

Use the entry file that matches your tool:

| Tool        | Entry file  | How to use it                      |
| ----------- | ----------- | ---------------------------------- |
| Claude Code | `CLAUDE.md` | Main PM workflow assistant         |
| Codex CLI   | `AGENTS.md` | Codex-based PM and repo workflows  |
| Gemini CLI  | `GEMINI.md` | Gemini-based PM workflow assistant |

The repo is designed so the same OS can work across different AI tools.

### 3. Run onboarding

Ask your AI assistant:

```text
Computer, onboard me into this OS.
```

The assistant should help you set up:

* Your PM role and working style
* Current goals
* Active projects
* Tasks and blockers
* Key stakeholders
* Privacy boundaries
* Preferred cadence for daily and weekly planning

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

The `Examples/` folder shows lightweight sample outputs from the OS.

* [`sample-ai-feature-prd.md`](Examples/sample-ai-feature-prd.md)
* [`sample-eval-review.md`](Examples/sample-eval-review.md)
* [`sample-launch-gate.md`](Examples/sample-launch-gate.md)

---

## Design principles

* Keep it lightweight
* Make workflows repeatable
* Store context in simple files
* Separate drafting from reviewing
* Make quality checks explicit
* Keep private context private
* Let the PM stay in control

---

## One-liner

A practical AI PM OS for turning messy product work into clearer workflows, stronger artifacts, and better product decisions.

---

## Acknowledgments

This OS started as a fork of [Carl Vellotti's Product OS](https://github.com/carlvellotti/carls-product-os) and has since been substantially extended into a harness-neutral template. Additions on top of the original:

- **Harness-neutral operation** — one configuration surface working across Claude Code, Codex CLI, and Gemini CLI (`CLAUDE.md` / `AGENTS.md` / `GEMINI.md`)
- **Offline eval suites** with author/grader separation, gold datasets, and run logs (`Evals/`)
- **Repo-native memory layer** with an explicit write-gate policy (`Memory/`)
- **Provenance-tagged knowledge layers** with a hypothesis/decision lifecycle (`Knowledge/`)
- **Interactive onboarding workflow** with per-file confirmation gates (`Workflows/interactive-onboarding.md`)
- **Quality gates** for PRDs, research sufficiency, launch readiness, and pre-publish review (`.claude/skills/`)

Thanks to Carl for the original foundation.
