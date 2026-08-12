#!/usr/bin/env python3
"""以唯讀方式掃描香港繁體中文候選問題。"""

from __future__ import annotations

import argparse
import fnmatch
import json
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass(frozen=True)
class Rule:
    term: str
    suggestion: str
    category: str
    reason: str


@dataclass(frozen=True)
class Finding:
    path: str
    line: int | None
    column: int | None
    matched: str | None
    suggestion: str
    category: str
    reason: str


RULES = (
    Rule("乎合", "符合", "A", "明顯輸入或 OCR 錯誤"),
    Rule("户", "戶", "A", "簡體殘留"),
    Rule("用户", "用戶", "A", "簡體殘留"),
    Rule("账户", "帳戶", "A", "簡體殘留"),
    Rule("帐户", "帳戶", "A", "簡體殘留"),
    Rule("门户", "門戶", "A", "簡體殘留"),
    Rule("門户", "門戶", "A", "簡繁混用"),
    Rule("说明", "說明", "A", "簡體殘留"),
    Rule("説明", "說明", "B", "香港慣用字形"),
    Rule("查阅", "查閱", "A", "簡體殘留"),
    Rule("查閲", "查閱", "B", "香港慣用字形"),
    Rule("卫星", "衛星", "A", "簡體殘留"),
    Rule("衞星", "衛星", "B", "香港慣用字形"),
    Rule("群组", "群組", "A", "簡體殘留"),
    Rule("羣組", "群組", "B", "香港慣用字形"),
    Rule("设置", "設定", "A", "簡體殘留"),
    Rule("默认", "預設", "A", "簡體殘留"),
    Rule("导出", "匯出", "A", "簡體殘留；仍須分辨下載與匯出"),
    Rule("导入", "匯入", "A", "簡體殘留"),
    Rule("审批", "批核／審核／評核", "A", "簡體殘留；譯詞依流程決定"),
    Rule("自定义", "自訂", "A", "簡體殘留"),
    Rule("界面", "介面", "B", "香港產品文件較常用"),
    Rule("模块", "模組", "A", "簡體殘留"),
    Rule("志愿者", "義工", "A", "簡體殘留；香港社福語境通常用義工"),
    Rule("志願者", "義工", "B", "香港社福語境通常用義工"),
    Rule("登录", "登入", "A", "簡體殘留"),
    Rule("登錄", "登入", "B", "香港產品介面較常用"),
    Rule("邮件", "電郵", "A", "簡體殘留"),
    Rule("郵件", "電郵", "B", "香港一般用語"),
    Rule("邮箱", "電郵地址", "A", "簡體殘留"),
    Rule("郵箱", "電郵地址", "B", "香港一般用語"),
    Rule("访问控制", "存取控制", "A", "簡體殘留"),
    Rule("兼容", "相容", "A", "簡體殘留"),
    Rule("日志", "日誌", "A", "簡體殘留"),
    Rule("回滚", "還原／回滾", "A", "簡體殘留；技術語境依項目統一"),
    Rule("羣", "群", "B", "香港慣用字形"),
    Rule("説", "說", "B", "香港慣用字形"),
    Rule("閲", "閱", "B", "香港慣用字形"),
    Rule("衞", "衛", "B", "香港慣用字形"),
    Rule("爲", "為", "B", "香港慣用字形"),
    Rule("啓", "啟", "B", "香港慣用字形"),
    Rule("模板", "範本", "C", "依客戶及項目字彙表統一"),
    Rule("排班", "編更／排更", "D", "依義工服務流程及客戶用語判斷"),
    Rule("值班", "當值", "D", "依義工服務流程及客戶用語判斷"),
    Rule("數據", "資料／數據", "D", "泛指 data 可用資料；統計數字可用數據"),
    Rule("文件", "文件／檔案", "D", "正式文書用文件；computer file 常用檔案"),
    Rule("下載", "下載／匯出", "D", "取得既有檔案用下載；產生輸出檔用匯出"),
    Rule("審核", "審核／批核／評核", "D", "依內容檢查、行政批准或表現評估判斷"),
)

TEXT_SUFFIXES = {
    ".arb", ".c", ".conf", ".cpp", ".cs", ".css", ".csv", ".go", ".h", ".html",
    ".ini", ".java", ".js", ".json", ".jsx", ".kt", ".lua", ".md", ".mdx", ".php",
    ".po", ".pot", ".properties", ".py", ".rb", ".resx", ".rs", ".rst", ".sh", ".sql",
    ".srt", ".strings", ".svg", ".swift", ".toml", ".ts", ".tsx", ".txt", ".vue",
    ".vtt", ".xml", ".yaml", ".yml",
}
IMAGE_SUFFIXES = {".avif", ".bmp", ".gif", ".heic", ".jpeg", ".jpg", ".png", ".tif", ".tiff", ".webp"}
RESOURCE_SUFFIXES = {".doc", ".docx", ".key", ".numbers", ".pages", ".pdf", ".ppt", ".pptx", ".xls", ".xlsx"}
SKIP_DIRS = {
    ".git", ".hg", ".svn", ".next", ".nuxt", ".pytest_cache", ".tox",
    ".venv", "__pycache__", "build", "coverage", "dist", "node_modules", "target", "vendor",
}


