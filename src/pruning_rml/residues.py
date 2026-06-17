"""Helpers for reasoning about surviving capabilities after pruning."""

def residue_delta(before, after):
    """Compute change in capability metrics."""
    return {k: after.get(k, 0) - before.get(k, 0) for k in before}
