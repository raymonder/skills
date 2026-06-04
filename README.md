# Skills

> 一组从真实工作里长出来的 AI agent skills。  
> 它们不是某一个工具的专属附件，而是一批可以被 Codex、Claude Code，或其他理解 `SKILL.md` 的 agent 复用和改造的工作方法。

## 背景

这些 skill 不是从空白处写出来的。

它们先是工作里反复出现的一些小麻烦：见客户前资料太散，RFP 里的功能描述太干，筹款方案需要证据又不能乱承诺，飞书接入总卡在身份和权限，人与 AI 长期协作之后也需要回头看一看哪里顺、哪里返工。

一开始，解决这些问题靠的是临场经验：几句提醒，一段命令，一个模板，一次「不对，重新做」之后留下的记忆。可当同一种问题第三次出现，就不该再靠人脑硬扛。于是我把这些经验整理成 skill：把现场判断写成流程，把容易遗漏的检查点写成规则，把反复用到的输出结构固定下来。

这里的每个 skill 都可以直接安装使用，也可以被拆开、改写、接进你自己的工作流里。它们不是标准答案，更像是一组已经磨过一轮的工作手稿：保留一点现场的温度，也尽量把方法写到足够清楚。

## 安装方式

通常把需要的 skill clone 到你的 agent skills 目录即可。不同工具的目录可能不同，例如：

```bash
cd ~/.codex/skills
git clone <skill-repo-url>
```

或：

```bash
cd ~/.claude/skills
git clone <skill-repo-url>
```

安装后重启对应 agent，或重新打开会话，让 skill metadata 被重新加载。

## 当前 Skills

