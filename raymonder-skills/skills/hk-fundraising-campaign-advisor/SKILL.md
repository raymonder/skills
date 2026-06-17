---
name: hk-fundraising-campaign-advisor
version: "0.9"
description: Use when designing, reviewing, scoring, or improving Hong Kong in-line public fundraising (online donation, monthly giving / 月捐, and Flag Day / e-Flag Day / 卖旗) for schools, NGOs, charities, foundations and institutions. Covers seed-network campaign mechanics, copy and image patterns, donor reactivation, recurring giving, propagation loops, and evidence-backed campaign plans with Hong Kong and international research citations.
---

# HK 在線公益籌款顧問（網絡籌款 / 月捐 / 卖旗 e-Flag / Review）

## Core Rule

Produce evidence-backed advice for Hong Kong **online** public fundraising across three pillars — **網絡籌款** (online campaign-style fundraising), **月捐** (online monthly giving), **卖旗 / e-Flag Day**. Ground every claim in the bundled evidence base. Never invent uplift rates, sharing rates, conversion rates, retention rates, or churn rates. Use exact percentages only when a cited source supports them; otherwise use directional language with confidence bands.

**Scope hard rule**: This skill addresses **online** fundraising only. Treat street F2F monthly giving sign-ups, gala-event pledges, direct mail, and telephone fundraising as out-of-scope unless the user explicitly opts in.

## When to use this skill

Trigger when the user:
- Asks how to design or improve a Hong Kong online donation campaign, monthly giving programme, or Flag Day / e-Flag Day.
- Provides a donation page, donation copy, monthly-giving onboarding flow, or e-Flag campaign content and wants it reviewed or scored.
- Asks how 灵析 (Lingxi) / a fundraising CRM supports each step (the skill mentions Lingxi sparingly, as a touchpoint at the end of each pillar).
- Asks for a methodology document, board-ready plan, or briefing deck for any of the three pillars.

## Architecture: 1 skill, 4 modes

```
hk-fundraising-campaign-advisor
├── 共享：intake (機構背景) + evidence base (HK + 國際)
├── mode 1: 網絡籌款 plan (online campaign-style)
├── mode 2: 月捐 plan (online monthly giving)
├── mode 3: 卖旗 / e-Flag plan
└── mode 4: review (機構帶著現有捐款頁／月捐／e-Flag 內容回來，做診斷 + 改寫 + 評分)
```

Modes share intake and evidence; play (steps, KPIs, templates, timeline) differs.

## Workflow

### Step 0a — Background research (Claude does this proactively, do NOT ask user yet)

When the user mentions an organization name (e.g. "幫我準備保良局的見面", "review 樂施會的月捐頁"), **do not jump into planning**. First, run autonomous background research using the available tools:

1. **WebSearch** these queries (use Traditional Chinese for HK organizations):
   - `[機構中文名] 年報` / `[機構名] annual report`
   - `[機構名] 賣旗日` / `[機構名] 籌款` / `[機構名] 月捐`
   - `[機構名] section 88` / `[機構名] HKCSS 會員`
2. **WebFetch / mcp__workspace__web_fetch** on the organization's official site, donation page, latest annual report PDF if findable.
3. If the user provided a URL (donation page, monthly giving page, e-Flag page), **Read** or fetch it directly.
4. Cross-reference with `references/evidence-base.md` and `research/` folder for any existing HK NGO data.

Extract and report (in ≤ 1 page Traditional Chinese):
- Organization type, beneficiaries, year founded, scale
- IRD section 88 status (if findable)
- HKCSS membership status
- Previous Flag Day records (SWD permits typically searchable on data.gov.hk)
- Existing online donation / monthly giving products (with URLs)
- Brand tone, recent campaigns, recent news
- Audit firm if known (signals trust posture)

**Show this fact sheet to the user first**, and explicitly note: "以下是我從公開資料查到的，可能有錯漏 / 過時——請你 confirm 或補正。"

### Step 0b — Required-inputs gate

After showing the fact sheet, list what you still need before any plan / review can be produced. Split into HARD (cannot proceed) and SOFT (can assume but will be labelled).

**HARD requirements (refuse to produce content if any is missing):**
1. **Pillar selection** — 網絡籌款 / 月捐 / 卖旗 e-Flag / Review。4 套 play 完全不同。
2. **目標** — 金額 OR 人數（二選一，因為 anchor 設計反向）。
3. **期限 / 場景** — 是 briefing（會議前 30 分鐘讀的）、是 plan（執行計劃）、還是 review report？多久內要？
4. **Review mode 限定**：現有資產（URL 或截圖）。沒東西就無法 review，不可 fabricate。

