from dataclasses import dataclass
from typing import List

@dataclass
class Edge:
    id: str
    edge: List[str]
    attribute: List[str]
