"""Reject changes to separately owned repository paths."""
from __future__ import annotations

import argparse
import subprocess

PROTECTED_FILES = {"README.md", "index.html", ".nojekyll", "LICENSE"}
PROTECTED_PREFIXES = ("RESEARCH/",)


def blocked_paths(
    paths: list[str], allowed_files: set[str] | None = None
) -> list[str]:
    """Return protected paths not explicitly allowed for this invocation."""
    allowed_files = allowed_files or set()
    return [
        path
        for path in paths
        if (path in PROTECTED_FILES and path not in allowed_files)
        or path.startswith(PROTECTED_PREFIXES)
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    parser.add_argument("--allow-file", action="append", default=[])
    args = parser.parse_args()
    result = subprocess.run(
        ["git", "diff", "--name-only", f"{args.base_ref}..HEAD"],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    paths = [
        line.strip().replace("\\", "/")
        for line in result.stdout.splitlines()
        if line.strip()
    ]
    blocked = blocked_paths(paths, set(args.allow_file))
    if blocked:
        print("protected path changes:\n" + "\n".join(blocked))
        return 1
    print("protected path scope: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())