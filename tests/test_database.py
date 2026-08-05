import sqlite3
import unittest
from CODE.continuum_db import GraphDB


class DatabaseTests(unittest.TestCase):
    def setUp(self):
        self.db = GraphDB()

    def tearDown(self):
        self.db.close()

    def test_foreign_keys_and_edge_versions(self):
        self.assertEqual(self.db.conn.execute("PRAGMA foreign_keys").fetchone()[0], 1)
        with self.assertRaises(sqlite3.IntegrityError):
            self.db.insert_edge("missing", "also-missing", "rel")
        for version in (1, 2):
            self.db.insert_node("a", f"a{version}", version)
            self.db.insert_node("b", f"b{version}", version)
            self.db.insert_edge("a", "b", "rel", version)
        self.assertEqual(self.db.conn.execute("SELECT count(*) FROM edges").fetchone()[0], 2)

    def test_upsert_keeps_fts_synchronized(self):
        self.db.insert_node("a", "old phrase")
        self.assertEqual(self.db.semantic_search("old phrase")[0]["node_id"], "a")
        self.db.insert_node("a", "new phrase")
        self.assertEqual(self.db.semantic_search("old phrase"), [])
        self.assertEqual(self.db.semantic_search("new phrase")[0]["node_id"], "a")

    def test_savepoint_rejects_injection_and_releases_after_rollback(self):
        with self.assertRaises(ValueError):
            self.db.fork('bad"; DROP TABLE nodes;--')
        self.db.fork("safe")
        self.db.insert_node("x", "temporary", commit=False)
        self.db.rollback_fork("safe")
        self.db.fork("safe")
        self.db.commit_fork("safe")
        self.assertNotIn("x", self.db.get_all_nodes())