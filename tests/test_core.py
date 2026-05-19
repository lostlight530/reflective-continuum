import unittest
from src.reflective_continuum import delta, phase

class TestCognitiveDelta(unittest.TestCase):
    def test_structural_delta_deterministic(self):
        # Even without a real DB, the function must return an exact dictionary type
        result = delta.compute_structural_delta(None, "t1", "t2")
        self.assertIsInstance(result, dict)
        self.assertIn("added", result)

    def test_self_consistency_boolean(self):
        # Must return exactly True or False, no fuzzy logic
        result = delta.verify_self_consistency({}, ["RULE-1"])
        self.assertIsInstance(result, bool)

class TestPhaseBoundary(unittest.TestCase):
    def test_topological_entropy(self):
        # Given deterministic PageRank scores, entropy must be exact
        scores = [0.5, 0.5]
        entropy = phase.calculate_topological_entropy(scores)
        # - (0.5 * ln(0.5) + 0.5 * ln(0.5)) = 0.693147...
        self.assertAlmostEqual(entropy, 0.6931471805599453)

    def test_phase_transition_trigger(self):
        scores = [0.25, 0.25, 0.25, 0.25]
        # High entropy should trigger transition if above a low threshold
        self.assertTrue(phase.check_phase_boundary(scores, threshold=1.0))
        # Low entropy (or high threshold) should NOT trigger
        self.assertFalse(phase.check_phase_boundary(scores, threshold=2.0))

if __name__ == '__main__':
    unittest.main()
