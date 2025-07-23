from pydantic import BaseModel
from typing import List, Tuple, Literal

class RouteRequest(BaseModel):
    grid: List[List[int]]
    start: Tuple[int, int]
    end: Tuple[int, int]
    algorithm: Literal["dijkstra", "astar"] = "astar"

class RouteResponse(BaseModel):
    path: List[Tuple[int, int]]
    cost: int