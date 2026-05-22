import sys
from CODE.continuum_db import GraphDB
from CODE.drift_detector import compute_semantic_delta

class SemanticDriftAudit:
    """
    T-06 Analysis: Weekly Semantic Drift Audit.
    Evaluates whether the core intent (semantics) of key terms has drifted
    across versions using FTS5 deterministic search ranking.
    """

    def __init__(self):
        self.db = GraphDB(":memory:")
        self._seed_data()

    def _seed_data(self):
        """Seeds the in-memory database with versioned data for auditing."""
        # Version 1 (Baseline)
        self.db.insert_node("Core_Concept_1", "Determinism means predictable rules.", version=1)
        self.db.insert_node("Core_Concept_2", "AI safety requires observability.", version=1)

        # Version 2 (Drifted State)
        # Core_Concept_1 changes slightly but keeps the same keyword
        self.db.insert_node("Core_Concept_1", "Determinism in modern AI is about predictable rules.", version=2)
        # A new node becomes highly relevant to "safety"
        self.db.insert_node("Core_Concept_3", "AI safety is exclusively achieved via rollback constraints.", version=2)

    def run_audit(self, query: str) -> bool:
        """
        Executes the drift audit for a specific query.
        Returns True if drift is detected (top result changed).
        """
        print(f"[SemanticDriftAudit] Initiating T-06 Analysis for query: '{query}'")

        drifted = compute_semantic_delta(self.db.conn, query, v1=1, v2=2)

        if drifted:
            print(f"[SemanticDriftAudit] ALERT: Semantic drift detected for query '{query}' between V1 and V2.")
        else:
            print(f"[SemanticDriftAudit] OK: Semantic stability maintained for query '{query}'.")

        return drifted

if __name__ == "__main__":
    audit = SemanticDriftAudit()

    # Check a stable query
    audit.run_audit("predictable rules")

    # Check a query designed to drift based on seeded data
    audit.run_audit("safety")
