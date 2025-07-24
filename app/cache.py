import redis
import json
from typing import Tuple

# cached: key: {grid, start, end, algo}, value: {path, cost}

r = redis.Redis(host='localhost', port=6379, db=0)

def generate_cache_key(grid: list, start: Tuple[int, int], end: Tuple[int, int], algorithm: str) -> str:
    return json.dumps({"grid": grid, "start": start, "end": end, "algo": algorithm})

def get_cached_value(key: str):
    cached = r.get(key)
    return json.loads(cached) if cached else None

def set_cached_value(key: str, value: dict):
    r.set(key, json.dumps(value), ex=3600) # expiration 1 hr