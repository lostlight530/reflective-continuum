import os
import sys
import hashlib
from CODE.continuum_db import GraphDB
from CODE.reflective_validator import RuleEngine
from CODE.cortex_observer import CortexObserver

class ConvergenceDrill:
    """
    T-07 Grounding: Metacognitive Convergence Drill.
    Verifies that self-reflection leads to deterministic stable states.
    Ensures that identical inputs always result in the identical system state hash.
    """

    def __init__(self, iterations: int = 100):
        self.iterations = iterations

    def run_drill(self) -> bool:
        print(f"[ConvergenceDrill] Initializing T-07 Grounding ({self.iterations} iterations)...")

        final_states = []

        # Hardcoded deterministic input sequence
        inputs = [
            ("Node_A", "Axiom 1: Determinism", []),
            ("Node_B", "Axiom 2: Isolation", [("Node_A", "Node_B", "depends_on")]),
            ("Node_C", "Observation 1: Drift", [("Node_B", "Node_C", "implies"), ("Node_C", "Node_A", "validates")])
        ]

        for i in range(self.iterations):
            # 1. Isolated Environment Setup
            db = GraphDB(":memory:")
            rules = RuleEngine()
            cortex = CortexObserver(db, rules, entropy_threshold=0.1)

            # 2. Process Sequence
            for node_id, content, edges in inputs:
                cortex.process_input(node_id, content, edges)

            # 3. Capture Hash of Final State
            cursor = db.conn.cursor()
            cursor.execute("SELECT node_id, content FROM nodes ORDER BY node_id")
            rows = cursor.fetchall()

            # Convert Rows to stable tuples for reliable hashing
            stable_data = [(row['node_id'], row['content']) for row in rows]
            state_data = str(stable_data).encode('utf-8')
            state_hash = hashlib.sha256(state_data).hexdigest()

            final_states.append(state_hash)
            db.close()

            if i % 20 == 0 and i > 0:
                print(f"[ConvergenceDrill] Completed iteration {i}...")

        # 4. Verify Zero-Entropy (All hashes must be identical)
        unique_states = set(final_states)
        if len(unique_states) == 1:
            print(f"[ConvergenceDrill] SUCCESS: Convergence achieved. Zero-Entropy state locked. Hash: {list(unique_states)[0]}")
            return True
        else:
            print(f"[ConvergenceDrill] FAILURE: Divergence detected! Found {len(unique_states)} distinct end states.")
            return False

if __name__ == "__main__":
    drill = ConvergenceDrill(iterations=100)
    success = drill.run_drill()
    if not success:
        sys.exit(1)
