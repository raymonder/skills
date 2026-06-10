# 财报数据抓取工作流

香港受社署资助的 NGO 每年必须在官网公布一份 **Annual Financial Report for Social Services Units Subsidised by Social Welfare Department**。这份 PDF 是会前简报最有价值的单一数据源。

## Step 1 · 找 PDF

在机构官网上一般通过以下 3 条路径之一可找到：

1. **「关于我们 → 财务报告 / 年报 / 公告」** 栏目
2. **「捐款 / 支持我们 / 透明度」** 栏目（部分机构把财报放在这里显示透明度）
3. **顶部 sitemap** 或「下载专区」

若上述都找不到，用 Google：
```
site:<官网域名> filetype:pdf financial
site:<官网域名> filetype:pdf 財務 OR 財政
site:<官网域名> subunit financial
```

文件名通常类似 `subunit-financial-2024-25.pdf` 或 `financial_report_2024.pdf`。

**重要**：香港财年是 **4 月 1 日 - 3 月 31 日**。2024/25 财年报表通常在 **10 月左右** 签发公布。如果现在是 5-9 月，最新公开版本是上一财年（2024/25）；10 月后当年的（2025/26）才会出来。

## Step 2 · 直接尝试 WebFetch

大多数 PDF 可以直接用 WebFetch 提取文本。prompt 示例：

```
提取 2024/25 年度 Social Services Units 社署资助板块的财务数据，包括：
- Total Income
- LSG (Lump Sum Grant), 包括 Provident Fund 部分
- Fee Income
- Central Items
- Rent and Rates
- Other Income
- Total Expenditure
- Personal Emoluments (Salaries + Provident Fund)
- Other Charges 细目（Utilities, Food, Stores and Equipment, Repair, Programme, Insurance, Misc）
- Surplus for the year
同时提取核数师名称、签发日期。
对比 2023/24 数字，列出同比变化。
```

## Step 3 · 如果 WebFetch 返回空或乱码——PDF 是扫描版

很多老牌 NGO 的财报是打印后扫描回 PDF。这种情况 WebFetch 会返回「无法提取」或乱码。

> **⚠️ 这一步不能跳过。** 扫描版 PDF 的 OCR 是会前简报的"必经之路"。常见失败模式：看到扫描版就在简报里写「AFR 为扫描版，未能 OCR 提取细项」然后转向用机构简介页的宽泛数字——这是**错的**。一旦放弃 OCR，就失去了 Admin Expenses / Stores and Equipment / Programme Expenses 同比变化这些**最硬的数字化投入信号**，简报会从 insight 型沦落成罗列型。
>
> 正确做法：走下面的 OCR 流程，英文单语言包就够，一页一页抠数字。花 3-5 分钟的 OCR，换回来的是整份简报 80% 的弹药。

走 OCR 路径：

### 3.1 下载 PDF 到本地

```bash
curl -L -o /tmp/report.pdf "<PDF URL>"
```

### 3.2 先试 pdftotext（最快）

```bash
pdftotext /tmp/report.pdf /tmp/report.txt
cat /tmp/report.txt | head -50
```

如果输出为空，说明是图片扫描 PDF。继续下一步。

### 3.3 OCR

把 PDF 每页转成 ppm 图片，逐页 OCR：

```bash
cd /tmp
pdftoppm -r 300 report.pdf p
# 产生 p-1.ppm, p-2.ppm, ...

# 如果系统有 tesseract-ocr-chi-tra 就用繁中 + 英文
for f in p-*.ppm; do
  tesseract "$f" "${f%.ppm}" -l chi_tra+eng --psm 6
done

# 如果 tesseract 只有英文（sandbox 环境经常这样），单英文也够用
# 财报里最关键的是数字和英文账目名称，中文名缺失不影响核心数据
for f in p-*.ppm; do
  tesseract "$f" "${f%.ppm}" -l eng --psm 6
done

cat p-*.txt
```

### 3.4 如果安装语言包被 sandbox 拒绝

常见错误：`sudo: no new privileges flag is set`

**不要硬装**。改用纯英文 OCR 即可——财报的关键数字和账目名（Salaries / Provident Fund / Stores and Equipment / LSG）都是英文，不影响可用性。

## Step 4 · 提取关键数字

从 OCR 文本里摘出以下数字，填入模板：

### 收入端

