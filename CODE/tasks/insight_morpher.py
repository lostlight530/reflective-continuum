import sys
import json
import os
from CODE.continuum_db import GraphDB
from CODE.cortex_observer import CortexObserver
from CODE.reflective_validator import RuleEngine

class InsightMorpher:
    """
    T-10 Synthesis: Ingestion and Morphing of External Signals.
    Processes external data points into strictly formatted structural nodes.
    Supports ingestion from file-based signals.
    """

    def __init__(self, db_path=":memory:"):
        self.db = GraphDB(db_path)
        self.rules = RuleEngine()
        self.cortex = CortexObserver(self.db, self.rules)

    def morph_from_file(self, file_path: str) -> bool:
        """Loads signals from a JSON file and morphs them."""
        if not os.path.exists(file_path):
            print(f"[InsightMorpher] Error: File not found {file_path}")
            return False

        with open(file_path, "r", encoding="utf-8") as f:
            try:
                signals = json.load(f)
                return self.morph_signals(signals)
            except Exception as e:
                print(f"[InsightMorpher] Error parsing {file_path}: {e}")
                return False

    def morph_signals(self, raw_signals: list) -> bool:
        """
        Takes raw signals and deterministically morphs them into the Knowledge Graph.
        Returns True if all signals were successfully ingested without cognitive rejection.
        """
        print(f"[InsightMorpher] Initializing T-10 Synthesis for {len(raw_signals)} signals...")
        success_count = 0

        for sig in raw_signals:
            node_id = sig.get("id")
            content = sig.get("content")
            edges = sig.get("edges", [])

            if not node_id or not content:
                print(f"[InsightMorpher] Warning: Invalid signal format: {sig}")
                continue

            print(f"[InsightMorpher] Morphing signal: {node_id}")
            self.cortex.process_input(node_id, content, edges)

            # Verify if the node actually made it into the DB (not rolled back)
            if node_id in self.db.get_all_nodes():
                success_count += 1
            else:
                print(f"[InsightMorpher] Signal {node_id} was rejected by Cortex constraints.")

        print(f"[InsightMorpher] Synthesis complete. Successfully ingested {success_count}/{len(raw_signals)} signals.")
        return success_count == len(raw_signals)

if __name__ == "__main__":
    # Example usage
    test_signals = [
        {"id": "SIG_2026_01", "content": "NVIDIA Blackwell B200 deterministic benchmarks", "edges": []},
        {"id": "SIG_2026_02", "content": "OpenAI o1 scaling limits observed", "edges": [("SIG_2026_01", "SIG_2026_02", "context")]}
    ]
    morpher = InsightMorpher()
    morpher.morph_signals(test_signals)
