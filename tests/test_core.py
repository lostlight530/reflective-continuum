import unittest
from CODE.continuum_db import GraphDB
from CODE.cortex_observer import CortexObserver
from CODE.reflective_validator import RuleEngine


class CoreIntegrationTests(unittest.TestCase):
    def test_versioned_ingestion_and_snapshot(self):
        with GraphDB() as db:
            observer = CortexObserver(db, RuleEngine(), entropy_threshold=10.0)
            self.assertTrue(observer.process_input("a", "version one", [], 1).accepted)
            self.assertTrue(observer.process_input("a", "version two", [], 2).accepted)
            self.assertNotEqual(db.snapshot_digest(1), db.snapshot_digest(2))

    def test_invalid_policy_input_does_not_mutate(self):
        with GraphDB() as db:
            result = CortexObserver(db, RuleEngine()).process_input("", "", [])
            self.assertFalse(result.accepted)
            self.assertEqual(db.get_all_nodes(), [])