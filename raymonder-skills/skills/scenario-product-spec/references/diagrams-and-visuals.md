# 给产品方案配图：流程图 + 效果图

文字写透后，在关键链路补图。**两类图、两个工具**，别混用。

---

## A. 流程图 / 状态机 / 时序图 → feishu-editable-diagrams

**何时用**：逻辑类图，且希望评审能在飞书里改框连线。典型场景：
- **状态机**：计划生命周期 Draft→Pending→Approved→Ended→Closed（带 Rework 回流）。
- **决策分支**：退款按付款方式分流（信用卡原路退 / 非卡一次性 URL）。
- **时序图**：在线报名+支付的跨系统调用（SSO→CCRM→Payment Hub→Account System）。
- **循环**：候补转正—超时顺延。

**为什么不用死图**：这些图评审常想改，做成可编辑白板（SVG → Feishu whiteboard）比 PNG 强。

### 操作步骤（依赖 feishu-editable-diagrams skill，先读它）

1. **验证工具与认证**：
   ```bash
   lark-cli --version && lark-cli auth status
   npx -y @larksuite/whiteboard-cli@^0.2.11 -v
   ```
   在 Cowork 沙盒里 lark-cli 跑不通时，通过 `mcp__Control_your_Mac__osascript` 在用户真机 shell 调用，每条命令前 `export PATH=$HOME/.npm-global/bin:$PATH`，并加 `--as user`。

2. **写 Feishu-friendly 的 `diagram.svg`**：只用 `<rect> <circle> <ellipse> <polygon> <line> <polyline> 简单<path> <text> <g>`；避开 `<filter> <gradient> <pattern> <clipPath> <mask> foreignObject`；每行文字用独立 `<text>`，不靠自动换行；转义 `&`→`&amp;`、`<`→`&lt;`；形状给足宽高留文字膨胀空间。**图标一律留空**（无填充、浅虚线小方框占位），由人后期在飞书填。

3. **三步校验**（缺一不可）：
   ```bash
   npx -y @larksuite/whiteboard-cli@^0.2.11 -i "$DIR/diagram.svg" -o "$DIR/diagram.png" -f svg
   npx -y @larksuite/whiteboard-cli@^0.2.11 -i "$DIR/diagram.svg" -f svg --check
   npx -y @larksuite/whiteboard-cli@^0.2.11 -i "$DIR/diagram.svg" -f svg --to openapi --format json > "$DIR/diagram.json"
   ```
   - `text-overflow`、`textOcclusion` 是**阻断项**，必须改（缩字号/拆行/加宽）。
   - `nodeOverlap` 仅在"父容器套子卡片"的刻意嵌套下可接受。
   - 先肉眼看 `diagram.png` 再动文档。

4. **插入飞书文档**（先 `--dry-run` 再真插）：
   ```bash
   (printf '<whiteboard type="svg">'; cat "$DIR/diagram.svg"; printf '</whiteboard>') \
     | lark-cli docs +update --api-version v2 --doc "$DOC_URL" \
         --command block_insert_after --block-id "$ANCHOR_BLOCK_ID" --content - --as user
   ```
   先用 `docs +fetch --detail with-ids --scope keyword --keyword "<锚点词>"` 找到插入锚点 block id。

5. **核对**：`lark-cli whiteboard +query --whiteboard-token "$TOKEN" --output_as image --output "$DIR" --overwrite --as user`，把服务端预览和本地图对一遍，服务端预览为准。

> Mermaid 备选：飞书也支持 `<whiteboard type="mermaid">…</whiteboard>` 直接写 sequenceDiagram/flowchart/gantt（箭头 `--&gt;`、`&` 写 `&amp;`、避免 `<br/>`；**不支持 quadrantChart**）。纯流程/时序若不需要后期可视化编辑，Mermaid 更快；需要在飞书改框连线就用上面的 SVG 白板。

---

## B. 效果图 / 概念图 / 精致配图 → gpt-image-2

**何时用**：观感类图。典型场景：
- 开篇**总览概念图**（四大目标 + 八大模块关系）。
- 模块的**界面效果示意 / UI mockup**。
- **架构 / 拓扑 / 集成关系**类精致配图。

**为什么用它**：GPT Image 2 出图精致、有冲击力，适合"给人看的观感图"，走用户已有的 ChatGPT 订阅、无额外计费。

### 操作步骤（依赖 gpt-image-2 skill）

1. 生成（prompt 原样传，别擅自加风格词，除非要）：
   ```bash
   bash scripts/gen.sh --prompt "<对图的描述>" --out /abs/path/out.png
   ```
   图-生-图（带参考图）：追加 `--ref /abs/ref.png`（可重复多张做多参考合成）。
   前提：用户真机装了 `codex` 且 `codex login` 过 ChatGPT Plus/Pro。Cowork 下经真机 shell 跑；生图是长任务，必要时 `nohup … &` 后台跑再轮询，避免 osascript 超时。

2. **配图文字默认用英文**（贴合此类投标方案"图内文字英文"的既定规范，除非用户另有要求）。

3. 插入飞书 docx（注意限制）：
   ```bash
   lark-cli docs +media-insert --doc "<docx URL，非 /wiki/>" --file ./out.png \
     --align center --caption '...' --width 1000 --as user
   ```
   - 媒体插入需要 **docx document_id**（不是 /wiki/ 链接）。
   - 只能插在**文末**，再用 `block_move_after` 挪到目标位置。
   - `--content/--file` 用相对路径：先 `cd` 到文件目录再 `--file ./x.png`。

---

## C. 选型速查

| 内容 | 工具 | 形态 |
|---|---|---|
| 状态机 / 决策分支 / 时序 / 循环，需可编辑 | feishu-editable-diagrams（SVG 白板） | 可编辑 |
| 纯流程/时序、不需后期编辑、要快 | Mermaid 白板 | 半可编辑 |
| 总览 / UI 效果 / 精致架构概念图 | gpt-image-2 | 精致位图 |

**配图克制**：一个模块通常 0–1 张图；只在文字说不清的复杂链路才配。先把字写透，图是补充不是主角。
