"""Explicit validation configuration; prose ADRs are not executable policy."""
from __future__ import annotations
import ast
import sys
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class RuleConfig:
    max_reflection_depth: int = 3
    entropy_threshold: float = 1.0
    max_content_chars: int = 100_000

    def __post_init__(self) -> None:
        if not 1 <= self.max_reflection_depth <= 100:
            raise ValueError("max_reflection_depth must be within 1..100")
        if self.entropy_threshold < 0:
            raise ValueError("entropy_threshold must be non-negative")
        if not 1 <= self.max_content_chars <= 1_000_000:
            raise ValueError("max_content_chars is out of bounds")


@dataclass(frozen=True, slots=True)
class ValidationResult:
    accepted: bool
    reasons: tuple[str, ...] = ()


class RuleEngine:
    def __init__(self, adr_dir: str | None = None, *, config: RuleConfig | None = None) -> None:
        self.config = config or RuleConfig()
        self.adr_dir = adr_dir  # retained for source compatibility; never parsed as runtime policy
        self.constants = {"N": self.config.max_reflection_depth, "H_threshold": self.config.entropy_threshold}
        self.constraints: dict[str, list[str]] = {}

    def verify_stdlib_only(self, code: str) -> bool:
        try:
            tree = ast.parse(code)
        except SyntaxError:
            return False
        roots = set(sys.stdlib_module_names)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                names = [alias.name.split(".", 1)[0] for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
                names = [node.module.split(".", 1)[0]]
            else:
                continue
            if any(name not in roots for name in names):
                return False
        return True

    def validate(self, state_delta: dict[str, Any]) -> ValidationResult:
        if not isinstance(state_delta, dict):
            return ValidationResult(False, ("state_delta_not_mapping",))
        reasons: list[str] = []
        node_id = state_delta.get("node_id")
        content = state_delta.get("content")
        if not isinstance(node_id, str) or not node_id or len(node_id) > 200:
            reasons.append("invalid_node_id")
        if not isinstance(content, str) or not content or len(content) > self.config.max_content_chars:
            reasons.append("invalid_content")
        if state_delta.get("content_type") == "python" and isinstance(content, str) and not self.verify_stdlib_only(content):
            reasons.append("non_stdlib_or_invalid_python")
        return ValidationResult(not reasons, tuple(reasons))

    def verify_consistency(self, state_delta: dict[str, Any], context: dict[str, Any] | None = None) -> bool:
        return self.validate(state_delta).accepted