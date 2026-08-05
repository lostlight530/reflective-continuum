import tempfile
import unittest
from pathlib import Path
from CODE.continuum_db import GraphDB
from CODE.tasks.convergence_drill import run_drill
from CODE.tasks.cortex_selfcheck import selfcheck
from CODE.tasks.semantic_drift_audit import run_audit


class TaskTests(unittest.TestCase):
    def test_repeatability_claim_is_scoped(self):
        result = run_drill(3)
        self.assertTrue(result["repeatable"])
        self.assertEqual(result["scope"], "fixed local SQLite fixture")

    def test_selfcheck_uses_observed_values(self):
        result = selfcheck()
        self.assertTrue(result["healthy"])
        self.assertEqual(result["counts"], {"nodes": 0, "edges": 0})

    def test_audit_does_not_write_implicitly(self):
        uri = "file:reflective_audit_test?mode=memory&cache=shared"
        before = set(Path.cwd().iterdir())
        with GraphDB(uri) as db:
            db.insert_node("a", "safety old", 1)
            db.insert_node("a", "safety new", 2)
            report = run_audit(uri, ["safety"], 1, 2)
        self.assertEqual(report["database"], uri)
        self.assertEqual(set(Path.cwd().iterdir()), before)