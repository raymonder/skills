#!/usr/bin/env python3
"""在研发项目约定文件中插入或更新精简 AI coding 规则。"""

from __future__ import annotations

import argparse
from pathlib import Path


START = "<!-- AI_CODING_AGENT_CORE_RULES:start -->"
END = "<!-- AI_CODING_AGENT_CORE_RULES:end -->"

DEFAULT_TARGETS = [
    "AGENTS.md",
    "cursor.md",
    "CLAUDE.md",
    "Claude.md",
    "CLOUD.md",
    "Cloud.md",
]

RULES = """## 研发项目 AI Coding Agent 核心规则

<!-- AI_CODING_AGENT_CORE_RULES:start -->
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
<!-- AI_CODING_AGENT_CORE_RULES:end -->
"""


def replace_block(text: str) -> tuple[str, bool]:
    start_index = text.find(START)
    end_index = text.find(END)
    if start_index == -1 or end_index == -1 or end_index < start_index:
        separator = "\n\n" if text.strip() else ""
        return text.rstrip() + separator + RULES, True

    end_index += len(END)
    new_text = text[:start_index]
    for heading in ["## AI Coding Agent 核心规则\n\n", "## 研发项目 AI Coding Agent 核心规则\n\n"]:
        if new_text.endswith(heading):
            new_text = new_text[: -len(heading)]
            break
    new_text = new_text.rstrip() + "\n\n" + RULES + text[end_index:].lstrip("\n")
    return new_text, new_text != text


def update_file(path: Path, dry_run: bool) -> bool:
    old_text = path.read_text(encoding="utf-8") if path.exists() else ""
    new_text, changed = replace_block(old_text)
    if changed and not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(new_text, encoding="utf-8")
    return changed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="要更新的研发项目仓库根目录")
    parser.add_argument("--targets", nargs="*", default=DEFAULT_TARGETS, help="相对仓库根目录的目标文件")
    parser.add_argument("--create-missing", action="store_true", help="创建所有缺失的目标文件")
    parser.add_argument("--dry-run", action="store_true", help="只打印计划改动，不写入文件")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    targets = [root / target for target in args.targets]
    existing = [path for path in targets if path.exists()]

    if args.create_missing:
        selected = targets
    elif existing:
        selected = existing
    else:
        selected = [root / "AGENTS.md"]

    changed = []
    unchanged = []
    for path in selected:
        if update_file(path, args.dry_run):
            changed.append(path)
        else:
            unchanged.append(path)

    action = "将更新" if args.dry_run else "已更新"
    for path in changed:
        print(f"{action}: {path}")
    for path in unchanged:
        print(f"未变化: {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
