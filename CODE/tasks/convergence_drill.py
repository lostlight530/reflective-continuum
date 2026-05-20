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
    """

    def __init__(self, iterations: int = 100):
        self.iterations = iterations

    def run_drill(self):
        print(f"[BlastTester] Initializing T-07 Grounding ({self.iterations} iterations)...")

        final_states = []

        for i in range(self.iterations):
            # 1. Isolated Environment
            db = GraphDB(":memory:")
            rules = RuleEngine()
            cortex = CortexObserver(db, rules, entropy_threshold=0.1)

            # 2. Deterministic Input Sequence
            inputs = [
                ("A", "Fact 1", []),
                ("B", "Fact 2", [("A", "B", "rel")]),
                ("C", "Fact 3", [("B", "C", "rel"), ("C", "A", "rel")])
            ]

            for node_id, content, edges in inputs:
                cortex.process_input(node_id, content, edges)

            # 3. Capture Hash of Final State
            cursor = db.conn.cursor()
            cursor.execute("SELECT node_id, content FROM nodes ORDER BY node_id")
            rows = cursor.fetchall()
            # Convert Rows to stable tuples for hashing
            stable_data = [(row['node_id'], row['content']) for row in rows]
            state_data = str(stable_data).encode('utf-8')
            state_hash = hashlib.sha256(state_data).hexdigest()
            final_states.append(state_hash)
            db.close()

            if i % 20 == 0:
                print(f"[BlastTester] Completed iteration {i}...")

        # 4. Consistency Verification
        unique_states = set(final_states)
        if len(unique_states) == 1:
            print(f"[BlastTester] SUCCESS: System Locked at Zero-Entropy State (Hash: {unique_states.pop()[:12]})")
        else:
            print(f"[BlastTester] FAILURE: Entropy leakage detected! {len(unique_states)} unique states found.")
            sys.exit(1)

if __name__ == "__main__":
    tester = ConvergenceDrill()
    tester.run_drill()
