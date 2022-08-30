import json
from dataclasses import dataclass
from typing import List
from classes.edge import Edge
from classes.transition import Transition

@dataclass
class Path:
    id: str
    edges_id_list: List[str]
    edges_list: List[Edge]


@dataclass
class PathOutputData:
    pathid: str
    data: List[Transition]

    def __repr__(self):
        return json.dumps(({
            "pathid": self.pathid,
            "data": json.loads(str(self.data))
        }))
