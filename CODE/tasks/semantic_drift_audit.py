import os
import re
import math
import typing

class SemanticDriftAudit:
    """
    T-06 Analysis: Specialized Semantic Drift & Metacognitive Alignment.
    Audits the Gaseous Phase's reflection logs against the Spec.
    """

    def __init__(self, root: str = "."):
        self.root = root
        self.code_dir = os.path.join(root, "CODE")
        self.adr_dir = os.path.join(root, "ADR")
        self.meth_dir = os.path.join(root, "METHODOLOGY")

    def run_audit(self) -> float:
        """
        Calculates Structural KL Divergence between implementation and specification.
        Returns a value representing the 'misalignment'.
        """
        print("[AbyssalEchoes] Initializing T-06 Analysis...")

        # 1. Check for bilingual completeness (ADR and Methodology)
        total_docs = 0
        bilingual_count = 0

        for folder in [self.adr_dir, self.meth_dir]:
            if not os.path.exists(folder): continue
            for f in os.listdir(folder):
                if f.endswith(".md"):
                    total_docs += 1
                    path = os.path.join(folder, f)
                    with open(path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        # Simple check for Chinese characters as proxy for bilingualism
                        if re.search(r'[\u4e00-\u9fff]', content):
                            bilingual_count += 1

        doc_misalignment = 1.0 - (bilingual_count / total_docs if total_docs > 0 else 0)
        print(f"[AbyssalEchoes] Document Bilingual Misalignment: {doc_misalignment:.4f}")

        # 2. Check for Implementation drift (Does CODE/ match naming conventions?)
        expected_files = ["nexus_core.py", "lattice.py", "axioms.py", "topology.py", "differential.py"]
        found_files = os.listdir(self.code_dir) if os.path.exists(self.code_dir) else []

        match_count = sum(1 for f in expected_files if f in found_files)
        code_misalignment = 1.0 - (match_count / len(expected_files))
        print(f"[AbyssalEchoes] Code Structure Misalignment: {code_misalignment:.4f}")

        # 3. Calculate "KL Divergence" (Weighted mismatch)
        # Using a simplified weighted average as the deterministic proxy for KL divergence
        dk_l = (doc_misalignment * 0.4) + (code_misalignment * 0.6)

        print(f"[AbyssalEchoes] Total Structural KL Divergence (D_KL): {dk_l:.4f}")

        if dk_l > 0.05:
            print("[AbyssalEchoes] D_KL > 0.05! Triggering T-08 PHYSICAL PRUNING / Cognitive Rejection.")
            raise Exception(f"Structural Integrity Violation: D_KL = {dk_l:.4f}")

        print("[AbyssalEchoes] T-09 Coherence Check: System is Locked at Diamond-Hard Consistency.")
        return dk_l

if __name__ == "__main__":
    auditor = SemanticDriftAudit()
    try:
        auditor.run_audit()
    except Exception as e:
        print(f"FAILED: {e}")
        exit(1)
