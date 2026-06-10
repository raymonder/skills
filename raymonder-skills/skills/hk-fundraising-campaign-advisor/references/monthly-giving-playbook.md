# 月捐 Playbook（mode 2）

> 香港 NGO **在線**月捐方法論。5 階段 + 90 天 onboarding + churn 防禦 + 升級規則。
> 引用詳見 `evidence-base.md`。

## 為什麼月捐是 NGO 的「複利槓桿」

3 個非說不可的數字：
- **月捐 LTV ≈ 5.4–9× 一次性**（Classy 2023）；Blackbaud donorCentrics FY24：以月捐獲取的 donor 三年累計 $405 vs 一次性 $161。
- **月捐人年留存 78–90%**（FEP 2024 / Blackbaud FY24）；新一次性 donor 次年留存只有 **19.4%**（FEP Q4 2024）。
- **月捐平均壽命 7.5-8 年**（Neon One 2026），一次性 1.5-2 年。

「每 5 個一次性 donor 才換到 1 個月捐 donor 的價值」——這是月捐的全部商業邏輯。

---

## 5 階段架構

```
Stage 1 喚醒（Awareness）       → 為什麼需要月捐 / 月捐做什麼
Stage 2 承諾（Commitment）      → 在線開通流程設計
Stage 3 上線 90 天（Activation） → 黃金期 onboarding journey
Stage 4 年度續費（Year 1+）     → 防止「我已 commit 過」疲勞
Stage 5 危機與挽留（Churn）     → 失敗付款 + 主動取消挽回
```

---

## Stage 1 — 喚醒：為什麼是月捐

**做什麼**：
- 月捐 ask 必須有 **獨立的著陸頁**（非單純加在一次性捐款頁底部 toggle）。
- 解釋月捐**做的事**，不是月捐**是什麼**：「你每月 HK$200 = 1 個小孩一週午餐」。
- 用 **日感金額表述**：「每天 HK$5」優於「每月 HK$150」。
- 列舉 **3 個具體 impact / 1 年**（基於該月捐金額）。

**證據**：
- 家扶基金會：月捐入口「每天存 10 元、月捐 300」明確錨點。
- Wang, Wang & Jiang 2023 (Journal of Marketing)：framing 為「禮物」（gift）而非「donation」提升 intention 與金額。
- Hsee et al. (Journal of Marketing Research)：對比 indulgent 商品（精品咖啡、酒）顯著提升捐款金額。

**不要做**：
- 把月捐當「一次性的捐多次版本」推銷——失去月捐獨有的承諾感。
- 用抽象口號（「成為長期夥伴」）取代具體 impact。

---

## Stage 2 — 承諾：開通流程

**做什麼**：
- 開通流程目標：**< 90 秒完成**。
- **金額 ladder：5 檔，default 預選第 2 或第 3**。HK sweet spot：**HK$150 / 200 / 300 / 500 / 1000**。
- 支付方式優先級：
  1. **信用卡（Visa / Master）** — tokenization 可自動續扣。
  2. **AlipayHK / WeChat Pay HK 自動扣賬** — 已支持 recurring。
  3. **FPS / 轉數快** — 2026/5 仍是 push-based，月捐需 NGO 自建提醒重發機制（或用 PSP eDDA 接 Direct Debit 服務）。
- **3-step 表單**：金額 → 個人資料（姓名 + Email + 電話） → 支付。
- **預設 PICS（PDPO 直銷同意）勾選**：分兩個 checkbox（收據用途 + 推廣用途），不可合併。
- **承諾 framing**：「我承諾每月 HK$XXX，未來我可隨時調整或取消」——降低承諾門檻。

**證據**：
- HKMA：FPS 註冊 17M+（2025 中），日均 1.98M 筆（2025/3，+32.9%）；HKPC 2023：B2C 接受 FPS 70%、信用卡 67%、Mobile QR 61%。
- M+R 2024：金額 ladder 不超過 5 個選項。
- NextAfter：**default-to-monthly 弱 default 預選** 提升 +348%（須清楚標示可改回一次性）。
- PCPD：違反 PDPO 直銷條款最高 HK$500k + 3 年監禁；提供第三方則 HK$1M + 5 年。

**不要做**：
- 一鍵勾選同時授權直銷 + 第三方分享 + 收據（PDPO 高風險）。
- 用「打勾預設月捐」但隱藏取消方法（DOJ guidance dark pattern 範圍）。

---

## Stage 3 — 上線 90 天：onboarding journey

**這是月捐生死期。** M+R 2024 數據：**新月捐者 10% 在前 2 個月內取消**；12 個月後剩 71%；直接 acquisition 月捐 13 個月留存只有 **47%**（Blackbaud FY24）。

### 90 天 sequence

| 天數 | 動作 | 目的 | 證據 |
|---|---|---|---|
| **D0** | 自動 email：收據（IRD 編號）+ welcome 信（CEO / 項目經理真名）+ 60 秒迎新短片 | 第一印象 / 真實感 | NextAfter：真人姓名 +920% |
| **D1** | WhatsApp broadcast 加入「月捐家人群」（或機構頻道） | 社群歸屬 | 行為公益遊戲化（騰訊小紅花模型） |
| **D3** | Email：第一段具體 impact 故事（不要 ask） | 確認「我捐的有用」 | Burk |
| **D7** | 真人 thank-you 電話 / WhatsApp 語音 / Personalized video | 留存提升 33%→58% | Burk; NextAfter |
| **D14** | Email：你的月捐配對的具體 cause / project（如能個人化）| 承諾感強化 | World Vision HK donor portal mechanic |
| **D30** | 第一份正式 impact report（mini，2 頁 PDF） | 兌現承諾 | Althoff 5pp retention lift |
| **D45** | 「你有什麼想知道的？」邀請反饋（不 ask 升級） | donor-centered 文化 | Donor-Centered Fundraising |
| **D60** | Story：另一位月捐人為何加入 | 社會認同 | CAF 2025 social reasons |
| **D75** | Email：本季度大型計劃預告 + 邀請參與線下活動 | 社群活化 | — |
| **D90** | Mini impact report (Q1) + 升級邀請（first ask） | 黃金期內升級 | Classy 2023: 29% 升級 |

