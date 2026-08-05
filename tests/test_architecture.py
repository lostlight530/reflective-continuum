import unittest
import CODE
from CODE.reflective_validator import RuleConfig, RuleEngine


class ArchitectureContractTests(unittest.TestCase):
    def test_public_api_is_explicit(self):
        self.assertEqual(set(CODE.__all__), {"CortexObserver", "GraphDB", "ProcessResult", "RuleConfig", "RuleEngine", "ValidationResult"})

    def test_documentation_cannot_change_runtime_policy(self):
        rules = RuleEngine("ADR", config=RuleConfig(max_reflection_depth=5, entropy_threshold=0.25))
        self.assertEqual(rules.constants, {"N": 5, "H_threshold": 0.25})
        self.assertEqual(rules.constraints, {})