import typing
from .continuum_db import GraphDB
from .entropy_analyzer import check_phase_boundary, compute_pagerank
from .drift_detector import compute_structural_delta
from .reflective_validator import RuleEngine

class CortexObserver:
    """
    Metacognitive Observer for the Reflective Continuum (Gaseous Phase).
    Monitors the continuum's entropy and manages self-reflective cycles.
    Adheres to ADR-002, ADR-004, and ADR-005.
    """

    def __init__(self, db: GraphDB, rule_engine: RuleEngine, max_depth: int = None, entropy_threshold: float = None):
        self.db = db
        self.rules = rule_engine

        # Extract constants from RuleEngine (parsed from ADRs) or use defaults
        self.max_depth = max_depth if max_depth is not None else int(self.rules.constants.get("N", 3))
        self.entropy_threshold = entropy_threshold if entropy_threshold is not None else self.rules.constants.get("H_threshold", 1.0)

        self.current_depth = 0
        self.phase = "LIQUID"

        print(f"[Cortex] Initialized with N={self.max_depth}, H_threshold={self.entropy_threshold}")

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
                print(f"[Cortex] Input {node_id} committed successfully.")
            else:
                print(f"[Cortex] Rejecting input {node_id} due to inconsistency or cognitive rejection.")
                self.db.rollback_fork(input_fork)
                self.phase = "LIQUID"

        except Exception as e:
            print(f"[Cortex] Critical error processing input: {e}")
            try:
                self.db.rollback_fork(input_fork)
            except Exception as rollback_e:
                print(f"[Cortex] Rollback failed: {rollback_e}")

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
                print(f"[Cortex] Phase Boundary Detected (H > {self.entropy_threshold})! Transitioning to GASEOUS.")
                self.phase = "GASEOUS"
                return self._start_reflection_cycle()
            else:
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
        Returns True if the cycle completes successfully within depth N.
        """
        if self.current_depth >= self.max_depth:
            print(f"[Cortex] COGNITIVE REJECTION: Max reflection depth {self.max_depth} reached (ADR-002).")
            self.current_depth = 0
            return False

        self.current_depth += 1
        print(f"[Cortex] Reflection Cycle Depth: {self.current_depth}/{self.max_depth}")

        # 1. Fork state for simulation
        fork_name = f"reflection_v{self.current_depth}"
        self.db.fork(fork_name)

        try:
            # 2. Verify current state consistency
            if self._verify_current_state():
                print(f"[Cortex] Self-Consistency Verified at depth {self.current_depth}.")
                self.db.commit_fork(fork_name)
                # If still high entropy, it will stay in GASEOUS and check again next cycle
                return True
            else:
                print("[Cortex] Inconsistency Detected during reflection! Performing Hard Rollback.")
                self.db.rollback_fork(fork_name)
                self.current_depth = 0
                return False

        except Exception as e:
            print(f"[Cortex] Error during reflection: {e}")
            try:
                self.db.rollback_fork(fork_name)
            except Exception:
                pass
            self.phase = "LIQUID"
            self.current_depth = 0
            return False