**證據總結**：
- M+R 2024：月捐前 2 個月 10% 取消、7 個月後剩 81%、12 個月後剩 71%。
- Blackbaud FY24：直接 acquisition 月捐 13 個月留存 47%。
- Burk：48 小時內真人電話 +39% 下次金額；90 天內 ≥1 通電話留存 33%→58%。
- NextAfter：90 天 offer-focused welcome series +920% 下游轉化。

**不要做**：
- D0 自動 email 用機構地址（Donations@xxx.org.hk）作 sender——必須真人姓名。
- 90 天內 ask 任何升級或額外捐款（只可在 D90+ ask）。
- 把 onboarding 完全自動化（D7 真人接觸不可省）。

---

## Stage 4 — 年度續費與升級

**做什麼**：
- **每季度 1 份 impact report**（紙本 / PDF / 影片三選一，先紙本給金額前 20%）。
- **生日 / 紀念日 / 機構週年**個人化問候（不 ask）。
- **年度大型 impact 報告**（年報濃縮版，3-5 頁）+ 升級 ask（漸進式：「+ HK$50 / 月」）。
- **里程碑慶祝**（捐滿 1 年、3 年、5 年）：勳章 / 紀念紀念品 / 名字公告。

**證據**：
- 台灣家扶 / 世展：「定期寫信 / 兒童回信」是月捐 retention 最強槓桿；NPOst 採訪結論：「**收到認養兒童來信」是維持月捐動力的第一變量，「機構負面新聞」是第一流失變量**。
- 騰訊小紅花成長體系（Lv1-Lv8）：行為公益遊戲化提升 retention。

**不要做**：
- 全年只在年度大會 ask 升級——錯失季度小升級機會。
- 升級 ask 直接跳 2× 倍（漸進 +25-50% 才合理）。

---

## Stage 5 — 危機與挽留：churn 防禦

**月捐流失分兩類**：
- **Involuntary churn（非自願）**：信用卡到期 / 餘額不足 / 卡片更換——佔流失 **15-30%**。
- **Voluntary churn（自願）**：donor 主動取消——剩下的 70-85%。

### Involuntary 防禦（純技術）

| 動作 | 目的 | 證據 |
|---|---|---|
| 接 **Visa / Mastercard Account Updater** | 自動同步新卡資料 | CharityEngine：降低 20-30% 失敗 |
| **Smart retry logic**：D3 / D7 / D14 三輪 | 救回時間性失敗 | 業界 best practice |
| Dunning email sequence：D0 system / D3 真人 email / D7 WhatsApp/電話 / D14 改用 FPS | 真人接觸救回 | DonorVoice：真人 50%+ vs 自動 10-15% |

**HK 特殊性**：信用卡到期週期 3-5 年，5 年月捐 cohort 必經歷一次續卡。沒接 Account Updater + retry = **每年丟 15%+ 純技術原因**。

### Voluntary 防禦

- **主動取消 flow 設計**：取消按鈕後跳「降低金額」「暫停 3 個月」「轉一次性」三選項，最後才確認取消。
- **流失原因問卷**：必填 1 題（5 選項）+ 選填留言；統計提供未來改進。
- **取消後 30 天 reactivation**：發 1 封「我們繼續服務」impact email，**不 ask**（純維繫關係）。
- **取消後 6 個月 reactivation**：發新 ask（新故事 / 新項目）。

**證據**：
- 聯合勸募 2025/1-10：公開「近 4,000 筆停捐、總額近 1,300 萬」——主動披露 churn 是信任資產。

---

## 一頁 KPI 對照表

| 指標 | 健康值 | 來源 |
|---|---|---|
| 月捐開通流程完成時間 | < 90 秒 | UX best practice |
| Default-to-monthly 預選 conversion lift | +200%-348% | NextAfter |
| 月捐 13 個月留存 | 70%+（目標）vs 47%（行業均值） | Blackbaud FY24 |
| 90 天真人電話完成率 | 100%（金額前 20%）+ 50%（中間 60%） | Burk |
| Involuntary churn | < 10% / 年 | Account Updater + retry |
| Voluntary churn | 15-25% / 年 | M+R 2024 baseline |
| 一次性轉月捐 D+30 升級率 | 5-10% | Classy 2023 |
| 月捐升級 ask 接受率 | 20-30% | 進階目標 |

---

## 灵析在月捐的工具支持

- Stage 2：月捐獨立著陸頁 + 5 檔金額 + default-to-monthly + 3-step 表單 + PDPO 雙 checkbox 模板。
- Stage 2 支付：信用卡 tokenization + AlipayHK / WeChat Pay HK recurring + FPS 月捐提醒方案。
- Stage 3：90 天 onboarding sequence 模板（D0/D3/D7 自動觸發 + D7 真人 task 派發）。
- Stage 3 內容：donor portal（受惠者最新進展、寫信、視頻），對標 World Vision HK 的 My WV portal。
- Stage 4：季度 impact report 自動分組推送 + 里程碑勳章。
- Stage 5：Account Updater 對接 + smart retry + 主動取消 flow + 流失原因問卷模板。
