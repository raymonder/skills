---
name: feishu-editable-diagrams
description: Use when creating, converting, inserting, or updating SVG-based editable diagrams in Feishu/Lark documents or whiteboards, especially when the user wants boxes, text, arrows, and layout elements to remain editable instead of becoming a static PNG/JPG.
metadata:
  version: "0.9"
---

# Feishu Editable Diagrams

## Overview

Create diagrams as SVG first, then import the SVG into Feishu as an editable whiteboard. Prefer this workflow whenever the user wants to edit boxes, text, arrows, containers, labels, or placeholders inside Feishu.

Use static PNG/JPG only when the user explicitly wants a non-editable image, or when the content is a photo/screenshot that should remain a raster asset.

Also use the `lark-doc`, `lark-whiteboard`, and `lark-shared` skills when available.

## Workflow

### 1. Verify Tools And Auth

Run these before touching the document:

```bash
lark-cli --version
lark-cli auth status
npx -y @larksuite/whiteboard-cli@^0.2.11 -v
```

Use `--as user` for user-owned Feishu docs. If auth is missing or scopes are denied, switch to `feishu-setup` / `lark-shared`.

### 2. Choose The Target Operation

Use one of these routes:

- Insert a new editable diagram into a document: create `diagram.svg`, wrap it in `<whiteboard type="svg">...</whiteboard>`, and insert it with `lark-cli docs +update`.
- Append a new editable diagram to the end of a document: use the same SVG wrapper and append or insert after the final block.
- Update an existing whiteboard: convert `diagram.svg` to OpenAPI JSON and update with `lark-cli whiteboard +update`.
- Keep external icons/screenshots as placeholders unless the user specifically provides raster assets to embed later.
If the user gives a document URL and a desired location, fetch nearby blocks to find the insertion anchor:

```bash
lark-cli docs +fetch --api-version v2 \
  --doc "$DOC_URL_OR_TOKEN" \
  --scope keyword \
  --keyword "$ANCHOR_KEYWORD" \
  --context-before 2 --context-after 2 \
  --detail with-ids \
  --as user
```

Extract the block id you will insert after. If the user does not provide a location and appending is acceptable, insert at the end of the document.

### 3. Create Feishu-Friendly SVG

Create a local artifact directory:

```bash
mkdir -p "diagrams/$(date +%Y-%m-%dT%H%M%S)-$SLUG"
```

Write `diagram.svg` with parser-friendly SVG:

- Use: `<rect>`, `<circle>`, `<ellipse>`, `<polygon>`, `<line>`, `<polyline>`, simple `<path>`, `<text>`, `<g>`.
- Avoid: `<filter>`, `<radialGradient>`, `<linearGradient>`, `<pattern>`, `<clipPath>`, `<mask>`, `foreignObject`.
- Use real `<text>` nodes instead of outlined text.
- Use separate `<text>` elements for separate lines; do not rely on automatic wrapping.
- Escape text content: `&` -> `&amp;`, `<` -> `&lt;`.
- Prefer inline attributes such as `fill`, `stroke`, `stroke-width`, `font-size`, and `font-family`; avoid complex CSS selectors.
- Give shapes enough width and height for text expansion after import.
- Leave clear placeholder rectangles/circles for icons or screenshots when the user plans to paste those assets manually.
### 4. Render, Check, And Export

Run all three commands before inserting into Feishu:

```bash
npx -y @larksuite/whiteboard-cli@^0.2.11 \
  -i "$DIR/diagram.svg" \
  -o "$DIR/diagram.png" \
  -f svg

npx -y @larksuite/whiteboard-cli@^0.2.11 \
  -i "$DIR/diagram.svg" \
  -f svg \
  --check

npx -y @larksuite/whiteboard-cli@^0.2.11 \
  -i "$DIR/diagram.svg" \
  -f svg \
  --to openapi \
  --format json > "$DIR/diagram.json"
```

Inspect `diagram.png` visually before touching the document.

Validation rules:

- `text-overflow` errors are blocking. Fix spacing, font size, or line breaks.
- `textOcclusion` is blocking.
- `nodeOverlap` warnings are acceptable only for deliberate parent-child nesting, such as a container rectangle holding inner cards. Verify with preview and, if needed:
```bash
jq -r '.data.result.nodes[] | select(.id=="NODE_ID") | {id,type,x,y,width,height,text:(.text.text // ""),shape:(.composite_shape.type // "")}' "$DIR/diagram.json"
```

