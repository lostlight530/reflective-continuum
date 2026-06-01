from insight_morpher import InsightMorpher
import sys

signals = [
    {"id": "S_001", "content": "DeepMind releases paper on deterministic agent alignment.", "edges": [("S_001", "Determinism", "relates_to")]},
    {"id": "S_002", "content": "OpenAI research shows metacognition layers improve safety constraints.", "edges": [("S_002", "Metacognition", "relates_to")]},
    {"id": "S_003", "content": "New framework proposes zero-entropy architectures for recursive self-improvement.", "edges": [("S_003", "Zero_Entropy", "relates_to")]}
]
morpher = InsightMorpher("continuum.db")
morpher.morph_signals(signals)
