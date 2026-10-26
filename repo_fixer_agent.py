#!/usr/bin/env python3
"""repo-fixer-agent: lightweight repository health checks."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def scan_repository(path: Path) -> list[str]:
    """Check a repository for common quality issues."""
    findings: list[str] = []

    if not path.exists():
        raise FileNotFoundError(f"Path does not exist: {path}")

    if not path.is_dir():
        raise NotADirectoryError(f"Expected a directory but got: {path}")

    if not (path / "README.md").exists():
        findings.append("README.md is missing")

    for file_path in path.rglob("*"):
        if not file_path.is_file():
            continue

        if ".git" in file_path.parts:
            continue

        try:
            text = file_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        if re.search(r"TODO|FIXME|XXX", text, flags=re.IGNORECASE):
            findings.append(f"{file_path.relative_to(path)} contains TODO/FIXME markers")

    if not findings:
        findings.append("No obvious issues found")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a repository for common issues.")
    parser.add_argument("--path", default=".", help="Path to the repository to scan")
    args = parser.parse_args()

    repo_path = Path(args.path).resolve()
    print(f"Repository scan for {repo_path}")

    try:
        findings = scan_repository(repo_path)
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(f"Error: {exc}")
        return 1

    print("\nIssues found:")
    for item in findings:
        print(f"- {item}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
