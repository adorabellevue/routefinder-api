import heapq
from typing import List, Tuple, Optional

def dijkstra(grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> Tuple[List[Tuple[int, int]], int]:
    rows, cols = len(grid), len(grid[0])
    dist = [[float('inf')] * cols for _ in range(rows)] # shortest distance from start to that cell
    prev = [[None for _ in range(cols)] for _ in range(rows)] # previous cell in shortest path

    heap = [(0, start)] # (cost to cell, (r, c))
    dist[start[0]][start[1]] = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    while heap:
        curr, (r, c) = heapq.heappop(heap)
        if (r, c) == end:
            break
        for (dr, dc) in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new = curr + grid[nr][nc]
                if new < dist[nr][nc]:
                    dist[nr][nc] = new
                    prev[nr][nc] = (r, c)
                    heapq.heappush(heap, (new, (nr, nc)))

    if dist[end[0]][end[1]] == float('inf'):
        return [], -1 # no path found
    
    # reconstruct path backwards
    path = []
    curr = end
    while curr:
        path.append(curr)
        curr = prev[curr[0]][curr[1]]
    path.reverse()

    return path, dist[end[0]][end[1]]