---
name: weekly-ai-and-me-reflection
version: "0.9"
description: Use when creating a recurring or on-demand AI collaboration reflection report from recent chat, agent, or coding-session transcripts, especially when the user wants weekly patterns, feedback, rework analysis, improvement actions, and a static dashboard.
---

# Weekly AI and Me Reflection

Generate an evidence-based collaboration reflection report from recent AI interaction transcripts, then update a static dashboard. The report is about how the human and AI collaborated, not a general life diary.

## Core Principle

Evidence first. Do not invent collaboration patterns, praise, criticism, adoption rates, rework counts, or correction events. Every negative observation must point to a real correction, rejection, rework, repeated clarification, or explicit user signal in the available transcripts.

## Required Setup

Before generating a report, determine:

- **Output directory**: ask the user if not specified. Default to `./ai-and-me` in the current workspace.
- **Date window**: default to the last 7 calendar days ending at the current local date/time.
- **Human label**: default to `Human`; use a provided name only if the user explicitly asks.
- **AI label**: default to `AI assistant`; use a provided agent name only if the user explicitly asks.
- **Transcript source**: use available session/transcript tools when present. If no transcript tool exists, ask the user to provide transcript files or a source path.

Do not hard-code personal names, emails, usernames, private paths, tenant names, or local machine paths into the skill or generated setup instructions.

## Output Structure

Create or update these files under the output directory:

```text
ai-and-me/
├── decisions.md          # Optional. User-maintained stable decisions and "do not re-raise" items.
├── index.html            # Static dashboard, rewritten each run.
└── weekly/
    └── YYYY-MM-DD-report.md
```

`YYYY-MM-DD` is the report end date. Create `weekly/` if it does not exist. Do not write outside the chosen output directory.

## Workflow

### 1. Load Available Transcript Tools

Use local or MCP transcript/session tools when available. Tool names vary by environment, so discover first instead of assuming fixed names.

If transcript tools are unavailable:

1. Ask the user for transcript files, exported logs, or a directory.
2. Continue only with the data provided.
3. Mark the report as based on user-provided transcript data.

### 2. Collect This Week's Interactions

Gather sessions active within the date window. Include chat, coding-agent, and coworking sessions when the source can provide them.

For each session:

- Read transcript content.
- Filter messages by timestamp so long-running sessions do not leak older weeks into this report.
- Preserve enough context to understand the task arc, not only the tail.
- For long transcripts, sample the beginning, end, and correction-heavy middle segments.

Scan for correction/rework signals such as:

```text
wrong / not that / redo / rework / start over / this is not what I meant
不对 / 不是这个意思 / 重新做 / 回炉 / 返工 / 改一下 / 跑偏了
```

Do not rely only on exact strings. Use semantic grouping after finding candidate events.

### 3. Track Data Quality

Keep a simple source ledger:

- sessions found
- sessions read
- sessions failed
- messages included after date filtering
- transcript source type

If a meaningful share of transcripts cannot be read, say the report is based on incomplete data. Do not present a complete-looking report from partial evidence.

If no interactions exist in the date window, write a short "no active conversations this week" report and still update the dashboard.

### 4. Respect Decisions

If `decisions.md` exists, read it before analysis. Treat it as a "do not re-litigate" list:

- Items marked as settled should not appear again as criticisms.
- Stable preferences should shape recommendations.
- If an item contradicts transcript evidence, mention the tension neutrally rather than overriding the decision.

If `decisions.md` is missing, continue without error.

### 5. Analyze Across Sessions

Write sections in this order:

1. **This Week's Work**: what the human used AI for, scoped as "visible through AI interactions," not as a claim about their whole week.
2. **Human Collaboration Style**: prompt style, preferred outputs, decision habits, feedback patterns.
3. **Human Communication: Helpful and Harder Patterns**: neutral observations for better collaboration; exclude settled decisions.
4. **AI Self-Reflection**: what worked and what failed. Every "failed" item needs a concrete correction or rework event.
5. **Next Improvements**: specific actions for both sides.
6. **Compared With Last Week**: read the most recent previous report in `weekly/` if present.

## Report Template

Use this Markdown shape:

````markdown
# AI Collaboration Report · {start_date} – {end_date}

> Generated at {local_datetime}
> Data quality: {complete | partial | user-provided | no active conversations}

## 0. Weekly Numbers

| Metric | This week | Last week | Trend |
|---|---:|---:|---|
| Active sessions | n | n/a | — |
| Main themes | n | n/a | — |
| Accepted deliverables | x/y | n/a | — |
| Rework events | n | n/a | — |
| Correction events | n | n/a | — |
| Recurring issues | item + streak | — | — |

Counting notes:
- Rework means a delivered result was requested again or substantially redone.
- Correction means a specific output was rejected, corrected, or redirected during the task.
- Accepted deliverables means no later correction was visible in the available transcript window.
- These are heuristic collaboration signals; trend matters more than absolute precision.

### 0.1 Prompt / Process Suggestions
- Promote:
- Retire:

## A. This Week's Work
...

## B. Human Collaboration Style
...

## C. Human Communication: Helpful and Harder Patterns
**Helpful**
- ...

**Harder**
- ...

## D. AI Self-Reflection
**Worked well**
- ...

**Needs improvement**
- ...

## E. Next Improvements
**Human can try**
- ...

**AI should adjust**
- ...

## F. Compared With Last Week
...

<!-- Machine-readable block for dashboard aggregation. Do not delete. -->
```yaml
week: YYYY-MM-DD
date_range:
  start: YYYY-MM-DD
  end: YYYY-MM-DD
sessions:
  total: n
  read: n
  failed: n
adopted_rate: 0.00
rework: n
corrections: n
recurring_issues:
  - id: normalized-issue-id
    streak: n
prompt_suggestions:
  promote: []
  retire: []
data_quality: complete
```
````

Do not add a tail section after the YAML block.

## Dashboard

Rewrite `index.html` every run. Do not append.

Dashboard requirements:

- Single static HTML file with embedded CSS.
- No external CDN, JavaScript framework, remote font, or tracking script.
- Light, readable layout.
- Header: `AI and me · Collaboration Reports`.
- Summary area 1: recurring issues from the machine-readable YAML blocks.
- Summary area 2: recent four-week trend for accepted rate, rework, and corrections.
- Main area: one card per weekly report, newest first.
- Each card includes date range, short extracted summary, top harder patterns, top AI improvement items, and a relative link to the Markdown report.

When extracting summaries, parse the generated Markdown files directly. Prefer simple section parsing over brittle global regexes.

## Writing Rules

- Match the user's requested language; default to the conversation language.
- Keep claims scoped to the available AI interaction transcripts.
- Be concrete and humane, not performative.
- Avoid vague criticism that cannot be traced to a session.
- Do not reveal private transcript snippets unless the user explicitly asked for quotes.
- Do not include names, emails, private paths, account IDs, tenant names, or organization-specific details unless the user explicitly wants them in the generated report.
- If there is too little data, say so plainly.

## Final Response

After writing files, respond with only:

- The report file path or link.
- The dashboard file path or link.
- A one-line data quality note.

Do not restate the report content in chat.
