---
name: dev-project-init
description: 初始化或更新研发项目级 AI Coding Agent 规则。用户要求为研发项目创建、添加、同步、安装、维护项目提示词/通用研发规则时使用，尤其是要写入 AGENTS.md、cursor.md、CLAUDE.md、Cloud.md 或类似项目约定文件；也适用于用户要求创建“研发项目初始化”“研发通用规则”类可复用 skill 的场景。
---

# 研发项目初始化

## 工作流程

1. 先阅读仓库中已有的项目约定文件，再编辑；优先检查 `AGENTS.md`、`cursor.md`、`CLAUDE.md`、`Claude.md`、`CLOUD.md`、`Cloud.md` 和 `.cursor/rules/*`。
2. 保留项目已有的专属约定；除非用户明确要求，不要整文件覆盖。
3. 只插入或更新下面两个标记之间的规则区块：
   - `<!-- AI_CODING_AGENT_CORE_RULES:start -->`
   - `<!-- AI_CODING_AGENT_CORE_RULES:end -->`
4. 使用 `scripts/update_project_rules.py` 做确定性、幂等更新。
5. 更新完成后说明改了哪些文件，并提醒用户：“经验候选”是任务完成时的输出习惯，不代表每次都要自动改文档。

## 默认命令

在仓库根目录运行：

```bash
python3 /Users/raymond/.codex/skills/dev-project-init/scripts/update_project_rules.py --root .
```

默认行为：

- 更新已存在的 `AGENTS.md`、`cursor.md`、`CLAUDE.md`、`Claude.md`、`CLOUD.md`、`Cloud.md`。
- 如果这些文件都不存在，则创建 `AGENTS.md`。
- 除非传入 `--create-missing`，否则不会创建所有可能的目标文件。
- 如果已有标记区块，会替换旧区块，不会重复追加。

常用参数：

```bash
python3 /Users/raymond/.codex/skills/dev-project-init/scripts/update_project_rules.py --root . --targets AGENTS.md cursor.md CLAUDE.md
python3 /Users/raymond/.codex/skills/dev-project-init/scripts/update_project_rules.py --root . --create-missing
python3 /Users/raymond/.codex/skills/dev-project-init/scripts/update_project_rules.py --root . --dry-run
```

## 写入的核心规则

脚本会写入下面这段精简规则：

```md
- 必须先理解业务流程和现有实现，再修改代码。
- 修 bug 必须先基于证据定位根因，不能把现象当根因。
- 修改必须覆盖真实业务链路：入口、权限、数据读写、页面交互、异常状态和回显。
- 权限、可见性、编辑能力必须以后端校验为准。
- 行为变更和缺陷修复必须补测试，且测试必须覆盖问题场景。
- 涉及业务流程时，必须验证正常态、空状态、最后一项、无权限和非法参数。
- 测试数据必须唯一、隔离、可重复。
- 修改后必须运行相关验证；无法运行时必须说明原因、风险和替代验证。
- 部署、同步、合并必须使用安全隔离方式，不能污染环境或带入无关改动。
- 最终回复必须说明改动、原因、验证、commit/分支和部署/合并结果。
- 每次完成一个明确任务后，必须输出一小段经验候选，说明这次学到的通用注意点，并询问是否需要沉淀到项目文档。
```

## 约束

- 不要覆盖用户已有的项目约定。
- 不要默认把长篇复盘写进项目文档。
- 如果用户要调整规则内容，先改脚本里的规则区块，再重新运行脚本。
