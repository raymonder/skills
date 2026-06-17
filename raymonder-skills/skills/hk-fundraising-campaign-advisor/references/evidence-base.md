# Evidence Base（2026/05 最新版）

> 所有 4 個 mode 共用的引證庫。每條都標 source / data point / 應用 / 遷移風險。
> 詳版見 `research/` 子目錄 5 個調研文件。
> Citation 規則：HK 本地數據優先；其次國際學術；最後行業 benchmark。

## 引用使用規則

- `HK 本地數據`：強——可直接作 HK 渠道 / 支付 / 信任假設。
- `國際田野實驗`：機制與方向，標 transferability 風險。
- `平台 dataset / 報告`：在線捐贈行為趨勢，標 context 和日期。
- 不可編造本地轉化率。無本地數據時，建議測試 + 給 evidence-informed 假設。

---

## A. HK 數字 + 支付 + 設備（2024-2025 最新）

| 來源 | 數據 | Campaign 含義 |
|---|---|---|
| DataReportal Digital 2025 HK | 7.10M 互聯網用戶；**96.0% 滲透率**；6.15M 社交用戶（83.1%）；18+ 社交滲透 85.5% | Mobile-first 在線籌款已是主流。社交分享應作一級設計。 |
| Digital 2025 HK | Facebook 廣告觸達 4.55M；IG 3.70M；YouTube 6.15M；LinkedIn 3.80M | FB 社群 / 校友 / 家長；IG 視覺故事；LinkedIn CSR；YouTube 長 impact。 |
| C&SD THS Report No. 82（2025/6 發布）| 家庭家中互聯網 96.7%；智能手機 96.3%；**15+ 過去 12 個月用過手機支付 65.6%** | 捐款頁必須 mobile-first；付款摩擦是 fundraising 策略，不是 IT 細節。 |
| HKMA QB Mar 2024 / HKICL | FPS 註冊 **15.79M（2024 底，YoY +16%）→ 17M+（2025 中）**；日均 1.98M 筆（2025/3，+32.9%） | Visa/Master 是基線；FPS 是必選；轉數快 push-based，月捐需 NGO 加提醒機制。 |
| HKMA Payment Connect | 2025/6 跨境 FPS × 內地 IBPS 上線 | 月捐給內地家屬 / 跨境捐贈場景新機會。 |
| HKPC 2023（最新權威）| B2C 接受 FPS 70% / 信用卡 67% / Mobile QR 61%；平均 5.6 種支付方式 | NGO 接 3+ 種支付是常識（FPS + 信用卡 + Apple Pay 起步）。 |

---

## B. HK 捐方信任、行為、合規

| 來源 | 數據 | Campaign 含義 |
|---|---|---|
| CAF World Giving Report 2025 | **HK 捐方 77% 流向正式機構，9% 流向個人**（全球極端低）；亞洲均捐 1.28% 收入（全球 1.04%） | HK 捐方對「機構品牌化」接受度極高——首屏 logo / 認證 / 透明度比個人故事更前置。 |
| HKCSS / HKU POP 2009（迄今未重做）| 91% 重視機構聲譽 / 86% 透明 / 73% 便利 / 38% 公眾人物呼籲 | 信任 > 名人；機構品牌比 KOL 重要；便利是 fundraising 策略。 |
| HKCSS / HKU POP 2009 | 重複捐贈觸發：75% 善款使用 / 61% 受惠者狀況 / 50% 項目進展 / 41% 更便利 | Reactivation copy 以「impact proof」開頭，再 ask。 |
| HKU JC ESG NGO Transparency Index | 2024-2025 新框架，量化 HK NGO 公開透明度 | 當前 HK 信任研究最新基準；NGO 應主動引用排名。 |
| IRD 慈善地位指引 | section 88；認可捐款 ≥ HK$100 可扣，**上限 35% 應評稅入息** | 收據 / 稅務 copy 不應作主訴求，作 footnote 即可。 |
| PCPD PDPO Part VIA | 直銷需 PICS + 明示同意；**違規 HK$500k + 3 年監禁**；第三方共享 HK$1M + 5 年 | 收據用途 / 推廣用途 / 第三方分享必須拆分 checkbox。 |
| SWD 慈善籌款監管 | PSP 三類（賣旗 / 一般 / 簽名授權）；**Good Practice Guide 為 PSP 條件**（2024/11 LCQ17 不強制法定化） | NGO 在 PSP 下守 GPG 即可，無需擔心新合規負擔。 |
| 慈善機構統計（2024/9）| **10,699 間稅務豁免慈善**（+3.4% YoY） | HK NGO 市場規模 lower bound。 |
| IRD 認可捐款金額 | 2022/23 **HK$124.3 億**（YoY -13.1%） | HK 公眾捐款規模下限；實際更高（未申報扣稅者）。 |