| 字段 | 英文名 | 单位 |
|---|---|---|
| LSG 整筆撥款（不含 PF） | Lump Sum Grant | HKD |
| LSG 公積金 | Provident Fund Grant | HKD |
| 服務收費 | Fee Income | HKD |
| 中央項目撥款 | Central Items | HKD |
| 租金雜費補貼 | Rent and Rates Subsidy | HKD |
| 其他收入 | Other Income (Programme + Misc) | HKD |
| 利息 | Interest Income | HKD |
| **總收入** | **Total Income** | HKD |

### 支出端

| 字段 | 英文名 | 单位 |
|---|---|---|
| 薪酬 | Salaries | HKD |
| 公積金 | Provident Fund | HKD |
| 人事成本小計 | Personal Emoluments Sub-total | HKD |
| 租金雜費 | Rent and Rates | HKD |
| 水電 | Utilities | HKD |
| 食物 | Food | HKD |
| 商店及設備 | Stores and Equipment | HKD |
| 維修 | Repair and Maintenance | HKD |
| 活動 | Programme | HKD |
| 保險 | Insurance | HKD |
| 雜項 | Miscellaneous | HKD |
| **總支出** | **Total Expenditure** | HKD |
| **本年度盈餘** | **Surplus for the Year** | HKD |

### 元数据

- 核数师名称（Auditor）
- 签发日期（通常在签字页）
- 财报年度（fiscal year）

## Step 5 · 同比分析（每一条都要带 so-what）

财报通常在每一行旁边标当年 + 上年度两列数字。**同比变化是销售信号**。提取时每一条信号都必须配一句"所以灵析应该⋯⋯"，不能只记数字：

| 信号 | 含义 | so-what（必须写进简报） |
|---|---|---|
| **LSG 增长 >8%** | 机构扩张阶段 | → 预算松 → 可推中间 / 高级版 |
| **LSG 下降或持平** | 紧缩信号 | → 谨慎报价 → 强调 ROI |
| **Central Items 骤减**（专项津贴消失） | 津贴断供 | → 机构要自筹补钱 → 灵析筹款工具是刚需 |
| **Stores and Equipment +30% 以上** | 硬件扩张 | → 在买 IT 设备 → 系统软件需求同时在升温 |
| **Administrative Expenses +50% 以上** | 行政 / IT 外包 / 订阅快涨 | → 系统升级或外包扩张 → **当下有预算**，黄金窗口 |
| **Programme Expenses 翻倍** | 项目规模扩张 | → 背后通常对应新的指定用途拨款 → 去问金主是谁 |
| **"Other Funds or Donations for Designated Purposes" 从 0 突增到千万级** | 异常大额专项 | → **异常信号 · 现场必问**是哪个金主 / 什么用途 / 是否允许数字化支出 |
| **Salary 占比 >80%** | 人力密集 | → 强调"释放员工时间"的价值主张 |
| **Salary 占比 60–70%** | 多元化较好 | → 可能已有数字化工具 → 先盘再推 |
| **盈余 >5% 总收入** | 储备充足 | → 敢花钱 → 锚定高档报价 |
| **盈余 <2% 或亏损** | 紧缩 | → 试点报价 · 从单中心切入 |
| **LSG 储备（Reserve）≥ 100M** | 有定存家底 | → 机构不差钱 → 预算不是障碍，决心是障碍 → 话术转向"决策速度" |

> **硬规则**：简报的"同比关键变化"段落，**必须至少挑 2-3 条命中的信号，每条带一句 so-what**。只列数字不讲解读 = 没做 Phase 2。

## Step 6 · 员工规模估算

```
员工数 ≈ 薪酬总额 ÷ 香港社福前线平均年薪（35–45 万）
```

前线社工（SWA / ASWO）：30–45 万 / 年
中层（SWO）：45–70 万 / 年
高级（SSWO 及以上）：70 万+

按 40 万平均数做粗估。如果员工里护理员比重高（安老院），按 30 万估。

## 常见陷阱

1. **两本账**：社福板块（社署财报）和总会/弘法账目是分开的。**只能推断社福板块的数字，不能用社福数字推断整个机构**。
2. **财年不同步**：有些非政府资助机构用日历年（1–12 月），不是 4 月财年。看签发日期判断。
3. **同比列的坑**：对比年度时注意哪一列是当年哪一列是上年——通常左侧是当年、右侧是上年，但偶有反转。
4. **PF 双重计算**：LSG 里已含一部分 PF，Salary 旁边还有一个 PF 支出——**不要把 LSG 的 PF 当额外收入加一遍**。
