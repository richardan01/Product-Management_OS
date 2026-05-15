# PM OS Best Practices — Research Synthesis

**Date:** 2026-05-15
**Purpose:** Comprehensive research on best practices for building and maintaining a Product Management Operating System
**Status:** Complete

---

## 1. What Is a PM OS?

A PM OS is the combination of tools, templates, cadences, decision frameworks, and context files that let a PM manage their work systematically rather than reactively. It answers four recurring questions:

- **Task layer:** What should I be working on right now?
- **Goal layer:** What have I committed to deliver?
- **Knowledge layer:** What do I know and what decisions have I made?
- **Stakeholder layer:** Who are the humans I need to keep aligned?

**Why PMs need one:** PM work has no natural container. Unlike engineering (code in a repo) or design (in Figma), PM work sprawls across tools, meetings, and conversations. Without a personal system, context lives in the PM's head — and evaporates.

**2025-2026 shift:** Many PMs now build their OS inside AI-native environments (Claude Code, Cursor), where a master context file replaces a static wiki and AI skills automate overhead tasks. — Source: [news.aakashg.com/p/pm-os](https://www.news.aakashg.com/p/pm-os)

---

## 2. Core Components — Six Layers

| Layer | Contents | Common home |
|---|---|---|
| **Task management** | Sprint tasks, weekly priorities, someday/maybe | Notion, Linear, calendar blocking |
| **Goal tracking** | OKRs, 30-60-90 plan, personal metrics | GOALS.md or Notion database |
| **Knowledge base** | Meeting notes, research, decisions, frameworks | Obsidian vault or Notion pages |
| **Stakeholder map** | Influence grid, communication prefs, relationship log | Notion CRM or dedicated tracker |
| **Decision log** | Context, alternatives, rationale, expected outcome, actual outcome | Running markdown doc |
| **Artifact library** | PRD, one-pager, launch brief, retro, strategy doc | Templates folder |

**AI-era addition — master context file:** In modern setups, the PM maintains a `CLAUDE.md` or equivalent that tells the AI about the company, team, stakeholders, and current priorities. This replaces a static onboarding doc and becomes the working memory of the system.

---

## 3. Frameworks Applied to PM Work

### LNO (Shreyas Doshi — highest signal for daily prioritization)
Categorize every PM task as **Leverage**, **Neutral**, or **Overhead**:
- **L tasks:** High-multiplier work (strategy, key decisions, stakeholder alignment). Pursue perfection.
- **N tasks:** Normal 1:1 output. Aim for B-.
- **O tasks:** Necessary overhead. Actively try to do a bad job — your floor is still acceptable.

> "There are actually very few L tasks on a to-do list." — Doshi

Key insight: most PM calendars are dominated by N and O work. Identifying L tasks is the core skill. — Source: [coda.io/@shreyas/lno-framework](https://coda.io/@shreyas/lno-framework)

### PARA (Tiago Forte)
Organize everything as **Projects, Areas, Resources, Archives**. Maps cleanly to PM work:
- Projects = active workstreams
- Areas = ongoing responsibilities (strategy, stakeholders)
- Resources = research and frameworks
- Archives = completed sprints

PARA answers "where does this live?" — it is an organization system, not a task system.

### Building a Second Brain (Tiago Forte — BASB)
Adds a **CODE** workflow on top of PARA: Capture → Organize → Distill → Express. Especially useful for synthesizing user research, competitive intel, and strategy reading into reusable notes. — Source: [buildingasecondbrain.com](https://www.buildingasecondbrain.com/)

### Zettelkasten
Atomic note-taking with bidirectional links — each note is one idea, linked to related ideas. More useful for PMs doing deep research or strategy writing than for task management. Obsidian is the dominant tool. Best used alongside PARA (PARA for artifacts, Zettelkasten for thinking).

### GTD (David Allen)
Answers "what should I do next?" — an action system, not a knowledge system.
- Two-minute rule universally cited as the highest-signal habit
- "Waiting For" list for delegated items widely adopted
- Source: [lennysnewsletter.com — time management](https://www.lennysnewsletter.com/p/time-management-techniques-that-actually)

### Karpathy LLM Wiki Pattern (2025)
Obsidian vault where an AI agent continuously converts raw saved content into an interconnected markdown knowledge base. "A system that gets smarter the more you use it." Being adopted by technical and AI PMs as their knowledge layer. — Source: [mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code](https://www.mindstudio.ai/blog/andrej-karpathy-llm-wiki-knowledge-base-claude-code)

---

## 4. Goal and OKR Management

### 30-60-90 Day Plan structure
| Period | Focus |
|---|---|
| Days 1-30 | Listen, learn, map — understand product, team, stakeholders, metrics |
| Days 31-60 | Start contributing — quick wins, validate assumptions, ship something small |
| Days 61-90 | Drive outcomes — own a roadmap decision, align on OKRs, show strategic thinking |

Success metrics: quantitative (completion rates, metrics moved) + qualitative (stakeholder feedback).

### OKR alignment
- 3-5 Objectives that connect individual success to company priorities
- Key Results: quarterly and quantifiable
- Common mistake: using OKRs as a task list instead of a measurement framework

### Personal metrics worth tracking
- Feature adoption rate of shipped work
- Decision speed (problem identified → decision logged)
- Leverage task ratio (% of week spent on L vs. O tasks)
- Learning velocity (frameworks internalized per quarter)

---

## 5. Operating Cadence

| Cadence | Duration | Purpose |
|---|---|---|
| Daily self-standup | 10-15 min | 1-3 priorities, inbox to zero, check blockers |
| Weekly review | 45-60 min | OKR progress, decision log, notes → knowledge base, stakeholder updates |
| Biweekly 1:1s | 25-30 min | Relationship maintenance, surface blockers, alignment |
| Monthly retro | 30-45 min | What shipped? Decisions made? What to change? |
| Quarterly planning | 90-120 min | Reset OKRs, update 30-60-90, calibrate roadmap |

**Lenny Rachitsky's personal daily system:**
- Calendar-based task management (tasks become calendar events)
- 1-3 daily priorities identified each morning (Matt Mochary's "Top Goal" approach)
- Protected deep work blocks (2-3 per week, from Cal Newport)
- No meetings after 3pm
- VA delegation for overhead tasks

**Reforge's key distinction:** An **operating cadence** (scheduled touchpoints) vs. an **operating rhythm** (momentum between touchpoints). Both are required. — Source: [reforge.com/blog/operating-cadence](https://www.reforge.com/blog/operating-cadence)

---

## 6. Stakeholder and Relationship Management

**Influence grid model:** Map stakeholders on influence × interest:
- High influence / high interest → manage closely
- High influence / low interest → keep satisfied
- Low influence / high interest → keep informed
- Low influence / low interest → monitor only

**CRM-style relationship log:**
- Log every meaningful stakeholder interaction
- Track: what was discussed, what they care about, what you committed to
- Review before every major presentation involving that stakeholder

**Pro principle:** Treat the stakeholder map like a sales team treats its CRM — regular updates with explicit next actions, not just contact info.

---

## 7. Decision Logging

**Why it matters:** Without a log, teams relitigate old choices, context is lost, and post-mortems become blame sessions.

**Best-practice fields for a decision log entry:**
1. Problem statement — business context and constraints
2. Options — at minimum default path and recommended path
3. Recommendation — PM's direction and rationale
4. Decision maker — explicitly named (not "the team")
5. Stakeholders consulted
6. Timeline — when the decision was needed
7. Tradeoffs — what is being sacrificed
8. Expected outcome — what success looks like and when to check
9. **Actual outcome** — updated later; never edit the original rationale

> "Context is the most important field because it's the first thing people forget." — Amy Mitchell

**SPADE framework (Gokul Rajaram — Square):**
- **S**etting — context
- **P**eople — who decides, who is consulted, who is informed
- **A**lternatives — at least 3 options
- **D**ecide — decision maker chooses after soliciting input
- **E**xplain — written rationale shared broadly

Free Coda template: [coda.io/@gokulrajaram/gokuls-spade-toolkit](https://coda.io/@gokulrajaram/gokuls-spade-toolkit)

---

## 8. Templates and Artifacts

### PRD landscape
| Template | Origin | Best for |
|---|---|---|
| Lenny's 1-Pager | Lenny Rachitsky | Most projects — lightweight, fast |
| Kevin Yien PRD | Square | Scale; strong "Non-Goals" section |
| Working Backwards PR/FAQ | Amazon (Ian McAllister) | Major new product bets |
| Shape Up Pitch | Basecamp | Teams using Shape Up method |
| V2MOM | Salesforce (Marc Benioff) | Team and product strategy |
| SPADE | Square (Gokul Rajaram) | High-stakes decisions |

### Minimum standard artifact library
- PRD / 1-pager (problem-first, with non-goals)
- Product strategy one-pager (DHM model or equivalent)
- Launch brief (separate from PRD; tactical, time-bound)
- Retrospective template
- Decision log entry template
- Stakeholder map / influence grid
- OKR tracker
- 30-60-90 day plan
- Weekly update template

---

## 9. AI-Augmented PM OS

PMs are using AI in three distinct modes:

**Mode 1: Chat collaborator (Claude.ai, ChatGPT)**
- Thought partner for strategy docs, stakeholder messaging, tricky situations
- ~80% of PM AI use cases; no special setup required

**Mode 2: Agentic workflows (Claude Code, Cursor)**
- Multi-step autonomous execution: transcribe interviews → summarize → synthesize → draft PRD
- Local file access means the AI reads your vault, templates, and past decisions
- **Documented time savings:**
  - PRD drafting: 4-8 hours → 30 minutes (Aakash Gupta)
  - Interview synthesis: 2-3 hours → 15 minutes (Sachin Rekhi)
- **Specific skills practitioners have built:**
  - `/prioritize` — daily sweep of task board, surfaces stale tickets
  - `/pulse` — analytics briefing: usage metrics, anomaly flags, quality grades
  - Strategy critique skill — feeds PM frameworks, returns critique against best practices
  - Competitor pricing matrix — browser agent visits pricing pages in real-time
  - Data query skill — natural language → SQL → HTML report
  - Release notes from GitHub commits

**Key architecture principle:** Store all product context and documentation in local markdown files. Creates rich, portable, vendor-independent context. — Source: [sachinrekhi.com](https://www.sachinrekhi.com/p/claude-code-for-product-managers)

> "The conversation is the work" — consolidating 10+ tools into single Claude threads where thinking through product decisions directly generates implementation specs. — every.to

**Mode 3: Custom AI mini-apps (Claude Projects, Custom GPTs)**
- System prompt + reference materials = reusable assistant for a specific recurring problem

**Claude Code vs. chat tools:** Claude Code executes multi-step workflows autonomously, accesses databases, runs scripts, calls external APIs via MCP, and creates reusable skills. Qualitatively different from chat, not just faster.

---

## 10. Tools

| Tool | Strengths | Weaknesses | Price |
|---|---|---|---|
| **Notion** | Relational databases, stakeholder CRM, roadmap, PRD — all in one; large template library | Heavy; can become bloated | Free / $10 mo |
| **Obsidian** | Local markdown, bidirectional links, Zettelkasten, AI-native via plugins, Karpathy pattern | No native collaboration | Free / $4 mo sync |
| **Linear** | Best-in-class issue tracking, sprint management, cycle tracking | Not a knowledge base | Free / $8 user/mo |
| **Coda** | Powerful databases + formulas + docs; SPADE template lives here | Steeper learning curve | Free / $10 mo |
| **Logseq** | Open-source, local-first Roam alternative | Smaller ecosystem | Free |
| **Claude Code** | Agentic multi-step automation, local file access, skills, MCP integrations | Technical setup required | Usage-based |

**Tool selection principle:** The best PM OS uses the fewest tools necessary to cover all six layers. Every additional tool creates a seam where context gets lost. One "home base" tool (Notion or Obsidian) plus discipline to resist adding others.

---

## 11. Common Failure Modes

1. **Overengineering before using** — building a complex vault before any real work runs through it. The system becomes a hobby.
2. **Tool sprawl** — notes in Notion, tasks in Linear, decisions in Google Docs, stakeholder maps in a spreadsheet. Context is scattered.
3. **Building for the system, not the work** — spending Sunday reorganizing the vault instead of doing actual PM work.
4. **No update cadence** — templates created but never filled. Decision logs abandoned after two entries. A weekly review ritual is required to keep the system alive.
5. **Conflating roadmaps with plans** — treating a strategic roadmap as a tactical plan (or vice versa). Different artifacts, different audiences, different update cadences.
6. **No mechanism for closing loops** — decisions logged but never updated with actual outcomes. Knowledge accumulates but never compounds.
7. **Ignoring the stakeholder layer** — most PM systems focus on tasks and goals but omit relationship tracking. Stakeholder misalignment is the leading cause of PM failure.
8. **Using AI as a search engine** — treating Claude or ChatGPT as a smarter Google instead of building reusable skills and agentic workflows.

---

## 12. Notable Practitioners

| Practitioner | Key contribution | Link |
|---|---|---|
| **Shreyas Doshi** (Stripe, Twitter, Google) | LNO Framework; pre-mortems; three levels of product work | [coda.io/@shreyas/lno-framework](https://coda.io/@shreyas/lno-framework) |
| **Lenny Rachitsky** (Airbnb) | Most comprehensive public PM template library; daily system; 574K subscriber newsletter | [lennysnewsletter.com](https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37) |
| **Gibson Biddle** (Netflix, Chegg) | DHM model; GEM model; SMT framework for roadmap alignment | [askgib.substack.com](https://askgib.substack.com) |
| **Gokul Rajaram** (Square, DoorDash) | SPADE decision framework — most widely adopted structured decision template | [coda.io/@gokulrajaram/gokuls-spade-toolkit](https://coda.io/@gokulrajaram/gokuls-spade-toolkit) |
| **Tiago Forte** (Forte Labs) | PARA method; Building a Second Brain — foundational PKM frameworks | [buildingasecondbrain.com](https://www.buildingasecondbrain.com/) |
| **Aakash Gupta** (Product Growth) | AI-native PM OS kit — 41 commands, 7 reviewer sub-agents, CLAUDE.md architecture | [news.aakashg.com/p/pm-os](https://www.news.aakashg.com/p/pm-os) |
| **Sachin Rekhi** (LinkedIn) | Claude Code workflows for PMs — strategy critique, competitor pricing automation, interview synthesis pipeline | [sachinrekhi.com](https://www.sachinrekhi.com/p/claude-code-for-product-managers) |

---

## Key Recommendations

1. **Adopt LNO as a daily lens** — tag every task as L, N, or O before starting the day. 5 minutes. Forces prioritization at the category level.
2. **Implement a decision log immediately** — SPADE for high-stakes decisions; 5-field format (context, options, decision, tradeoffs, expected outcome) for routine ones. Update actual outcome at retros.
3. **Build a stakeholder map as a living document** — not a contact list, but a relationship log with last touchpoint, what they care about, and next action.
4. **Standardize on 1-3 daily priorities** — the highest-ROI cadence habit across all practitioners reviewed.
5. **Build one reusable AI skill per major recurring workflow** — start with the highest-frequency overhead task. Automate O-category work first.
6. **Keep the OS lean** — if a component hasn't been touched in 2 weeks, audit it.
7. **Run a monthly personal retrospective** — what did I ship? What decisions did I make? What did I learn? This closes the loop most systems leave open.

---

*Research completed 2026-05-15. Sources: Lenny's Newsletter, Shreyas Doshi / Coda, Sachin Rekhi, Aakash Gupta, every.to, Reforge, Tiago Forte / BASB, Gokul Rajaram / First Round Review, Amy Mitchell / Substack, Andrej Karpathy / Mindstudio, CPO Club, Product School, Ant Murphy.*
