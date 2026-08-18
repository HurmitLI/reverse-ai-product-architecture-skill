#!/usr/bin/env python3
"""Validate evidence boundaries and structural coverage in an HTML analysis."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


DEFAULT_SECTIONS = ["证据", "用户旅程", "Agent", "工具", "全局上下文"]
REQUIRED_LABEL_GROUPS = [
    ("【已确认】", "已确认"),
    ("【合理推断】", "合理推断"),
    ("【建议设计】", "建议设计"),
    ("【未知】", "未知"),
]
RISKY_PATTERNS = {
    "隐藏思维链断言": re.compile(r"(已经|已|成功)(读取|还原|展示).{0,8}(隐藏|内部)(思维链|推理链)"),
    "计划直接当执行": re.compile(r"计划.{0,12}(证明|确认).{0,8}(工具|调用).{0,6}(成功|完成)"),
    "不加边界的官方 Prompt": re.compile(r"(这是|还原出|以下为).{0,8}官方\s*System\s*Prompt"),
}


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an evidence-based AI product analysis HTML file.")
    parser.add_argument("html", type=Path)
    parser.add_argument("--require-section", action="append", default=[])
    args = parser.parse_args()

    path = args.html.expanduser().resolve()
    text = path.read_text(encoding="utf-8")
    errors: list[str] = []
    warnings: list[str] = []

    if "<html" not in text.lower() or "</html>" not in text.lower():
        errors.append("not a standalone HTML document")

    ids = re.findall(r'\bid=["\']([^"\']+)["\']', text)
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if duplicates:
        errors.append("duplicate ids: " + ", ".join(duplicates))

    for alternatives in REQUIRED_LABEL_GROUPS:
        if not any(label in text for label in alternatives):
            errors.append("missing evidence label: " + " / ".join(alternatives))

    for section in DEFAULT_SECTIONS + args.require_section:
        if section not in text:
            warnings.append(f"section keyword not found: {section}")

    if not re.search(r"S\d{2}", text):
        warnings.append("no screenshot evidence id like S01 found")
    if not re.search(r"E\d{2}", text):
        warnings.append("no synthesized evidence id like E01 found")

    for label, pattern in RISKY_PATTERNS.items():
        if pattern.search(text):
            errors.append(f"risky claim detected: {label}")

    print(f"file: {path}")
    print(f"bytes: {len(text.encode('utf-8'))}")
    print(f"ids: {len(ids)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        return 1
    print("OK: structural and evidence-boundary checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
