import unittest
from CODE import differential as delta, thermodynamics as phase
from CODE.substrate import GraphDB

class TestCognitiveDelta(unittest.TestCase):

    def setUp(self):
        self.db = GraphDB(":memory:")

        # Version 1 setup
        self.db.insert_node("A", "The capital of France is Paris.", version=1)
        self.db.insert_node("B", "Reflective Continuum avoids probabilities.", version=1)

        # Version 2 setup
        self.db.insert_node("B", "Reflective Continuum uses strict determinism.", version=2) # Modified
        self.db.insert_node("C", "New axiom established.", version=2) # Added
        # A is not present in version 2 (Removed logically from that snapshot for test)

    def tearDown(self):
        self.db.close()

    def test_structural_delta_deterministic(self):
        diff = delta.compute_structural_delta(self.db.conn, 1, 2)

        self.assertIn("A", diff["removed"])
        self.assertIn("C", diff["added"])
        self.assertIn("B", diff["modified"])

    def test_semantic_delta_drift(self):
        # In version 1, searching "Reflective Continuum" should return node B
        # In version 2, searching "Reflective Continuum" should also return node B
        # Since the top result node_id is the same across versions, drift should be False.
        drift_b = delta.compute_semantic_delta(self.db.conn, "Reflective Continuum", 1, 2)
        self.assertFalse(drift_b)

        # In version 1, searching "Paris" returns node A.
        # In version 2, searching "Paris" returns nothing (A is deleted).
        # Drift should be True because the top results (A vs None) differ.
        drift_a = delta.compute_semantic_delta(self.db.conn, "Paris", 1, 2)
        self.assertTrue(drift_a)

    def test_self_consistency_boolean(self):
        class MockRuleEngine:
            def verify_consistency(self, delta): return True
        result = delta.verify_self_consistency({}, MockRuleEngine())
        self.assertIsInstance(result, bool)

class TestPhaseBoundary(unittest.TestCase):

    def test_pure_pagerank(self):
        nodes = ["A", "B", "C"]
        edges = [("A", "B"), ("B", "C"), ("C", "A")] # Cycle

        pr = phase.compute_pagerank(nodes, edges, damping=0.85, max_iterations=50)

        # In a perfect cycle, all nodes should converge to 1/3
        for node in nodes:
            self.assertAlmostEqual(pr[node], 1.0/3.0, places=5)

    def test_topological_entropy(self):
        scores = [0.5, 0.5]
        entropy = phase.calculate_topological_entropy(scores)
        self.assertAlmostEqual(entropy, 0.6931471805599453)

    def test_phase_transition_trigger(self):
        pr_dict = {"A": 0.25, "B": 0.25, "C": 0.25, "D": 0.25}

        # High entropy should trigger transition if above a low threshold
        self.assertTrue(phase.check_phase_boundary(pr_dict, threshold=1.0))
        # Low entropy (or high threshold) should NOT trigger
        self.assertFalse(phase.check_phase_boundary(pr_dict, threshold=2.0))

if __name__ == '__main__':
    unittest.main()
