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