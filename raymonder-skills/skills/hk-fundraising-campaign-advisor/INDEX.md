# HK Fundraising Campaign Advisor — 工作目錄索引

最後更新：2026-05-27

## 6 大類

### 01 過程資料（research/）
5 個 subagent 並行調研產出，作為 evidence-base 的原始檔案。

- `research/01_網絡籌款證據基.md` — Athey 2024 / Karlan-List / Gneezy / Castillo / M+R 2026
- `research/02_月捐證據基.md` — Classy 2023 / Blackbaud FY24 / FEP Q4 2024 / Neon One 2026 / Burk
- `research/03_賣旗e-Flag證據基.md` — SWD 規則 / 12 週時間線 / 8 個公開案例 / 動員 4 場景
- `research/04_HK本地context.md` — DataReportal 2025 / HKMA FPS / CAF 2025 / PDPO / 10,699 慈善機構
- `research/05_華人地區案例.md` — 99 公益日 / 聯勸暴走 / 台灣世展 / giving.sg

### 02 Skill 核心（根目錄 + references/）
給 Claude 跑 skill 時加載。1 個 skill + 4 個 mode。

- ⭐ `SKILL.md` — 入口檔，定義 4 mode 與 workflow
- `references/intake.md` — 4 mode 共用的機構背景收集
- `references/campaign-playbook.md` — 網絡籌款 7 步法
- `references/monthly-giving-playbook.md` — 月捐 5 階段（新增）
- `references/e-flag-playbook.md` — 卖旗 / e-Flag 12 週（新增）
- `references/scorecard.md` — Review checklist + 100 分 scorecard
- `references/evidence-base.md` — 共用證據庫（已更新到 2026）
- `references/output-template.md` — 4 mode 的標準輸出模板
- `references/full-research-report.md` — 舊版長篇研究報告（保留作 deep reference）

### 03 交付物（deliverables/）
給 NGO 機構看的最終 PDF。

- ⭐ `deliverables/HK在線公益籌款方法論_v1.pdf` — **最終交付，56 頁繁體中文**
- `deliverables/source/main.html` — PDF 源 HTML + CSS

### 04 歷史版本（歷史版本/）
舊版檔案，保留作版本對比。

- `歷史版本/SKILL_v1_20260525.md`
- `歷史版本/campaign-playbook.md` etc.

### 05 程式（scripts/）
- `scripts/score_campaign.py` — 100 分加權評分計算

### 06 配置（agents/）
- `agents/openai.yaml` — OpenAI agent 配置（沿用）

---

## PDF 內容結構（56 頁）

| 範圍 | 頁 | 內容 |
|---|---|---|
| 封面 | 1 | 三 pillar 主視覺 |
| 致信 | 2 | 給 NGO 籌款夥伴的開場 |
| 目錄 | 3-4 | 6 個 Part 導航 |
| Part 1 | 5-12 | HK 在線公益籌款的全局判斷 |
| Part 2 | 13-26 | 網絡籌款 7 步法 |
| Part 3 | 27-36 | 月捐 5 階段 |
| Part 4 | 37-44 | 卖旗 / e-Flag 12 週 |
| Part 5 | 45-47 | 三場景聯動 + 一年運營節奏 |
| Part 6 | 48-52 | Review Checklist + Scorecard |
| 附錄 | 53-56 | 52 條參考文獻 |

---

## 校驗清單（已通過）

- ✓ 56 頁，符合 50-60 目標
- ✓ 7 個 Part divider 完整（5 Part + Appendix + 0 cover）
- ✓ 全文無「銷售」「sales」「pitch」「客戶填完」等違反 NGO-facing 定位的字眼
- ✓ Castillo 8 個精確數字（4.4 / 12.6 / 16.9 / 14 / 8.4 / 26.3 / 11.6 / 1.89）全部出現
- ✓ Karlan-List 1.22 risk ratio、Gneezy「翻倍」、Athey n>400k 均到位
- ✓ HK 本地數據 2025/2026 最新（FPS 17M+、賣旗 56 日、慈善 10,699 間）
- ✓ 繁體中文，無簡體殘留
- ✓ 7 處 divider + 25 個 H2 章節
- ✓ 52 條參考文獻分 4 類（學術 / 行業 / HK 政府 / 華人地區）
