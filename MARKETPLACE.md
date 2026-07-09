# 作为插件市场使用（Claude Code / Cowork）

本仓库是一个 **Claude Code 插件市场（marketplace）**，市场名 `raymonder-skills`。
里面每个 skill 都是**独立的插件**，可以按需单独安装，互不强制。

## 仓库结构

```
.claude-plugin/marketplace.json     # 市场目录，列出全部插件
plugins/<skill名>/
  .claude-plugin/plugin.json        # 该插件清单（未设 version → 每次 commit 即新版本）
  skills/<skill名>/SKILL.md         # skill 本体
```

## 安装

只需加一次市场，然后挑你要的装：

```shell
/plugin marketplace add raymonder/skills
/plugin install tender-proposal-writing@raymonder-skills
/plugin install ngo-client-brief@raymonder-skills
# …想要哪个装哪个，不需要的不装
```

桌面版 Cowork：插件设置 → Add from a repository → 填 `raymonder/skills`，然后在目录里逐个安装需要的。

## 可装的插件

| 插件名 | 用途 |
|---|---|
| `tender-proposal-writing` | 投标 / RFP / RFQ 方案撰写方法论 |
| `scenario-product-spec` | 场景化产品 / 功能方案写作 |
| `ngo-client-brief` | NGO 首次拜访会前简报 |
| `hk-fundraising-campaign-advisor` | 香港公众筹款方案设计与评审 |
| `feishu-setup` | 飞书 / Lark 接入与鉴权 |
| `feishu-editable-diagrams` | 飞书可编辑 SVG 图表 |
| `transcript-to-corrected-minutes` | 转写稿→校正纪要 |
| `weekly-ai-and-me-reflection` | 每周 AI 协作复盘 |
| `dev-project-init` | 初始化 / 更新研发项目 AI Coding Agent 规则 |

## 更新

改完某个 skill → push 本仓库 → 在 Claude 里 `/plugin update <插件名>@raymonder-skills`，或在市场上开「自动同步 / Enable auto-update」，开新会话即生效。
已写 `version` 的插件按 `plugin.json` 版本号识别；未写 `version` 的插件则每次 commit 都被视为新版本。

## 新增一个 skill

```
plugins/<新skill名>/
  .claude-plugin/plugin.json        # {"name":"<新skill名>","description":"...","author":{"name":"Raymond"}}
  skills/<新skill名>/SKILL.md
```

再在 `.claude-plugin/marketplace.json` 的 `plugins` 数组里加一条 `{"name":"<新skill名>","source":"./plugins/<新skill名>","description":"..."}`，push 即可。

## 给 Codex 用

Codex 不认 marketplace，但认同一套 `SKILL.md`。本机已把 9 个 skill 软链进 `~/.codex/skills/`，指向本仓库 `plugins/<skill>/skills/<skill>`，`git pull` 后 Codex 即用最新版。
