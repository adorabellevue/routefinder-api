import httpx

# start fastAPI server before running test.py

payload = {
    "grid": [[1, 1, 1], [1, 999, 1], [1, 1, 1]],
    "start": [0, 0],
    "end": [2, 2],
    "algorithm": "dijkstra"
}

response = httpx.post("http://127.0.0.1:8000/route", json=payload)
print("Status:", response.status_code)
print("Body:", response.json())
