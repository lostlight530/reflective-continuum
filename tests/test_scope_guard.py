"""Tests for protected repository path ownership."""
import unittest
from unittest.mock import patch

from scope_guard import blocked_paths, main


class ScopeGuardTests(unittest.TestCase):
    def test_readme_is_blocked_by_default(self) -> None:
        self.assertEqual(blocked_paths(["README.md"]), ["README.md"])

    def test_readme_can_be_explicitly_allowed(self) -> None:
        self.assertEqual(blocked_paths(["README.md"], {"README.md"}), [])

    def test_other_protected_paths_remain_blocked_when_readme_is_allowed(self) -> None:
        paths = ["index.html", ".nojekyll", "LICENSE", "RESEARCH/daily/x.md"]
        self.assertEqual(blocked_paths(paths, {"README.md"}), paths)

    def test_explicit_research_allowlist_is_exact(self) -> None:
        target = "RESEARCH/daily/2026-11-07-dehydrated-report.md"
        sibling = "RESEARCH/daily/2026-11-07-cortex-selfcheck.md"
        unrelated = "RESEARCH/monthly/2026-11-architecture-audit.md"
        self.assertEqual(blocked_paths([target], {target}), [])
        self.assertEqual(
            blocked_paths([target, sibling, unrelated], {target}),
            [sibling, unrelated],
        )

    def test_allowing_research_file_does_not_allow_root_controls(self) -> None:
        target = "RESEARCH/daily/2026-11-07-cortex-selfcheck.md"
        self.assertEqual(
            blocked_paths([target, "README.md", "LICENSE"], {target}),
            ["README.md", "LICENSE"],
        )

    def test_research_directory_name_is_not_a_wildcard_allowance(self) -> None:
        target = "RESEARCH/daily/2026-11-07-cortex-selfcheck.md"
        self.assertEqual(
            blocked_paths([target], {"RESEARCH/", "RESEARCH/daily/"}),
            [target],
        )

    @patch("scope_guard.subprocess.run")
    def test_cli_repeated_exact_research_allowances(self, run: object) -> None:
        run.return_value.stdout = (
            "RESEARCH/daily/2026-11-07-dehydrated-report.md\n"
            "RESEARCH/daily/2026-11-07-cortex-selfcheck.md\n"
        )
        with patch(
            "sys.argv",
            [
                "scope_guard.py",
                "--base-ref",
                "exact-base",
                "--allow-file",
                "RESEARCH/daily/2026-11-07-dehydrated-report.md",
                "--allow-file",
                "RESEARCH/daily/2026-11-07-cortex-selfcheck.md",
            ],
        ):
            self.assertEqual(main(), 0)

    @patch("scope_guard.subprocess.run")
    def test_allow_file_can_be_repeated(self, run: object) -> None:
        run.return_value.stdout = "README.md\nLICENSE\n"
        with patch(
            "sys.argv",
            [
                "scope_guard.py",
                "--base-ref",
                "base",
                "--allow-file",
                "README.md",
                "--allow-file",
                "LICENSE",
            ],
        ):
            self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()