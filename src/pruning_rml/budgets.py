"""Utilities for comparing training budgets."""

def token_efficiency(score, tokens):
    """Return score per million tokens."""
    if tokens <= 0:
        raise ValueError("tokens must be positive")
    return score / (tokens / 1_000_000)
