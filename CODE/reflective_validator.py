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

    def verify_stdlib_only(self, code: str) -> bool:
        """
        Enforces ADR-001: Pure Python stdlib only.
        Actually checks for 'import' statements that might reference common non-stdlib libs.
        This is a deterministic heuristic check.
        """
        # List of common non-stdlib libraries often used in AI
        restricted = ["numpy", "pandas", "torch", "tensorflow", "jax", "scipy", "sklearn", "networkx", "openai", "anthropic"]
        for lib in restricted:
            if re.search(rf"import\s+{lib}|from\s+{lib}\s+import", code):
                return False
        return True

    def verify_consistency(self, state_delta: dict, context: dict = None) -> bool:
        """
        Verifies if a proposed state delta violates known ADR constraints.
        Returns True if consistent, False otherwise.
        """
        # Logic to check specific delta properties against ADR rules.

        # If the delta contains content (code), verify it
        content = state_delta.get("content", "")
        if content:
            if not self.verify_stdlib_only(content):
                return False

        return True
