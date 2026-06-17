"""Reset versus revision comparisons."""

from dataclasses import dataclass

@dataclass
class Comparison:
    method: str
    score: float
    tokens: int


def winner(a, b):
    """Return the better-performing comparison."""
    return a if a.score >= b.score else b
