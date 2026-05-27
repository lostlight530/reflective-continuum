import os
import re
import typing

class RuleEngine:
    """
    Deterministic Rule Engine that parses ADRs and enforces architectural constraints.
    Adheres to ADR-001 (Pure Python, no external dependencies).
    """

    def __init__(self, adr_dir: str = "ADR"):
        self.adr_dir = adr_dir
        self.constraints = self._load_constraints()
        self.constants = self._extract_constants()

    def _load_constraints(self) -> typing.Dict[str, typing.List[str]]:
        """
        Parses ADR files to extract sections under 'Architectural Constraints'.
        """
        constraints = {}
        if not os.path.exists(self.adr_dir):
            return constraints

        for filename in sorted(os.listdir(self.adr_dir)):
            if filename.endswith(".md"):
                path = os.path.join(self.adr_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    # Extract the Architectural Constraints section
                    match = re.search(r"## Architectural Constraints.*?\n(.*?)(?=\n##|\Z)", content, re.DOTALL)
                    if match:
                        lines = match.group(1).strip().split("\n")
                        # Clean up list markers
                        cleaned_lines = [re.sub(r"^\d+\.\s*|-\s*", "", line).strip() for line in lines if line.strip()]
                        constraints[filename] = cleaned_lines
        return constraints

    def _extract_constants(self) -> typing.Dict[str, float]:
        """
        Extracts mathematical constants like N or H_threshold from ADR text.
        """
        constants = {
            "N": 3.0,  # Default fallback
            "H_threshold": 1.0  # Default fallback
        }

        # Look for  = [value]$ or {threshold} = [value]$ pattern
        # We also look for mention of constants in the text
        for filename, lines in self.constraints.items():
            text = " ".join(lines)

            # Extract N from ADR-002 context if specifically assigned
            if "ADR-002" in filename:
                # Heuristic: search for N in the file content
                path = os.path.join(self.adr_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    full_content = f.read()
                    n_match = re.search(r"N\s*=\s*(\d+)", full_content)
                    if n_match:
                        constants["N"] = float(n_match.group(1))

            # Extract H_threshold from ADR-005
            if "ADR-005" in filename:
                path = os.path.join(self.adr_dir, filename)
                with open(path, "r", encoding="utf-8") as f:
                    full_content = f.read()
                    h_match = re.search(r"H_{threshold}\s*>\s*([\d.]+)", full_content)
                    if h_match:
                        constants["H_threshold"] = float(h_match.group(1))

        return constants

    def verify_stdlib_only(self, code: str) -> bool:
        """
        Enforces ADR-001: Pure Python stdlib only.
        Checks for 'import' statements that reference common non-stdlib libs.
        """
        restricted = ["numpy", "pandas", "torch", "tensorflow", "jax", "scipy", "sklearn", "networkx", "openai", "anthropic"]
        for lib in restricted:
            if re.search(rf"import\s+{lib}|from\s+{lib}\s+import", code):
                return False
        return True

    def verify_consistency(self, state_delta: dict, context: dict = None) -> bool:
        """
        Verifies if a proposed state delta violates known ADR constraints.
        """
        content = state_delta.get("content", "")
        if content:
            if not self.verify_stdlib_only(content):
                return False

        # Additional structural checks could be added here
        return True
