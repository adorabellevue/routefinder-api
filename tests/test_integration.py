import httpx
import redis
import time
from app.cache import generate_cache_key

def test_cache_integration():
    payload = {
        "grid": [[1, 1, 1], [1, 999, 1], [1, 1, 1]],
        "start": [0, 0],
        "end": [2, 2],
        "algorithm": "dijkstra"
    }

    r = redis.Redis(decode_responses=True)
    key = generate_cache_key(payload["grid"], payload["start"], payload["end"], payload["algorithm"])
    r.delete(key)

    # first request: compute result
    t1 = time.time()
    res1 = httpx.post("http://localhost:8000/route", json=payload)
    t2 = time.time()
    
    assert res1.status_code == 200
    assert r.get(key) is not None # cached result stored under key

    # second request: same call, test cache hit
    t3 = time.time()
    res2 = httpx.post("http://localhost:8000/route", json=payload)
    t4 = time.time()
    
    assert res2.status_code == 200
    assert res2.json() == res1.json() # same result as res1

    # assert cache hit
    compute_time = t2 - t1
    cache_time = t4 - t3
    assert cache_time < compute_time # cache result should be faster than compute timer