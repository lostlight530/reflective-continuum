import math
import unittest
from CODE.continuum_db import GraphDB
from CODE.drift_detector import compute_rank_delta, compute_semantic_delta, compute_structural_delta
from CODE.entropy_analyzer import calculate_topological_entropy, compute_pagerank


class AnalysisTests(unittest.TestCase):
    def test_pagerank_validates_and_normalizes(self):
        rank = compute_pagerank(["a", "b"], [("a", "b")])
        self.assertTrue(math.isclose(sum(rank.values()), 1.0))
        with self.assertRaises(ValueError):
            compute_pagerank(["a"], [("a", "missing")])
        with self.assertRaises(ValueError):
            calculate_topological_entropy([math.nan])

    def test_version_scoped_deltas_are_sorted(self):
        with GraphDB() as db:
            db.insert_node("same", "old safety", 1)
            db.insert_node("gone", "gone", 1)
            db.insert_node("same", "new safety", 2)
            db.insert_node("added", "added", 2)
            self.assertEqual(compute_structural_delta(db.conn, 1, 2), {"added": ["added"], "removed": ["gone"], "modified": ["same"]})
            self.assertFalse(compute_semantic_delta(db.conn, "safety", 1, 2))
        self.assertEqual(compute_rank_delta({"b": 0.1}, {"a": 0.2, "b": 0.3}, 0.15), ["a", "b"])