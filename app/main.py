from fastapi import FastAPI
from app.models import RouteRequest, RouteResponse
from app.solver import dijkstra, astar

app = FastAPI()

@app.post("/route", response_model=RouteResponse)
def compute_route(req: RouteRequest):
    if req.algorithm == "dijkstra":
        path, cost = dijkstra(req.grid, req.start, req.end)
    elif req.algorithm == "astar":
        path, cost = astar(req.grid, req.start, req.end)
    else:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")
    
    return RouteResponse(path=path, cost=cost)