import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))

xy = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(graph, x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    size = 1

    while queue:
        x, y = queue.popleft()
        for dx, dy in xy:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                size += 1

    return size

pictures = []
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] and not visited[i][j]:
            pictures.append(bfs(graph, i, j, visited))

print(len(pictures))
print(0 if not pictures else max(pictures))