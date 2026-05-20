import typing
from .substrate import GraphDB
from .thermodynamics import check_phase_boundary, compute_pagerank
from .differential import compute_structural_delta
from .orthodoxy import RuleEngine

class Cortex:
    """
    The central orchestrator for the Reflective Continuum.
    Manages phase transitions and reflection depth.
    """

    def __init__(self, db: GraphDB, rule_engine: RuleEngine, max_depth: int = 3, entropy_threshold: float = 1.0):
        self.db = db
        self.rules = rule_engine
        self.max_depth = max_depth
        self.entropy_threshold = entropy_threshold
        self.current_depth = 0
        self.phase = "LIQUID"

    def process_input(self, node_id: str, content: str, edges: typing.List[typing.Tuple[str, str, str]]):
        """
        Standard execution mode (Liquid Phase).
        """
        print(f"[Cortex] Processing input: {node_id} (Phase: {self.phase})")

        # 1. Fork state before mutation to allow hard rollback (ADR-004)
        input_fork = f"input_{node_id}"
        self.db.fork(input_fork)

        try:
            # 2. Update Knowledge Graph
            self.db.insert_node(node_id, content, commit=False)
            for src, dst, rel in edges:
                self.db.insert_edge(src, dst, rel, commit=False)

            # 3. Check for Phase Boundary and perform Reflection
            success = self._check_and_reflect()

            if success:
                self.db.commit_fork(input_fork)
            else:
                print(f"[Cortex] Rejecting input {node_id} due to inconsistency or rejection.")
                self.db.rollback_fork(input_fork)
                self.phase = "LIQUID"

        except Exception as e:
            print(f"[Cortex] Critical error processing input: {e}")
            self.db.rollback_fork(input_fork)

    def _check_and_reflect(self) -> bool:
        """
        Evaluates topological entropy and triggers Gaseous Phase if needed.
        Returns True if the state is considered consistent/stable.
        """
        # ADR-004: Every state mutation must be validated.
        if not self._verify_current_state():
            return False

        nodes = self.db.get_all_nodes()
        edges = self.db.get_all_edges()

        pr = compute_pagerank(nodes, edges)
        should_transition = check_phase_boundary(pr, self.entropy_threshold)

        if should_transition:
            if self.phase == "LIQUID":
                print("[Cortex] Phase Boundary Detected! Transitioning to GASEOUS PHASE.")
                self.phase = "GASEOUS"
                return self._start_reflection_cycle()
            else:
                # Already in GASEOUS phase, another reflection cycle may be needed if not converged
                return self._start_reflection_cycle()
        elif self.phase == "GASEOUS":
            print("[Cortex] Entropy stabilized. Returning to LIQUID PHASE.")
            self.phase = "LIQUID"
            self.current_depth = 0
            return True

        return True

    def _verify_current_state(self) -> bool:
        """
        Performs deterministic consistency verification on all nodes in the current state.
        """
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT node_id, content FROM nodes")
        nodes_data = cursor.fetchall()

        for row in nodes_data:
            if not self.rules.verify_consistency({"node_id": row["node_id"], "content": row["content"]}):
                print(f"[Cortex] Inconsistency detected in node: {row['node_id']}")
                return False
        return True

    def _start_reflection_cycle(self) -> bool:
        """
        Metacognitive self-observation (Gaseous Phase).
        Returns True if the cycle completes successfully.
        """
        if self.current_depth >= self.max_depth:
            print(f"[Cortex] COGNITIVE REJECTION: Max reflection depth {self.max_depth} reached.")
            # Upon rejection, we return False to trigger rollback of the input that caused high entropy/no convergence
            self.current_depth = 0
            return False

        self.current_depth += 1
        print(f"[Cortex] Reflection Cycle Depth: {self.current_depth}")

        # 1. Fork state for simulation
        fork_name = f"reflection_v{self.current_depth}"
        self.db.fork(fork_name)

        try:
            # 2. Verify current state consistency
            # Fetch content for actual verification
            cursor = self.db.conn.cursor()
            cursor.execute("SELECT node_id, content FROM nodes")
            nodes_data = cursor.fetchall()

            is_consistent = True
            for row in nodes_data:
                if not self.rules.verify_consistency({"node_id": row["node_id"], "content": row["content"]}):
                    is_consistent = False
                    break

            if is_consistent:
                print("[Cortex] Self-Consistency Verified.")
                self.db.commit_fork(fork_name)
                return True
            else:
                print("[Cortex] Inconsistency Detected! Performing Hard Rollback.")
                self.db.rollback_fork(fork_name)
                self.current_depth = 0
                return False

        except Exception as e:
            print(f"[Cortex] Error during reflection: {e}")
            self.db.rollback_fork(fork_name)
            self.phase = "LIQUID"
            self.current_depth = 0
            return False
