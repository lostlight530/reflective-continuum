import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_document_contracts(self):
        for path in sorted((ROOT / "ADR").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            for heading in ("## Status", "## Context", "## Decision", "## Consequences", "## Verification"):
                self.assertIn(heading, text, path)
        for path in sorted((ROOT / "METHODOLOGY").glob("*.md")):
            text = path.read_text(encoding="utf-8")
            for heading in ("## Inputs", "## Procedure", "## Outputs", "## Failure conditions"):
                self.assertIn(heading, text, path)

    def test_schemas_are_closed(self):
        for path in (ROOT / "schemas").glob("*.json"):
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["$schema"], "https://json-schema.org/draft/2020-12/schema")
            self.assertFalse(data["additionalProperties"])

    def test_actions_use_full_sha(self):
        for path in (ROOT / ".github" / "workflows").glob("*.yml"):
            for line in path.read_text(encoding="utf-8").splitlines():
                if "uses:" in line:
                    self.assertRegex(line, r"uses:\s+[\w.-]+/[\w.-]+@[0-9a-f]{40}(?:\s+#.*)?$")