# Product Management OS 🧠

A lightweight AI Product Management operating system for PMs who want a more structured way to manage daily execution, PRDs, stakeholder updates, product reviews, evals, and launch readiness.

This repo is designed to help a Product Manager work with AI more intentionally — not just by prompting randomly, but by creating repeatable workflows, reusable context, and quality gates.

---

## What this is

Product work is messy.

On any given day, a PM may need to:

* Clarify priorities
* Prepare for stakeholder meetings
* Write or review a PRD
* Synthesize research
* Track risks
* Review launch readiness
* Follow up on open decisions
* Keep context across multiple projects

A single long AI prompt is usually not enough.

**Product Management OS** gives the PM a simple structure for turning that messy work into repeatable AI-supported workflows.

---

## Who this is for

This OS is for Product Managers who want to:

* 🧭 Run daily and weekly product execution more clearly
* 📝 Draft and review stronger PRDs
* 🧪 Add eval and quality-gate thinking to AI product work
* 🤝 Prepare better stakeholder updates
* 🔍 Synthesize research without losing context
* ✅ Review launch readiness before shipping
* 🧠 Keep reusable product context in one place
* 🤖 Work across tools like Claude Code, Codex CLI, or Gemini CLI

You do not need to be an engineer to use this.
You just need to be comfortable working with files, markdown, and AI assistants.

---

## How the OS works

```text
PM asks for help
   ↓
"Computer, [task]"
   ↓
The OS routes the task
   ↓
Relevant workflow / skill is used
   ↓
Context is pulled from project files, goals, tasks, and knowledge
   ↓
A product artifact is created or reviewed
   ↓
Quality gate checks the output
```

The goal is to make AI useful for real PM work, not just one-off content generation.

---

## Core idea

Instead of asking AI random questions every day, the PM builds a small operating system around their work.

That means:

* Goals live in `GOALS.md`
* Active work lives in `Tasks/`
* Project context lives in `Projects/`
* Stakeholder context lives in `Knowledge/People/`
* Templates live in `Templates/`
* Repeatable workflows live in `Workflows/`
* Evals and checks live in `Evals/`
* Durable preferences live in `Memory/`

The assistant becomes more useful because it has a clear place to look, a clear workflow to follow, and a clear quality standard to apply.

---

## What you can use it for

### 🧭 Daily execution

Use the OS to decide what matters today, what is blocked, and what needs follow-up.

```text
Computer, what should I focus on today?
```

### 🤝 Meeting preparation

Prepare for stakeholder meetings using project context, open risks, and previous decisions.

```text
Computer, prep me for my 1:1 with [stakeholder].
```

### 📝 PRD drafting and review

Draft or review PRDs using structured templates and readiness checks.

```text
Computer, help me draft an AI feature PRD.
Computer, review this PRD before I share it.
```

### 🧪 Eval and quality review

Use eval thinking to check whether an AI feature, output, or product artifact is good enough.

```text
Computer, review this eval plan.
Computer, identify failure modes before launch.
```

### 📊 Stakeholder updates

Turn messy progress notes into clear weekly updates.

```text
Computer, draft my weekly product update.
```

### ✅ Launch readiness

Check whether a product, feature, or AI workflow is ready to move forward.

```text
Computer, run a launch readiness review.
```

---

## Repository structure

```text
Product-Management_OS/
├── CLAUDE.md
├── AGENTS.md
├── GEMINI.md
├── GOALS.md
├── Tasks/
├── Projects/
├── Knowledge/
├── Memory/
├── Templates/
├── Workflows/
├── Evals/
└── Examples/
```

### Key folders

| Folder       | Purpose                                                     |
| ------------ | ----------------------------------------------------------- |
| `Tasks/`     | Current work, backlog, blockers, and follow-ups             |
| `Projects/`  | Product/project context that the assistant can reuse        |
| `Knowledge/` | Stakeholder notes, reference material, and reusable context |
| `Memory/`    | Durable working preferences and operating rules             |
| `Templates/` | PRDs, updates, reviews, and product artifact templates      |
| `Workflows/` | Step-by-step PM workflows                                   |
| `Evals/`     | Eval suites, rubrics, and quality checks                    |
| `Examples/`  | Sample outputs to show how the OS can be used               |

---

## Supported AI tools

This OS is designed to be harness-neutral.

| Tool        | Entry file  | How it is used                             |
| ----------- | ----------- | ------------------------------------------ |
| Claude Code | `CLAUDE.md` | Main PM workflow assistant                 |
| Codex CLI   | `AGENTS.md` | Agentic workflow and code-adjacent support |
| Gemini CLI  | `GEMINI.md` | Alternative AI assistant runtime           |

The same operating system can be used across different AI tools.
The entry files simply tell each tool how to behave inside this repo.

---

## Quick start

### 1. Fork or clone the repo

```bash
git clone https://github.com/richardan01/Product-Management_OS.git
```

### 2. Open the repo in your AI tool

Use Claude Code, Codex CLI, Gemini CLI, or another assistant that can read local repo files.

### 3. Start onboarding

```text
Computer, onboard me into this OS.
```

The assistant should ask about your:

* Product role
* Current goals
* Active projects
* Stakeholders
* Work style
* Operating cadence
* Privacy boundaries

### 4. Start your first working session

```text
Computer, what should I focus on today?
```

---

## First 7 days

| Day   | What to do                                 |
| ----- | ------------------------------------------ |
| Day 1 | Run onboarding and set up your goals       |
| Day 2 | Add active tasks and current blockers      |
| Day 3 | Add one project brief                      |
| Day 4 | Add key stakeholder notes                  |
| Day 5 | Use it for meeting prep or a weekly update |
| Day 6 | Draft or review one PRD                    |
| Day 7 | Run a weekly review and improve the OS     |

The goal is not to make it perfect.
The goal is to make it useful within one week.

---

## Example workflow

```text
You have a new AI feature idea
   ↓
Add project context in Projects/
   ↓
Use Templates/prd-ai-feature.md
   ↓
Ask the OS to draft the PRD
   ↓
Run PRD readiness review
   ↓
Run eval / failure-mode review
   ↓
Prepare stakeholder update
   ↓
Decide next action
```

---

## Sample artifacts

The `Examples/` folder can be used to show what good output looks like.

Suggested examples:

```text
Examples/
├── sample-ai-feature-prd.md
├── sample-eval-review.md
└── sample-launch-gate.md
```

These examples help new users understand how to work with the OS.

---

## Privacy note

This repo is meant to be forked or copied.

Keep personal context, company-sensitive details, customer information, credentials, and private documents out of the public repo.

Use a private fork or local copy for real work.

---

## Design principles

* Keep the system lightweight
* Store context in simple markdown files
* Make workflows repeatable
* Make quality checks explicit
* Separate drafting from reviewing
* Keep private context private
* Let the PM stay in control

---

## One-liner

A practical AI Product Management OS for turning messy PM work into clearer workflows, stronger artifacts, better reviews, and more reliable execution.
