# hk-fundraising-campaign-advisor

版本：0.9

这个 skill 用来设计、审阅和优化香港 NGO、学校、基金会、慈善机构的线上筹款方案，覆盖网络筹款、月捐、卖旗日和 e-Flag Day。它适合把一个还比较散的筹款想法，整理成有目标、有证据、有时间线、可执行的行动计划。

## 能实现什么功能

- 设计香港在线筹款活动的完整执行方案，包括页面、文案、传播、种子网络、时间线和指标。
- 设计月捐项目，包括 90 天 onboarding、续捐防流失、升级路径和支付方式建议。
- 设计卖旗 / e-Flag Day 的 12 周筹备计划、队伍动员机制、金旗层级和活动后月捐转化。
- 审阅现有捐款页、月捐页或 e-Flag 物料，用 100 分 scorecard 诊断问题并给出改写建议。
- 为董事会、筹款团队或客户会议输出有证据支撑的行动计划。
- 在合适位置说明灵析相关触点，例如捐款页、支付、CRM、月捐自动续扣、e-Flag 页面和捐款人再激活。

## 安装方式

把这个仓库 clone 到你的 agent skills 目录即可，例如 Codex：

```bash
cd ~/.codex/skills
git clone https://github.com/raymonder/hk-fundraising-campaign-advisor.git
```

如果你使用其他自定义 skills 目录，把仓库 clone 到对应目录下即可。目录结构应保持为：

```text
~/.codex/skills/
└── hk-fundraising-campaign-advisor/
    ├── SKILL.md
    └── references/
```

安装后重启 agent，或重新打开会话，让 skill metadata 被重新加载。

## 怎么使用

在对话中直接提出香港线上筹款相关任务即可触发，例如：

```text
帮我 review 这个香港 NGO 的月捐页，看哪里可以提升。
```

```text
帮我为某某机构设计一个 e-Flag Day 的线上筹款方案。
```

```text
我们要给香港学校做一个网上筹款活动，请给我一份执行计划。
```

如果你要做 review，请提供现有 URL、截图或文案。
如果你要做方案，请至少提供筹款柱线、目标金额或人数、期限或使用场景。

## 输入要求

硬性必需信息：

- 选择柱线：网络筹款、月捐、卖旗 / e-Flag、或 review。
- 目标：金额或人数二选一。
- 期限 / 场景：会议简报、执行计划、审阅报告，或其他具体用途。
- review 模式必须提供现有资产：URL、截图、页面文案或活动物料。

可选但有帮助的信息：

- 过去 12 个月筹款活动数量和结果。
- 筹款团队规模和可投入工时。
- 校友、企业 CSR、教会、义工、会员等可动员网络。
- 当前 CRM、支付方式、收据和捐款人数据现状。
- 与机构关系：首次拜访、已合作、售前推进或客户服务中。

## 目录结构

```text
hk-fundraising-campaign-advisor/
├── SKILL.md
├── INDEX.md
└── references/
    ├── campaign-playbook.md
    ├── e-flag-playbook.md
    ├── evidence-base.md
    ├── full-research-report.md
    ├── intake.md
    ├── monthly-giving-playbook.md
    ├── output-template.md
    └── scorecard.md
```

## 主要限制

- 只覆盖线上筹款；街站面对面月捐、电话筹款、邮寄筹款、晚宴 pledge 等不在默认范围内。
- 不会编造 uplift、转化率、分享率、留存率或流失率；没有证据支持时只能使用方向性判断。
- 不能替代法律意见。涉及香港 PDPO、直接促销同意、收据和个人资料使用时，只能给合规提醒。
- review 模式没有现有页面或物料时，不能凭空评分。
- 对敏感服务对象，如儿童、医疗、贫困、家暴、精神健康、难民和少数群体，必须优先保护尊严、同意和非识别性。
- 公开资料可能过时，机构事实应在正式对外使用前再次核实。

## 维护建议

- 定期更新 `references/evidence-base.md`，尤其是香港本地政策、支付方式、卖旗日规则和筹款研究。
- 新增 playbook 时保持 `SKILL.md` 轻量，把长材料放在 `references/`。
- 如果需要稳定评分脚本，可以在 `scripts/` 下补充工具，并在 `SKILL.md` 中说明何时调用。