| Skill | 当前版本 | 仓库 |
|---|---:|---|
| `hk-fundraising-campaign-advisor` | `0.9` | [GitHub](https://github.com/raymonder/hk-fundraising-campaign-advisor) |
| `ngo-client-brief` | `0.9` | [GitHub](https://github.com/raymonder/ngo-client-brief) |
| `scenario-product-spec` | `0.9` | [GitHub](https://github.com/raymonder/scenario-product-spec) |
| `feishu-setup` | `0.9` | [GitHub](https://github.com/raymonder/feishu-setup) |
| `weekly-ai-and-me-reflection` | `0.9` | [GitHub](https://github.com/raymonder/weekly-ai-and-me-reflection) |

---

## hk-fundraising-campaign-advisor

香港线上公益筹款顾问 skill，用于设计、审阅和优化香港 NGO / 学校 / 慈善机构的线上筹款方案，覆盖网络筹款、月捐、卖旗日和 e-Flag Day。

| 项目 | 说明 |
|---|---|
| 适用场景 | 设计或 review 香港 NGO、学校、基金会、慈善机构的线上捐款页、月捐项目、卖旗日或 e-Flag Day 活动。 |
| 具体解决什么问题 | 把零散的筹款想法整理成有目标、有证据、有优先级的执行方案；避免凭感觉写筹款建议，也避免编造转化率、分享率、留存率或 uplift。 |
| 典型产出 | 筹款活动计划、月捐 onboarding、e-Flag 12 周时间线、100 分 review scorecard、页面和文案改写建议、A/B test 和衡量指标。 |
| 需要的输入 | 机构名称、筹款柱线、目标金额或人数、期限、现有页面 URL / 截图 / 文案、过往筹款结果、可动员网络。 |
| 适合谁用 | 做香港 NGO fundraising、公益 SaaS、CRM 售前、筹款顾问、学校或机构线上筹款的人。 |
| 当前版本 | `0.9` |

安装：

```bash
git clone https://github.com/raymonder/hk-fundraising-campaign-advisor.git
```

---

## ngo-client-brief

为首次拜访 NGO 客户前生成会前简报的 skill。它把公开资料、财务数字和销售关注点整理成一份会议前可速读、会议中可翻阅、会后可回灌的作战文件。

| 项目 | 说明 |
|---|---|
| 适用场景 | 首次拜访 NGO、协会、慈善机构、学校或社会服务机构前，需要快速生成一份聚焦业务切入点的会前简报。 |
| 具体解决什么问题 | 避免客户背景研究写成百科式资料堆砌；把年报、财务、服务点、官网、筹款入口和数字化痕迹压缩成「这家机构为什么值得聊、该从哪里切、哪些数字能变成问题」的会议判断。 |
| 典型产出 | 一页纸速览、机构基本面、年度收支解读、网络筹款 / 会员管理 / Service Center / 年度收支四大关注点、数字化缺口估算、会议提示、报价锚定和红线提醒。 |
| 需要的输入 | 机构名称、联系人、职位、会议目的、官网或年报链接、当前关系状态、想推进的产品线。 |
| 适合谁用 | NGO / 公益行业销售、售前、客户成功、CRM 顾问、需要在会议前快速形成客户判断的人。 |
| 当前版本 | `0.9` |

安装：

```bash
git clone https://github.com/raymonder/ngo-client-brief.git
```

---

## scenario-product-spec

场景化产品方案写作 skill，用于把功能清单、需求矩阵或 RFP 条款扩写成「角色 + 场景 + 条件 + 系统响应 + 业务价值」的完整产品叙事。

| 项目 | 说明 |
|---|---|
| 适用场景 | 投标技术方案、产品方案、需求理解、解决方案设计、PRD 或 RFP 回复，需要把需求矩阵扩写成端到端叙事。 |
| 具体解决什么问题 | 很多方案不是没有功能，而是写得像清单。这个 skill 解决「评审知道你有功能，但感受不到你真的懂业务」的问题。 |
| 典型产出 | 模块化产品叙事、关键业务规则、端到端链路说明、需求编号回标、流程图 / 状态机 / 效果图建议。 |
| 需要的输入 | 原始需求清单、需求编号体系、已锁定技术口径、目标文档位置、项目边界、已有方案或原型信息。 |
| 适合谁用 | 产品经理、售前方案、投标文档作者、技术方案作者、需要把「功能点」写成「业务场景」的人。 |
| 当前版本 | `0.9` |

安装：

```bash
git clone https://github.com/raymonder/scenario-product-spec.git
```

---

## feishu-setup

飞书 / Lark 接入 skill，用于帮助 AI agent 安装和配置 `lark-cli`，完成 App 凭证、OAuth device flow、user / bot 身份验证和常见权限排查。

| 项目 | 说明 |
|---|---|
| 适用场景 | agent 需要接入飞书 / Lark，准备读写文档、Wiki、表格、Base、IM、日历或邮件之前，先把认证和权限跑通。 |
| 具体解决什么问题 | 飞书 API 真正麻烦的地方常常不是调用，而是 App ID / Secret、scope、user vs bot、device flow、permission denied。这个 skill 只负责把门打开。 |
| 典型产出 | 可用的 `lark-cli` 配置、user token 验证、bot/user 身份判断、权限错误排查路径，以及后续切换到 `lark-doc`、`lark-sheets` 等 skill 的指引。 |
| 需要的输入 | Feishu/Lark App ID、App Secret、目标租户、所需资源类型、授权用户。 |
| 适合谁用 | 需要让 AI agent 操作飞书 / Lark 资源的人，尤其是第一次接入或权限经常卡住的场景。 |
| 当前版本 | `0.9` |

安装：

```bash
git clone https://github.com/raymonder/feishu-setup.git
```

---

## weekly-ai-and-me-reflection

AI 协作反思周报 skill，用于从最近一周的 chat、agent 或 coding-session transcript 里生成协作观察、双向反馈、改进建议和静态 dashboard。

| 项目 | 说明 |
|---|---|
| 适用场景 | 每周或按需回顾人与 AI 的协作记录，想知道这周做了什么、哪里顺、哪里返工、下周双方怎么配合得更好。 |
| 具体解决什么问题 | 避免凭感觉评价 AI 协作质量；用真实纠错、返工、采纳和重复问题作为证据，不编造批评，也不写商业互吹。 |
| 典型产出 | Markdown 周报、机器可读 YAML、静态 `index.html` dashboard、与上一周对比、下一步改进建议。 |
| 需要的输入 | 最近 7 天 transcript、输出目录、human / AI 显示名称、可选 `decisions.md`。 |
| 适合谁用 | 长期和 AI agent 协作的人、团队、独立工作者，尤其适合想把 AI 从「一次性回答器」变成长期协作对象的场景。 |
| 当前版本 | `0.9` |

安装：

```bash
git clone https://github.com/raymonder/weekly-ai-and-me-reflection.git
```

---

## 版本说明

当前所有 skill 从 `0.9` 开始。

这个版本号的含义是：已经能在实际工作中使用，但还保留继续打磨的空间。后续如果某个 skill 的结构、触发条件、输出模板或引用资料发生明显变化，可以单独升级它的版本。

## 使用和改造建议

- 先直接安装单个 skill，确认它能触发并产出你想要的东西。
- 如果你的业务场景不同，不要整包照搬，优先改 `SKILL.md` 的触发条件和输出规则。
- 大段行业资料、模板、范例建议放进 `references/` 或 `templates/`，不要把 `SKILL.md` 写得太胖。
- 真正反复使用后，再把你自己的修订沉淀成新版本。
