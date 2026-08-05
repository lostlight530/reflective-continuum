import sqlite3
import unittest
from CODE.continuum_db import GraphDB
from CODE.cortex_observer import CortexObserver
from CODE.reflective_validator import RuleConfig, RuleEngine


class ObserverTests(unittest.TestCase):
    def setUp(self):
        self.db = GraphDB()

    def tearDown(self):
        self.db.close()

    def test_low_entropy_input_commits(self):
        result = CortexObserver(self.db, RuleEngine()).process_input("a", "content", [])
        self.assertTrue(result.accepted)
        self.assertEqual(self.db.get_all_nodes(), ["a"])

    def test_depth_is_real_and_exhaustion_rolls_back(self):
        self.db.insert_node("base", "baseline")
        observer = CortexObserver(self.db, RuleEngine(), max_depth=2, entropy_threshold=0.0)
        result = observer.process_input("a", "content", [])
        self.assertFalse(result.accepted)
        self.assertEqual(result.reflection_depth, 2)
        self.assertEqual(result.reasons, ("reflection_depth_exhausted",))
        self.assertEqual(self.db.get_all_nodes(), ["base"])

    def test_database_errors_propagate_and_roll_back(self):
        observer = CortexObserver(self.db, RuleEngine())
        with self.assertRaises(sqlite3.IntegrityError):
            observer.process_input("a", "content", [("missing", "a", "rel")])
        self.assertEqual(self.db.get_all_nodes(), [])
