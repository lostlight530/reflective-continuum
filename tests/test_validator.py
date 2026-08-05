import unittest
from CODE.reflective_validator import RuleConfig, RuleEngine


class ValidatorTests(unittest.TestCase):
    def test_configuration_is_explicit(self):
        rules = RuleEngine("ADR", config=RuleConfig(max_reflection_depth=4, entropy_threshold=0.5))
        self.assertEqual(rules.constants, {"N": 4, "H_threshold": 0.5})
        self.assertEqual(rules.constraints, {})

    def test_ast_based_stdlib_check(self):
        rules = RuleEngine()
        self.assertTrue(rules.verify_stdlib_only("import json\nfrom pathlib import Path"))
        self.assertFalse(rules.verify_stdlib_only("import numpy as np"))
        self.assertFalse(rules.verify_stdlib_only("not valid python"))

    def test_validation_reasons_are_structured(self):
        result = RuleEngine().validate({"node_id": "", "content": ""})
        self.assertFalse(result.accepted)
        self.assertEqual(result.reasons, ("invalid_node_id", "invalid_content"))