Confirm editability:

```bash
jq '.data.result.nodes | length' "$DIR/diagram.json"
jq '.. | objects | select(has("type")) | .type' "$DIR/diagram.json" | sort | uniq -c
```

A good result has multiple native nodes such as `text_shape`, `composite_shape`, and connector-like lines. A single embedded image node is not acceptable when the user asked for editable content.

### 5. Insert A New Diagram Into A Feishu Doc

Wrap the SVG as a Feishu whiteboard block. Always dry-run before the real edit:

```bash
(printf '<whiteboard type="svg">'; cat "$DIR/diagram.svg"; printf '</whiteboard>') \
  | lark-cli docs +update --api-version v2 \
      --doc "$DOC_URL_OR_TOKEN" \
      --command block_insert_after \
      --block-id "$ANCHOR_BLOCK_ID" \
      --content - \
      --dry-run \
      --as user
```

If the dry-run targets the correct document and block, execute without `--dry-run`:

```bash
(printf '<whiteboard type="svg">'; cat "$DIR/diagram.svg"; printf '</whiteboard>') \
  | lark-cli docs +update --api-version v2 \
      --doc "$DOC_URL_OR_TOKEN" \
      --command block_insert_after \
      --block-id "$ANCHOR_BLOCK_ID" \
      --content - \
      --as user
```

Capture `data.document.new_blocks[0].block_token`; this is the new whiteboard token.

If appending to the end of a document, use the document's supported append command or insert after the final block returned by `docs +fetch --detail with-ids`.

### 6. Update An Existing Whiteboard

Do not overwrite an existing whiteboard silently. Query it first:

```bash
lark-cli whiteboard +query \
  --whiteboard-token "$TOKEN" \
  --output_as image \
  --output "$DIR" \
  --overwrite \
  --as user

lark-cli whiteboard +query \
  --whiteboard-token "$TOKEN" \
  --output_as code \
  --as user
```

Convert the SVG to OpenAPI JSON:

```bash
npx -y @larksuite/whiteboard-cli@^0.2.11 \
  -i "$DIR/diagram.svg" \
  -f svg \
  --to openapi \
  --format json > "$DIR/diagram.json"
```

Dry-run the update:

```bash
cat "$DIR/diagram.json" | lark-cli whiteboard +update \
  --whiteboard-token "$TOKEN" \
  --source - \
  --input_format raw \
  --idempotent-token "$UNIQUE_TOKEN" \
  --overwrite \
  --dry-run \
  --as user
```

If existing nodes will be deleted or replaced, get explicit user confirmation before the real update.

### 7. Verify In Feishu

Export the server-rendered whiteboard preview:

```bash
lark-cli whiteboard +query \
  --whiteboard-token "$NEW_WHITEBOARD_TOKEN" \
  --output_as image \
  --output "$VERIFY_DIR" \
  --overwrite \
  --as user
```

Open the exported image and compare against the local preview. Report:

- insertion anchor block id, if relevant
- whiteboard token
- local `diagram.svg`, `diagram.json`, and server preview paths
- any known caveats, such as placeholder icons or deliberate container overlap warnings
## Adjustment Loop

- If text overflows, split the label into shorter `<text>` lines, reduce font size, or widen the container.
- If nodes overlap unintentionally, adjust coordinates and dimensions in the SVG, then rerun render/check/export.
- If colors or strokes do not survive import, replace CSS classes with inline SVG attributes.
- If the imported result becomes one image-like node, remove unsupported SVG features and simplify into native primitives.
- If the Feishu server preview differs from the local preview, treat the server preview as authoritative and adjust the SVG.
## Common Pitfalls

- Always use `--content -` or `--source -` for large SVG/JSON payloads.
- Do not upload PNG/JPG when the user asked for an editable diagram.
- Do not overwrite, delete, or replace existing whiteboard content unless explicitly requested.
- Do not trust CLI success alone; always export and inspect the Feishu server preview.
- Keep generated content generic unless the user provides the subject matter or a reference style.
- If `lark-cli` prints an update notice, mention it after finishing; do not let it block the current task unless the command fails.