def is_ignored(path: Path, root: Path, patterns: list[str]) -> bool:
    rel = path.relative_to(root).as_posix() if path != root else "."
    return any(fnmatch.fnmatch(rel, pattern) or fnmatch.fnmatch(path.name, pattern) for pattern in patterns)


def iter_files(targets: list[Path], patterns: list[str]):
    seen: set[Path] = set()
    for target in targets:
        if target.is_file():
            resolved = target.resolve()
            if resolved not in seen:
                seen.add(resolved)
                yield resolved, target.parent.resolve()
            continue
        root = target.resolve()
        for path in root.rglob("*"):
            if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
                continue
            if path.is_file() and not is_ignored(path, root, patterns):
                resolved = path.resolve()
                if resolved not in seen:
                    seen.add(resolved)
                    yield resolved, root


def scan_text(path: Path, display_path: str, allowed_terms: set[str]) -> list[Finding]:
    try:
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        return []

    findings: list[Finding] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        occupied: list[tuple[int, int]] = []
        for rule in sorted(RULES, key=lambda item: len(item.term), reverse=True):
            if rule.term in allowed_terms:
                continue
            start = 0
            while True:
                column = line.find(rule.term, start)
                if column == -1:
                    break
                end = column + len(rule.term)
                start = end
                if any(column < used_end and end > used_start for used_start, used_end in occupied):
                    continue
                findings.append(Finding(
                    path=display_path,
                    line=line_number,
                    column=column + 1,
                    matched=rule.term,
                    suggestion=rule.suggestion,
                    category=rule.category,
                    reason=rule.reason,
                ))
                occupied.append((column, end))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="要掃描的檔案或目錄")
    parser.add_argument("--ignore", action="append", default=[], metavar="GLOB", help="額外略過的相對路徑 glob，可重複使用")
    parser.add_argument("--allow", action="append", default=[], metavar="TERM", help="視為項目既定用語而不報告的詞，可重複使用")
    parser.add_argument("--format", choices=("text", "json"), default="text", help="輸出格式")
    parser.add_argument("--no-image-list", action="store_true", help="不要列出待人工檢查的圖片")
    args = parser.parse_args()

    targets = [Path(value).expanduser() for value in args.paths]
    missing = [str(path) for path in targets if not path.exists()]
    if missing:
        print(f"找不到路徑: {', '.join(missing)}", file=sys.stderr)
        return 2

    findings: list[Finding] = []
    scanned_files = 0
    for path, root in iter_files(targets, args.ignore):
        display_path = path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)
        suffix = path.suffix.lower()
        if suffix in IMAGE_SUFFIXES and not args.no_image_list:
            findings.append(Finding(display_path, None, None, None, "人工預覽／OCR 檢查", "IMAGE", "圖片只報告，未經授權不得修改"))
        elif suffix in TEXT_SUFFIXES or path.name in {"Dockerfile", "Makefile"}:
            scanned_files += 1
            findings.extend(scan_text(path, display_path, set(args.allow)))

        elif suffix in RESOURCE_SUFFIXES:
            findings.append(Finding(display_path, None, None, None, "使用相應工具檢查完整結構", "RESOURCE", "容器文件不可只靠純文字掃描"))

    order = {"A": 0, "B": 1, "C": 2, "D": 3, "IMAGE": 4, "RESOURCE": 5}
    findings.sort(key=lambda item: (order[item.category], item.path, item.line or 0, item.column or 0))

    if args.format == "json":
        print(json.dumps({"scanned_text_files": scanned_files, "findings": [asdict(item) for item in findings]}, ensure_ascii=False, indent=2))
    else:
        print(f"已掃描文字檔: {scanned_files}")
        if not findings:
            print("未發現規則命中；仍須人工覆檢上下文及非文字資源。")
        for item in findings:
            location = item.path if item.line is None else f"{item.path}:{item.line}:{item.column}"
            matched = "" if item.matched is None else f"「{item.matched}」 -> "
            print(f"[{item.category}] {location}: {matched}{item.suggestion} ({item.reason})")

    return 1 if any(item.category == "A" for item in findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
