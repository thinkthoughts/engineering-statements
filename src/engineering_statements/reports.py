def report_slug(arxiv_id: str) -> str:
    """Convert an arXiv identifier to a lab report slug."""
    return arxiv_id.replace(".", "-")
