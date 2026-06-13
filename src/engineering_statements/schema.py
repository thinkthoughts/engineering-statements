from dataclasses import dataclass, field
from typing import List

@dataclass
class EngineeringStatement:
    source: str
    objective: str
    contexts: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    evidence: List[str] = field(default_factory=list)
    outputs: List[str] = field(default_factory=list)
    next_steps: List[str] = field(default_factory=list)
