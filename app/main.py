from fastapi import FastAPI
from app.models import RouteRequest, RouteResponse
from app.solver import dijkstra

app = FastAPI()

@app.post("/route", response_model=RouteResponse)
def compute_route(req: RouteRequest):
    if req.algorithm == "dijkstra":
        path, cost = dijkstra(req.grid, req.start, req.end)
    else:
        return RouteResponse(path=[], cost=-1)
    
    return RouteResponse(path=path, cost=cost)