import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHECKOUT_SHA = "3d3c42e5aac5ba805825da76410c181273ba90b1"
SETUP_PYTHON_SHA = "5fda3b95a4ea91299a34e894583c3862153e4b97"


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

    def test_verified_action_runtime_pins(self):
        ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        pages = (ROOT / ".github" / "workflows" / "pages.yml").read_text(encoding="utf-8")
        checkout = f"actions/checkout@{CHECKOUT_SHA} # v7.0.1"
        setup_python = f"actions/setup-python@{SETUP_PYTHON_SHA} # v7.0.0"
        self.assertIn(checkout, ci)
        self.assertIn(checkout, pages)
        self.assertIn(setup_python, ci)

    def test_dependabot_groups_action_updates(self):
        text = (ROOT / ".github" / "dependabot.yml").read_text(encoding="utf-8")
        self.assertRegex(
            text,
            r'(?m)^    groups:\n      actions:\n        patterns:\n          - "\*"$',
        )

    def test_readme_claims_stay_within_evidence_scope(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        lowered = text.lower()
        for obsolete in (
            "metacognition",
            "metacognitive observer",
            "cognitive rollback",
            "gaseous phase",
            "\u5143\u8ba4\u77e5\u89c2\u5bdf\u5668",
            "proves cognition",
            "\u8bc1\u660e\u8ba4\u77e5",
        ):
            self.assertNotIn(obsolete, lowered)
        for link in (
            "[Engineering specification](SPECIFICATION.md)",
            "[Evidence baseline](EVIDENCE_BASELINE.md)",
            "[Reproducibility](REPRODUCIBILITY.md)",
            "[Security policy](SECURITY.md)",
        ):
            self.assertIn(link, text)
        for contract in (
            "SQLite",
            "FTS5",
            "PageRank-derived Shannon entropy",
            "Structural delta",
            "reflection hook",
            "Migration warning",
            "python -m CODE.tasks.cortex_selfcheck",
            "python -m CODE.tasks.convergence_drill --iterations 100",
            "Non-goals and ownership",
        ):
            self.assertIn(contract, text)