---

## C. 在線捐贈、分享、留存研究

### C.1 頁面轉化機制

| 來源 | 數據 | 應用 |
|---|---|---|
| Athey et al. 2024 (Stanford GSB, PayPal Giving Fund, n > 400k) | 高 anchor 提升總金額；低 anchor 提升人數；兩者皆提升 default 選擇率 | Ask string 按目標選 anchor。 |
| Karlan & List 2007 (AER, n > 50k) | 1:1 match risk ratio ≈ 1.22；**2:1 / 3:1 無額外效果**；紅州 1.53 / 藍州 1.05 | 1:1 配對足夠；配對訊息在 ask 之前。 |
| Gneezy, Keenan & Gneezy 2014 (Science, n = 40k) | 「seed money cover overhead」 vs 「matching」/「seed」——**捐款人數翻倍** | 「行政費由 X 贊助」標出，預期 2× 提升。 |
| Karlan, List & Shafir 2011 (JPubE) | Small matches 已夠 | 不需追大配對 ratio。 |
| Small, Loewenstein & Slovic 2007 (OBHDP) | identifiable victim 比 statistical 顯著高金額；deliberative thinking 反向減少 caring | Headline 用一人故事，統計放下方。 |
| Lee & Feeley 2023 (Collabra: Psychology) | 大規模重複實驗，原效應確認 | 同上，仍然成立。 |
| Wang, Guo & Wu 2024 (IT & People) | beneficiary photo + warmth-framed 提升 intention；自助 framing > 被動受助 | Hero image 單一受惠者面部 + 自助行動。 |
| M+R Benchmarks 2025 / 2026 | Donation page completion 12%（Desktop 11%，**Mobile 8%**，小型 NGO mobile 4%）；avg gift Desktop $168 vs Mobile $88 | HK NGO 必須真機測試；FPS 加持目標 mobile 15%+。 |

### C.2 社交分享 / 裂變

| 來源 | 數據（精確）| 應用 |
|---|---|---|
| Castillo, Petrie & Wardell 2014 (JPubE) | 無激勵 4.4% / $1 → 12.6% / $5 → 16.9%；Wall post 14% vs Private message 8.4%；已登入 FB 26.3% vs 未登入 11.6% | 不付 incentive；wall / IG Story / FB 公開分享 > 私訊。 |
| Castillo 2014（下游）| 所有分享 1.2% 帶來新捐款；wall post 1.89%；新捐款均值 $49.00 vs 原 $55.73 無顯著差異 | 分享是複利，非倍數魔法。 |
| Lam & Nie 2020 (VOLUNTAS, 427 HK 社服 NGO) | 資訊類 post 拿 likes；**行動類 post 拿 shares**；依賴政府資助者較少上線 | 籌款 ask 走行動類格式；社署資助 NGO 在線是「0 到 1」。 |

### C.3 Onboarding / 留存

| 來源 | 數據 | 應用 |
|---|---|---|
| Althoff & Leskovec 2015 (WWW, DonorsChoose, 1.5M donors) | 74% 只捐一次；26% 回頭；1% 達 5 次；首項目成功 +5pp 回頭機率（+29% relative） | 致謝 / impact 是 retention 基建。 |
| Network for Good / TrueSense Online Giving Study | branded charity pages > generic portals；recurring 是主驅動 | 自家品牌頁強於 third-party portal。 |
| Penelope Burk《Donor-Centered Fundraising》 | 48h 真人電話：下次 ask 金額 +39%；14 個月後仍 +42%。90 天內 ≥1 通電話：留存 33% → 58% | D+7 真人接觸不可省。 |
| NextAfter《New Donor Welcome Study》（147 NGO）| 90 天 offer-focused welcome series 帶 **+920%** 下游轉化；brand value-prop **+760%**；70% NGO 用機構名而非真人姓名作 sender | Welcome sequence 是月捐生死。 |
| NextAfter | Default-to-monthly 弱 default **+348%** | 月捐 toggle 默認 on（清楚可改）。 |

