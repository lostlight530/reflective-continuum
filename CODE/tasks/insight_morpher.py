import sys
from CODE.continuum_db import GraphDB
from CODE.cortex_observer import CortexObserver
from CODE.reflective_validator import RuleEngine

class InsightMorpher:
    """
    T-10 Synthesis: Ingestion and Morphing of External Signals.
    Processes external data points into strictly formatted structural nodes.
    """

    def __init__(self):
        self.db = GraphDB(":memory:")
        self.rules = RuleEngine()
        self.cortex = CortexObserver(self.db, self.rules)

    def morph_signals(self, raw_signals: list) -> bool:
        """
        Takes raw signals and deterministically morphs them into the Knowledge Graph.
        Returns True if all signals were successfully ingested without cognitive rejection.
        """
        print("[InsightMorpher] Initializing T-10 Synthesis...")
        success_count = 0

        for sig in raw_signals:
            node_id = sig.get("id")
            content = sig.get("content")
            edges = sig.get("edges", [])

            if not node_id or not content:
                print(f"[InsightMorpher] Warning: Invalid signal format: {sig}")
                continue

            print(f"[InsightMorpher] Morphing signal: {node_id}")
            # Process via the Cortex Observer to ensure phase transitions and rollback constraints apply
            self.cortex.process_input(node_id, content, edges)

            # Verify if the node actually made it into the DB (not rolled back)
            if node_id in self.db.get_all_nodes():
                success_count += 1
            else:
                print(f"[InsightMorpher] Signal {node_id} was rejected by Cortex constraints.")

        print(f"[InsightMorpher] Synthesis complete. Successfully ingested {success_count}/{len(raw_signals)} signals.")
        return success_count == len(raw_signals)

if __name__ == "__main__":
    # Test data representing industry signals
    test_signals = [
        {"id": "SIG_001", "content": "NVIDIA advances deterministic execution", "edges": []},
        {"id": "SIG_002", "content": "OpenAI test-time limits reached", "edges": [("SIG_001", "SIG_002", "contrasts")]}
    ]
    morpher = InsightMorpher()
    morpher.morph_signals(test_signals)
