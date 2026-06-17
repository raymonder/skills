# weekly-ai-and-me-reflection

版本：0.9

这个 skill 用来从最近一段时间的人机协作记录里生成 AI 协作复盘。它可以按周使用，也可以按需使用：把对话、智能体执行记录或编码会话记录整理成一份有证据、有观察、有改进建议的报告，并更新一个静态 dashboard。

## 能做什么

- 回顾最近的 AI 协作 transcript。
- 总结这一段时间通过 AI 协作完成了哪些工作。
- 观察人的协作方式、提示习惯和反复出现的沟通模式。
- 给人和 AI 双方生成基于证据的反馈。
- 用启发式方法统计已采纳交付、返工、纠错等事件。
- 和上一周报告做对比，观察趋势变化。
- 更新静态 `index.html` dashboard。
- 在报告末尾保留机器可读 YAML 区块，方便后续聚合趋势。

## 安装方式

```bash
cd ~/.codex/skills
git clone https://github.com/raymonder/weekly-ai-and-me-reflection.git
```

安装后重启 Codex，或重新打开会话，让 skill metadata 被重新加载。

## 怎么使用

在对话里要求生成 AI 协作周报或复盘即可，例如：

```text
用最近一周的对话生成一份 AI 协作周报。
```

```text
回顾我最近 7 天的 AI sessions，并更新 AI-and-me dashboard。
```

```text
用最近一周的 transcript 生成复盘，输出到 ./ai-and-me。
```

如果当前环境不能直接读取 transcript，请提供导出的 transcript 文件或目录路径。

## 默认输出

默认输出目录是 `./ai-and-me`，除非你指定其他路径：

```text
ai-and-me/
├── decisions.md
├── index.html
└── weekly/
    └── YYYY-MM-DD-report.md
```

`decisions.md` 是可选文件，用来记录长期偏好、已经确认的判断，或“不再重复提醒”的事项。

## 适合什么时候用

- 想知道这一周 AI 到底帮你做了什么。
- 想复盘哪些任务顺、哪些任务返工多。
- 想看自己的提问、修正、验收方式有没有固定模式。
- 想把 AI 从一次性问答工具，变成长期协作对象。

## 主要限制

- 只能分析它能访问到的 transcript。
- 数量统计是启发式判断，不是精确的数据分析系统。
- 没有 transcript 证据时，不应编造批评或表扬。
- 默认不暴露私人 transcript 细节、姓名、邮箱、账号、租户名称或本地路径，除非你明确要求写入报告。
- 这个 skill 不会自动创建定时任务。如果想每周自动运行，应使用宿主应用的 automation / reminder 功能。
