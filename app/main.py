from fastapi import FastAPI, HTTPException
from app.models import RouteRequest, RouteResponse
from app.solver import dijkstra, astar
from app.cache import generate_cache_key, get_cached_value, set_cached_value

app = FastAPI()

@app.post("/route", response_model=RouteResponse)
def compute_route(req: RouteRequest):
    key = generate_cache_key(req.grid, req.start, req.end, req.algorithm)
    cached = get_cached_value(key)
    if cached:
        return RouteResponse(**cached)

    if req.algorithm == "dijkstra":
        path, cost = dijkstra(req.grid, req.start, req.end)
    elif req.algorithm == "astar":
        path, cost = astar(req.grid, req.start, req.end)
    else:
        raise HTTPException(status_code=400, detail="Unsupported algorithm")
    
    set_cached_value(key, {"path": path, "cost": cost})
    return RouteResponse(**cached)