### C.4 月捐 LTV / Churn

| 來源 | 數據 | 應用 |
|---|---|---|
| Classy 2023 State of Modern Philanthropy | 月捐 LTV / 一次性 **5.4× – 9×**；平均月捐壽命 **4.6 年**；首 90 天 **29%** 一次性升級月捐 | 月捐黃金期 = 首 90 天。 |
| Blackbaud Sustainer Summit FY24 | 月捐獲取 cohort 3 年累計 LTV **$405** vs 單次 $161（2.5×）；直接 acquisition 13 個月留存 **47%** | 直接 acq 質量參差；需 90 天計劃。 |
| Neon One 2026 Recurring Giving Statistics（4,107 NGO）| 月捐平均壽命 **7.5-8 年** vs 一次性 1.5-2；LTV $7,288 vs $3,607 | 月捐結構性優勢全球確認。 |
| DonorPerfect Monthly Donor Metrics | 月捐留存 ≈ **85%** vs 一次性 ≈ 28%；LTV $2,400 vs $70 | 留存 = ROI 槓桿。 |
| Fundraising Effectiveness Project Q4 2024 | 整體 retention 42.9%（-2.6pp）；**新一次性 19.4%**；repeat 69.2%；月捐 78-90% | 一次性是漏斗破洞。 |
| M+R Benchmarks 2024 | 月捐前 2 個月 10% 取消；7 個月後剩 81%；12 個月剩 71% | 90 天 onboarding 是必選。 |
| M+R Benchmarks 2025 / 2026 | Monthly 占 online revenue **31%**（2024）→ 27%（2025）；avg monthly $24；avg one-time $126 | 月捐已是 1/3 在線收入。 |
| Donorbox / Bonterra | Checkout lightbox upsell 平均 3.5%（健康 3-5%）；97% 升級者最終金額 > 原一次禮物 | Checkout 升級必裝。 |
| Industry estimates | Involuntary churn 占月捐流失 **15-30%**；Account Updater + retry 降 20-30% 失敗 | 純技術可救 15%+ retention。 |
| DonorVoice / Agitator | 卡片失敗 7 天內真人電話救回率 50%+；自動 email 只 10-15% | Dunning 必須有真人 leg。 |

### C.5 行業 benchmark

| 來源 | 數據 | 應用 |
|---|---|---|
| M+R Benchmarks 2025 / 2026 | Email list +5%；revenue per subscriber $2.40；fundraising CTR 0.48%；平均年發 62 封 | Email 是 retention 基建，非廣告。 |
| Blackbaud Charitable Giving Report 2024 | 在線 +2.2%（5,151 NGO）；小型 NGO 線上 13.4% 占比 +3.3% | 中小型 NGO 在線增長率最高。 |
| CAF World Giving Report 2025 | 全球 36% 捐款；HK 機構占比 77% / 直接 9%；亞洲均捐 1.28% 收入 | HK 機構化捐款全球領先。 |

---

## D. 卖旗 / e-Flag 證據

