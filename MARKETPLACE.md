# raymonder-skills

Raymond 的个人 Agent Skill 集合，做成一个 **Claude Code 插件市场（plugin marketplace）**，一个仓库统一维护、一条命令全部更新。底层是开放的 `SKILL.md` 标准，因此同样的 skill 也能直接给 **Codex / Cursor / Gemini CLI** 用。

## 包含的 skill

| skill | 用途 |
|---|---|
| `tender-proposal-writing` | 投标 / RFP / RFQ 方案撰写方法论（腔调、需求回标、各分章要求） |
| `scenario-product-spec` | 场景化产品方案写作（功能短句→业务语句） |
| `ngo-client-brief` | NGO 首次拜访会前简报 |
| `hk-fundraising-campaign-advisor` | 香港在线 / 月捐 / 卖旗筹款方案 |
| `feishu-editable-diagrams` | 飞书可编辑 SVG 图表 |
| `feishu-setup` | 飞书 / lark-cli 接入配置 |
| `transcript-to-corrected-minutes` | 录音转写→校正会议纪要 |
| `weekly-ai-and-me-reflection` | 每周 AI 协作复盘 |

## 仓库结构

```
.claude-plugin/marketplace.json     # 市场目录（列出插件）
raymonder-skills/                   # 唯一的插件
  .claude-plugin/plugin.json        # 插件清单（未设 version → 每次 commit 即新版本）
  skills/<skill名>/SKILL.md         # 各 skill
```

## 安装（Claude Code / Cowork）

```shell
/plugin marketplace add raymonder/raymonder-skills
/plugin install raymonder-skills@raymonder-skills
```

## 新增一个 skill

直接在**插件的 skills 目录**下建文件夹即可，不用改任何 json（skill 从 `skills/` 自动发现）：

```
raymonder-skills/skills/<新skill名>/SKILL.md
```

然后 `git add -A && git commit -m "add <skill>" && git push`，再在 Claude 里 update（见下）。
注意：必须放在 `raymonder-skills/skills/` 下，放仓库根目录不会被识别。

## 开启自动更新（每次打开 Claude 自动拉最新）

`/plugin` → **Marketplaces** 标签 → 选 `raymonder-skills` → **Enable auto-update**。
开启后每次启动 Claude 会自动刷新市场并更新插件，有更新时提示 `/reload-plugins`（或新开会话生效）。
第三方市场默认关闭，所以需手动开这一次。Cowork 中对应「自动同步」开关。

## 分享给别人

仓库设为 public 后，别人跑这两条即可用（私有库需对方有访问权）：
```shell
/plugin marketplace add raymonder/raymonder-skills
/plugin install raymonder-skills@raymonder-skills
```

## 更新到最新版

改完任何 skill → push 到本仓库 → 在 Claude 里：

```shell
/plugin marketplace update raymonder-skills
/plugin update raymonder-skills
```

然后**新开一个会话**即生效（同一会话里已调用过的 skill 内容已定格，不会重读）。
插件管理界面打开「自动同步」后，push 后最长约 30 分钟自动更新，可省去手动命令。

## 给 Codex 用

Codex 不认 Claude 的 marketplace，但认同一套 `SKILL.md`。把本仓库的 skill 软链进 Codex 的 skill 目录即可：

```bash
git clone git@github.com:raymonder/raymonder-skills.git ~/code/raymonder-skills
for d in ~/code/raymonder-skills/raymonder-skills/skills/*/; do
  ln -s "$d" ~/.codex/skills/$(basename "$d")
done
```

更新：`cd ~/code/raymonder-skills && git pull`，Codex 重启后即用最新版。