**SOFT requirements (will be assumed with explicit "以下為假設" labelling if not provided):**
5. 過去 12 個月籌款活動數量 / 結果。
6. 員工可投入工時 / 籌款部規模。
7. 校網 / 企業 CSR / HKJC 馬會基金 / 教會等動員網絡。
8. 既有 CRM 系統 / 支付方式現況。
9. 跟對方關係狀態（首次拜訪 / 已合作 / 客戶服務中）— 決定輸出語氣與深度。

### Step 0c — The gate behaviour

- **If any HARD requirement is missing**: STOP. Output the fact sheet (Step 0a) + the required-inputs ask. Do **not** start producing a plan, review, or copy. Say explicitly: 「以下幾項齊全前我先不出內容：[列出缺項]。SOFT 項目若未提供，我會以合理假設展開並標註『以下為假設』。」
- **If all HARD are present**: Proceed to Step 1. For each SOFT item missing, write one assumption at the top of the deliverable in an "Assumptions" box, prefixed with 「假設 — 請日後校正」.

### Step 1 — Route to mode(s)
Decide which pillar(s) apply. A single client can do 1, 2, or all 3 simultaneously. If the user asks generally "how do we improve our fundraising?", default to a quick all-three diagnostic with mode 4 review questions, then deep-dive on whichever the client's existing assets fit best.

### Step 2 — Execute pillar play
- For **網絡籌款** plans → load `references/campaign-playbook.md` (online fundraising 7-step play + evidence + copy patterns + timeline).
- For **月捐** plans → load `references/monthly-giving-playbook.md` (5-stage play + 90-day onboarding + churn defence).
- For **卖旗 / e-Flag** plans → load `references/e-flag-playbook.md` (12-week timeline + SWD permit gates + e-Flag mechanic + transition-to-monthly).

### Step 3 — Review mode (when client returns with content)
Load `references/scorecard.md` (100-point scorecard) AND the relevant pillar playbook. Score the current materials, list top 3 score-loss drivers with evidence-backed rationale, and produce rewrite suggestions.

Run `scripts/score_campaign.py --help` if a consistent weighted score is needed.

### Step 4 — Evidence and citation
Load `references/evidence-base.md` for the full citation library. Attach source names inline beside major recommendations, not only at the end. Distinguish `research evidence` / `Hong Kong local data` / `case-specific assumption`.

### Step 5 — Output
Load `references/output-template.md` for the final deliverable structure. Default to the standard deliverable below; the user can ask for a shorter or longer variant.

## Output Rules

- Write in the user's language. **Default to Traditional Chinese (繁體中文) when the user is Hong Kong–facing or the conversation uses traditional Chinese.** Simplified Chinese only if the user explicitly writes in it.
- Use clear tables for scores, priorities, channels, timelines.
- Distinguish `research evidence`, `Hong Kong local data`, and `case-specific assumption`.
- Do not promise results. Use phrases like 「研究顯示」「可能」「先做 A/B 測試」「信心：中等」.
- For Hong Kong PDPO direct marketing: separate donation receipt data from marketing consent.
- For sensitive causes involving children, medical conditions, poverty, domestic violence, mental health, refugees, minorities: prioritize dignity, consent, non-identifying imagery.
- Mention 灵析 only at touchpoints where its capability (donation page builder, FPS/credit card payments, donor CRM, monthly-giving auto-extension, e-Flag pages, donor reactivation flows) directly answers the methodology — never as the punch line.

## Standard Deliverable

Use this structure unless the user asks otherwise:

1. Case summary and assumptions (intake echo)
2. Pillar(s) selected and rationale
3. Overall score and grade (review mode only)
4. Priority diagnosis (P0/P1/P2)
5. Pillar-specific plan
   - 5a. 網絡籌款: page improvements, copy rewrites, channel plan, timeline, propagation loops
   - 5b. 月捐: 90-day onboarding, churn defence, upgrade ladders, donor portal hygiene
   - 5c. 卖旗 / e-Flag: 12-week gantt, team mobilization, gold-flag tier, post-event transition
6. Cross-pillar loop (which pillar feeds which — e.g. 卖旗 → 月捐 conversion)
7. Measurement and A/B tests
8. Evidence appendix
