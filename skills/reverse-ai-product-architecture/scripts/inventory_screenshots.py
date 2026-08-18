#!/usr/bin/env python3
"""Build a deterministic screenshot evidence manifest without external packages."""

from __future__ import annotations

import argparse
import csv
import struct
from pathlib import Path


SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".gif"}


def image_size(path: Path) -> tuple[int | None, int | None]:
    with path.open("rb") as file:
        head = file.read(32)
        if head.startswith(b"\x89PNG\r\n\x1a\n") and len(head) >= 24:
            return struct.unpack(">II", head[16:24])
        if head[:6] in (b"GIF87a", b"GIF89a") and len(head) >= 10:
            return struct.unpack("<HH", head[6:10])
        if head.startswith(b"RIFF") and head[8:12] == b"WEBP":
            return None, None
        if head.startswith(b"\xff\xd8"):
            file.seek(2)
            while True:
                byte = file.read(1)
                if not byte:
                    break
                if byte != b"\xff":
                    continue
                marker = file.read(1)
                while marker == b"\xff":
                    marker = file.read(1)
                if marker in {b"\xd8", b"\xd9"}:
                    continue
                length_raw = file.read(2)
                if len(length_raw) != 2:
                    break
                length = struct.unpack(">H", length_raw)[0]
                if marker and marker[0] in range(0xC0, 0xC4):
                    data = file.read(5)
                    if len(data) == 5:
                        height, width = struct.unpack(">HH", data[1:5])
                        return width, height
                    break
                file.seek(max(length - 2, 0), 1)
    return None, None


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a CSV manifest for screenshot evidence.")
    parser.add_argument("directory", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    root = args.directory.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    files = sorted(
        (path for path in root.rglob("*") if path.is_file() and path.suffix.lower() in SUPPORTED),
        key=lambda path: path.relative_to(root).as_posix().lower(),
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["evidence_id", "relative_path", "filename", "width", "height", "notes"])
        for index, path in enumerate(files, 1):
            width, height = image_size(path)
            writer.writerow(
                [
                    f"S{index:02d}",
                    path.relative_to(root).as_posix(),
                    path.name,
                    width or "",
                    height or "",
                    "",
                ]
            )
    print(f"wrote {len(files)} evidence rows to {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
