from fastapi import FastAPI
from app.models import RouteRequest, RouteResponse
from app.solver import dijkstra

app = FastAPI()

def compute_route(req: RouteRequest):
    if req.algorithm == "dijkstra":
        path, cost = dijkstra(req.grid, req.start, req.end)
    else:
        return {"path": [], "cost": -1} # fallback
    
    return RouteResponse(path=path, cost=cost)