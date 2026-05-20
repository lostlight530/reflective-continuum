import unittest
from src.reflective_continuum.graph_db import GraphDB
from src.reflective_continuum.rules import RuleEngine
from src.reflective_continuum.cortex import Cortex

class TestArchitectureIntegration(unittest.TestCase):
    def setUp(self):
        self.db = GraphDB()
        self.rules = RuleEngine()
        # Set low entropy threshold to trigger phase change easily for testing
        self.cortex = Cortex(self.db, self.rules, max_depth=5, entropy_threshold=0.1)

    def test_full_reflection_cycle(self):
        """
        Tests the transition from Liquid to Gaseous and the self-consistency check.
        """
        # 1. Liquid Phase: Initial state
        self.cortex.process_input("A", "System start", [])
        self.assertEqual(self.cortex.phase, "LIQUID")

        # 2. Increase complexity to trigger Phase Boundary
        # Adding a triangle graph increases entropy
        self.cortex.process_input("B", "State mutation B", [("A", "B", "rel")])
        self.cortex.process_input("C", "State mutation C", [("B", "C", "rel"), ("C", "A", "rel")])

        # 3. Verify Gaseous Phase was triggered
        # Note: Depending on threshold, it might trigger and return to liquid if consistent
        # In our mock implementation, it verifies and remains in Gaseous if entropy is still high
        self.assertEqual(self.cortex.phase, "GASEOUS")
        self.assertGreater(self.cortex.current_depth, 0)

    def test_cognitive_rejection(self):
        """
        Tests that the system stops reflecting at max depth (ADR-002).
        """
        # Set max_depth to 1 for quick rejection test
        self.cortex.max_depth = 1

        # Trigger reflection
        self.cortex.process_input("A", "X", [])
        self.cortex.process_input("B", "Y", [("A", "B", "rel")])
        self.cortex.process_input("C", "Z", [("B", "C", "rel"), ("C", "A", "rel")])

        # After triggering depth 1, the phase should return to LIQUID
        self.assertEqual(self.cortex.phase, "LIQUID")

    def test_rule_violation_rollback(self):
        """
        Tests that a rule violation (e.g. non-stdlib code) causes a rollback.
        """
        # 1. Process a malicious node
        # It should be rejected because it contains 'import numpy'
        self.cortex.process_input("MALICIOUS", "import numpy", [])

        # 2. Verify that MALICIOUS node is NOT in the database
        nodes = self.db.get_all_nodes()
        self.assertNotIn("MALICIOUS", nodes)

        # 3. Process node that triggers reflection, but try to sneak in a violation later
        # (This tests the rollback of a mutation that triggers a reflection which then fails)
        self.cortex.process_input("A", "Valid content", [])
        self.cortex.process_input("B", "Valid content", [("A", "B", "rel")])

        # This one triggers reflection (due to triangle/entropy) but contains invalid code
        self.cortex.process_input("C", "import torch", [("B", "C", "rel"), ("C", "A", "rel")])

        nodes = self.db.get_all_nodes()
        self.assertNotIn("C", nodes)
        self.assertEqual(self.cortex.phase, "LIQUID")

if __name__ == "__main__":
    unittest.main()
