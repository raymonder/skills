# feishu-editable-diagrams

版本：0.9

这个 skill 用来在飞书 / Lark 文档或白板里制作可编辑图表。它的重点不是生成一张好看的 PNG，而是把流程图、架构图、关系图先做成适合飞书导入的 SVG，再转成白板节点，让文字、方框、箭头、容器和占位元素导入后仍然可以继续编辑。

## 能做什么

- 用矩形、文字、线条、分组和简单路径等 SVG 元素制作飞书友好的图表。
- 把 SVG 转成飞书白板可用的 OpenAPI JSON。
- 通过 `lark-cli docs +update` 把新的可编辑白板插入到飞书文档里。
- 通过 `lark-cli whiteboard +update` 更新已有飞书白板。
- 在写入飞书之前检查渲染效果、文字溢出、节点重叠和可编辑性。
- 插入或更新后导出飞书服务端渲染预览，确认线上效果和本地预览一致。

## 安装方式

把仓库 clone 到你的 agent skills 目录即可，例如 Codex：

```bash
cd ~/.codex/skills
git clone https://github.com/raymonder/feishu-editable-diagrams.git
```

如果你使用其他 skills 目录，把仓库放到对应目录下即可。目录结构应保持为：

```text
skills/
└── feishu-editable-diagrams/
    ├── SKILL.md
    ├── README.md
    └── agents/
```

安装后重启 agent，或重新打开会话，让 skill metadata 被重新加载。

## 怎么使用

在对话里直接提出“飞书可编辑图表”相关需求即可，例如：

```text
帮我在这个飞书文档里插入一个可编辑的流程图。
```

```text
把这张架构图做成飞书里可以编辑的白板，不要只是 PNG。
```

```text
更新这个飞书白板，保持里面的文字、方框和箭头都能继续编辑。
```

## 依赖条件

- 已安装 Node.js 和 npm。
- 已安装并认证 `lark-cli`。
- 可以通过 `npx` 使用 `@larksuite/whiteboard-cli`。
- 对目标飞书 / Lark 文档或白板有访问权限。
- 如果环境里有 `lark-doc`、`lark-whiteboard`、`lark-shared` 等 skill，应配合使用。

## 主要限制

- 这个 skill 处理的是可编辑图表，不负责照片修图、截图美化或纯图片设计。
- 复杂 SVG 特性可能无法稳定导入，例如滤镜、渐变、mask、clipPath、pattern、`foreignObject`。
- 自动换行不可靠，长文字应拆成多行独立 `<text>`。
- 更新已有白板前必须确认目标，不能静默覆盖已有内容。
- CLI 返回成功不代表最终效果正确，还需要导出飞书服务端预览进行检查。
- 如果遇到权限、scope 或登录问题，应先用飞书接入相关 skill 把认证和权限处理好。
