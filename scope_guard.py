"""Reject changes to separately owned repository paths."""
from __future__ import annotations
import argparse
import subprocess

PROTECTED_FILES = {"README.md", "index.html", ".nojekyll", "LICENSE"}
PROTECTED_PREFIXES = ("RESEARCH/",)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref", required=True)
    base = parser.parse_args().base_ref
    result = subprocess.run(["git", "diff", "--name-only", f"{base}...HEAD"], check=True, capture_output=True, text=True, encoding="utf-8")
    paths = [line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()]
    blocked = [path for path in paths if path in PROTECTED_FILES or path.startswith(PROTECTED_PREFIXES)]
    if blocked:
        print("protected path changes:\n" + "\n".join(blocked))
        return 1
    print("protected path scope: passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())