| 來源 | 數據 | 應用 |
|---|---|---|
| SWD「賣旗日」官方頁 | 全港 + 分區 PSP；2025-26 **56 個賣旗日**（28 全港 + 28 分區）；時段 **07:00-12:30** | 申請週期 6-12 個月提前。 |
| SWD「公開籌款許可證」 | section 88 + 過去 3 年慈善活動；署長發、警方協助 | 中小新 NGO 第 4 年才合資格。 |
| SWD「賣旗日條件」2026-27 | **行政費 ≤ 10% 總收入**；獨立核數師審；公布 data.gov.hk | e-Flag 平台費計入 10% 封頂。 |
| HKFHY 2020/7 案例 | COVID 取消街頭純線上，籌款額大幅下跌 | e-Flag 不能完全替代街頭，混合最佳。 |
| 公益金 2024 | 全港賣旗逾 HK$340 萬；全數撥捐 168 機構零行政扣減 | 「零開支」是公益金品牌資產。 |
| 保良局 2025 | 全港賣旗動員 **17,000+ 義工** | HK 最大規模賣旗義工動員。 |
| HKBWS 2024 | 新界區賣旗 HK$398,802 / 目標 HK$700,000（57% 達成）；SparkRaise | 中小機構若無校網 / 企業關係，光靠 SaaS 難破百萬。 |
| AVS 2025 | 55 週年；目標 110 萬 / 6,000 義工；三類排行榜（個人 / 機構 / 最具動員力團隊） | 排行榜 4 類設計成熟。 |
| Digital 2025 HK | WhatsApp 滲透 74.7%；FB 73.5%；HK 每人均用 6.4 個社交平台 | e-Flag 分享按鈕順序：WhatsApp / FB / IG。 |

---

## E. 華人地區案例

| 案例 | 數據 | HK 遷移 |
|---|---|---|
| 99 公益日（騰訊久久公益節）2024 | 互動 7 億人次；捐款 4,600 萬人次；5,500+ 項目；騰訊 4 億配捐 | 限時窗口 + 1:1 配對是 e-Flag 可借鑒「峰值事件」。 |
| 港版 99 公益日 2023 | 22 機構參與；騰訊配捐上限 HK$200 萬（每機構 HK$50 萬） | 已有 HK 在地經驗。 |
| 上海聯勸「一個雞蛋的暴走」2024 第十四屆 | 14 萬人；超 1 億 RMB；32 省 1,035 項目；2,000+ 隊員徒步 50 公里 | Peer-to-peer 賭注式籌款；HK Trailwalker 之外的中小型模板。 |
| 壹基金海洋天堂 2010-2018 | 605 家組織；20 萬+ 特需兒童；18.8 萬家庭；4,000+ 行動 | 電影 IP → 議題型月捐。 |
| 字節跳動公益 2024 | 捐贈 3.5 億+；1,727 機構；3,500+ 項目；公益視頻 600 億播放；單條 100 萬+ | 創作者經濟 × 公益模式。 |
| 螞蟻森林 2020/8 | 5 億用戶；792 萬噸碳減排；種樹 1.22 億；支付寶公益累計 91.6 億元 | 行為公益遊戲化。 |
| 騰訊小紅花 | Lv1-Lv8 成長體系 | 月捐 onboarding 遊戲化模型。 |
| 台灣世界展望會 | 月捐資助 40 國 28 萬兒童；國際 NT$700 / 月；國內 NT$2,000 / 月 | 「月捐 = 認養 1 名具名兒童」高於抽象訴求。 |
| 台灣家扶 | 73 年；NPO 自律聯盟 7 大；「每天 10 元」錨點 | 日感金額 > 月感金額（HK 可測 +3 / 天）。 |
| 公益責信《公益觀察 2021》 | 台灣 46% 人口曾捐；2020 個人捐款 1,062 億；年輕族群重便利、中產重透明 | 受眾分層 = 入口分層。 |
| 聯合勸募 2025/1-10 | 公開停捐 4,000+ 筆 / 1,300 萬 | 主動披露 churn = 信任資產。 |
| Singapore giving.sg | 700+ 慈善；2024 全年 S$86.7M / 2025 S$104.9M | HK 5 年內可能演化的「國家平台」方向。 |
| NVPC National Giving Study 2023 | SG 2021 月捐佔 **20%** | HK 估 < 10%，至少 2× 增量空間。 |

---

## F. 引用與 transferability 標示原則

- `Observed in source`：原文精確百分比，可直接引。
- `Evidence-informed estimate`：基於來源 + 本地渠道契合度，給範圍 + 信心。
- `Unknown`：需要 campaign analytics 才能說的，標清楚要測。

對所有國際田野實驗，標出：**樣本來源 + 年份 + 是否可遷 HK**。
