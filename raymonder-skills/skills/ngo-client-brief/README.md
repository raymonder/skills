# ngo-client-brief

版本：0.9

这个 skill 用来在首次拜访 NGO、协会、慈善机构、学校或社会服务机构之前，生成一份会前简报。它会把公开资料、财务数字和业务切入点整理成一份会议前可速读、会议中可翻阅、会后可继续跟进的作战文件。

## 能实现什么功能

- 为香港或内地 NGO 客户生成首次拜访前的会前简报。
- 围绕四大关注点组织信息：网络筹款、会员管理、Service Center、年度收支。
- 从官网、年报、Annual Financial Report、HKCSS、HKNGO、社署资料等公开渠道提取客户背景。
- 对财报数字做销售解读，强调“数字 + so-what”，不是只堆资料。
- 识别卖旗日、财年、筹款高峰和系统换期等可转成销售动作的时间窗口。
- 盘点机构已有数字化建设、子域名、招聘、IT 投入和潜在系统缺口。
- 按固定模板输出简报，避免尾部自评、打分或泛泛总结。

## 安装方式

把这个仓库 clone 到你的 agent skills 目录即可，例如 Codex：

```bash
cd ~/.codex/skills
git clone https://github.com/raymonder/ngo-client-brief.git
```

目录结构应保持为：

```text
~/.codex/skills/
└── ngo-client-brief/
    ├── SKILL.md
    ├── agents/
    ├── references/
    └── templates/
```

安装后重启 agent，或重新打开会话，让 skill metadata 被重新加载。

## 怎么使用

在对话中说出你要见的机构即可，例如：

```text
明天要见香港某某机构，帮我准备会前简报。
```

```text
帮我做一份某某 NGO 的背景研究，聚焦业务上可以怎么切入。
```

```text
我要第一次拜访某某协会，抽取客户信息并给我会议作战提示。
```

如果你知道联系人、职级、会议目的或已有关系状态，一并提供会更准。

## 推荐输入

最少输入：

- 机构名称。
- 拜访目的或场景，例如首次拜访、售前推进、续约、产品演示。

强烈建议补充：

- 见面对象姓名、职位和部门。
- 会议日期。
- 当前关系状态：陌生拜访、已有联系、客户转介绍或老客户。
- 你最想推动的产品线或合作方向。
- 已知线索，如官网、年报链接、捐款页、会员页或卖旗日信息。

## 输出内容

skill 会按模板生成会前简报，通常包括：

- 一页纸速览。
- 机构基本面。
- 年度收支和关键财务信号。
- 网络筹款、会员管理、Service Center、年度收支四大关注点。
- 已有数字化盘点和缺口估算。
- 会议作战提示。
- 报价锚定话术。
- 红线提醒。
- 会后必做。
- 资料来源。

## 目录结构

```text
ngo-client-brief/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── financial-extraction-workflow.md
│   ├── lingxi-4-concerns.md
│   └── public-data-sources.md
└── templates/
    └── brief-template.md
```

## 主要限制

- 依赖公开资料。机构官网、年报、财报或招标资料缺失时，只能明确标注“未查到”或“初步估算”。
- 财报扫描版需要 OCR；如果本地缺少 `pdftoppm`、`tesseract` 或语言包，提取质量会下降。
- 不能把估算值当成硬数据。员工数、公众筹款占比、数字化投入等必须标注为推估。
- 不替代尽职调查、财务审计或法律意见。
- 对宗教型 umbrella NGO、社福板块和总会板块要区分“两本账”，不能混讲。
- 不适合写成通用百科介绍；如果信息和四大关注点无关，应压缩或删去。
- 默认不在末尾加自评、评分或“做得好/不足”总结。

## 维护建议

- 定期更新 `references/public-data-sources.md`，确保香港 NGO 数据源仍可访问。
- 更新 `references/financial-extraction-workflow.md` 中的 OCR 命令和财报字段映射。
- 根据真实会后反馈迭代 `templates/brief-template.md`，但保持固定结构，避免每次输出漂移。
- 如新增行业分支，例如宗教、长者服务、青少年服务，可放到 `references/`，不要把 `SKILL.md` 写得过长。
